import streamlit as st
import pandas as pd
import plotly.express as px

# Função para ler o arquivo CSV
@st.cache_data
def load_data(file):
    data = pd.read_csv(file)
    return data

# Carregar os dados
data = load_data('Annotation_RepCount.csv')

# # Calcular os totais
# totals = data.groupby('type').size()
# subsampled_totals = data[data['subsampled'] == 'yes'].groupby('type').size()
# annotated_totals = data[data['annotation'] == 'yes'].groupby('type').size()

# # Preenchendo valores faltantes com 0
# subsampled_totals = subsampled_totals.reindex(totals.index, fill_value=0)
# annotated_totals = annotated_totals.reindex(totals.index, fill_value=0)

# # Definir os rótulos explicitamente
# exercise_types = totals.index.tolist()

# # Configuração do gráfico estático
# fig_static, ax_static = plt.subplots(figsize=(20, 12))

# x = range(len(totals))

# ax_static.bar(x, totals, width=0.2, label='Total de Vídeos', align='center')
# ax_static.bar([p + 0.2 for p in x], subsampled_totals, width=0.2, label='Subsampled', align='center')
# ax_static.bar([p + 0.4 for p in x], annotated_totals, width=0.2, label='Anotados', align='center')

# # Configurando tamanhos das fontes e rotacionando os rótulos do eixo X
# ax_static.set_xlabel('Tipo de Exercício', fontsize=18)
# ax_static.set_ylabel('Quantidade', fontsize=18)
# ax_static.set_title('Distribuição de Vídeos por Tipo', fontsize=22)
# ax_static.set_xticks([p + 0.2 for p in x])
# ax_static.set_xticklabels(exercise_types, fontsize=14, rotation=45, ha='right')
# ax_static.legend(fontsize=14)

# # Aumentando o tamanho dos ticks do eixo y
# plt.yticks(fontsize=14)

# # Exibir gráfico estático no Streamlit
# st.pyplot(fig_static)

######################## GRÁFICO INTERATIVO PLOTLY
# Calcular os totais
totals = data.groupby('type').size().reset_index(name='count')
subsampled_totals = data[data['subsampled'] == 'yes'].groupby('type').size().reset_index(name='count')
annotated_totals = data[data['annotation'] == 'yes'].groupby('type').size().reset_index(name='count')

# Juntar os dados em um único DataFrame para facilitar o gráfico
totals['category'] = 'Total'
subsampled_totals['category'] = 'Subsampled'
annotated_totals['category'] = 'Annotated'

all_data = pd.concat([totals, subsampled_totals, annotated_totals])

# Configuração do gráfico interativo com Plotly Express
fig = px.bar(all_data, x='type', y='count', color='category', barmode='group',
             labels={'type': 'Type of exercise', 'count': 'Quantity'},
             title='Video Distribution by Type')

# Ajustar layout para melhorar visualização
fig.update_layout(xaxis_tickangle=-45, height=800)

# Exibir gráfico no Streamlit
st.plotly_chart(fig)

##################### Distribuição dos motivos de exclusão

# 1 incorrect execution
# 2 more than one person in the video
# 3 does not show the entire body
# 4 change of angle or distance
# 5 more than one exercise or variation
# 6 low resolution
# 7 text in front
# 8 incomplete execution
# 9 other reasons
# 10 exercise excluded

totals = data.groupby('type').size().reset_index(name='count')

reason1 = data[data['primary exclusion reason'] == 1].groupby('type').size().reset_index(name='count')
reason2 = data[data['primary exclusion reason'] == 2].groupby('type').size().reset_index(name='count')
reason3 = data[data['primary exclusion reason'] == 3].groupby('type').size().reset_index(name='count')
reason4 = data[data['primary exclusion reason'] == 4].groupby('type').size().reset_index(name='count')
reason5 = data[data['primary exclusion reason'] == 5].groupby('type').size().reset_index(name='count')
reason6 = data[data['primary exclusion reason'] == 6].groupby('type').size().reset_index(name='count')
reason7 = data[data['primary exclusion reason'] == 7].groupby('type').size().reset_index(name='count')
reason8 = data[data['primary exclusion reason'] == 8].groupby('type').size().reset_index(name='count')
reason9 = data[data['primary exclusion reason'] == 9].groupby('type').size().reset_index(name='count')
reason10 = data[data['primary exclusion reason'] == 10].groupby('type').size().reset_index(name='count')

# Juntar os dados em um único DataFrame para facilitar o gráfico
reason1['category'] = 'Incorrect execution'
reason2['category'] = 'More than one person in the video'
reason3['category'] = "Doesn't show the entire body"
reason4['category'] = "Change of angle or distance"
reason5['category'] = "More than one exercise or variation"
reason6['category'] = "Low resolution"
reason7['category'] = "Text in front"
reason8['category'] = "Incomplete execution"
reason9['category'] = "Other reasons"
reason10['category'] = "Exercise excluded"

all_data_exclusion = pd.concat([totals, reason1, reason2, reason3, reason4, reason5, reason6, reason7, reason8, reason9, reason10])

# Configuração do gráfico interativo com Plotly Express
fig = px.bar(all_data_exclusion, x='type', y='count', color='category', barmode='group',
             labels={'type': 'Type of exercise', 'count': 'Quantity'},
             title='Distribution of reasons for deleting videos by Type of exercise')

# Ajustar layout para melhorar visualização
fig.update_layout(xaxis_tickangle=-45, height=800)

# Exibir gráfico no Streamlit
st.plotly_chart(fig)

######################## Distribuição da contagem de repetições por tipo

# Calcular a soma das repetições por tipo de exercício
repetitions = data.groupby('type')['count'].mean().reset_index(name='total_reps')
repetitions['category'] = 'Total'

repetitions_annotated = data[data['annotation'] == 'yes'].groupby('type')['count'].mean().reset_index(name='total_reps')
repetitions_annotated['category'] = 'Annotated videos'

alldata_repetition = pd.concat([repetitions,repetitions_annotated])

# Configuração do gráfico interativo com Plotly Express
fig = px.bar(alldata_repetition, x='type', y='total_reps',color='category', barmode='group', 
             labels={'type': 'Type of exercise', 'total_reps': 'Average repetitions'},
             title='Distribution of average repetitions by type of exercise')

# Ajustar layout para melhorar visualização
fig.update_layout(xaxis_tickangle=-45, height=800)

# Exibir gráfico no Streamlit
st.plotly_chart(fig)