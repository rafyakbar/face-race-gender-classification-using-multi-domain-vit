"""Dataset loading for DemogPairs."""

import os

import pandas as pd

from .constants import DEMOGPairs_CLASSES, DEMOGPairs_LABEL_TO_IDX


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
