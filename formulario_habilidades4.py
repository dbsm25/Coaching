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

# Función para crear un PDF a partir de los CSVs
def crear_pdf():
    habilidades_df = st.session_state.habilidades_df
    objetivos_smart_df = st.session_state.objetivos_smart_df

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Título del PDF
    pdf.cell(200, 10, txt="Resumen de Habilidades Técnicas 4", ln=True, align='C')
    pdf.ln(10)

    # Añadir datos del CSV de Habilidades Técnicas
    for index, row in habilidades_df.iterrows():
        pdf.cell(200, 10, txt=f"Nombre de la Habilidad: {row['Nombre de la Habilidad']}", ln=True)
        pdf.cell(200, 10, txt=f"Nivel de Dominio: {row['Nivel de Dominio']}", ln=True)
        pdf.cell(200, 10, txt=f"Años de Experiencia: {row['Años de Experiencia']}", ln=True)
        pdf.cell(200, 10, txt=f"Ejemplo de Uso/Logro Específico: {row['Ejemplo de Uso/Logro Específico']}", ln=True)
        pdf.ln(5)

    pdf.add_page()
    pdf.cell(200, 10, txt="Resumen de Objetivos SMART", ln=True, align='C')
    pdf.ln(10)

    # Añadir datos del CSV de Objetivos SMART
    for index, row in objetivos_smart_df.iterrows():
        pdf.cell(200, 10, txt=f"Específico: {row['Específico']}", ln=True)
        pdf.cell(200, 10, txt=f"Medible: {row['Medible']}", ln=True)
        pdf.cell(200, 10, txt=f"Alcanzable: {row['Alcanzable']}", ln=True)
        pdf.cell(200, 10, txt=f"Relevante: {row['Relevante']}", ln=True)
        pdf.cell(200, 10, txt=f"Temporal: {row['Temporal']}", ln=True)
        pdf.ln(5)

    # Guardar el PDF
    pdf.output("resumen_habilidades_objetivos.pdf")

    return "resumen_habilidades_objetivos.pdf"

# Función para eliminar una habilidad técnica
def eliminar_habilidad(index):
    st.session_state.habilidades_df.drop(index, inplace=True)
    st.session_state.habilidades_df.to_csv("habilidades_tecnicas.csv", index=False)

# Función para eliminar un objetivo SMART
def eliminar_objetivo(index):
    st.session_state.objetivos_smart_df.drop(index, inplace=True)
    st.session_state.objetivos_smart_df.to_csv("objetivos_smart.csv", index=False)

# Si no está autenticado, muestra la pantalla de autenticación
if not st.session_state.authenticated:
    authenticate()
