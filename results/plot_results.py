import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

# Encontra o arquivo de profiling mais recente
csv_files = glob.glob("results/profiling_*.csv")
if not csv_files:
    print("Nenhum arquivo de resultados encontrado!")
    exit()

latest_file = max(csv_files, key=os.path.getctime)
df = pd.read_csv(latest_file)

print("=== RESULTADOS DO PERFILAMENTO ===")
print(df)

# Gráfico de Speedup
plt.figure(figsize=(10, 6))
plt.plot(df['processos'], df['processos'], 'r--', label='Ideal', linewidth=2)
plt.plot(df['processos'], df['speedup'], 'bo-', label='Real', linewidth=2)
plt.xlabel('Número de Processos')
plt.ylabel('Speedup')
plt.title('Speedup - Estimação de π Monte Carlo')
plt.legend()
plt.grid(True)
plt.savefig('results/speedup_windows.png', dpi=300, bbox_inches='tight')

# Gráfico de Tempo
plt.figure(figsize=(10, 6))
plt.plot(df['processos'], df['tempo_segundos'], 'go-', linewidth=2)
plt.xlabel('Número de Processos')
plt.ylabel('Tempo (segundos)')
plt.title('Tempo de Execução - Estimação de π Monte Carlo')
plt.grid(True)
plt.savefig('results/tempo_windows.png', dpi=300, bbox_inches='tight')

print(f"\nGráficos salvos em:")
print("- results/speedup_windows.png")
print("- results/tempo_windows.png")