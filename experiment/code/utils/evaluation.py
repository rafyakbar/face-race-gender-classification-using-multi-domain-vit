"""Model evaluation and GridSearchCV helpers."""

import os
import time

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)

from .display import h, html_br, display_table
from .serialization import save_json, save_object, load_object


def _serialize_dict(d: dict) -> dict:
    """Convert non-serializable values to strings for display."""
    result = d.copy()
    for key in result:
        val = result[key]
        if val is not None and not isinstance(val, (str, int, float, bool)):
            result[key] = str(val)
        if isinstance(result[key], str):
            result[key] = result[key].split("(")[0]
    return result


def _compute_class_metrics(
    y_test: np.ndarray, y_pred: np.ndarray, target_names: list[str]
) -> list[dict]:
    """Compute per-class metrics from confusion matrix (OvR approach)."""
    cm = confusion_matrix(y_test, y_pred)
    total = cm.sum()
    class_metrics = []
    for idx, label in enumerate(target_names):
        tp = cm[idx, idx]
        fn = cm[idx].sum() - tp
        fp = cm[:, idx].sum() - tp
        tn = total - tp - fp - fn
        ovr_acc = (tp + tn) / total
        class_prec = tp / (tp + fp) if (tp + fp) > 0 else 0
        class_rec = tp / (tp + fn) if (tp + fn) > 0 else 0
        class_f1 = 2 * class_prec * class_rec / (class_prec + class_rec) if (class_prec + class_rec) > 0 else 0
        class_metrics.append({
            "Class": label,
            "OvR Accuracy": ovr_acc,
            "Precision": class_prec,
            "Recall": class_rec,
            "F1-Score": class_f1,
            "Support": int(tp + fn),
        })
    return class_metrics


def _format_cv_results(cv_results_df: pd.DataFrame) -> list[dict]:
    """Format GridSearchCV results into readable list of dicts."""
    result_columns = {
        "params": "Params",
        **{f"split{c}_test_accuracy": f"Fold {c + 1}" for c in range(5)},
        "mean_test_accuracy": "Accuracy Mean",
        "mean_test_f1": "F1 Score Mean",
        "mean_test_precision": "Precision Mean",
        "mean_test_recall": "Recall Mean",
        "mean_fit_time": "Train Time Mean",
    }
    fold_results = cv_results_df[list(result_columns.keys())].rename(
        columns=result_columns
    ).to_dict("records")

    return [
        {"No": i + 1, **{k: _serialize_dict(v) if k == "Params" else round(v, 4) for k, v in r.items()}}
        for i, r in enumerate(fold_results)
    ]


def evaluate_models(
    grid_models: dict,
    x_train: np.ndarray,
    y_train: np.ndarray,
    x_test: np.ndarray,
    y_test: np.ndarray,
    model_prefix: str = "models/clf_",
    target_names: list[str] | None = None,
    results_path: str = "results/result_",
) -> tuple[list[dict], list[dict]]:
    """
    Train, evaluate, and serialize multiple GridSearchCV models.

    Args:
        grid_models: Dict of {name: GridSearchCV estimator}.
        x_train, y_train: Training data.
        x_test, y_test: Test data.
        model_prefix: Directory/prefix for saved model files.
        target_names: Class names for classification_report.
        results_path: Directory/prefix for result JSON files.

    Returns:
        Tuple of (evaluation_results, fold_results).
    """
    evaluation_results = []

    for model_name, model in grid_models.items():
        short_name = model_name.split("(")[0]
        model_file = f"{model_prefix}{short_name}.pkl"
        print(f"Evaluating: {short_name}")

        # Load or train
        if not os.path.exists(model_file):
            start = time.time()
            trained_model = model.fit(x_train, y_train)
            elapsed = time.time() - start
            save_object((trained_model, elapsed), model_file)
        else:
            trained_model, elapsed = load_object(model_file)

        # Predict and metrics
        y_pred = trained_model.predict(x_test)
        test_acc = accuracy_score(y_test, y_pred)
        test_prec = precision_score(y_test, y_pred, average="macro")
        test_rec = recall_score(y_test, y_pred, average="macro")
        test_f1 = f1_score(y_test, y_pred, average="macro")
        cls_report = classification_report(y_test, y_pred, output_dict=True, target_names=target_names)

        # CV results
        cv_df = pd.DataFrame(trained_model.cv_results_)
        cv_df["param_classifier"] = cv_df["param_classifier"].astype(str)
        cv_df = cv_df.sort_values(by="mean_test_accuracy", ascending=False)
        fold_results = _format_cv_results(cv_df)

        best_params = _serialize_dict(trained_model.best_params_)

        # Save results
        saved_result = {
            "model_name": short_name,
            "model_file_path": model_file,
            "best_parameters": best_params,
            "y_test": y_test.tolist(),
            "y_pred": y_pred.tolist(),
            "test_accuracy": test_acc,
            "test_precision": test_prec,
            "test_recall": test_rec,
            "test_f1": test_f1,
            "classification_metrics": cls_report,
        }
        save_json(saved_result, f"{results_path}{short_name}.json")

        # Display
        h(5, "Best Parameters")
        print(best_params)

        h(5, "Test Results")
        print(f"Accuracy  : {test_acc}")
        print(f"Precision : {test_prec}")
        print(f"Recall    : {test_rec}")
        print(f"F1 Score  : {test_f1}")
        print(classification_report(y_test, y_pred, target_names=target_names, digits=4))

        html_br()
        class_metrics = _compute_class_metrics(y_test, y_pred, target_names)
        display_table(class_metrics)

        # Confusion matrix - save to images/
        html_br()
        cm = confusion_matrix(y_test, y_pred)
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(
            cm,
            annot=True,
            fmt="d",
            cmap="Blues",
            xticklabels=target_names,
            yticklabels=target_names,
            ax=ax,
        )
        ax.set_xlabel("Predicted Labels")
        ax.set_ylabel("True Labels")
        ax.set_title("Confusion Matrix")

        # Save to images/ folder with descriptive name
        os.makedirs("images", exist_ok=True)
        model_file_stem = os.path.splitext(os.path.basename(model_file))[0]
        fig_name = f"cm_{model_file_stem.replace('clf_demogpairs_', '')}.png"
        fig_path = os.path.join("images", fig_name)
        fig.savefig(fig_path, dpi=150, bbox_inches="tight")
        plt.close(fig)
        print(f"Confusion matrix saved: {fig_path}")

        # Display image inline (Jupyter: HTML img, terminal: path only)
        from .display import printhtml, IS_NOTEBOOK
        if IS_NOTEBOOK:
            printhtml(f'<img src="{fig_path}" width="600">')

        # Print confusion matrix as text array with labels
        print("\nConfusion Matrix:")
        print(f"{'':>20s}", end="")
        for name in target_names:
            print(f"{name:>18s}", end="")
        print()
        for i, row_label in enumerate(target_names):
            print(f"{row_label:>20s}", end="")
            for j in range(len(target_names)):
                print(f"{cm[i][j]:>18d}", end="")
            print()

        evaluation_results.append(
            {
                "model_name": short_name,
                "model_file_path": model_file,
                "best_parameters": best_params,
                "test_accuracy": test_acc,
                "test_f1": test_f1,
                "test_precision": test_prec,
                "test_recall": test_rec,
                "parameter_combinations": len(cv_df),
            }
        )

    return evaluation_results, fold_results
