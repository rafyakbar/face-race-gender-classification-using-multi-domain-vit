import os
import sys
import time
import json
import subprocess
import ctypes
from ctypes import wintypes
from datetime import datetime

# Lock runner to P-Cores on Intel Hybrid CPUs and prevent throttling
if sys.platform == "win32":
    try:
        _k32 = ctypes.WinDLL("kernel32", use_last_error=True)
        _k32.GetCurrentProcess.restype = wintypes.HANDLE
        _k32.SetProcessAffinityMask.argtypes = [wintypes.HANDLE, ctypes.c_size_t]
        _k32.SetProcessAffinityMask.restype = wintypes.BOOL
        _k32.SetPriorityClass.argtypes = [wintypes.HANDLE, wintypes.DWORD]
        _k32.SetPriorityClass.restype = wintypes.BOOL

        _handle = _k32.GetCurrentProcess()
        _mask = (1 << 12) - 1  # Threads 0-11 (P-cores for i9-13900H)
        _k32.SetProcessAffinityMask(_handle, _mask)
        _k32.SetPriorityClass(_handle, 0x00008000)  # ABOVE_NORMAL
    except Exception:
        pass

_curr = os.path.dirname(os.path.abspath(__file__))
EXPERIMENT_DIR = os.path.dirname(_curr) if os.path.basename(_curr) == "scripts" else _curr
RESULTS_DIR = os.path.join(EXPERIMENT_DIR, "results")
LOG_FILE = os.path.join(RESULTS_DIR, "remaining_queue_log.txt")

PYTHON_EXE = r"C:\Users\Rafy\miniconda3\envs\torch-gpu\python.exe"
if not os.path.exists(PYTHON_EXE):
    PYTHON_EXE = sys.executable
    local_bin = os.path.expanduser("~/.local/bin")
    if os.path.isdir(local_bin):
        os.environ["PATH"] = local_bin + os.pathsep + os.environ.get("PATH", "")

REMAINING_QUEUE = [
    # --- Batch 1: Logistic Regression (7 notebooks) ---
    ("2.5.1_lr_vit-face_demogpairs.ipynb", "demogpairs_lr_vit-face_LogisticRegression.json"),
    ("2.5.2_lr_vit-emotion_demogpairs.ipynb", "demogpairs_lr_vit-emotion_LogisticRegression.json"),
    ("2.5.3_lr_vit-age_demogpairs.ipynb", "demogpairs_lr_vit-age_LogisticRegression.json"),
    ("2.5.4_lr_vit-face-age_demogpairs.ipynb", "demogpairs_lr_vit-face-age_LogisticRegression.json"),
    ("2.5.5_lr_vit-emotion-age_demogpairs.ipynb", "demogpairs_lr_vit-emotion-age_LogisticRegression.json"),
    ("2.5.6_lr_vit-emotion-face_demogpairs.ipynb", "demogpairs_lr_vit-emotion-face_LogisticRegression.json"),
    ("2.5.7_lr_vit-face-emotion-age_demogpairs.ipynb", "demogpairs_lr_vit-face-emotion-age_LogisticRegression.json"),

    # --- Batch 2: Random Forest (7 notebooks) ---
    ("2.4.1_rf_vit-face_demogpairs.ipynb", "demogpairs_rf_vit-face_RandomForestClassifier.json"),
    ("2.4.2_rf_vit-emotion_demogpairs.ipynb", "demogpairs_rf_vit-emotion_RandomForestClassifier.json"),
    ("2.4.3_rf_vit-age_demogpairs.ipynb", "demogpairs_rf_vit-age_RandomForestClassifier.json"),
    ("2.4.4_rf_vit-face-age_demogpairs.ipynb", "demogpairs_rf_vit-face-age_RandomForestClassifier.json"),
    ("2.4.5_rf_vit-emotion-age_demogpairs.ipynb", "demogpairs_rf_vit-emotion-age_RandomForestClassifier.json"),
    ("2.4.6_rf_vit-emotion-face_demogpairs.ipynb", "demogpairs_rf_vit-emotion-face_RandomForestClassifier.json"),
    ("2.4.7_rf_vit-face-emotion-age_demogpairs.ipynb", "demogpairs_rf_vit-face-emotion-age_RandomForestClassifier.json"),

    # --- Batch 3: SVM Remaining (6 notebooks) ---
    ("2.1.2_svm_vit-emotion_demogpairs.ipynb", "demogpairs_svm_vit-emotion_SVC.json"),
    ("2.1.3_svm_vit-age_demogpairs.ipynb", "demogpairs_svm_vit-age_SVC.json"),
    ("2.1.4_svm_vit-face-age_demogpairs.ipynb", "demogpairs_svm_vit-face-age_SVC.json"),
    ("2.1.5_svm_vit-emotion-age_demogpairs.ipynb", "demogpairs_svm_vit-emotion-age_SVC.json"),
    ("2.1.7_svm_vit-face-emotion-age_demogpairs.ipynb", "demogpairs_svm_vit-face-emotion-age_SVC.json"),
    ("2.1.6_svm_vit-emotion-face_demogpairs.ipynb", "demogpairs_svm_vit-emotion-face_SVC.json"),
]

