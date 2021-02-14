import streamlit as st
import pandas as pd
from datetime import date

st.write(
    """
    ** Ações web app **
    """
)

st.sidebar.header("Escolha sua ação")

def get_data():
    path = 'C:/Users/fabri/Google Drive/codifike/23 - WebAppAcoes/all_bovespa.csv'
    return pd.read_csv(path)

df = get_data()

df_data = pd.to_datetime(df['data_pregao']).dt.date.drop_duplicates()

min_date = min(df_data)
max_date = max(df_data)

stock = df['sigla_acao'].drop_duplicates()

stock_choices = st.sidebar.selectbox('Escolha sua ação', stock)