import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("ESTADISTICA DE SALAS ")

df = pd.read_csv('static\datasets\Salas2 (1).csv', parse_dates=['HORA'])

DIA = st.multiselect('DIA', sorted(set(df['DIA'].unique())))
HORA = st.multiselect('HORA', sorted(set(df['HORA'].dt.strftime('%H:%M').unique())))

df_filtrado = df[df['DIA'].isin(DIA) & df['HORA'].dt.strftime('%H:%M').isin(HORA)]

# Crea un gráfico  
if not df_filtrado.empty:  
    DIA = df_filtrado['DIA'].tolist()
    HORA = df_filtrado['HORA'].tolist()
    
    plt.plot(DIA, HORA)
    plt.xlabel("Eje DIA")
    plt.ylabel("Eje HORA")  
 
    # Muestra el gráfico en Streamlit
    st.pyplot(plt)
else:
    st.write("No hay datos disponibles para los filtros seleccionados.")
#-----------------------------------------------------------------------------------

#Filtro 2 