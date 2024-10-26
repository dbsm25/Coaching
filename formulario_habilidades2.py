import streamlit as st
import pandas as pd
import os

# Título de la aplicación con estilo
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>Formato de Evaluación de Habilidades Técnicas</h1>",
    unsafe_allow_html=True
)
st.write("<hr style='border-top: 2px solid #4CAF50;'>", unsafe_allow_html=True)

# Nombre del archivo CSV
csv_file = "habilidades_tecnicas.csv"

# Verificar si el archivo CSV ya existe y cargar datos previos al DataFrame
if os.path.exists(csv_file):
    habilidades_df = pd.read_csv(csv_file)
else:
    habilidades_df = pd.DataFrame(columns=["Nombre de la Habilidad", "Nivel de Dominio", "Años de Experiencia", "Ejemplo de Uso/Logro Específico"])

# Inicializar los valores de estado de sesión para el formulario
if "habilidades_tecnicas" not in st.session_state:
    st.session_state["habilidades_tecnicas"] = habilidades_df

if "nombre_habilidad" not in st.session_state:
    st.session_state["nombre_habilidad"] = ""
if "nivel_dominio" not in st.session_state:
    st.session_state["nivel_dominio"] = "Básico"
if "anos_experiencia" not in st.session_state:
    st.session_state["anos_experiencia"] = 0
if "logro" not in st.session_state:
    st.session_state["logro"] = ""

# Función para limpiar el formulario después de enviar
def clear_form():
    st.session_state["nombre_habilidad"] = ""
    st.session_state["nivel_dominio"] = "Básico"
    st.session_state["anos_experiencia"] = 0
    st.session_state["logro"] = ""

# Campos del formulario de entrada
st.markdown("<h2 style='color: #4CAF50;'>Ingrese los detalles de su habilidad técnica-v2</h2>", unsafe_allow_html=True)
nombre_habilidad = st.text_input("🛠️ Nombre de la Habilidad Técnica", key="nombre_habilidad")
nivel_dominio = st.selectbox("📊 Nivel de Dominio", ["Básico", "Intermedio", "Avanzado"], key="nivel_dominio")
anos_experiencia = st.number_input("📅 Años de Experiencia", min_value=0, step=1, key="anos_experiencia")
logro = st.text_area("💡 Ejemplo de Uso/Logro Específico", key="logro")

# Botón para agregar la habilidad al archivo CSV
if st.button("Agregar Habilidad"):
    # Crear un DataFrame temporal para la nueva habilidad
    nueva_habilidad = pd.DataFrame([{
        "Nombre de la Habilidad": nombre_habilidad,
        "Nivel de Dominio": nivel_dominio,
        "Años de Experiencia": anos_experiencia,
        "Ejemplo de Uso/Logro Específico": logro
    }])

    # Concatenar el nuevo dato con el DataFrame existente en session_state y actualizar el CSV
    st.session_state["habilidades_tecnicas"] = pd.concat([st.session_state["habilidades_tecnicas"], nueva_habilidad], ignore_index=True)
    st.session_state["habilidades_tecnicas"].to_csv(csv_file, index=False)
    
    st.success("Habilidad agregada correctamente.")
    clear_form()  # Limpiar el formulario después de enviar

# Mostrar la tabla de habilidades ingresadas
if not st.session_state["habilidades_tecnicas"].empty:
    st.markdown("<h2 style='color: #4CAF50;'>Resumen de Habilidades Técnicas</h2>", unsafe_allow_html=True)
    st.table(st.session_state["habilidades_tecnicas"])

    # Botón para descargar el DataFrame en formato CSV
    csv = st.session_state["habilidades_tecnicas"].to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Descargar habilidades en CSV",
        data=csv,
        file_name="habilidades_tecnicas.csv",
        mime="text/csv"
    )

# Separador final para estética
st.write("<hr style='border-top: 2px solid #4CAF50;'>", unsafe_allow_html=True)


