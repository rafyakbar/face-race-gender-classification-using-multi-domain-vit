"""Dataset loading and subject-disjoint partitioning for DemogPairs."""

import os
from collections import defaultdict
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from .constants import DEMOGPairs_CLASSES, DEMOGPairs_LABEL_TO_IDX


def load_demogpairs(
    metadata_path: str = "dataset/demogpairs/metadata",
    images_path: str = "dataset/demogpairs/images",
) -> list[dict]:
    """
    Load DemogPairs dataset metadata and map to structured records.

    Returns:
        List of dicts with keys: db_code, image_path, full_path, label, label_idx, subject_id.
    """
    data = []
    for class_name in DEMOGPairs_CLASSES:
        meta_file = os.path.join(metadata_path, f"{class_name}.txt")
        df = pd.read_csv(meta_file, sep=r"\s+")
        for row in df.to_dict("records"):
            row["full_path"] = os.path.join(images_path, row["image_path"])
            row["label"] = class_name
            row["label_idx"] = DEMOGPairs_LABEL_TO_IDX[class_name]
            # Normalize path separator and extract identity/subject folder name
            row["subject_id"] = row["image_path"].replace("\\", "/").split("/")[0]
            data.append(row)
    return data


def split_demogpairs_subject_disjoint(
    data: list[dict],
    train_ratio: float = 0.8,
    random_state: int = 42,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Split DemogPairs into train and test indices strictly at the subject level,
    preserving exact demographic class stratification (0% identity overlap).

    For an 80/20 split across 600 subjects (100 subjects × 6 classes, 18 imgs/subject):
      - Train: 80 subjects × 18 imgs = 1,440 imgs/class (8,640 total imgs)
      - Test : 20 subjects × 18 imgs = 360 imgs/class (2,160 total imgs)
      - Zero identity overlap between train and test sets.

    Returns:
        Tuple of (train_indices, test_indices) as numpy arrays.
    """
    class_subjects = defaultdict(set)
    for d in data:
        class_subjects[d["label"]].add(d["subject_id"])

    train_indices = []
    test_indices = []

    for label in sorted(class_subjects.keys()):
        sorted_subs = sorted(list(class_subjects[label]))
        tr_subs, te_subs = train_test_split(
            sorted_subs,
            train_size=train_ratio,
            random_state=random_state,
        )
        tr_set = set(tr_subs)
        te_set = set(te_subs)

        for idx, d in enumerate(data):
            if d["label"] == label:
                if d["subject_id"] in tr_set:
                    train_indices.append(idx)
                elif d["subject_id"] in te_set:
                    test_indices.append(idx)

    return np.array(train_indices), np.array(test_indices)

