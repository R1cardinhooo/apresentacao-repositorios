import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from sklearn.linear_model import LinearRegression

#Comando para iniciar a interface - (streamlit run app.py)

df = pd.read_csv("cotacao.csv")

modelo = LinearRegression()
x = df[["real"]]
y = df[["dolar"]]
modelo.fit(x, y)

st.title("Cotação de Real para Dólar Americano")
st.divider()

cotacao = st.number_input("Insira o valor em real para a conversão.")

if cotacao:
    conversao_prevista = modelo.predict([[cotacao]])[0][0]
    st.write(f"O valor de {cotacao:.2f} reais para dolar é {conversao_prevista:.2f}")