#!/usr/bin/env python3
"""
Gerador de dados sintéticos para o projeto Monte Carlo π
Permite gerar conjuntos de dados de diferentes tamanhos para teste
"""

import numpy as nps
import argparse
import time
import json
import os

def gerar_dados_monte_carlo(tamanho, seed=None, salvar_arquivo=False):
    """
    Gera dados sintéticos para simulação Monte Carlo
    
    Args:
        tamanho (int): Número de pontos a gerar
        seed (int): Seed para reproducibilidade
        salvar_arquivo (bool): Se deve salvar em arquivo
    
    Returns:
        dict: Dados gerados e metadados
    """
    
    if seed is not None:
        np.random.seed(seed)
    
    print(f"Gerando {tamanho:,} pontos aleatórios...")
    inicio = time.time()
    
    # Gera coordenadas x, y uniformemente distribuídas
    x = np.random.uniform(-1, 1, tamanho)
    y = np.random.uniform(-1, 1, tamanho)
    
    # Calcula quais pontos estão dentro do círculo
    distancia_quadrado = x**2 + y**2
    dentro_circulo = distancia_quadrado <= 1
    pontos_dentro = np.sum(dentro_circulo)
    
    # Estima π
    pi_estimado = 4 * pontos_dentro / tamanho
    erro = abs(pi_estimado - np.pi)
    
    fim = time.time()
    tempo_geracao = fim - inicio
    
    # Metadados
    metadados = {
        'tamanho_amostra': tamanho,
        'seed_utilizada': seed,
        'pi_estimado': float(pi_estimado),
        'erro_absoluto': float(erro),
        'pontos_dentro_circulo': int(pontos_dentro),
        'pontos_fora_circulo': int(tamanho - pontos_dentro),
        'tempo_geracao_segundos': float(tempo_geracao),
        'data_geracao': time.strftime('%Y-%m-%d %H:%M:%S')
    }
    
    dados = {
        'x': x.tolist(),
        'y': y.tolist(), 
        'dentro_circulo': dentro_circulo.tolist(),
        'metadados': metadados
    }
    
    if salvar_arquivo:
        # Cria diretório se não existir
        os.makedirs('data_sample', exist_ok=True)
        
        # Salva em formato numpy para eficiência
        arquivo_npy = f'data_sample/dados_{tamanho}.npz'
        np.savez_compressed(arquivo_npy, x=x, y=y, dentro_circulo=dentro_circulo)
        
        # Salva metadados em JSON
        arquivo_json = f'data_sample/metadados_{tamanho}.json'
        with open(arquivo_json, 'w') as f:
            json.dump(metadados, f, indent=2)
        
        print(f"Dados salvos em {arquivo_npy}")
        print(f"Metadados salvos em {arquivo_json}")
    
    print(f"Geração concluída em {tempo_geracao:.2f} segundos")
    print(f"π estimado: {pi_estimado:.10f}")
    print(f"Erro absoluto: {erro:.10f}")
    print(f"Pontos dentro do círculo: {pontos_dentro}/{tamanho} ({pontos_dentro/tamanho*100:.2f}%)")
    
    return dados

def gerar_dataset_completo():
    """Gera um conjunto completo de dados para testes"""
    
    tamanhos = [1000, 10000, 100000, 1000000, 10000000]
    seeds = [42, 123, 456, 789, 999]
    
    print("=== GERANDO DATASET COMPLETO PARA TESTES ===")
    print(f"Tamanhos: {tamanhos}")
    print(f"Seeds: {seeds}")
    print()
    
    resultados = {}
    
    for i, tamanho in enumerate(tamanhos):
        seed = seeds[i % len(seeds)]
        print(f"\n--- Gerando dataset {i+1}/{len(tamanhos)} ---")
        print(f"Tamanho: {tamanho:,} | Seed: {seed}")
        
        dados = gerar_dados_monte_carlo(tamanho, seed, salvar_arquivo=True)
        resultados[tamanho] = dados['metadados']
    
    # Salva sumário
    sumario = {
        'datasets_gerados': len(tamanhos),
        'tamanhos_disponiveis': tamanhos,
        'resultados': resultados
    }
    
    with open('data_sample/sumario_datasets.json', 'w') as f:
        json.dump(sumario, f, indent=2)
    
    print(f"\n=== DATASET COMPLETO GERADO ===")
    print(f"Sumário salvo em data_sample/sumario_datasets.json")

def main():
    parser = argparse.ArgumentParser(description='Gerador de dados para Monte Carlo π')
    parser.add_argument('--tamanho', type=int, default=1000000, 
                       help='Número de pontos a gerar (padrão: 1.000.000)')
    parser.add_argument('--seed', type=int, default=42, 
                       help='Seed para reproducibilidade (padrão: 42)')
    parser.add_argument('--salvar', action='store_true',
                       help='Salvar dados em arquivo')
    parser.add_argument('--dataset-completo', action='store_true',
                       help='Gerar dataset completo para testes')
    
    args = parser.parse_args()
    
    if args.dataset_completo:
        gerar_dataset_completo()
    else:
        gerar_dados_monte_carlo(args.tamanho, args.seed, args.salvar)

if __name__ == '__main__':
    main()