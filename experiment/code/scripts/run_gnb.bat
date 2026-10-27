@echo off
title GNB Multi-ViT Experiment Runner
cd /d "%~dp0\.."
echo ======================================================================
echo    Multi-ViT Demographic Pairs - Gaussian Naive Bayes Runner
echo ======================================================================
call C:\Users\Rafy\miniconda3\condabin\conda.bat activate torch-gpu
"C:\Users\Rafy\miniconda3\envs\torch-gpu\python.exe" scripts\run_gnb_queue.py
pause
