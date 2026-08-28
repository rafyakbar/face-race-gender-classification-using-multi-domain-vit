"""Constants for DemogPairs dataset."""

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

# Backward-compatible aliases
demogpairs_classes = DEMOGPairs_CLASSES
demogpairs_label_to_idx = DEMOGPairs_LABEL_TO_IDX
demogpairs_idx_to_label = DEMOGPairs_IDX_TO_LABEL
