import subprocess
import time
import csv
import os

def run_mpi(processes):
    """Executa o código MPI e retorna tempo e resultado"""
    start_time = time.time()
    result = subprocess.run(
        f'mpiexec -n {processes} python src/main.py',
        capture_output=True, 
        text=True,
        shell=True
    )
    end_time = time.time()
    
    # Parse output
    output = result.stdout
    pi_value = "N/A"
    tempo_value = "N/A"
    
    for line in output.split('\n'):
        if 'PI estimado' in line:
            pi_value = line.split('=')[1].strip().split()[0]
        elif 'Tempo' in line:
            tempo_value = line.split('=')[1].strip().split()[0]
    
    return float(tempo_value) if tempo_value != "N/A" else end_time - start_time, pi_value

def main():
    processes_list = [1, 2, 4, 8]
    results = []
    
    os.makedirs('results', exist_ok=True)
    
    print("=== PERFILAMENTO HPC COM PYTHON ===")
    
    for processes in processes_list:
        print(f"\nExecutando com {processes} processos...")
        tempo, pi = run_mpi(processes)
        results.append((processes, tempo, pi))
        print(f"  PI: {pi} | Tempo: {tempo:.4f}s")
    
    # Calcula speedup e eficiência
    tempo_1_processo = results[0][1]
    final_results = []
    
    for processes, tempo, pi in results:
        if processes == 1:
            speedup = 1.0
            efficiency = 1.0
        else:
            speedup = tempo_1_processo / tempo
            efficiency = speedup / processes
        
        final_results.append((processes, tempo, speedup, efficiency, pi))
    
    # Salva CSV
    with open('results/profiling_python.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['processos', 'tempo_segundos', 'speedup', 'eficiencia', 'pi_estimado'])
        for row in final_results:
            writer.writerow(row)
    
    # Mostra resultados
    print("\n=== RESULTADOS FINAIS ===")
    print("Processos | Tempo (s) | Speedup | Eficiência | π Estimado")
    print("-" * 60)
    for processes, tempo, speedup, efficiency, pi in final_results:
        print(f"{processes:9} | {tempo:9.4f} | {speedup:7.2f} | {efficiency:9.2f} | {pi}")

if __name__ == "__main__":
    main()