import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Configuração visual
sns.set(style='whitegrid', context='talk')

# Configuração da página
st.set_page_config(
    page_title='Análise Bivariada - Previsão de Renda',
    page_icon='📊',
    layout='wide'
)

# Título
st.title('📊 Entendimento dos Dados - Análise Bivariada')

st.write(
    '''
    Nesta etapa foram avaliadas as relações entre as variáveis explicativas
    e a variável alvo (renda).
    '''
)

# Carregamento da base de dados
renda = pd.read_csv(
    r'C:\Users\olive\OneDrive\Área de Trabalho\EBAC\Python_cinencia_dados\Profissão Cientista de Dados M16 2 Projeto\projeto 2\input\previsao_de_renda.csv'
)

# ==========================================
# Sidebar - Filtros
# ==========================================

st.sidebar.header('Filtros')

educacao = st.sidebar.multiselect(
    'Escolaridade',
    renda['educacao'].unique(),
    default=renda['educacao'].unique()
)

tipo_renda = st.sidebar.multiselect(
    'Tipo de renda',
    renda['tipo_renda'].unique(),
    default=renda['tipo_renda'].unique()
)

# Aplicando filtros
renda_filtrada = renda[
    (renda['educacao'].isin(educacao)) &
    (renda['tipo_renda'].isin(tipo_renda))
]

# ==========================================
# Métricas
# ==========================================

st.write('## Indicadores Gerais')

col1, col2, col3 = st.columns(3)

col1.metric('Total de Registros', len(renda_filtrada))
col2.metric('Renda Média', f"R$ {renda_filtrada['renda'].mean():,.2f}")
col3.metric('Idade Média', round(renda_filtrada['idade'].mean(), 1))

# ==========================================
# Boxplot - Escolaridade x Renda
# ==========================================

st.write('## Renda por Escolaridade')

fig1, ax1 = plt.subplots(figsize=(12, 6))

sns.boxplot(
    x='educacao',
    y='renda',
    data=renda_filtrada,
    ax=ax1
)

ax1.tick_params(axis='x', rotation=45)

st.pyplot(fig1)

# ==========================================
# Scatterplot - Idade x Renda
# ==========================================

st.write('## Relação entre Idade e Renda')

fig2, ax2 = plt.subplots(figsize=(12, 6))

sns.scatterplot(
    x='idade',
    y='renda',
    hue='tipo_renda',
    data=renda_filtrada,
    ax=ax2
)

st.pyplot(fig2)

# ==========================================
# Barplot - Tipo de Renda
# ==========================================

st.write('## Média de Renda por Tipo de Renda')

fig3, ax3 = plt.subplots(figsize=(12, 6))

sns.barplot(
    x='tipo_renda',
    y='renda',
    data=renda_filtrada,
    ax=ax3
)

ax3.tick_params(axis='x', rotation=45)

st.pyplot(fig3)

# ==========================================
# Estado Civil x Renda
# ==========================================

st.write('## Renda por Estado Civil')

fig4, ax4 = plt.subplots(figsize=(12, 6))

sns.boxplot(
    x='estado_civil',
    y='renda',
    data=renda_filtrada,
    ax=ax4
)

ax4.tick_params(axis='x', rotation=45)

st.pyplot(fig4)

# ==========================================
# Heatmap de Correlação
# ==========================================

st.write('## Correlação entre Variáveis Numéricas')

fig5, ax5 = plt.subplots(figsize=(12, 8))

corr = renda_filtrada.corr(numeric_only=True)

sns.heatmap(
    corr,
    annot=True,
    cmap='coolwarm',
    ax=ax5
)

st.pyplot(fig5)

# ==========================================
# Tabela de Dados
# ==========================================

st.write('## Base de Dados Filtrada')

st.dataframe(renda_filtrada)
