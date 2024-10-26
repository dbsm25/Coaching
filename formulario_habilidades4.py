import streamlit as st
import pandas as pd
import os

# Configuración inicial de sesión para manejar el estado de la app
if 'habilidades_df' not in st.session_state:
    # Si el archivo CSV ya existe, cargar los datos
    if os.path.exists("habilidades_tecnicas.csv"):
        st.session_state.habilidades_df = pd.read_csv("habilidades_tecnicas.csv")
    else:
        # Crear un DataFrame vacío si no existe el archivo
        st.session_state.habilidades_df = pd.DataFrame(columns=["Nombre de la Habilidad", "Nivel de Dominio", "Años de Experiencia", "Ejemplo de Uso/Logro Específico"])

if 'objetivos_smart_df' not in st.session_state:
    # Si el archivo CSV ya existe, cargar los datos
    if os.path.exists("objetivos_smart.csv"):
        st.session_state.objetivos_smart_df = pd.read_csv("objetivos_smart.csv")
    else:
        # Crear un DataFrame vacío si no existe el archivo
        st.session_state.objetivos_smart_df = pd.DataFrame(columns=["Específico", "Medible", "Alcanzable", "Relevante", "Temporal"])

# Función para limpiar el formulario después de cada ingreso
def clear_form():
    st.session_state.setdefault("nombre_habilidad", "")
    st.session_state.setdefault("nivel_dominio", "Básico")
    st.session_state.setdefault("anos_experiencia", 0)
    st.session_state.setdefault("logro", "")
    st.session_state.setdefault("especifico", "")
    st.session_state.setdefault("medible", "")
    st.session_state.setdefault("alcanzable", "")
    st.session_state.setdefault("relevante", "")
    st.session_state.setdefault("temporal", "")

# Encabezado principal
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>Formato de Evaluación de Habilidades_Técnicas Multiple </h1>",
    unsafe_allow_html=True
)
st.write("<hr style='border-top: 2px solid #4CAF50;'>", unsafe_allow_html=True)

# Formulario de entrada de datos para habilidades técnicas
st.markdown("<h2 style='color: #4CAF50;'>Ingrese los detalles de su habilidad técnica</h2>", unsafe_allow_html=True)

# Campos del formulario
nombre_habilidad = st.text_input("Nombre de la Habilidad Técnica", key="nombre_habilidad")
nivel_dominio = st.selectbox("Nivel de Dominio", ["Básico", "Intermedio", "Avanzado"], key="nivel_dominio")
anos_experiencia = st.number_input("Años de Experiencia", min_value=0, step=1, key="anos_experiencia")
logro = st.text_area("Ejemplo de Uso/Logro Específico", key="logro")

# Botón para agregar la habilidad
if st.button("Agregar Habilidad"):
    # Agregar la habilidad ingresada al DataFrame de sesión
    nueva_habilidad = {
        "Nombre de la Habilidad": nombre_habilidad,
        "Nivel de Dominio": nivel_dominio,
        "Años de Experiencia": anos_experiencia,
        "Ejemplo de Uso/Logro Específico": logro
    }
    
    st.session_state.habilidades_df = pd.concat(
        [st.session_state.habilidades_df, pd.DataFrame([nueva_habilidad])], ignore_index=True
    )
    
    # Guardar en el archivo CSV y limpiar el formulario
    st.session_state.habilidades_df.to_csv("habilidades_tecnicas.csv", index=False)
    st.success("Habilidad agregada correctamente.")
    clear_form()  # Limpiar el formulario después de agregar

# Mostrar la tabla de habilidades ingresadas
if not st.session_state.habilidades_df.empty:
    st.header("Resumen de Habilidades Técnicas")
    st.table(st.session_state.habilidades_df)

    # Botón para descargar en formato CSV
    csv = st.session_state.habilidades_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Descargar habilidades en CSV",
        data=csv,
        file_name="habilidades_tecnicas.csv",
        mime="text/csv"
    )

# Sección para Objetivos SMART
st.markdown("<h2 style='color: #4CAF50;'>Formato de Definición de Objetivos SMART</h2>", unsafe_allow_html=True)
st.markdown("<p>Objetivo: Establecer un objetivo claro y alcanzable para guiar el proceso de recolocación.</p>", unsafe_allow_html=True)

# Campos del formulario SMART
especifico = st.text_area("Específico: Descripción detallada del objetivo laboral", key="especifico")
medible = st.text_area("Medible: Cómo se medirá el progreso", key="medible")
alcanzable = st.text_area("Alcanzable: Factores que lo hacen alcanzable", key="alcanzable")
relevante = st.text_area("Relevante: Explicación de por qué es importante", key="relevante")
temporal = st.text_area("Temporal: Plazo para cumplir el objetivo, con hitos clave", key="temporal")

# Botón para agregar el objetivo SMART
if st.button("Agregar Objetivo SMART"):
    # Agregar el objetivo ingresado al DataFrame de sesión
    nuevo_objetivo = {
        "Específico": especifico,
        "Medible": medible,
        "Alcanzable": alcanzable,
        "Relevante": relevante,
        "Temporal": temporal
    }
    
    st.session_state.objetivos_smart_df = pd.concat(
        [st.session_state.objetivos_smart_df, pd.DataFrame([nuevo_objetivo])], ignore_index=True
    )
    
    # Guardar en el archivo CSV y limpiar el formulario
    st.session_state.objetivos_smart_df.to_csv("objetivos_smart.csv", index=False)
    st.success("Objetivo SMART agregado correctamente.")
    clear_form()  # Limpiar el formulario después de agregar

# Mostrar la tabla de objetivos SMART ingresados
if not st.session_state.objetivos_smart_df.empty:
    st.header("Resumen de Objetivos SMART")
    st.table(st.session_state.objetivos_smart_df)

    # Botón para descargar en formato CSV
    csv_smart = st.session_state.objetivos_smart_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Descargar objetivos SMART en CSV",
        data=csv_smart,
        file_name="objetivos_smart.csv",
        mime="text/csv"
    )
