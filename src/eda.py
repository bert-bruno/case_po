# --- Imports --- #
from dataclasses import dataclass
from pathlib import Path
import pandas as pd

# --- Classe para Análise Exploratória --- #

class EDA:

    @property
    def get_instances_path(cls):
        ''' Retorna o diretório daas instâncias.
            - IMPORTANTE: este script foi desenvolvido respeitando uma determinada estrutura de diretórios.
                - As instâncias deverão constar no diretório `data`;
                - Os scripts devem estar dentro do diretório `src`.
                Caso esta estrutura, por algum motivo, não possa ser respeitada, recomenda-se ao usuário que
                faça a entrada manual dos dados, ou, ainda, que modifique este script.
            - Sprints futuras: implementar teste de validação do path.
        '''
        # --- Body --- #
        parent_path = Path.cwd().parent # coleta o diretório pai de 'src' -> raiz do projeto.
        instances_path = parent_path / 'data' # direciona ao diretório 'data' -> local onde estão as instâncias.
        # --- Output --- #
        return instances_path 

    @classmethod
    def read_instances(cls, path, file_extension: str = 'csv') -> str:
        ''' Lê e retorna as instâncias presentes na pasta.
            - file_extension = ['csv', 'xlsx'].
        '''
        # --- Body --- #
        if not Path(path).exists(): # verifica se o diretório existe.
            raise FileNotFoundError(f'O diretório {path} não foi encontrado.')
        # --- #
        instances = list(Path(path).glob(f'*.{file_extension}')) # realiza a coleta das instâncias.
        if not instances: # caso não sejam encontradas instâncias, retorna erro ao usuário.
            raise FileNotFoundError(f'Não foram encontrados arquivos com a extensão solicitada.')
        # --- #
        dataframes = [] # lista para armazenar os dataframes.
        for file in instances: # itera sobre as instâncias, verifica a extensão, lê e armazena na lista.
            if file_extension == 'csv':
                df = pd.read_csv(file)
            elif file_extension == 'xlsx':
                df = pd.read_excel(file)
            else: # caso a extensão não seja contemplada, retorna erro ao usuário.
                raise ValueError(f'Esta função não contempla esta extensão de arquivo.')
            # -- #
            dataframes.append(df)
        # --- Output --- #
        return dataframes 
