import streamlit as st
import pandas as pd
import os

# Función para limpiar el formulario
def clear_form():
    st.session_state["nombre_habilidad"] = ""
    st.session_state["nivel_dominio"] = "Básico"
    st.session_state["anos_experiencia"] = 0
    st.session_state["logro"] = ""

# Configuración inicial de valores predeterminados en session_state
if "nombre_habilidad" not in st.session_state:
    st.session_state["nombre_habilidad"] = ""
if "nivel_dominio" not in st.session_state:
    st.session_state["nivel_dominio"] = "Básico"
if "anos_experiencia" not in st.session_state:
    st.session_state["anos_experiencia"] = 0
if "logro" not in st.session_state:
    st.session_state["logro"] = ""

# Título de la aplicación
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>Formato de Evaluación de Habilidades Técnicas</h1>",
    unsafe_allow_html=True
)
st.write("<hr style='border-top: 2px solid #4CAF50;'>", unsafe_allow_html=True)

# Formulario de entrada de datos
st.markdown("<h2 style='color: #4CAF50;'>Ingrese los detalles de su habilidad técnica</h2>", unsafe_allow_html=True)
nombre_habilidad = st.text_input("🏷️ Nombre de la Habilidad Técnica", key="nombre_habilidad")
nivel_dominio = st.selectbox("📊 Nivel de Dominio", ["Básico", "Intermedio", "Avanzado"], key="nivel_dominio")
anos_experiencia = st.number_input("📅 Años de Experiencia", min_value=0, step=1, key="anos_experiencia")
logro = st.text_area("🌟 Ejemplo de Uso/Logro Específico", key="logro")

# Archivo CSV para almacenar las habilidades
archivo_csv = "habilidades_tecnicas.csv"

# Botón para agregar la habilidad
if st.button("Agregar Habilidad"):
    nueva_habilidad = {
        "Nombre de la Habilidad": nombre_habilidad,
        "Nivel de Dominio": nivel_dominio,
        "Años de Experiencia": anos_experiencia,
        "Ejemplo de Uso/Logro Específico": logro
    }

    # Cargar habilidades previas y agregar la nueva
    if os.path.exists(archivo_csv):
        habilidades_df = pd.read_csv(archivo_csv)
        habilidades_df = habilidades_df.append(nueva_habilidad, ignore_index=True)
    else:
        habilidades_df = pd.DataFrame([nueva_habilidad])

    # Guardar en el archivo CSV
    habilidades_df.to_csv(archivo_csv, index=False)
    st.success("Habilidad agregada correctamente.")

    # Limpiar el formulario
    clear_form()

# Mostrar la tabla de habilidades ingresadas
if os.path.exists(archivo_csv):
    st.header("Resumen de Habilidades Técnicas")
    habilidades_df = pd.read_csv(archivo_csv)
    st.table(habilidades_df)

    # Botón para descargar en formato CSV
    csv = habilidades_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Descargar habilidades en CSV",
        data=csv,
        file_name="habilidades_tecnicas.csv",
        mime="text/csv"
    )



