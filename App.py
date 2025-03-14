import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configurar la página
st.set_page_config(page_title="Recolección de Llantas", page_icon="\U0001F6E3", layout="wide")

# Sesión para almacenar datos del formulario
if 'submitted' not in st.session_state:
    st.session_state['submitted'] = False

if not st.session_state['submitted']:
    st.title("Registro de Datos para Recolección")
    
    with st.form("user_form"):
        nombre = st.text_input("Nombre")
        direccion = st.text_input("Dirección")
        capacidad = st.number_input("Capacidad de almacenamiento (en llantas)", min_value=0)
        cantidad = st.number_input("Cantidad de llantas almacenadas", min_value=0)
        agendar = st.checkbox("Agendar recolección automática")
        
        submitted = st.form_submit_button("Enviar")
        
        if submitted:
            st.session_state['submitted'] = True
            st.session_state['data'] = {
                "Nombre": nombre,
                "Dirección": direccion,
                "Capacidad": capacidad,
                "Cantidad": cantidad,
                "Agendado": agendar
            }
            st.experimental_rerun()
else:
    st.title("Resumen de Datos y Estadísticas")
    
    st.subheader("Datos Ingresados")
    for key, value in st.session_state['data'].items():
        st.write(f"**{key}:** {value}")
    
    st.subheader("Ubicación (Mapa de Referencia)")
    st.image("https://source.unsplash.com/800x400/?map,location", caption="Mapa de referencia", use_column_width=True)
    
    st.subheader("Métricas del Almacenamiento")
    fig, ax = plt.subplots()
    labels = ["Capacidad Máxima", "Llantas Almacenadas"]
    values = [st.session_state['data']['Capacidad'], st.session_state['data']['Cantidad']]
    ax.bar(labels, values, color=['blue', 'red'])
    ax.set_ylabel("Cantidad de Llantas")
    st.pyplot(fig)
    
    if st.button("Volver al inicio"):
        st.session_state['submitted'] = False
        st.experimental_rerun()
