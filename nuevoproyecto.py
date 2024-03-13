import streamlit as st

def main():
    st.title('Formulario de Registro de Transportador para Cobrar')

    # Campos del formulario
    nombre = st.text_input('Nombre del transportador')
    apellido = st.text_input('Apellido del transportador')
    empresa = st.text_input('Nombre de la empresa')
    email = st.text_input('Correo electrónico')
    telefono = st.text_input('Teléfono')
    direccion = st.text_input('Dirección')

    # Botón para enviar los datos
    if st.button('Registrar'):
        # Validación de datos (puedes agregar más validaciones según tus necesidades)
        if nombre and email:
            # Procesamiento de los datos (aquí puedes agregar el código para cobrar)
            st.success('¡Datos registrados correctamente!')
        else:
            st.error('Por favor completa los campos obligatorios: Nombre y Correo electrónico')

if __name__ == '__main__':
    main()
