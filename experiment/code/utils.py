"""
Utility functions for Face Race & Gender Classification using Multi-Domain ViT.

Provides dataset loading, ViT feature extraction, SVM model evaluation,
and display helpers for Jupyter notebooks.
"""

import os
import json
import time
import warnings
from typing import Any, Optional

import numpy as np
import pandas as pd
import torch
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
from IPython.display import display, HTML
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from transformers import AutoImageProcessor, AutoModelForImageClassification

warnings.filterwarnings("ignore")

# =============================================================================
# Constants
# =============================================================================

DEMOGPairs_CLASSES = [
    "Asian_Females",
    "Asian_Males",
    "Black_Females",
    "Black_Males",
    "White_Females",
    "White_Males",
]

DEMOGPairs_LABEL_TO_IDX = {
    "Black_Males": 0,
    "White_Females": 1,
    "Asian_Males": 2,
    "White_Males": 3,
    "Black_Females": 4,
    "Asian_Females": 5,
}

DEMOGPairs_IDX_TO_LABEL = {v: k for k, v in DEMOGPairs_LABEL_TO_IDX.items()}

# Backward-compatible aliases (used in notebooks)
demogpairs_classes = DEMOGPairs_CLASSES
demogpairs_label_to_idx = DEMOGPairs_LABEL_TO_IDX
demogpairs_idx_to_label = DEMOGPairs_IDX_TO_LABEL


# =============================================================================
# Serialization
# =============================================================================


def save_object(obj: Any, filename: str, compress: int = 9) -> None:
    """Save object to disk using joblib with compression."""
    with open(filename, "wb") as f:
        joblib.dump(obj, f, compress=compress)


def load_object(filename: str) -> Any:
    """Load object from disk using joblib."""
    with open(filename, "rb") as f:
        return joblib.load(f)


def save_json(data: dict, json_file: str) -> None:
    """Save dictionary to JSON file."""
    with open(json_file, "w") as f:
        json.dump(data, f, indent=4)


def load_json(file_path: str) -> Optional[dict]:
    """Load dictionary from JSON file. Returns None on error."""
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading '{file_path}': {e}")
        return None


# =============================================================================
# Dataset
# =============================================================================


def load_demogpairs(
    metadata_path: str = "dataset/demogpairs/metadata",
    images_path: str = "dataset/demogpairs/images",
) -> list[dict]:
    """
    Load DemogPairs dataset metadata and map to structured records.

    Returns:
        List of dicts with keys: db_code, image_path, full_path, label, label_idx.
    """
    data = []
    for class_name in DEMOGPairs_CLASSES:
        meta_file = os.path.join(metadata_path, f"{class_name}.txt")
        df = pd.read_csv(meta_file, sep=r"\s+")
        for row in df.to_dict("records"):
            row["full_path"] = os.path.join(images_path, row["image_path"])
            row["label"] = class_name
            row["label_idx"] = DEMOGPairs_LABEL_TO_IDX[class_name]
            data.append(row)
    return data


# =============================================================================
# Feature Extraction
# =============================================================================


def extract_vit_features(
    img: str | np.ndarray,
    model: Optional[AutoModelForImageClassification] = None,
    model_path: str = "models/codewithdark/vit-chest-xray",
    device: Optional[torch.device] = None,
    feature_type: str = "cls",
) -> np.ndarray:
    """
    Extract features from a ViT model using [CLS] token or mean pooling.

    Args:
        img: File path (str) or NumPy array (H x W x C).
        model: Pre-loaded model. If None, loads from model_path.
        model_path: HuggingFace model path or local directory.
        device: torch device. Auto-detects CUDA if None.
        feature_type: 'cls' for [CLS] token, 'pool' for mean pooling.

    Returns:
        1D NumPy array of shape (hidden_dim,).
    """
    if device is None:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    if model is None:
        model = AutoModelForImageClassification.from_pretrained(model_path)
    model = model.to(device)
    model.eval()

    processor = AutoImageProcessor.from_pretrained(model_path)

    # Load image
    if isinstance(img, str):
        image = Image.open(img)
    elif isinstance(img, np.ndarray):
        image = Image.fromarray(img.astype("uint8"))
    else:
        raise ValueError("img must be a file path or NumPy array.")

    if image.mode != "RGB":
        image = image.convert("RGB")

    # Preprocess and extract features
    inputs = processor(images=image, return_tensors="pt").to(device)

    with torch.no_grad():
        vit_outputs = model.vit(**inputs)
        hidden_states = vit_outputs.last_hidden_state  # [batch, seq_len, hidden_dim]

    if feature_type == "cls":
        features = hidden_states[:, 0, :]  # [CLS] token
    elif feature_type == "pool":
        features = hidden_states.mean(dim=1)  # mean pooling
    else:
        raise ValueError("feature_type must be 'cls' or 'pool'.")

    return features.squeeze(0).cpu().numpy()


# =============================================================================
# Display Helpers
# =============================================================================


def printhtml(html: str) -> None:
    """Display raw HTML in Jupyter."""
    display(HTML(html))


def html_br() -> None:
    """Display a line break in Jupyter."""
    printhtml("<br>")


def h(level: int, text: str) -> None:
    """Display an HTML heading (h1-h6) in Jupyter."""
    if not 1 <= level <= 6:
        raise ValueError("Heading level must be between 1 and 6.")
    display(HTML(f"<h{level}>{text}</h{level}>"))


