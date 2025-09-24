import numpy as np

def monte_carlo_pi(n):
    """Estima π usando n amostras de Monte Carlo."""
    x = np.random.uniform(-1, 1, n)
    y = np.random.uniform(-1, 1, n)
    dentro = np.sum(x**2 + y**2 <= 1)
    return 4 * dentro / n