#!/usr/bin/env bash
set -e

echo "=== PERFILAMENTO DO PROJETO HPC ==="
echo "Data: $(date)"
echo ""

# Configurações
PROCESSOS="1 2 4 8 16"
AMOSTRAS=10000000
ARQUIVO_RESULTADOS="results/profiling_$(date +%Y%m%d_%H%M%S).csv"

# Cabeçalho do CSV
echo "processos,amostras,tempo_segundos,speedup,eficiencia,pi_estimado,memoria_mb" > $ARQUIVO_RESULTADOS

# Função para medir memória
medir_memoria() {
    if command -v ps > /dev/null; then
        ps -o rss= -p $1 | awk '{print $1/1024}'
    else
        echo "N/A"
    fi
}

echo "Executando perfilamento com $AMOSTRAS amostras..."
echo "Processos: $PROCESSOS"
echo ""

TEMPO_REFERENCIA=0

for np in $PROCESSOS; do
    echo "-> Executando com $np processos..."
    
    # Limpa cache se possível
    if [ "$(whoami)" = "root" ]; then
        sync && echo 3 > /proc/sys/vm/drop_caches
    fi
    
    # Executa e mede tempo
    COMANDO="mpirun -np $np python3 src/main.py"
    
    if command -v /usr/bin/time > /dev/null; then
        # Usa time para medição precisa
        SAIDA=$(/usr/bin/time -f "%e %M" $COMANDO 2>&1)
        TEMPO=$(echo "$SAIDA" | tail -1 | awk '{print $1}')
        MEMORIA=$(echo "$SAIDA" | tail -1 | awk '{print $2}')
        MEMORIA_MB=$(echo "scale=2; $MEMORIA/1024" | bc)
        PI_ESTIMADO=$(echo "$SAIDA" | grep "π estimado" | awk '{print $4}')
    else
        # Fallback básico
        INICIO=$(date +%s.%N)
        SAIDA=$($COMANDO)
        FIM=$(date +%s.%N)
        TEMPO=$(echo "$FIM - $INICIO" | bc)
        MEMORIA_MB="N/A"
        PI_ESTIMADO=$(echo "$SAIDA" | grep "π estimado" | awk '{print $4}')
    fi
    
    # Calcula speedup e eficiência
    if [ $np -eq 1 ]; then
        TEMPO_REFERENCIA=$TEMPO
        SPEEDUP=1.00
        EFICIENCIA=1.00
    else
        SPEEDUP=$(echo "scale=2; $TEMPO_REFERENCIA / $TEMPO" | bc)
        EFICIENCIA=$(echo "scale=2; $SPEEDUP / $np" | bc)
    fi
    
    # Salva resultados
    echo "$np,$AMOSTRAS,$TEMPO,$SPEEDUP,$EFICIENCIA,$PI_ESTIMADO,$MEMORIA_MB" >> $ARQUIVO_RESULTADOS
    
    echo "   Tempo: ${TEMPO}s | Speedup: ${SPEEDUP} | Eficiência: ${EFICIENCIA}"
    echo "   π estimado: $PI_ESTIMADO"
    echo ""
done

echo "=== RESULTADOS FINAIS ==="
echo "Arquivo gerado: $ARQUIVO_RESULTADOS"
echo ""
cat $ARQUIVO_RESULTADOS

# Gera gráfico simples se python estiver disponível
if command -v python3 > /dev/null; then
    python3 << END
import pandas as pd
import matplotlib.pyplot as plt
import sys

try:
    df = pd.read_csv('$ARQUIVO_RESULTADOS')
    
    # Gráfico de Speedup
    plt.figure(figsize=(10, 6))
    plt.plot(df['processos'], df['processos'], 'r--', label='Ideal')
    plt.plot(df['processos'], df['speedup'], 'bo-', label='Real')
    plt.xlabel('Número de Processos')
    plt.ylabel('Speedup')
    plt.title('Speedup - Estimaçao de π Monte Carlo')
    plt.legend()
    plt.grid(True)
    plt.savefig('results/speedup_plot.png', dpi=300, bbox_inches='tight')
    
    # Gráfico de Tempo
    plt.figure(figsize=(10, 6))
    plt.plot(df['processos'], df['tempo_segundos'], 'go-')
    plt.xlabel('Número de Processos')
    plt.ylabel('Tempo (segundos)')
    plt.title('Tempo de Execução - Estimaçao de π Monte Carlo')
    plt.grid(True)
    plt.savefig('results/tempo_plot.png', dpi=300, bbox_inches='tight')
    
    print("Gráficos gerados em results/speedup_plot.png e results/tempo_plot.png")
except Exception as e:
    print("Erro ao gerar gráficos:", e)
END
fi

echo ""
echo "Perfilamento concluído!"