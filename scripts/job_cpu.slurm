#!/bin/bash
#SBATCH --job-name=monte_carlo_pi
#SBATCH --output=results/%x_%j.out
#SBATCH --error=results/%x_%j.err
#SBATCH --time=00:10:00
#SBATCH --ntasks=16
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G
#SBATCH --partition=cpu

echo "=== INICIANDO EXPERIMENTO NO SANTOS DUMONT ==="
echo "Data: $(date)"
echo "Host: $(hostname)"
echo "Job ID: $SLURM_JOB_ID"
echo "Processos: $SLURM_NTASKS"
echo ""

# Carrega módulos do SD
module load python/3.10
module load openmpi

# Cria ambiente virtual (boas práticas)
python -m venv venv_sd
source venv_sd/bin/activate

# Instala dependências
pip install --upgrade pip
pip install numpy mpi4py

echo "=== EXECUTANDO EXPERIMENTO ==="
srun python src/main.py

echo ""
echo "=== EXPERIMENTO CONCLUÍDO ==="
echo "Data: $(date)"
deactivate