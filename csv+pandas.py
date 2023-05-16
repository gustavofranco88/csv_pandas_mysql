import pandas as pd
from zipfile import ZipFile

with ZipFile('dados.zip', 'r') as dados:
    dados.extractall()

origem = pd.read_csv('origem-dados.csv')
tipos = pd.read_csv('tipos.csv')

dados_criticos = origem[origem['status'] == 'CRITICO']
dados_criticos = dados_criticos.merge(tipos, left_on='tipo', right_on='id')
dados_criticos = dados_criticos.sort_values(by='created_at')
dados_criticos.to_csv('dados_criticos.csv', index=False)
print(dados_criticos)

'''
    dtaframe esta com as duas colunas da tabela tipos'''