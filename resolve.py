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
