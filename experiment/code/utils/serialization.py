"""Serialization helpers for saving/loading objects and JSON."""

import json
from typing import Any, Optional

import joblib


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
