# Importando as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt


# Lendo o arquivo CSV e armazenando os dados em um DataFrame
df = pd.read_csv('sales_home.csv')

# Exibindo as primeiras linhas do DataFrame
print(df.head())

# Obtendo informações gerais sobre o DataFrame
print(df.info())

# Calculando algumas estatísticas básicas do DataFrame
print(df.describe())

# Plotando um gráfico de barras com as vendas totais por região
"df.groupby()['Sales'].sum().plot(kind='bar')"
plt.show()
