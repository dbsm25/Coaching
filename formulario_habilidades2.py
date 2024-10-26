import streamlit as st
import pandas as pd

# Encabezado principal con estilo
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>Formato de Evaluación de Habilidades Técnicas88</h1>",
    unsafe_allow_html=True
)
st.write("<hr style='border-top: 2px solid #4CAF50;'>", unsafe_allow_html=True)

# Nombre del archivo CSV
csv_file = "habilidades_tecnicas.csv"

# Leer el archivo CSV existente o crear un DataFrame vacío si no existe
try:
    habilidades_df = pd.read_csv(csv_file)
except FileNotFoundError:
    habilidades_df = pd.DataFrame(columns=["Nombre de la Habilidad", "Nivel de Dominio", "Años de Experiencia", "Ejemplo de Uso/Logro Específico"])

# Formulario de entrada de datos
st.markdown("<h2 style='color: #4CAF50;'>Ingrese los detalles de su habilidad técnica</h2>", unsafe_allow_html=True)

# Campos del formulario con emojis
nombre_habilidad = st.text_input("🛠️ Nombre de la Habilidad Técnica", key="nombre_habilidad")
nivel_dominio = st.selectbox("📊 Nivel de Dominio", ["Básico", "Intermedio", "Avanzado"], key="nivel_dominio")
anos_experiencia = st.number_input("📅 Años de Experiencia", min_value=0, step=1, key="anos_experiencia")
logro = st.text_area("🏆 Ejemplo de Uso/Logro Específico", key="logro")

# Botón para agregar la habilidad
if st.button("Agregar Habilidad"):
    # Crear un diccionario con los datos de la nueva habilidad
    nueva_habilidad = {
        "Nombre de la Habilidad": nombre_habilidad,
        "Nivel de Dominio": nivel_dominio,
        "Años de Experiencia": anos_experiencia,
        "Ejemplo de Uso/Logro Específico": logro
    }
    
    # Añadir la nueva habilidad al DataFrame
    habilidades_df = habilidades_df.append(nueva_habilidad, ignore_index=True)
    
    # Guardar el DataFrame actualizado en el archivo CSV (acumulando los datos)
    habilidades_df.to_csv(csv_file, index=False)
    
    # Confirmación de éxito
    st.success("Habilidad agregada correctamente.")

    # Limpiar el formulario después de agregar la habilidad
    st.session_state["nombre_habilidad"] = ""
    st.session_state["nivel_dominio"] = "Básico"
    st.session_state["anos_experiencia"] = 0
    st.session_state["logro"] = ""

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
