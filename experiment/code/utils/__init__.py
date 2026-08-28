"""
Utility functions for Face Race & Gender Classification using Multi-Domain ViT.

Provides dataset loading, ViT feature extraction, model evaluation,
and display helpers for Jupyter notebooks and terminal.
"""

import warnings
warnings.filterwarnings("ignore")

# Constants
from .constants import (
    DEMOGPairs_CLASSES,
    DEMOGPairs_LABEL_TO_IDX,
    DEMOGPairs_IDX_TO_LABEL,
    demogpairs_classes,
    demogpairs_label_to_idx,
    demogpairs_idx_to_label,
)

# Serialization
from .serialization import save_object, load_object, save_json, load_json

# Dataset
from .dataset import load_demogpairs

# Feature Extraction
from .extraction import extract_vit_features

# Display
from .display import printhtml, html_br, h, display_table, index_ranges, IS_NOTEBOOK

# Evaluation
from .evaluation import evaluate_models

# Time
from .time_helpers import seconds_to_time
