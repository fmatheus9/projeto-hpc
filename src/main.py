from mpi4py import MPI
import time
from monte_carlo import monte_carlo_pi

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Total de amostras
total_amostras = 10_000_000

# Divisão de trabalho
amostras_por_processo = total_amostras // size

# Sincronização
comm.Barrier()
t0 = time.time()

# Cada processo gera sua parte
local_pi = monte_carlo_pi(amostras_por_processo)

# Redução: soma todas as estimativas e divide pelo número de processos
pi_estimado = comm.reduce(local_pi, op=MPI.SUM, root=0)
if rank == 0:
    pi_estimado /= size
    t1 = time.time()
    print(f"π estimado = {pi_estimado:.10f}")
    print(f"Tempo = {t1 - t0:.4f} segundos")
    print(f"Processos = {size}")
else:
    pi_estimado = None