else:
    # Configuración inicial de sesión para manejar el estado de la app
    if 'habilidades_df' not in st.session_state:
        if os.path.exists("habilidades_tecnicas.csv"):
            st.session_state.habilidades_df = pd.read_csv("habilidades_tecnicas.csv")
        else:
            st.session_state.habilidades_df = pd.DataFrame(columns=["Nombre de la Habilidad", "Nivel de Dominio", "Años de Experiencia", "Ejemplo de Uso/Logro Específico"])

    if 'objetivos_smart_df' not in st.session_state:
        if os.path.exists("objetivos_smart.csv"):
            st.session_state.objetivos_smart_df = pd.read_csv("objetivos_smart.csv")
        else:
            st.session_state.objetivos_smart_df = pd.DataFrame(columns=["Específico", "Medible", "Alcanzable", "Relevante", "Temporal"])

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
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Evaluación de Habilidades Técnicas</h1>", unsafe_allow_html=True)
    st.write("<hr style='border-top: 2px solid #4CAF50;'>", unsafe_allow_html=True)

    # Formulario de entrada de datos para habilidades técnicas
    st.markdown("<h2 style='color: #4CAF50;'>Sección 1 : Ingrese los detalles de su habilidad técnica</h2>", unsafe_allow_html=True)

    nombre_habilidad = st.text_input("Nombre de la Habilidad Técnica", key="nombre_habilidad")
    nivel_dominio = st.selectbox("Nivel de Dominio", ["Básico", "Intermedio", "Avanzado"], key="nivel_dominio")
    anos_experiencia = st.number_input("Años de Experiencia", min_value=0, step=1, key="anos_experiencia")
    logro = st.text_area("Ejemplo de Uso/Logro Específico", key="logro")

    if st.button("Agregar Habilidad"):
        nueva_habilidad = {
            "Nombre de la Habilidad": nombre_habilidad,
            "Nivel de Dominio": nivel_dominio,
            "Años de Experiencia": anos_experiencia,
            "Ejemplo de Uso/Logro Específico": logro
        }
        
        st.session_state.habilidades_df = pd.concat([st.session_state.habilidades_df, pd.DataFrame([nueva_habilidad])], ignore_index=True)
        st.session_state.habilidades_df.to_csv("habilidades_tecnicas.csv", index=False)
        st.success("Habilidad agregada correctamente.")
        clear_form()

    if not st.session_state.habilidades_df.empty:
        st.header("Resumen de Habilidades Técnicas")
        st.dataframe(st.session_state.habilidades_df)
        for index, row in st.session_state.habilidades_df.iterrows():
            st.write(f"{row['Nombre de la Habilidad']} - {row['Nivel de Dominio']} - {row['Años de Experiencia']} - {row['Ejemplo de Uso/Logro Específico']}")
            if st.button(f"Eliminar Habilidad {index}"):
                eliminar_habilidad(index)
                st.experimental_rerun()
        csv = st.session_state.habilidades_df.to_csv(index=False).encode("utf-8")
        st.download_button(label="Descargar habilidades en CSV", data=csv, file_name="habilidades_tecnicas.csv", mime="text/csv")

    st.markdown("<h2 style='color: #000080;'>Sección 2 : Definición de Objetivos SMART</h2>", unsafe_allow_html=True)
    st.markdown("<p>Objetivo: Establecer un objetivo claro y alcanzable para guiar el proceso de recolocación.</p>", unsafe_allow_html=True)

    especifico = st.text_area("Específico: Descripción detallada del objetivo laboral", key="especifico")
    medible = st.text_area("Medible: Cómo se medirá el progreso", key="medible")
    alcanzable = st.text_area("Alcanzable: Factores que lo hacen alcanzable", key="alcanzable")
    relevante = st.text_area("Relevante: Explicación de por qué es importante", key="relevante")
    temporal = st.text_area("Temporal: Plazo para cumplir el objetivo, con hitos clave", key="temporal")

    if st.button("Agregar Objetivo SMART"):
        nuevo_objetivo = {
            "Específico": especifico,
            "Medible": medible,
            "Alcanzable": alcanzable,
            "Relevante": relevante,
            "Temporal": temporal
        }
        
        st.session_state.objetivos_smart_df = pd.concat([st.session_state.objetivos_smart_df, pd.DataFrame([nuevo_objetivo])], ignore_index=True)
        st.session_state.objetivos_smart_df.to_csv("objetivos_smart.csv", index=False)
        st.success("Objetivo SMART agregado correctamente.")
        clear_form()

    if not st.session_state.objetivos_smart_df.empty:
        st.header("Resumen de Objetivos SMART")
        st.dataframe(st.session_state.objetivos_smart_df)
        for index, row in st.session_state.objetivos_smart_df.iterrows():
            st.write(f"{row['Específico']} - {row['Medible']} - {row['Alcanzable']} - {row['Relevante']} - {row['Temporal']}")
            if st.button(f"Eliminar Objetivo {index}"):
                eliminar_objetivo(index)
                st.experimental_rerun()
        csv_smart = st.session_state.objetivos_smart_df.to_csv(index=False).encode("utf-8")
        st.download_button(label="Descargar objetivos SMART en CSV", data=csv_smart, file_name="objetivos_smart.csv", mime="text/csv")

    # Botón para crear y descargar el PDF
    if st.button("Crear PDF con Resumen"):
        pdf_file = crear_pdf()
        with open(pdf_file, "rb") as pdf:
            st.download_button(label="Descargar PDF con Resumen", data=pdf, file_name="resumen_habilidades_objetivos.pdf", mime="application/pdf")


