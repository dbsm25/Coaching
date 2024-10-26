import streamlit as st
import pandas as pd
import os

# Encabezado principal con estilo
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>Formato de Evaluación de Habilidades Técnicas</h1>",
    unsafe_allow_html=True
)
st.write("<hr style='border-top: 2px solid #4CAF50;'>", unsafe_allow_html=True)

# Nombre del archivo CSV
csv_file = "habilidades_tecnicas.csv"

# Verificar si el archivo CSV ya existe y cargar datos previos
if os.path.exists(csv_file):
    habilidades_df = pd.read_csv(csv_file)
else:
    habilidades_df = pd.DataFrame(columns=["Nombre de la Habilidad", "Nivel de Dominio", "Años de Experiencia", "Ejemplo de Uso/Logro Específico"])

# Inicializar el estado de sesión para limpiar el formulario después de agregar una habilidad
if "habilidades_tecnicas" not in st.session_state:
    st.session_state["habilidades_tecnicas"] = habilidades_df

# Función para limpiar el formulario
def clear_form():
    st.session_state["nombre_habilidad"] = ""
    st.session_state["nivel_dominio"] = "Básico"
    st.session_state["anos_experiencia"] = 0
    st.session_state["logro"] = ""

# Campos del formulario con estado de sesión
st.markdown("<h2 style='color: #4CAF50;'>Ingrese los detalles de su habilidad técnica</h2>", unsafe_allow_html=True)

nombre_habilidad = st.text_input("🛠️ Nombre de la Habilidad Técnica", key="nombre_habilidad")
nivel_dominio = st.selectbox("📊 Nivel de Dominio", ["Básico", "Intermedio", "Avanzado"], key="nivel_dominio")
anos_experiencia = st.number_input("📅 Años de Experiencia", min_value=0, step=1, key="anos_experiencia")
logro = st.text_area("💡 Ejemplo de Uso/Logro Específico", key="logro")

# Botón para agregar la habilidad
if st.button("Agregar Habilidad"):
    # Crear un DataFrame temporal con la nueva entrada
    nueva_habilidad = pd.DataFrame([{
        "Nombre de la Habilidad": nombre_habilidad,
        "Nivel de Dominio": nivel_dominio,
        "Años de Experiencia": anos_experiencia,
        "Ejemplo de Uso/Logro Específico": logro
    }])
    
    # Agregar la nueva habilidad al DataFrame en el estado de sesión y guardar en CSV
    habilidades_df = pd.concat([st.session_state["habilidades_tecnicas"], nueva_habilidad], ignore_index=True)
    habilidades_df.to_csv(csv_file, index=False)
    st.session_state["habilidades_tecnicas"] = habilidades_df  # Actualizar el DataFrame en el estado de sesión

    st.success("Habilidad agregada correctamente.")
    clear_form()  # Limpiar el formulario después de agregar la habilidad

# Mostrar la tabla de habilidades ingresadas
if not habilidades_df.empty:
    st.markdown("<h2 style='color: #4CAF50;'>Resumen de Habilidades Técnicas</h2>", unsafe_allow_html=True)
    st.table(habilidades_df)

    # Botón para descargar en formato CSV
    csv = habilidades_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Descargar habilidades en CSV",
        data=csv,
        file_name="habilidades_tecnicas.csv",
        mime="text/csv"
    )

# Separador final para estética
st.write("<hr style='border-top: 2px solid #4CAF50;'>", unsafe_allow_html=True)

