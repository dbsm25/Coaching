import streamlit as st
import pandas as pd

# Encabezado principal con estilo
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>Formato de Evaluación de Habilidades Técnicas</h1>",
    unsafe_allow_html=True
)
st.write("<hr style='border-top: 2px solid #4CAF50;'>", unsafe_allow_html=True)

# Crear una lista para almacenar las habilidades ingresadas
habilidades_tecnicas = []

# Formulario de entrada de datos
st.markdown("<h2 style='color: #4CAF50;'>Ingrese los detalles de su habilidad técnica</h2>", unsafe_allow_html=True)

# Campos del formulario con emojis
st.subheader("🛠️ Nombre de la Habilidad Técnica")
nombre_habilidad = st.text_input("Escribe el nombre de la habilidad")

st.subheader("📊 Nivel de Dominio")
nivel_dominio = st.selectbox("Selecciona el nivel de dominio", ["Básico", "Intermedio", "Avanzado"])

st.subheader("📅 Años de Experiencia")
anos_experiencia = st.number_input("Número de años de experiencia", min_value=0, step=1)

st.subheader("💡 Ejemplo de Uso/Logro Específico")
logro = st.text_area("Describe un ejemplo específico de cómo has usado esta habilidad o un logro relevante.")

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
    st.markdown("<h2 style='color: #4CAF50;'>Resumen de Habilidades Técnicas</h2>", unsafe_allow_html=True)
    habilidades_df = pd.DataFrame(habilidades_tecnicas)
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
