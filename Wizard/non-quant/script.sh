#!/bin/bash -l
#SBATCH --partition=gpu_long
#SBATCH --gres=gpu:1
#SBATCH --time=24:00:00
#SBATCH --output=/work/tomohiro-w/logs/%j.log
#SBATCH --error=/work/tomohiro-w/logs/%j.err

cd /work/tomohiro-w/utg/Wizard/non-quant
/work/tomohiro-w/utg/.venv/bin/python main.py
