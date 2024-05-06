import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt

def calcular_variancia_populacional(desvios):
    soma_desvios = sum(desvios)
    qtd_itens = len(desvios)
    variancia_populacional = soma_desvios / qtd_itens
    return variancia_populacional

def calcular_desvio_padrao(variancia_populacional):
    return sqrt(variancia_populacional)

def calcular_mediana(valores):
    valores_ordenados = sorted(valores)
    tamanho = len(valores_ordenados)
    if tamanho % 2 == 0:
        return (valores_ordenados[tamanho // 2 - 1] + valores_ordenados[tamanho // 2]) / 2
    else:
        return valores_ordenados[tamanho // 2]

dados = pd.read_csv('main-data.csv')
ano_selecionado = input("Digite o ano desejado para calcular a média das linguagens: ")
linguagens_interesse = ["JavaScript", "Python", "Shell", "Java", "Dockerfile", "TypeScript"]
dados_filtrados = dados[(dados['language'].isin(linguagens_interesse)) & (dados['year'] == int(ano_selecionado))]
media_pushes_por_linguagem = dados_filtrados.groupby('language')['num_pushers'].mean()
medianas_por_linguagem = [calcular_mediana(dados_filtrados[dados_filtrados['language'] == linguagem]['num_pushers']) for linguagem in linguagens_interesse]
modas_por_linguagem = dados_filtrados.groupby('language')['num_pushers'].apply(lambda x: x.mode().values[0] if not x.mode().empty else None)

desvios_por_linguagem = []
for linguagem in linguagens_interesse:
    valores_pushes = dados_filtrados[dados_filtrados['language'] == linguagem]['num_pushers']
    media_pushes = media_pushes_por_linguagem[linguagem]
    desvios = [(valor - media_pushes) ** 2 for valor in valores_pushes]
    desvios_por_linguagem.append(desvios)

variancias_populacionais = [sum(desvios) / len(desvios) for desvios in desvios_por_linguagem]

desvios_padrao = [calcular_desvio_padrao(variancia) for variancia in variancias_populacionais]

coefs_variacao = [(desvio_padrao / media_pushes) * 100 for desvio_padrao, media_pushes in zip(desvios_padrao, media_pushes_por_linguagem)]

cores = ['blue', 'green', 'orange', 'red', 'cyan', 'magenta']

# Plotando o gráfico de barras da média
plt.figure(figsize=(10, 6))
media_pushes_por_linguagem.plot(kind='bar', color=cores)
plt.title(f'Média de Pushes por Linguagem de Programação em {ano_selecionado}')
plt.xlabel('Linguagem de Programação')
plt.ylabel('Média de Pushes')
plt.xticks(rotation=45)
plt.grid(axis='y')

for index, value in enumerate(media_pushes_por_linguagem):
    plt.text(index, value, f'{value:.2f}', ha='center', va='bottom')

plt.tight_layout()
plt.show()

# Plotando o gráfico de linhas da mediana
plt.figure(figsize=(10, 6))
plt.plot(linguagens_interesse, medianas_por_linguagem, marker='H', markerfacecolor='blue', markeredgecolor='black', linestyle='None')
plt.title(f'Mediana de Pushes por Linguagem de Programação em {ano_selecionado}')
plt.xlabel('Linguagem de Programação')
plt.ylabel('Mediana de Pushes')
plt.xticks(rotation=45)
plt.grid(axis='y')

for index, value in enumerate(medianas_por_linguagem):
    plt.text(index, value, f'{value:.2f}', ha='left', va='bottom', weight='bold', fontsize=11)

plt.tight_layout()
plt.show()

# Plotando o gráfico de linhas da moda
plt.figure(figsize=(10, 6))
plt.plot(linguagens_interesse, modas_por_linguagem, marker='o', markerfacecolor='orange', markeredgecolor='black', linestyle='None')
plt.title(f'Moda de Pushes por Linguagem de Programação em {ano_selecionado}')
plt.xlabel('Linguagem de Programação')
plt.ylabel('Moda de Pushes')
plt.xticks(rotation=45)
plt.grid(axis='y')

for index, value in enumerate(modas_por_linguagem):
    if value is not None:
        plt.text(index, value, f'{value:.2f}', ha='left', va='bottom', weight='bold', fontsize=11)
    else:
        plt.text(index, 0, 'N/A', ha='left', va='bottom', weight='bold', fontsize=11)

plt.tight_layout()
plt.show()


# Plotando o gráfico de barras da variância populacional
plt.figure(figsize=(10, 6))
plt.bar(linguagens_interesse, variancias_populacionais, color=cores)
plt.title(f'Variância Populacional de Pushes por Linguagem de Programação em {ano_selecionado}')
plt.xlabel('Linguagem de Programação')
plt.ylabel('Variância Populacional de Pushes')
plt.xticks(rotation=45)
plt.grid(axis='y')

for index, value in enumerate(variancias_populacionais):
    plt.text(index, value, f'{value:.2f}', ha='center', va='bottom')

plt.tight_layout()
plt.show()

# Plotando o gráfico de barras do desvio padrão
plt.figure(figsize=(10, 6))
plt.bar(linguagens_interesse, desvios_padrao, color=cores)
plt.title(f'Desvio Padrão de Pushes por Linguagem de Programação em {ano_selecionado}')
plt.xlabel('Linguagem de Programação')
plt.ylabel('Desvio Padrão de Pushes')
plt.xticks(rotation=45)
plt.grid(axis='y')

for index, value in enumerate(desvios_padrao):
    plt.text(index, value, f'{value:.2f}', ha='center', va='bottom')

plt.tight_layout()
plt.show()

# Plotando o gráfico de linhas do coeficiente de variação
plt.figure(figsize=(10, 6))
plt.plot(linguagens_interesse, coefs_variacao, marker='D', markerfacecolor='blue', markeredgecolor='black', linestyle='dashed', color='cyan')
plt.title(f'Coeficiente de Variação de Pushes por Linguagem de Programação em {ano_selecionado}')
plt.xlabel('Linguagem de Programação')
plt.ylabel('Coeficiente de Variação')
plt.xticks(rotation=45)
plt.grid(axis='y')

for index, value in enumerate(coefs_variacao):
    plt.text(index, value, f'{value:.2f}%', ha='left', va='bottom', weight='bold', fontsize=11)

plt.tight_layout()
plt.show()
