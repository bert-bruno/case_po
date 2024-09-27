# --- Imports ---#
import json
import pyomo.environ as pyo
import pandas as pd
from pathlib import Path

# --- Inicialização de objeto do Pyomo --- #
model = pyo.ConcreteModel()

# --- Leitura de dados de entrada --- #
input_data_path = Path.cwd().parent / 'data' /  'Teste Pesquisa Operacional - Dados.xlsx' # coleta o caminho do arquivo de dados de entrada.
input_data = pd.read_excel(input_data_path) # Transporte o arquivo de dados de entrada para um pandas DataFrame.

# --- Leitura de dados de parâmetros pré-processados --- #
pre_processed_parameters_path = Path.cwd() / 'pre_processed_parameters.json' # coleta o caminho do arquivo de parâmetros pré-processados.
# --- #
with open(pre_processed_parameters_path, mode='r', encoding='utf8') as file: # abre o arquivo de parâmetros pré-processados.
    pre_processed_parameters_data = json.load(file) # carrega o arquivo de parâmetros pré-processados.
# --- #

# --- Inicialização de variáveis de parâmetros --- #
wave_capacity = pre_processed_parameters_data['Capacidade de produção por onda'] # Inicializa a capacidade de produção por onda.
# --- #
distinct_boxes_quantity = pre_processed_parameters_data['Quantidade de caixas distintas'] # Inicializa a quantidade de caixas distintas.
# --- #
total_itens_quantity = pre_processed_parameters_data['Quantidade total de Peças'] # Inicializa a quantidade total de peças.
# --- #
distinct_itens_quantity = pre_processed_parameters_data['Quantidade de Itens distintos'] # Inicializa a quantidade de itens distintos.
# --- #
itens_per_box_quantity = { 
    pre_processed_parameters_data['Quantidade de peças por caixa']}