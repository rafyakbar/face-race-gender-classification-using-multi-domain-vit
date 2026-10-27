@echo off
title Multi-ViT Experiment Queue Runner
cd /d "%~dp0\.."
echo ======================================================================
echo    Multi-ViT Demographic Pairs Automated Experiment Runner
echo ======================================================================
echo Mengaktifkan environment conda torch-gpu...
call C:\Users\Rafy\miniconda3\condabin\conda.bat activate torch-gpu

echo Menjalankan auto_run_experiments.py menggunakan env torch-gpu...
"C:\Users\Rafy\miniconda3\envs\torch-gpu\python.exe" scripts\auto_run_experiments.py

echo ======================================================================
echo Seluruh antrean eksperimen telah selesai!
echo ======================================================================
pause
