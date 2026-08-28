"""ViT feature extraction."""

from typing import Optional

import numpy as np
import torch
from PIL import Image
from transformers import AutoImageProcessor, AutoModelForImageClassification


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
