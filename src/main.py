from mpi4py import MPI
import time
import random

def monte_carlo_pi(n):
    """Estima π usando n amostras de Monte Carlo."""
    dentro = 0
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x*x + y*y <= 1:
            dentro += 1
    return 4 * dentro / n

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Ajusta o número de amostras para ser mais rápido no Windows
    total_amostras = 1000000 // size
    
    t0 = time.time()
    local_pi = monte_carlo_pi(total_amostras)
    pi_estimado = comm.reduce(local_pi, op=MPI.SUM, root=0)
    
    if rank == 0:
        pi_estimado /= size
        t1 = time.time()
        print(f"PI estimado = {pi_estimado:.10f}")
        print(f"Tempo = {t1 - t0:.4f} segundos")
        print(f"Processos = {size}")
        print(f"Amostras totais = {total_amostras * size:,}")
