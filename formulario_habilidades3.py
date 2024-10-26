import streamlit as st
import pandas as pd

# Encabezado principal con estilo
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>Formato de Evaluación de Habilidades Técnicas</h1>",
    unsafe_allow_html=True
)
st.write("<hr style='border-top: 2px solid #4CAF50;'>", unsafe_allow_html=True)

# Leer el archivo CSV si existe, de lo contrario crear un DataFrame vacío
try:
    habilidades_df = pd.read_csv("habilidades_tecnicas.csv")
except FileNotFoundError:
    habilidades_df = pd.DataFrame(columns=["Nombre de la Habilidad", "Nivel de Dominio", "Años de Experiencia", "Ejemplo de Uso/Logro Específico"])

# Función para limpiar el formulario después de agregar o editar la habilidad
def clear_form():
    st.session_state.setdefault("nombre_habilidad", "")
    st.session_state.setdefault("nivel_dominio", "Básico")
    st.session_state.setdefault("anos_experiencia", 0)
    st.session_state.setdefault("logro", "")

# Formulario de entrada de datos
st.markdown("<h2 style='color: #4CAF50;'>Ingrese los detalles de su habilidad técnica</h2>", unsafe_allow_html=True)

# Campos del formulario
nombre_habilidad = st.text_input("Nombre de la Habilidad Técnica", key="nombre_habilidad")
nivel_dominio = st.selectbox("Nivel de Dominio", ["Básico", "Intermedio", "Avanzado"], key="nivel_dominio")
anos_experiencia = st.number_input("Años de Experiencia", min_value=0, step=1, key="anos_experiencia")
logro = st.text_area("Ejemplo de Uso/Logro Específico", key="logro")

# Botón para agregar o actualizar la habilidad
if st.button("Agregar/Actualizar Habilidad"):
    # Crear una fila de datos
    nueva_habilidad = {
        "Nombre de la Habilidad": nombre_habilidad,
        "Nivel de Dominio": nivel_dominio,
        "Años de Experiencia": anos_experiencia,
        "Ejemplo de Uso/Logro Específico": logro
    }
    
    # Verificar si la habilidad ya existe y actualizarla
    if "selected_row" in st.session_state and st.session_state.selected_row is not None:
        habilidades_df.iloc[st.session_state.selected_row] = nueva_habilidad
        st.session_state.selected_row = None  # Limpiar selección
        st.success("Habilidad actualizada correctamente.")
    else:
        habilidades_df = habilidades_df.append(nueva_habilidad, ignore_index=True)
        st.success("Habilidad agregada correctamente.")
    
    # Guardar el DataFrame en un archivo CSV
    habilidades_df.to_csv("habilidades_tecnicas.csv", index=False)
    
    # Limpiar formulario
    clear_form()

# Mostrar la tabla de habilidades ingresadas con un selector para edición
if not habilidades_df.empty:
    st.header("Resumen de Habilidades Técnicas")

    # Selector de fila para edición
    selected_row = st.selectbox("Seleccione una habilidad para editar:", habilidades_df.index, format_func=lambda x: habilidades_df.at[x, "Nombre de la Habilidad"])

    if st.button("Cargar Habilidad Seleccionada"):
        # Cargar los valores seleccionados en el formulario para editar
        st.session_state["nombre_habilidad"] = habilidades_df.at[selected_row, "Nombre de la Habilidad"]
        st.session_state["nivel_dominio"] = habilidades_df.at[selected_row, "Nivel de Dominio"]
        st.session_state["anos_experiencia"] = habilidades_df.at[selected_row, "Años de Experiencia"]
        st.session_state["logro"] = habilidades_df.at[selected_row, "Ejemplo de Uso/Logro Específico"]
        st.session_state.selected_row = selected_row
    
    # Mostrar tabla de habilidades
    st.table(habilidades_df)

    # Botón para descargar en formato CSV
    csv = habilidades_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Descargar habilidades en CSV",
        data=csv,
        file_name="habilidades_tecnicas.csv",
        mime="text/csv"
    )
