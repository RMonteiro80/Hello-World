import streamlit as st
import pandas as pd 

import seaborn as sb 
import plotly as pl 
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv("supermarket_sales.csv")
st.write("Trabalho de Fundamentos de Ciência de Dados - Rafael e Roberto")
df["Date"] = pd.to_datetime(df ["Date"])
df = df.sort_values("Date")

df["Month"] = df['Date'].apply(lambda x: str(x.year) + "-" + str(x.month))
Month = st.sidebar.selectbox("Mês",df['Month'].unique())

df["Costumer"] = df['Costumer type']
Costumer = st.sidebar.selectbox("Tipo de Cliente",df['Costumer type'].unique())

df_filtered = df[df['Month'] == Month]

col_names_df_filtered= {'Invoice ID':'N.º de Fatura', 
                  'Branch':'Marca', 
                  'City':'Cidade', 
                  'Customer type':'Tipo de Cliente',
                  'Gender':'Género',
                  'Product line':'Gama de Produto', 
                  'Unit price':'Preço Unitário', 
                  'Quantity':'Quantidade',
                  'Tax 5%':'Imposto 5%',
                  'Date':'Data',
                  'Time':'Hora',
                  'Payment':'Método de Pagamento',
                  'cogs':'CMVMC',
                  'gross margin percentage':'Margem Bruta (em %)',
                  'gross income':'Margem Bruta',
                  'Rating':'Satisfação do Cliente',
                  'Month':'Mês'}
df_filtered= df_filtered.rename(columns=col_names_df_filtered)

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_date = px.bar(df_filtered, x="Data", y="Total", color="Cidade", title="Faturação por dia")
col1.plotly_chart(fig_date, use_container_width=True)

fig_prod = px.bar(df_filtered, x="Data", y="Gama de Produto", 
                  color="Cidade", title="Faturação Gama de Produto",
                  orientation="h")
col2.plotly_chart(fig_prod, use_container_width=True)

Cidade_total = df_filtered.groupby("Cidade")[["Total"]].sum().reset_index()
fig_cidade = px.bar(df_filtered, x="Cidade", y="Total", title="Faturação Cidade")
col3.plotly_chart(fig_cidade, use_container_width=True)

fig_pagamento = px.pie(df_filtered, values="Total", names="Método de Pagamento", title="Faturação por tipo de pagamento")
col4.plotly_chart(fig_pagamento, use_container_width=True)


Compra_media = df_filtered.groupby("Cidade")[["Total"]].mean().reset_index()
fig_media= px.bar(df_filtered, x="Cidade", y="Total", title="Faturação Média por Cidade")
col5.plotly_chart(fig_media, use_container_width=True)