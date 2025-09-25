#!/bin/bash
#SBATCH --job-name=monte_carlo_scaling
#SBATCH --output=results/scaling_%j.out
#SBATCH --error=results/scaling_%j.err
#SBATCH --time=00:20:00
#SBATCH --partition=cpu
#SBATCH --mem=4G

echo "=== TESTE DE ESCALABILIDADE NO SANTOS DUMONT ==="
echo "Data: $(date)"
echo "Testando com 1, 2, 4, 8, 16, 32 processos"
echo ""

module load python/3.10
module load openmpi

python -m venv venv_scale
source venv_scale/bin/activate
pip install numpy mpi4py

# Testa diferentes números de processos
for procs in 1 2 4 8 16 32; do
    echo "=== Executando com $procs processos ==="
    srun --ntasks=$procs python src/main.py
    echo "----------------------------------------"
    echo ""
done

deactivate
echo "=== TESTE DE ESCALABILIDADE CONCLUÍDO ==="
echo "Data: $(date)"
