# 🚀 Guia de Submissão - Santos Dumont

# Como usar no SD (resumo)

1. Faça login no nó de acesso do SD.
2. Crie um ambiente (módulos/conda) e compile (scripts/build.sh).
3. Copie/prepare dados em /scratch (evitar saturar /home).
4. Submeta: sbatch scripts/job_cpu.slurm (ou job_gpu.slurm).
5. Acompanhe: squeue -u $USER, sacct -j <jobid>, tail -f results/*.out.
6. Nunca rode cargas pesadas no nó de login.
7. Resultados e logs → pasta results/.