def index_ranges(data: list, n_items: list[int]) -> list[tuple[int, int]]:
    """
    Compute index ranges for paginated display.

    Args:
        data: Full data list.
        n_items: Number of items per segment [first, *middle, last].

    Returns:
        List of (start, end) tuples.
    """
    n = len(data)
    k = len(n_items)
    if k < 2:
        raise ValueError("Need at least 2 n_items values.")

    middle = n_items[1 : k - 1]
    divisor = len(middle) + 1
    distance = (n - sum(n_items)) // divisor

    ranges = [(0, n_items[0])]
    current = n_items[0]
    for ni in middle:
        current += distance
        ranges.append((current, current + ni))
        current += ni
    ranges.append((n - n_items[k - 1], n))
    return ranges


def display_table(
    data: list[dict],
    table_style: str = "width: 100%",
    column_widths: list[str] | None = None,
    text_aligns: list[str] | None = None,
    hidden_columns: list[str] | None = None,
    n_items: list[int] | None = None,
    save_excel: str | None = None,
    with_header: bool = True,
) -> list[dict]:
    """
    Display a list of dicts as an HTML table in Jupyter.

    Args:
        data: List of dictionaries to display.
        table_style: CSS style string for the table.
        column_widths: Per-column width percentages (e.g. ['10%', '90%']).
        text_aligns: Per-column text alignment.
        hidden_columns: Columns to exclude from display.
        n_items: Pagination params [first, *middle, last] for large datasets.
        save_excel: If set, export to this Excel file path.
        with_header: Whether to show header row.

    Returns:
        The (possibly paginated) data that was displayed.
    """
    if not data:
        print("Data kosong.")
        return []

    headers = [k for k in data[0].keys() if k not in (hidden_columns or [])]

    if n_items and len(n_items) >= 2:
        new_data = []
        for start, end in index_ranges(data, n_items):
            new_data += data[start:end]
            new_data.append({h_key: "..." for h_key in headers})
        new_data = new_data[: len(new_data) - 1]
    else:
        new_data = data.copy()

    if save_excel:
        pd.DataFrame(new_data).to_excel(save_excel, index=False)

    if not text_aligns:
        text_aligns = ["left"] * len(headers)

    # Build HTML
    html = f'<table style="{table_style}; border-collapse: collapse;">\n'

    if with_header:
        html += "  <tr>\n"
        for i, header in enumerate(headers):
            w = f"width: {column_widths[i]};" if column_widths and i < len(column_widths) else ""
            a = f"text-align: {text_aligns[i]};"
            html += f'    <th style="border: 1px solid black; padding: 8px; {w} {a}">{header}</th>\n'
        html += "  </tr>\n"

    for row in new_data:
        html += "  <tr>\n"
        for i, key in enumerate(headers):
            w = f"width: {column_widths[i]};" if column_widths and i < len(column_widths) else ""
            a = f"text-align: {text_aligns[i]};"
            html += f'    <td style="border: 1px solid black; padding: 8px; {w} {a}">{row[key]}</td>\n'
        html += "  </tr>\n"

    html += "</table>"
    printhtml(html)
    return new_data


# =============================================================================
# SVM Model Evaluation
# =============================================================================


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
    y_test: np.ndarray, y_pred: np.ndarray
) -> list[dict]:
    """Compute per-class One-vs-Rest metrics."""
    class_metrics = []
    for idx, label in DEMOGPairs_IDX_TO_LABEL.items():
        y_true_bin = y_test == idx
        y_pred_bin = y_pred == idx
        class_metrics.append(
            {
                "Class": label,
                "Accuracy": accuracy_score(y_true_bin, y_pred_bin),
                "Precision": precision_score(y_true_bin, y_pred_bin),
                "Recall": recall_score(y_true_bin, y_pred_bin),
                "F1-Score": f1_score(y_true_bin, y_pred_bin),
            }
        )
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

    For each model in grid_models:
    - Loads from disk if already trained, otherwise fits and saves.
    - Computes test metrics (accuracy, precision, recall, f1).
    - Saves detailed results to JSON.
    - Displays classification report and confusion matrix.

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
        print(classification_report(y_test, y_pred))

        html_br()
        class_metrics = _compute_class_metrics(y_test, y_pred)
        display_table(class_metrics)

        html_br()
        cm = confusion_matrix(y_test, y_pred)
        plt.figure(figsize=(8, 6))
        sns.heatmap(
            cm,
            annot=True,
            fmt="d",
            cmap="Blues",
            xticklabels=list(DEMOGPairs_IDX_TO_LABEL.values()),
            yticklabels=list(DEMOGPairs_IDX_TO_LABEL.values()),
        )
        plt.xlabel("Predicted Labels")
        plt.ylabel("True Labels")
        plt.title("Confusion Matrix")
        plt.show()

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


# =============================================================================
# Time Helpers
# =============================================================================


def seconds_to_time(seconds: float) -> dict:
    """
    Convert seconds to a human-readable time breakdown.

    Returns:
        Dict with days, hours, minutes, seconds, and a formatted text string.
    """
    seconds = float(seconds)
    days = int(seconds // 86400)
    hours = int((seconds % 86400) // 3600)
    minutes = int((seconds % 3600) // 60)
    remaining = round(seconds % 60, 2)

    return {
        "input_seconds": seconds,
        "days": days,
        "hours": hours,
        "minutes": minutes,
        "seconds": remaining,
        "text": f"{days} hari {hours} jam {minutes} menit {remaining} detik",
    }
