import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("Formato de Evaluación de Habilidades Técnicas")

# Crear una lista para almacenar las habilidades ingresadas
habilidades_tecnicas = []

# Formulario de entrada de datos
st.header("Ingrese los detalles de su habilidad técnica")

# Campos del formulario
nombre_habilidad = st.text_input("Nombre de la Habilidad Técnica")
nivel_dominio = st.selectbox("Nivel de Dominio", ["Básico", "Intermedio", "Avanzado"])
anos_experiencia = st.number_input("Años de Experiencia", min_value=0, step=1)
logro = st.text_area("Ejemplo de Uso/Logro Específico")

# Botón para agregar la habilidad
if st.button("Agregar Habilidad"):
    # Agregar la habilidad ingresada a la lista
    habilidades_tecnicas.append({
        "Nombre de la Habilidad": nombre_habilidad,
        "Nivel de Dominio": nivel_dominio,
        "Años de Experiencia": anos_experiencia,
        "Ejemplo de Uso/Logro Específico": logro
    })
    st.success("Habilidad agregada correctamente.")

# Mostrar la tabla de habilidades ingresadas
if habilidades_tecnicas:
    st.header("Resumen de Habilidades Técnicas")
    habilidades_df = pd.DataFrame(habilidades_tecnicas)
    st.table(habilidades_df)

    # Botón para descargar en formato CSV
    csv = habilidades_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Descargar habilidades en CSV",
        data=csv,
        file_name="habilidades_tecnicas.csv",
        mime="text/csv"
    )
