#!/usr/bin/env python3
"""
Simula a execução no Santos Dumont localmente
"""

import subprocess
import time
import os

def simulate_slurm_job(processes, job_name):
    """Simula um job SLURM localmente"""
    print(f"\n{'='*60}")
    print(f"SIMULANDO SLURM JOB: {job_name}")
    print(f"Processos: {processes} | Tempo limite: 10 minutos")
    print(f"{'='*60}")
    
    # Simula o comando srun
    cmd = f"mpiexec -n {processes} python src/main.py"
    
    start_time = time.time()
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    end_time = time.time()
    
    # Mostra resultados
    print("SAÍDA DO PROGRAMA:")
    print(result.stdout)
    
    if result.stderr:
        print("ERROS:")
        print(result.stderr)
    
    print(f"\nTempo de execução: {end_time - start_time:.2f} segundos")
    print(f"{'='*60}")

def main():
    print("🎯 SIMULAÇÃO SANTOS DUMONT - MONTE CARLO MPI")
    
    # Testa diferentes configurações (como no SD)
    configs = [
        (1, "Job Serial"),
        (2, "Job 2 Processos"), 
        (4, "Job 4 Processos"),
        (8, "Job 8 Processos"),
        (16, "Job 16 Processos (SD Padrão)")
    ]
    
    for processes, job_name in configs:
        simulate_slurm_job(processes, job_name)
        
        # Pausa entre jobs
        if processes < 16:
            input("Pressione Enter para próximo job...")

if __name__ == "__main__":
    main()