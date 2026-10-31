"""
Utility functions for Face Race & Gender Classification using Multi-Domain ViT.

Provides dataset loading, ViT feature extraction, model evaluation,
and display helpers for Jupyter notebooks and terminal.
"""

import warnings
warnings.filterwarnings("ignore")

import sys
import ctypes
from ctypes import wintypes

def optimize_cpu_affinity(p_core_threads: int = 12, verbose: bool = False) -> bool:
    """
    Lock the current process and its worker threads to Intel P-cores on Windows,
    and elevate process priority to ABOVE_NORMAL to prevent EcoQoS power throttling.
    
    For Intel Core i9-13900H:
      - Threads 0-11 = 6 P-Cores with Hyper-Threading (12 logical processors)
      - Threads 12-19 = 8 E-Cores (8 logical processors)
    """
    if sys.platform == "win32":
        try:
            kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
            kernel32.GetCurrentProcess.restype = wintypes.HANDLE
            kernel32.SetProcessAffinityMask.argtypes = [wintypes.HANDLE, ctypes.c_size_t]
            kernel32.SetProcessAffinityMask.restype = wintypes.BOOL
            kernel32.SetPriorityClass.argtypes = [wintypes.HANDLE, wintypes.DWORD]
            kernel32.SetPriorityClass.restype = wintypes.BOOL

            handle = kernel32.GetCurrentProcess()
            # 1. Set affinity mask to threads 0 through (p_core_threads - 1)
            mask = (1 << p_core_threads) - 1
            res_mask = kernel32.SetProcessAffinityMask(handle, mask)
            
            # 2. Set priority class to ABOVE_NORMAL_PRIORITY_CLASS (0x00008000)
            res_pri = kernel32.SetPriorityClass(handle, 0x00008000)
            
            if verbose:
                print(f"[utils] CPU Affinity locked to first {p_core_threads} P-Core threads (mask: 0x{mask:X}). Priority: ABOVE_NORMAL.")
            return bool(res_mask and res_pri)
        except Exception:
            return False
    return False

# Automatically activate P-Core optimization whenever utils is imported on Windows
optimize_cpu_affinity(p_core_threads=12, verbose=False)

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
from .dataset import load_demogpairs, split_demogpairs_subject_disjoint

# Feature Extraction
from .extraction import extract_vit_features, get_image_processor

# Display
from .display import printhtml, html_br, h, display_table, index_ranges, IS_NOTEBOOK

# Evaluation
from .evaluation import evaluate_models

# Time
from .time_helpers import seconds_to_time
