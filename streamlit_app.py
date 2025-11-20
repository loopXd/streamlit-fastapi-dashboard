import requests
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard de Vendas", layout="wide")

st.title("📊 Dashboard de Vendas")

# Endpoint da API
API_URL = "http://localhost:8080/dados"

try:
    response = requests.get(API_URL)
    
    if response.status_code == 200:
        dados = response.json()
        df = pd.DataFrame(dados)

        st.subheader("Tabela de Dados")
        st.dataframe(df, use_container_width=True)

        st.subheader("Gráfico de Vendas")
        st.bar_chart(df.set_index("mes")["vendas"])
    else:
        st.error(f"Erro ao consultar API: status {response.status_code}")
except Exception as e:
    st.error(f"Erro de conexão com a API: {e}")
