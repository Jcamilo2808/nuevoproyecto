import streamlit as st

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
        # Mostrar los datos ingresados por el cliente
        st.subheader('Datos del Cliente:')
        st.write(f'Nombre: {nombre}')
        st.write(f'Edad: {edad}')
        st.write(f'Email: {email}')
        st.write(f'Teléfono: {telefono}')
        st.write(f'Dirección: {direccion}')

if __name__ == '__main__':
    main()