def log(msg):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_msg = f"[{now}] {msg}"
    print(full_msg, flush=True)
    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(full_msg + "\n")

def is_valid_result(json_path):
    if not os.path.exists(json_path):
        return False
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return "test_accuracy" in data
    except Exception:
        return False

def run_notebook(nb_name, result_json_name):
    nb_path = os.path.join(EXPERIMENT_DIR, nb_name)
    result_path = os.path.join(RESULTS_DIR, result_json_name)

    if is_valid_result(result_path):
        try:
            with open(result_path, "r", encoding="utf-8") as f:
                res = json.load(f)
            acc = res.get("test_accuracy", 0) * 100
            f1 = res.get("test_f1", 0)
            log(f"[SKIP] {nb_name} sudah selesai (Akurasi: {acc:.2f}%, F1: {f1:.4f}).")
        except Exception:
            log(f"[SKIP] {nb_name} sudah selesai.")
        return True

    log("=" * 60)
    log(f"[START] Mengeksekusi: {nb_name}")
    start_time = time.time()

    cmd = [
        PYTHON_EXE, "-m", "nbconvert",
        "--to", "notebook",
        "--execute",
        "--inplace",
        "--ExecutePreprocessor.kernel_name=torch-gpu",
        "--ExecutePreprocessor.timeout=None",
        nb_name
    ]

    try:
        proc = subprocess.run(cmd, cwd=EXPERIMENT_DIR, capture_output=True, text=True)
        elapsed = time.time() - start_time
        mins = elapsed / 60.0

        if proc.returncode == 0 and is_valid_result(result_path):
            with open(result_path, "r", encoding="utf-8") as f:
                res = json.load(f)
            acc = res.get("test_accuracy", 0) * 100
            f1 = res.get("test_f1", 0)
            log(f"[DONE] {nb_name} SUKSES! Waktu: {mins:.1f} menit | Akurasi: {acc:.2f}% | Macro-F1: {f1:.4f}")
            return True
        else:
            log(f"[ERROR] {nb_name} gagal dengan returncode {proc.returncode}!")
            if proc.stderr:
                log(f"[STDERR]: {proc.stderr[-600:]}")
            return False
    except Exception as e:
        log(f"[EXCEPTION] Terjadi error pada {nb_name}: {e}")
        return False

def main():
    log("MEMULAI RUNNER ANTREAN SISA MODEL (LR -> RF -> SVM)")
    total = len(REMAINING_QUEUE)
    success = 0

    for idx, (nb_name, res_name) in enumerate(REMAINING_QUEUE, 1):
        log(f"\n--- Progress Antrean {idx}/{total} ---")
        ok = run_notebook(nb_name, res_name)
        if ok:
            success += 1
        time.sleep(2)

    log("\n" + "=" * 60)
    log(f"SELURUH EKSEKUSI ANTREAN SELESAI! ({success}/{total} sukses)")
    log("=" * 60)

if __name__ == "__main__":
    main()
