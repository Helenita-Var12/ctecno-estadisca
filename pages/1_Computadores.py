import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("ESTADISTICA DE COMPUTADORES ")

df = pd.read_csv('static/datasets/compudata22.csv', parse_dates=['HORA'])


DIA = st.multiselect('DIA', sorted(set(df['DIA'].unique())))
HORA = st.multiselect('HORA', sorted(set(df['HORA'].dt.strftime('%H:%M').unique())))


df_filtrado = df[df['DIA'].isin(DIA) & df['HORA'].dt.strftime('%H:%M').isin(HORA)]
# Crea un gráfico  
if not df_filtrado.empty:  

    DIA = df_filtrado['DIA'].tolist()
    HORA = df_filtrado['HORA'].tolist()
    
    #.dt.strftime('%H:%M')
   
    plt.plot(DIA, HORA)
    plt.xlabel("Eje DIA")
    plt.ylabel("Eje HORA")  
 
 # Muestra el gráfico en Streamlit
    st.pyplot(plt)
else:
    st.write("No hay datos disponibles para los filtros seleccionados.")

# DIA = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
# HORA = pd.to_datetime(['8:00', '10:00', '9:00', '13:00', '11:00', '11:00'])

# dia = st.multiselect ('DIA',sorted(df['DIA'].unique()))
# hora = st.multiselect ('HORA',sorted(df['HORA'].unique()))


# def Filtro1 (df, dia, hora):
#         df_copy = df.copy()

#         if len(dia) > 0:
#                 df_copy = df_copy [df_copy['DIA'].isin(dia)]
#         if len(hora) > 0:
#                 df_copy = df_copy [df_copy['HORA'].isin(hora)]

#         return df_copy

# df_ = filter_data(df, dia, hora)
# st.subheader ("DIA VS HORA")

# total_compu = len(df_)
# dia_mas = df_['Overall'].mean()
# hora_mas = df_['value'].mean()

# col1, col2, col3 = st.columns(3)
# col1.metric("compu", F"{total_compu:,.0F}")
# col1.metric("dia mas", F"{dia_mas:,.1F}")
# col1.metric("hora mas", F"{total_compu:,.0F}")
 





# def filto1():   
#     col1, col2 = st.columns(2)
#     with col1:
#         DIA = st.selectbox("DIA",DIAU + ['Todas'])
#     with col2:
#         HORA = st.selectbox("HORA", HORAU + ['Todas']) 

#     if DIA != 'Todas' and HORA != 'Todas':
#         filtered_df = df[(df['DIA'] == DIA) & (df['HORA'] == HORA)]
#     elif DIA != 'Todas':
#         filtered_df = df[df['DIA'] == DIA]
#     elif HORA != 'Todas':
#         filtered_df = df[df['HORA'] == HORA]
#     else:
#         filtered_df = df 
    
  
    # st.write(filtered_df)