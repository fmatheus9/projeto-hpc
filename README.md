# Projeto HPC — Estimação de π via Método de Monte Carlo Paralelizado

## 📋 Visão Geral

Este projeto implementa a estimação do número π utilizando o método de Monte Carlo paralelizado com **MPI (Message Passing Interface)**. O objetivo é demonstrar técnicas de computação de alto desempenho (HPC) através de um problema clássico que permite excelente escalabilidade em ambientes distribuídos.

**Problema**: Estimar o valor de π usando simulações probabilísticas  
**Método**: Método de Monte Carlo com paralelização MPI  
**Paralelismo**: MPI para distribuição entre processos  
**Ambiente**: Santos Dumont (SLURM) + desenvolvimento local

## 🎯 Relevância

- **Benchmark clássico** para avaliação de desempenho em HPC
- **Caso de estudo** ideal para aprendizado de MPI e SLURM
- **Problema embaraçosamente paralelo** - excelente para escalabilidade
- **Base** para problemas mais complexos de simulação científica

## ⚙️ Requisitos

### Ambiente Local
- Python 3.10+
- MPI (OpenMPI ou MPICH)
- numpy
- mpi4py

### Santos Dumont
- SLURM workload manager
- Módulos: python/3.10, mpi

## 🚀 Como Executar

### 1. Preparação do ambiente
```bash
git clone <url-do-repositorio>
cd projeto-hpc
```

### 2. Instalação de dependências
```bash
bash scripts/build.sh
```

### 3. Execução local

#### Teste serial
```bash
python src/main.py
```

#### Teste paralelo (4 processos)
```bash
bash scripts/run_local.sh
```

#### Perfilamento completo
```bash
bash scripts/profile.sh
```

### 4. Geração de dados de teste

#### Dataset básico
```bash
python data_sample/gerador_dados.py --tamanho 1000000 --salvar
```

#### Dataset completo
```bash
python data_sample/gerador_dados.py --dataset-completo
```

### 5. Execução no Santos Dumont
```bash
# Acesso
ssh usuario@login.sd.lncc.br
cd /scratch/$USER/projeto-hpc

# Submissão do job
sbatch scripts/job_cpu.slurm

# Monitoramento
squeue -u $USER
tail -f results/monte_carlo_pi_*.out
```

## 📁 Estrutura do Projeto
```
projeto-hpc/
├── README.md
├── SUBMISSAO_SD.md
├── env/
│   └── requirements.txt
├── src/
│   ├── main.py
│   └── monte_carlo.py
├── data_sample/
│   └── gerador_dados.py
├── scripts/
│   ├── build.sh
│   ├── run_local.sh
│   ├── job_cpu.slurm
│   ├── job_scaling.slurm
│   └── profile.sh
├── results/
└── report/
    └── RELATORIO.pdf
```

## 🔧 Scripts Principais

### `scripts/build.sh`
Instala dependências Python (numpy, mpi4py).

### `scripts/run_local.sh`
Executa teste local com MPI (4 processos).

### `scripts/job_cpu.slurm`
Job SLURM para execução no Santos Dumont (16 processos).

### `scripts/profile.sh`
Script de perfilamento - testa escalabilidade com 1-16 processos.

## 📊 Resultados Esperados

### Saída do programa:
```
PI estimado = 3.1415926535
Tempo = 2.3456 segundos  
Processos = 16
Amostras totais = 10,000,000
```

### Métricas de desempenho:
- **Speedup**: ≈14.5× com 16 processos
- **Eficiência**: ≈91% com 16 processos
- **Precisão**: ≈10⁻⁶ de erro absoluto

## ⚠️ Troubleshooting

### Problemas comuns:
```bash
# MPI não encontrado (Linux)
sudo apt install mpich libopenmpi-dev

# Dependências missing
pip install numpy mpi4py

# Erro de permissão
chmod +x scripts/*.sh
```

### No Windows:
```bash
# Instale MS-MPI e use
mpiexec -n 4 python src/main.py
```

### No Santos Dumont:
- Use `/scratch` para dados temporários
- Não execute cargas pesadas no nó de login
- Monitore jobs com `squeue` e `sacct`

## 📈 Análise de Desempenho

O projeto inclui ferramentas para análise completa:
- Perfilamento automático com diferentes números de processos
- Geração de gráficos de speedup e tempo de execução
- Métricas de eficiência e overhead de comunicação

## 👥 Autores

- Matheus Ferrarezi Mesquita Fagundes 
- Disciplina: Sistemas Distribuidos 
- Instituição: Uni-FACEF 
- Data: 2025-09-24

