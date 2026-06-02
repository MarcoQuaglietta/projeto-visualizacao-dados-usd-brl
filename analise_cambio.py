import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carregar e tratar os dados
# O CSV usa string para datas e números com ponto. Vamos ajustar.
df = pd.read_csv('USD_BRL_hist (1).csv')

# Tratando as datas (convertendo para o padrão do pandas)
df['Data'] = pd.to_datetime(df['Data'], format='%d.%m.%Y')
df = df.sort_values('Data').reset_index(drop=True)

# Criando colunas de Ano e Mês para análises secundárias
df['Ano'] = df['Data'].dt.year
df['Mes'] = df['Data'].dt.month

# Configuração de estilo dos gráficos
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# -------------------------------------------------------------
# GRÁFICO 1: Linha (Unidade: Valor Monetário em R$)
# Natureza: Tendência Temporal
# -------------------------------------------------------------
plt.figure()
plt.plot(df['Data'], df['USD_BRL'], color='darkblue', linewidth=1.5)
plt.title('Evolução Histórica da Taxa de Câmbio (USD/BRL)', fontsize=14, fontweight='bold')
plt.xlabel('Ano', fontsize=12)
plt.ylabel('Preço de Venda (R$)', fontsize=12)
plt.tight_layout()
plt.savefig('grafico_1_linha.png')
plt.close()

# -------------------------------------------------------------
# GRÁFICO 2: Barras (Unidade: Média Anual em R$ ou Variação)
# Natureza: Comparação de Categorias (Anos)
# -------------------------------------------------------------
media_anual = df.groupby('Ano')['USD_BRL'].mean().reset_index()

plt.figure()
sns.barplot(data=media_anual, x='Ano', y='USD_BRL', hue='Ano', palette='Blues_d', legend=False)
plt.title('Média Cotação Anual do Dólar (USD/BRL)', fontsize=14, fontweight='bold')
plt.xlabel('Ano', fontsize=12)
plt.ylabel('Média Anual (R$)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('grafico_2_barras.png')
plt.close()

# -------------------------------------------------------------
# GRÁFICO 3: Histograma (Unidade: Frequência / Dias)
# Natureza: Distribuição Estatística dos Dados
# -------------------------------------------------------------
plt.figure()
sns.histplot(df['USD_BRL'], bins=20, kde=True, color='teal')
plt.title('Distribuição de Frequência do Valor do Dólar', fontsize=14, fontweight='bold')
plt.xlabel('Faixa de Preço (R$)', fontsize=12)
plt.ylabel('Frequência (Quantidade de Dias)', fontsize=12)
plt.tight_layout()
plt.savefig('grafico_3_histograma.png')
plt.close()

print("Análise concluída! Os 3 gráficos foram gerados com sucesso.")