#!/bin/bash
# Script específico para o Santos Dumont

echo "=== CONFIGURANDO AMBIENTE NO SANTOS DUMONT ==="

# Carrega módulos necessários
module load python/3.10
module load openmpi

# Cria e ativa ambiente virtual
python -m venv venv_sd
source venv_sd/bin/activate

# Instala dependências
pip install --upgrade pip
pip install numpy mpi4py

echo "=== AMBIENTE CONFIGURADO ==="
echo "Para ativar o ambiente: source venv_sd/bin/activate"
echo "Para submeter jobs: sbatch scripts/job_cpu.slurm"