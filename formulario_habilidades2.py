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

# Campos del formulario
st.markdown("<h2 style='color: #4CAF50;'>Ingrese los detalles de su habilidad técnica</h2>", unsafe_allow_html=True)

nombre_habilidad = st.text_input("🛠️ Nombre de la Habilidad Técnica", "")
nivel_dominio = st.selectbox("📊 Nivel de Dominio", ["Básico", "Intermedio", "Avanzado"])
anos_experiencia = st.number_input("📅 Años de Experiencia", min_value=0, step=1)
logro = st.text_area("💡 Ejemplo de Uso/Logro Específico", "")

# Botón para agregar la habilidad
if st.button("Agregar Habilidad"):
    # Crear un DataFrame temporal con la nueva entrada
    nueva_habilidad = pd.DataFrame([{
        "Nombre de la Habilidad": nombre_habilidad,
        "Nivel de Dominio": nivel_dominio,
        "Años de Experiencia": anos_experiencia,
        "Ejemplo de Uso/Logro Específico": logro
    }])
    
    # Agregar la nueva habilidad al DataFrame existente y guardar en CSV
    habilidades_df = pd.concat([habilidades_df, nueva_habilidad], ignore_index=True)
    habilidades_df.to_csv(csv_file, index=False)
    
    st.success("Habilidad agregada correctamente.")
    
    # Blanquear los campos del formulario después de agregar la habilidad
    st.experimental_rerun()

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

