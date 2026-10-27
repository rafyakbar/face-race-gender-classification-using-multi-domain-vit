import os
import sys
import time
import json
import subprocess
from datetime import datetime

_curr = os.path.dirname(os.path.abspath(__file__))
EXPERIMENT_DIR = os.path.dirname(_curr) if os.path.basename(_curr) == "scripts" else _curr
RESULTS_DIR = os.path.join(EXPERIMENT_DIR, "results")
LOG_FILE = os.path.join(RESULTS_DIR, "gnb_execution_log.txt")

PYTHON_EXE = r"C:\Users\Rafy\miniconda3\envs\torch-gpu\python.exe"
if not os.path.exists(PYTHON_EXE):
    PYTHON_EXE = sys.executable

GNB_NOTEBOOKS = [
    ("2.2.1_gnb_vit-face_demogpairs.ipynb", "demogpairs_gnb_vit-face_GaussianNB.json"),
    ("2.2.2_gnb_vit-emotion_demogpairs.ipynb", "demogpairs_gnb_vit-emotion_GaussianNB.json"),
    ("2.2.3_gnb_vit-age_demogpairs.ipynb", "demogpairs_gnb_vit-age_GaussianNB.json"),
    ("2.2.4_gnb_vit-face-age_demogpairs.ipynb", "demogpairs_gnb_vit-face-age_GaussianNB.json"),
    ("2.2.5_gnb_vit-emotion-age_demogpairs.ipynb", "demogpairs_gnb_vit-emotion-age_GaussianNB.json"),
    ("2.2.6_gnb_vit-emotion-face_demogpairs.ipynb", "demogpairs_gnb_vit-emotion-face_GaussianNB.json"),
    ("2.2.7_gnb_vit-face-emotion-age_demogpairs.ipynb", "demogpairs_gnb_vit-face-emotion-age_GaussianNB.json"),
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

def run_gnb(nb_name, result_json_name):
    nb_path = os.path.join(EXPERIMENT_DIR, nb_name)
    result_path = os.path.join(RESULTS_DIR, result_json_name)

    if is_valid_result(result_path):
        try:
            with open(result_path, "r", encoding="utf-8") as f:
                res = json.load(f)
            acc = res.get("test_accuracy", 0) * 100
            f1 = res.get("test_f1", 0)
            log(f"[SKIP] {nb_name} sudah selesai sebelumnya (Akurasi: {acc:.2f}%, F1: {f1:.4f}).")
        except Exception:
            log(f"[SKIP] {nb_name} sudah selesai sebelumnya.")
        return True

    log("=" * 60)
    log(f"[START] Mengeksekusi notebook: {nb_name}")
    start_time = time.time()

    cmd = [
        PYTHON_EXE, "-m", "jupyter", "nbconvert",
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
    log("MEMULAI RUNNER GNB (GAUSSIAN NAIVE BAYES)")
    total = len(GNB_NOTEBOOKS)
    success = 0

    for idx, (nb_name, res_name) in enumerate(GNB_NOTEBOOKS, 1):
        log(f"\n--- Progress GNB {idx}/{total} ---")
        ok = run_gnb(nb_name, res_name)
        if ok:
            success += 1
        time.sleep(2)

    log("\n" + "=" * 60)
    log(f"SELURUH EKSEKUSI GNB SELESAI! ({success}/{total} sukses)")
    log("=" * 60)

if __name__ == "__main__":
    main()
