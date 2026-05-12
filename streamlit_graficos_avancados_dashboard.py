import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px

# Configurações
sns.set(style='darkgrid', context='talk')

st.set_page_config(
    page_title='Dashboard Avançado - Previsão de Renda',
    page_icon='📈',
    layout='wide'
)

# ==========================================
# Título
# ==========================================

st.title('📈 Dashboard Avançado - Análise Exploratória')

st.write(
    '''
    Dashboard contendo diferentes tipos de gráficos para análise exploratória
    da base de previsão de renda.
    '''
)

# ==========================================
# Carregamento da base
# ==========================================

renda = pd.read_csv(
    r'C:\Users\olive\OneDrive\Área de Trabalho\EBAC\Python_cinencia_dados\Profissão Cientista de Dados M16 2 Projeto\projeto 2\input\previsao_de_renda.csv'
)

# Conversão da data
renda['data_ref'] = pd.to_datetime(renda['data_ref'])

# ==========================================
# Sidebar
# ==========================================

st.sidebar.header('Filtros')

sexo = st.sidebar.multiselect(
    'Sexo',
    renda['sexo'].unique(),
    default=renda['sexo'].unique()
)

tipo_renda = st.sidebar.multiselect(
    'Tipo de renda',
    renda['tipo_renda'].unique(),
    default=renda['tipo_renda'].unique()
)

renda_filtrada = renda[
    (renda['sexo'].isin(sexo)) &
    (renda['tipo_renda'].isin(tipo_renda))
]

# ==========================================
# KPIs
# ==========================================

st.write('## Indicadores')

col1, col2, col3 = st.columns(3)

col1.metric('Total Clientes', len(renda_filtrada))
col2.metric('Renda Média', f"R$ {renda_filtrada['renda'].mean():,.2f}")
col3.metric('Maior Renda', f"R$ {renda_filtrada['renda'].max():,.2f}")

# ==========================================
# Histograma
# ==========================================

st.write('## Distribuição da Renda')

fig1, ax1 = plt.subplots(figsize=(12, 6))

sns.histplot(
    renda_filtrada['renda'],
    kde=True,
    bins=30,
    ax=ax1
)

st.pyplot(fig1)

# ==========================================
# Violin Plot
# ==========================================

st.write('## Distribuição da Renda por Sexo')

fig2, ax2 = plt.subplots(figsize=(12, 6))

sns.violinplot(
    x='sexo',
    y='renda',
    data=renda_filtrada,
    ax=ax2
)

st.pyplot(fig2)

# ==========================================
# Pie Chart
# ==========================================

st.write('## Distribuição por Tipo de Renda')

tipo_renda_count = renda_filtrada['tipo_renda'].value_counts()

fig3 = px.pie(
    values=tipo_renda_count.values,
    names=tipo_renda_count.index,
    title='Distribuição por Tipo de Renda'
)

st.plotly_chart(fig3, use_container_width=True)

# ==========================================
# Área Chart
# ==========================================

st.write('## Evolução da Renda ao Longo do Tempo')

renda_tempo = renda_filtrada.groupby('data_ref')['renda'].mean().reset_index()

fig4 = px.area(
    renda_tempo,
    x='data_ref',
    y='renda',
    title='Renda Média ao Longo do Tempo'
)

st.plotly_chart(fig4, use_container_width=True)

# ==========================================
# Treemap
# ==========================================

st.write('## Treemap - Escolaridade e Tipo de Renda')

fig5 = px.treemap(
    renda_filtrada,
    path=['educacao', 'tipo_renda'],
    values='renda'
)

st.plotly_chart(fig5, use_container_width=True)

# ==========================================
# Boxenplot
# ==========================================

st.write('## Distribuição da Renda por Estado Civil')

fig6, ax6 = plt.subplots(figsize=(12, 6))

sns.boxenplot(
    x='estado_civil',
    y='renda',
    data=renda_filtrada,
    ax=ax6
)

ax6.tick_params(axis='x', rotation=45)

st.pyplot(fig6)

# ==========================================
# Pairplot
# ==========================================

st.write('## Pairplot das Variáveis Numéricas')

numericas = renda_filtrada[['idade', 'tempo_emprego', 'qt_pessoas_residencia', 'renda']]

pairplot = sns.pairplot(numericas)

st.pyplot(pairplot.figure)

# ==========================================
# Hexbin Plot
# ==========================================

st.write('## Relação entre Idade e Tempo de Emprego')

fig7, ax7 = plt.subplots(figsize=(10, 6))

ax7.hexbin(
    renda_filtrada['idade'],
    renda_filtrada['tempo_emprego'],
    gridsize=25
)

ax7.set_xlabel('Idade')
ax7.set_ylabel('Tempo de Emprego')

st.pyplot(fig7)

# ==========================================
# Heatmap
# ==========================================

st.write('## Heatmap de Correlação')

fig8, ax8 = plt.subplots(figsize=(10, 8))

corr = renda_filtrada.corr(numeric_only=True)

sns.heatmap(
    corr,
    annot=True,
    cmap='viridis',
    ax=ax8
)

st.pyplot(fig8)

# ==========================================
# Dados
# ==========================================

st.write('## Base de Dados')

st.dataframe(renda_filtrada)
