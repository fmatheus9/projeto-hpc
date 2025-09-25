<<<<<<< HEAD
# Projeto HPC — Estimação de π via Método de Monte Carlo Paralelizado

##  Visão Geral

Este projeto implementa a estimação do número π utilizando o método de Monte Carlo paralelizado com **MPI (Message Passing Interface)**. O objetivo é demonstrar técnicas de computação de alto desempenho (HPC) através de um problema clássico que permite excelente escalabilidade em ambientes distribuídos.

**Problema**: Estimar o valor de π usando simulações probabilísticas  
**Método**: Método de Monte Carlo com paralelização MPI  
**Paralelismo**: MPI para distribuição entre processos  
**Ambiente**: Santos Dumont (SLURM) + desenvolvimento local

## Relevância

- **Benchmark clássico** para avaliação de desempenho em HPC
- **Caso de estudo** ideal para aprendizado de MPI e SLURM
- **Problema embaraçosamente paralelo** - excelente para escalabilidade
- **Base** para problemas mais complexos de simulação científica

## Requisitos

### Ambiente Local
- Python 3.10+
- MPI (OpenMPI ou MPICH)
- numpy
- mpi4py

### Santos Dumont
- SLURM workload manager
- Módulos: python/3.10, mpi

## Como Executar

### 1. Preparação do ambiente
bash
git clone <url-do-repositorio>
cd projeto-hpc

### 2. Instalação de dependências
bash scripts/build.sh

### 3. Execução local
**Teste serial**
-python3 src/main.py

**Teste paralelo (4 processos)**
- bash scripts/run_local.sh

**Perfilamento completo**
- bash scripts/profile.sh

### 4. Geração de dados de teste
**Dataset básico**
- python3 data_sample/gerador_dados.py --tamanho 1000000 --salvar

**Dataset completo**
- python3 data_sample/gerador_dados.py --dataset-completo
=======
# Projeto HPC — Estimação de π via Método de Monte Carlo Paralelizado

##  Visão Geral

Este projeto implementa a estimação do número π utilizando o método de Monte Carlo paralelizado com **MPI (Message Passing Interface)**. O objetivo é demonstrar técnicas de computação de alto desempenho (HPC) através de um problema clássico que permite excelente escalabilidade em ambientes distribuídos.

**Problema**: Estimar o valor de π usando simulações probabilísticas  
**Método**: Método de Monte Carlo com paralelização MPI  
**Paralelismo**: MPI para distribuição entre processos  
**Ambiente**: Santos Dumont (SLURM) + desenvolvimento local

## Relevância

- **Benchmark clássico** para avaliação de desempenho em HPC
- **Caso de estudo** ideal para aprendizado de MPI e SLURM
- **Problema embaraçosamente paralelo** - excelente para escalabilidade
- **Base** para problemas mais complexos de simulação científica

## Requisitos

### Ambiente Local
- Python 3.10+
- MPI (OpenMPI ou MPICH)
- numpy
- mpi4py

### Santos Dumont
- SLURM workload manager
- Módulos: python/3.10, mpi

## Como Executar

### 1. Preparação do ambiente
bash
git clone <url-do-repositorio>
cd projeto-hpc

### 2. Instalação de dependências
bash scripts/build.sh

### 3. Execução local
**Teste serial**
-python3 src/main.py

**Teste paralelo (4 processos)**
- bash scripts/run_local.sh

**Perfilamento completo**
- bash scripts/profile.sh

### 4. Geração de dados de teste
**Dataset básico**
- python3 data_sample/gerador_dados.py --tamanho 1000000 --salvar

**Dataset completo**
- python3 data_sample/gerador_dados.py --dataset-completo
>>>>>>> 612f558 (Projeto HPC - Monte Carlo MPI para Santos Dumont)
