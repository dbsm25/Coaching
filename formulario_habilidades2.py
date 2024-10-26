import streamlit as st
import pandas as pd
import os

# Encabezado principal con estilo
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>Formato de Evaluación de Habilidades Técnicas</h1>",
    unsafe_allow_html=True
)
st.write("<hr style='border-top: 2px solid #4CAF50;'>", unsafe_allow_html=True)

# Función para limpiar el formulario después de enviar la habilidad
def clear_form():
    st.session_state["nombre_habilidad"] = ""
    st.session_state["nivel_dominio"] = "Básico"
    st.session_state["anos_experiencia"] = 0
    st.session_state["logro"] = ""

# Función para cargar o crear el archivo CSV
def load_habilidades():
    if os.path.exists("habilidades_tecnicas.csv"):
        try:
            return pd.read_csv("habilidades_tecnicas.csv")
        except pd.errors.EmptyDataError:
            # Si el archivo está vacío, devuelve un DataFrame con las columnas necesarias
            return pd.DataFrame(columns=["Nombre de la Habilidad", "Nivel de Dominio", "Años de Experiencia", "Ejemplo de Uso/Logro Específico"])
    else:
        # Si no existe, crea un DataFrame vacío con las columnas adecuadas
        return pd.DataFrame(columns=["Nombre de la Habilidad", "Nivel de Dominio", "Años de Experiencia", "Ejemplo de Uso/Logro Específico"])

# Cargar habilidades previas
habilidades_df = load_habilidades()

# Formulario de entrada de datos
st.markdown("<h2 style='color: #4CAF50;'>Ingrese los detalles de su habilidad técnica</h2>", unsafe_allow_html=True)

# Campos del formulario con valores predeterminados en 'session_state' para poder limpiar
nombre_habilidad = st.text_input("Nombre de la Habilidad Técnica", key="nombre_habilidad")
nivel_dominio = st.selectbox("Nivel de Dominio", ["Básico", "Intermedio", "Avanzado"], key="nivel_dominio")
anos_experiencia = st.number_input("Años de Experiencia", min_value=0, step=1, key="anos_experiencia")
logro = st.text_area("Ejemplo de Uso/Logro Específico", key="logro")

# Botón para agregar la habilidad
if st.button("Agregar Habilidad"):
    # Crear un nuevo registro y añadirlo al DataFrame actual
    nueva_habilidad = pd.DataFrame({
        "Nombre de la Habilidad": [nombre_habilidad],
        "Nivel de Dominio": [nivel_dominio],
        "Años de Experiencia": [anos_experiencia],
        "Ejemplo de Uso/Logro Específico": [logro]
    })

    # Concatenar la nueva habilidad al DataFrame cargado
    habilidades_df = pd.concat([habilidades_df, nueva_habilidad], ignore_index=True)
    
    # Guardar en el CSV sin sobrescribir el contenido anterior
    habilidades_df.to_csv("habilidades_tecnicas.csv", index=False)
    st.success("Habilidad agregada correctamente.")
    
    # Limpiar el formulario
    clear_form()

# Mostrar la tabla de habilidades ingresadas
if not habilidades_df.empty:
    st.header("Resumen de Habilidades Técnicas")
    st.table(habilidades_df)

    # Botón para descargar en formato CSV
    csv = habilidades_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Descargar habilidades en CSV",
        data=csv,
        file_name="habilidades_tecnicas.csv",
        mime="text/csv"
    )

