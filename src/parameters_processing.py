# --- Imports --- #
import pandas as pd
from eda import EDA
import json

# --- Carregando os Dados --- #
eda = EDA()
# --- #
path = eda.get_instances_path # coleta o diretório das instâncias.
# --- #
dataframes = eda.read_instances(path, file_extension='xlsx') # Lê as instâncias presentes no diretório.
data = dataframes[0].copy() # coleta o dataframe.

# --- Pré-processamento de parâmetros do modelo de otimização --- #
# --- Quantidade de caixas --- #
quantidade_de_caixas = int(data['Caixa Id'].nunique())

# --- Quantidade de Peças --- #
quantidade_de_pecas = int(data['Peças'].sum())

# --- Quantidade de itens distintos (SKUs) ---- #
quantidade_de_itens = int(data['Item'].nunique())

# --- Quantidade de Peças por Caixa --- #
pecas_por_caixa = (data.groupby('Caixa Id')['Peças']
                       .sum()
                       .reset_index()
                       )

# --- Lista de itens em cada caixa --- #
itens_por_caixa = (data.groupby('Caixa Id')['Item']
                   .unique()
                   .apply(list)
                   .to_dict())

# --- Lista de itens em cada caixa --- #
pecas_por_caixa_lista = [
    {
        'Caixa' : int(row['Caixa Id']), # Converte 'Caixa Id' para inteiro.
        'Peças' : int(row['Peças']), # Converte 'Peças' para inteiro.
        'Itens' : list(map(str, itens_por_caixa.get(row['Caixa Id'], []))) # Converte 'Item' para uma lista de strings
    }
    for _, row in pecas_por_caixa.iterrows()
]

# --- Capacidade por onda --- #
capacidade_por_onda = 2000 # Dado do problema.

# --- Quantidade de ondas necessárias --- #
ondas_necessarias = int((quantidade_de_pecas // capacidade_por_onda) + 1)

# --- Armazenamento dos dados de parâmetros em um dicionário --- #
parametros_pre_processados = {
    'Quantidade de caixas distintas' : quantidade_de_caixas,
    'Quantidade total de peças' : quantidade_de_pecas,
    'Quantidade de itens distintos' : quantidade_de_itens,
    'Peças e Itens por caixa' : pecas_por_caixa_lista,
    'Capacidade de produção por onda' : capacidade_por_onda,
    'Quantidade necessária de ondas' : ondas_necessarias
}

# --- Converte para Json e exporta --- #
with open('parametros_pre_processados.json', mode='w', encoding='utf-8') as arquivo_json:
    try:
        json.dump(parametros_pre_processados, arquivo_json, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f'Erro! Não foi possível exportar os dados: {e}')