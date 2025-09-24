#!/bin/bash
#SBATCH --job-name=monte_carlo_pi
#SBATCH --output=results/%x_%j.out
#SBATCH --error=results/%x_%j.err
#SBATCH --time=00:10:00
#SBATCH --ntasks=16
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G
#SBATCH --partition=cpu

module load python/3.10 mpi

echo "Iniciando em $(date)"
srun python3 src/main.py
echo "Finalizado em $(date)"