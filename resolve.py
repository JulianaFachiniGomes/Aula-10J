import streamlit as st
import pandas as pd

##Dados mulheres
import requests as req
urlf= 'https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=F&ordem=ASC&ordenarPor=nome'

respostaf = req.get(urlf)
dadosf = respostaf.json()
dff = pd.DataFrame(dadosf['dados'])
dff['sexo'] = 'F'

###Dados homens
import requests as req
urlh= 'https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=M&ordem=ASC&ordenarPor=nome'

respostah = req.get(urlh)
dadosh = respostah.json()
dfh = pd.DataFrame(dadosh['dados'])
dfh['sexo'] = 'M'

todos = pd.concat([dff,dfh])

opcao = st.selectbox(
    'Qual o sexo?',
     todos['sexo'].unique())
dfFiltrado = todos[todos['sexo'] == opcao]
st.title('Deputados do sexo ' + opcao)

ocorrencias = dfFiltrado['siglaUf'].value_counts()

dfEstados = pd.DataFrame({
    'siglaUf': ocorrencias.index,
    'quantidade': ocorrencias.values}
    )

#item 7
#total de homens
totalHomens = dfh['id'].count()
st.metric('Total de Homens', totalHomens)
#total de mulheres
totalMulheres = dff['id'].count()
st.metric('Total de Mulheres', totalMulheres)
st.write('Total de deputadas do sexo ' + opcao)
st.bar_chart(dfEstados,
             x = 'siglaUf',
             y = 'quantidade',
             x_label='Siglas dos estados',
             y_label='Quantidade de deputados')
st.dataframe(dfFiltrado)
