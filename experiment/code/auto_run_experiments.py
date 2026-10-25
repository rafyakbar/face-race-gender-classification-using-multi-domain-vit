import os
import sys
import time
import json
import subprocess
from datetime import datetime

# Path setup - detects whether run from experiment/code or root
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if os.path.basename(CURRENT_DIR) == "code":
    EXPERIMENT_DIR = CURRENT_DIR
else:
    EXPERIMENT_DIR = os.path.join(CURRENT_DIR, "experiment", "code")

RESULTS_DIR = os.path.join(EXPERIMENT_DIR, "results")
LOG_FILE = os.path.join(RESULTS_DIR, "queue_execution_log.txt")

# Explicit conda python executable for torch-gpu
CONDA_PYTHON = r"C:\Users\Rafy\miniconda3\envs\torch-gpu\python.exe"
PYTHON_EXE = CONDA_PYTHON if os.path.exists(CONDA_PYTHON) else sys.executable

# Target result for 2.1.7 (currently being executed manually)
TRIGGER_RESULT_217 = os.path.join(RESULTS_DIR, "demogpairs_svm_vit-face-emotion-age_SVC.json")

# Mapping of notebooks to their expected result JSON files
# Ordered by execution priority: GNB (fastest ~10 min), LR (~30-45 min), RF (~1-2 hr), SVM (remaining ~8-10 hr)
NOTEBOOK_QUEUE = [
    # --- Batch 1: Gaussian Naive Bayes (Super Cepat ~5-10 menit total) ---
    ("2.2.1_gnb_vit-face_demogpairs.ipynb", "demogpairs_gnb_vit-face_GaussianNB.json"),
    ("2.2.2_gnb_vit-emotion_demogpairs.ipynb", "demogpairs_gnb_vit-emotion_GaussianNB.json"),
    ("2.2.3_gnb_vit-age_demogpairs.ipynb", "demogpairs_gnb_vit-age_GaussianNB.json"),
    ("2.2.4_gnb_vit-face-age_demogpairs.ipynb", "demogpairs_gnb_vit-face-age_GaussianNB.json"),
    ("2.2.5_gnb_vit-emotion-age_demogpairs.ipynb", "demogpairs_gnb_vit-emotion-age_GaussianNB.json"),
    ("2.2.6_gnb_vit-emotion-face_demogpairs.ipynb", "demogpairs_gnb_vit-emotion-face_GaussianNB.json"),
    ("2.2.7_gnb_vit-face-emotion-age_demogpairs.ipynb", "demogpairs_gnb_vit-face-emotion-age_GaussianNB.json"),

    # --- Batch 2: Logistic Regression (Cepat ~30-45 menit total) ---
    ("2.5.1_lr_vit-face_demogpairs.ipynb", "demogpairs_lr_vit-face_LogisticRegression.json"),
    ("2.5.2_lr_vit-emotion_demogpairs.ipynb", "demogpairs_lr_vit-emotion_LogisticRegression.json"),
    ("2.5.3_lr_vit-age_demogpairs.ipynb", "demogpairs_lr_vit-age_LogisticRegression.json"),
    ("2.5.4_lr_vit-face-age_demogpairs.ipynb", "demogpairs_lr_vit-face-age_LogisticRegression.json"),
    ("2.5.5_lr_vit-emotion-age_demogpairs.ipynb", "demogpairs_lr_vit-emotion-age_LogisticRegression.json"),
    ("2.5.6_lr_vit-emotion-face_demogpairs.ipynb", "demogpairs_lr_vit-emotion-face_LogisticRegression.json"),
    ("2.5.7_lr_vit-face-emotion-age_demogpairs.ipynb", "demogpairs_lr_vit-face-emotion-age_LogisticRegression.json"),

    # --- Batch 3: Random Forest (Sedang ~1-2 jam total) ---
    ("2.4.1_rf_vit-face_demogpairs.ipynb", "demogpairs_rf_vit-face_RandomForestClassifier.json"),
    ("2.4.2_rf_vit-emotion_demogpairs.ipynb", "demogpairs_rf_vit-emotion_RandomForestClassifier.json"),
    ("2.4.3_rf_vit-age_demogpairs.ipynb", "demogpairs_rf_vit-age_RandomForestClassifier.json"),
    ("2.4.4_rf_vit-face-age_demogpairs.ipynb", "demogpairs_rf_vit-face-age_RandomForestClassifier.json"),
    ("2.4.5_rf_vit-emotion-age_demogpairs.ipynb", "demogpairs_rf_vit-emotion-age_RandomForestClassifier.json"),
    ("2.4.6_rf_vit-emotion-face_demogpairs.ipynb", "demogpairs_rf_vit-emotion-face_RandomForestClassifier.json"),
    ("2.4.7_rf_vit-face-emotion-age_demogpairs.ipynb", "demogpairs_rf_vit-face-emotion-age_RandomForestClassifier.json"),

    # --- Batch 4: Support Vector Machine (Sisa SVM, ~8-10 jam total) ---
    ("2.1.2_svm_vit-emotion_demogpairs.ipynb", "demogpairs_svm_vit-emotion_SVC.json"),
    ("2.1.3_svm_vit-age_demogpairs.ipynb", "demogpairs_svm_vit-age_SVC.json"),
    ("2.1.4_svm_vit-face-age_demogpairs.ipynb", "demogpairs_svm_vit-face-age_SVC.json"),
    ("2.1.5_svm_vit-emotion-age_demogpairs.ipynb", "demogpairs_svm_vit-emotion-age_SVC.json"),
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

def wait_for_217():
    log("=" * 60)
    log("MONITORING AKTIF: Menunggu notebook 2.1.7 selesai dieksekusi...")
    log(f"Target file: {TRIGGER_RESULT_217}")
    log("=" * 60)
    
    poll_count = 0
    while not is_valid_result(TRIGGER_RESULT_217):
        time.sleep(20)
        poll_count += 1
        if poll_count % 15 == 0:  # Setiap 5 menit beri update
            log("Masih menunggu 2.1.7 (training SVM Tri-Domain masih berlangsung)...")
            
    # File sudah ada dan valid!
    time.sleep(5)  # Beri jeda 5 detik agar flush IO tuntas
    try:
        with open(TRIGGER_RESULT_217, "r", encoding="utf-8") as f:
            res = json.load(f)
        acc = res.get("test_accuracy", 0) * 100
        f1 = res.get("test_f1", 0)
        log("=" * 60)
        log(f"*** 2.1.7 SELESAI DENGAN SUKSES! ***")
        log(f"Test Accuracy 2.1.7: {acc:.2f}% | Macro-F1: {f1:.4f}")
        log("=" * 60)
    except Exception as e:
        log(f"2.1.7 selesai, tetapi gagal membaca detail ringkasan: {e}")

def run_notebook(nb_name, result_json_name):
    nb_path = os.path.join(EXPERIMENT_DIR, nb_name)
    result_path = os.path.join(RESULTS_DIR, result_json_name)

    if is_valid_result(result_path):
        try:
            with open(result_path, "r", encoding="utf-8") as f:
                res = json.load(f)
            acc = res.get("test_accuracy", 0) * 100
            log(f"[SKIP] {nb_name} sudah selesai sebelumnya (Akurasi: {acc:.2f}%).")
        except Exception:
            log(f"[SKIP] {nb_name} sudah selesai sebelumnya.")
        return True

    log("-" * 60)
    log(f"[START] Menjalankan: {nb_name}")
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
            log(f"[DONE] {nb_name} SUKSES dalam {mins:.1f} menit! (Akurasi: {acc:.2f}%, F1: {f1:.4f})")
            return True
        else:
            log(f"[ERROR] {nb_name} gagal atau returncode {proc.returncode}!")
            if proc.stderr:
                log(f"[STDERR]: {proc.stderr[-500:]}")
            return False
    except Exception as e:
        log(f"[EXCEPTION] Terjadi error saat mengeksekusi {nb_name}: {e}")
        return False

def main():
    log("MEMULAI SISTEM AUTOMATION QUEUE EXPERIMENT")
    # 1. Tunggu 2.1.7 selesai
    wait_for_217()

    # 2. Eksekusi antrean notebook berikutnya
    log("\nMEMULAI EKSEKUSI ANTREAN NOTEBOOK OTOMATIS...")
    total = len(NOTEBOOK_QUEUE)
    success_count = 0

    for idx, (nb_name, res_name) in enumerate(NOTEBOOK_QUEUE, 1):
        log(f"\n[PROGRESS {idx}/{total}]")
        ok = run_notebook(nb_name, res_name)
        if ok:
            success_count += 1
        time.sleep(3)

    log("=" * 60)
    log(f"SEMUA ANTREAN SELESAI! ({success_count}/{total} berhasil)")
    log("=" * 60)

if __name__ == "__main__":
    main()
