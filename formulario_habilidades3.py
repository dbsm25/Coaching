import streamlit as st
import pandas as pd
import os
from fpdf import FPDF

# Clave de acceso definida por ti
ACCESS_KEY = "MiClaveSecreta2024"

# Verificar si el usuario ha ingresado la clave correcta
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# Función para autenticar
def authenticate():
    user_key = st.text_input("Ingrese la clave de acceso:", type="password")
    if st.button("Acceder"):
        if user_key == ACCESS_KEY:
            st.session_state.authenticated = True
            st.success("Acceso concedido")
        else:
            st.error("Clave incorrecta. Intente nuevamente.")

# Función para crear una sección del PDF
def agregar_seccion_pdf(pdf, titulo, datos, columnas):
    pdf.add_page()
    pdf.cell(200, 10, txt=titulo, ln=True, align='C')
    pdf.ln(10)
    for index, row in datos.iterrows():
        for columna in columnas:
            pdf.cell(200, 10, txt=f"{columna}: {row[columna]}", ln=True)
        pdf.ln(5)

# Función para crear el PDF
def crear_pdf():
    pdf = FPDF()
    pdf.set_font("Arial", size=12)
    agregar_seccion_pdf(pdf, "Resumen de Habilidades Técnicas", st.session_state.habilidades_df,
                        ["Nombre de la Habilidad", "Nivel de Dominio", "Años de Experiencia", "Ejemplo de Uso/Logro Específico"])
    agregar_seccion_pdf(pdf, "Resumen de Objetivos SMART", st.session_state.objetivos_smart_df,
                        ["Específico", "Medible", "Alcanzable", "Relevante", "Temporal"])
    pdf.output("resumen_habilidades_objetivos.pdf")
    return "resumen_habilidades_objetivos.pdf"

# Función para inicializar un DataFrame vacío o cargar desde CSV
def cargar_datos(nombre_csv, columnas):
    if os.path.exists(nombre_csv):
        return pd.read_csv(nombre_csv)
    else:
        return pd.DataFrame(columns=columnas)

# Función para eliminar una fila del DataFrame y actualizar CSV
def eliminar_fila(df_key, index, filename):
    st.session_state[df_key].drop(index, inplace=True)
    st.session_state[df_key].to_csv(filename, index=False)

# Si no está autenticado, muestra la pantalla de autenticación
if not st.session_state.authenticated:
    authenticate()
else:
    # Cargar datos iniciales
    st.session_state.habilidades_df = cargar_datos("habilidades_tecnicas.csv", 
                                                   ["Nombre de la Habilidad", "Nivel de Dominio", "Años de Experiencia", "Ejemplo de Uso/Logro Específico"])
    st.session_state.objetivos_smart_df = cargar_datos("objetivos_smart.csv", 
                                                       ["Específico", "Medible", "Alcanzable", "Relevante", "Temporal"])

    # Función para limpiar el formulario
    def clear_form():
        for key in ["nombre_habilidad", "nivel_dominio", "anos_experiencia", "logro", "especifico", "medible", "alcanzable", "relevante", "temporal"]:
            st.session_state[key] = ""

    # Encabezado principal
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Evaluación de Habilidades Técnicas</h1>", unsafe_allow_html=True)
    st.write("<hr style='border-top: 2px solid #4CAF50;'>", unsafe_allow_html=True)

    # Sección 1: Formulario para habilidades técnicas
    st.markdown("<h2 style='color: #4CAF50;'>Sección 1: Ingrese los detalles de su habilidad técnica</h2>", unsafe_allow_html=True)
    nombre_habilidad = st.text_input("Nombre de la Habilidad Técnica", key="nombre_habilidad")
    nivel_dominio = st.selectbox("Nivel de Dominio", ["Básico", "Intermedio", "Avanzado"], key="nivel_dominio")
    anos_experiencia = st.number_input("Años de Experiencia", min_value=0, step=1, key="anos_experiencia")
    logro = st.text_area("Ejemplo de Uso/Logro Específico", key="logro")

    if st.button("Agregar Habilidad"):
        nueva_habilidad = {"Nombre de la Habilidad": nombre_habilidad, "Nivel de Dominio": nivel_dominio,
                           "Años de Experiencia": anos_experiencia, "Ejemplo de Uso/Logro Específico": logro}
        st.session_state.habilidades_df = pd.concat([st.session_state.habilidades_df, pd.DataFrame([nueva_habilidad])], ignore_index=True)
        st.session_state.habilidades_df.to_csv("habilidades_tecnicas.csv", index=False)
        st.success("Habilidad agregada correctamente.")
        clear_form()

    # Mostrar resumen de habilidades
    if not st.session_state.habilidades_df.empty:
        st.header("Resumen de Habilidades Técnicas")
        st.dataframe(st.session_state.habilidades_df)
        for index in st.session_state.habilidades_df.index:
            if st.button(f"Eliminar Habilidad {index}", key=f"del_hab_{index}"):
                eliminar_fila('habilidades_df', index, "habilidades_tecnicas.csv")

    # Sección 2: Formulario para objetivos SMART
    st.markdown("<h2 style='color: #000080;'>Sección 2: Definición de Objetivos SMART</h2>", unsafe_allow_html=True)
    especifico = st.text_area("Específico: Descripción detallada del objetivo laboral", key="especifico")
    medible = st.text_area("Medible: Cómo se medirá el progreso", key="medible")
    alcanzable = st.text_area("Alcanzable: Factores que lo hacen alcanzable", key="alcanzable")
    relevante = st.text_area("Relevante: Explicación de por qué es importante", key="relevante")
    temporal = st.text_area("Temporal: Plazo para cumplir el objetivo, con hitos clave", key="temporal")

    if st.button("Agregar Objetivo SMART"):
        nuevo_objetivo = {"Específico": especifico, "Medible": medible, "Alcanzable": alcanzable,
                          "Relevante": relevante, "Temporal": temporal}
        st.session_state.objetivos_smart_df = pd.concat([st.session_state.objetivos_smart_df, pd.DataFrame([nuevo_objetivo])], ignore_index=True)
        st.session_state.objetivos_smart_df.to_csv("objetivos_smart.csv", index=False)
        st.success("Objetivo SMART agregado correctamente.")
        clear_form()

    # Mostrar resumen de objetivos SMART
    if not st.session_state.objetivos_smart_df.empty:
        st.header("Resumen de Objetivos SMART")
        st.dataframe(st.session_state.objetivos_smart_df)
        for index in st.session_state.objetivos_smart_df.index:
            if st.button(f"Eliminar Objetivo {index}", key=f"del_obj_{index}"):
                eliminar_fila('objetivos_smart_df', index, "objetivos_smart.csv")

    # Botón para crear y descargar el PDF
    if st.button("Crear PDF con Resumen"):
        pdf_file = crear_pdf()
        with open(pdf_file, "rb") as pdf:
            st.download_button(label="Descargar PDF con Resumen", data=pdf, file_name="resumen_habilidades_objetivos.pdf", mime="application/pdf")
