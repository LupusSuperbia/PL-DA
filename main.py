import streamlit as st 
import pandas as pd
import numpy as np

data_vis = pd.read_csv("./data/csv/datos_coin.csv")

y = data_vis.drop(columns="Date")

columns = []
## ------------------------- 
# separar en columnas 
for i in range(len(y.columns)):
    name_coin = data_vis.drop(columns="Date").columns[i]
    columns.append(name_coin)
    
    
def mostrar_datos_cripto(dict_agg, selected_crypto):
    st.title("Datos de Criptomonedas")
    st.subheader(f"Criptomoneda seleccionada: {selected_crypto}")
    df = pd.DataFrame({
            "Date": dict_agg["Date"],
            "Valor": dict_agg[selected_crypto]
        })
    
    
    
    st.line_chart(data=df, x="Date", y="Valor")

st.sidebar.title("Seleccionar Criptomoneda")
selected_crypto = st.sidebar.selectbox("Seleccione una criptomoneda", list(data_vis.keys())[1:])

date_range = st.slider('Seleccionar Rango de Fechas', 0, len(data_vis)-1, (0, len(data_vis)-1))
start_date = data_vis.iloc[date_range[0]]["Date"]
end_date = data_vis.iloc[date_range[1]]["Date"]
st.write(f"Fecha de inicio: {start_date}, Fecha final: {end_date}")
filtered_data = data_vis[(data_vis["Date"] >= start_date) & (data_vis["Date"] <= end_date)]


## Datos de criptos 
st.title("Datos de Criptomonedas Historicos")
st.subheader(f"Datos historicos desde el 2013-2023")
st.line_chart(data=filtered_data, x="Date", y=columns)


mostrar_datos_cripto(filtered_data, selected_crypto)


