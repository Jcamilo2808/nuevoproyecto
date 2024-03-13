import streamlit as st
import pandas as pd
import subprocess

def main():
    st.title('Formulario de Información de Clientes')

    # Widgets para capturar información del cliente
    nombre = st.text_input('Nombre del cliente')
    edad = st.number_input('Edad del cliente', min_value=0, max_value=150, step=1)
    email = st.text_input('Correo electrónico del cliente')
    telefono = st.text_input('Teléfono del cliente')
    direccion = st.text_input('Dirección del cliente')

    # Botón para enviar los datos
    if st.button('Enviar'):
        # Crear un DataFrame con los datos del cliente
        data = {
            'Nombre': [nombre],
            'Edad': [edad],
            'Email': [email],
            'Teléfono': [telefono],
            'Dirección': [direccion]
        }
        df = pd.DataFrame(data)
        # Mostrar el DataFrame generado
        st.subheader('Datos del Cliente:')
        st.write(df)