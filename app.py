import streamlit as st
import pandas as pd
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="Control de Inocuidad", page_icon="🛡️", layout="wide")

st.title("🛡️ Dashboard de Calidad e Inocuidad Alimentaria")
st.markdown("### Monitoreo de Cadena de Frío y Puntos Críticos de Control (PCC)")

# 1. PANEL DE ENTRADA DE DATOS (Simulación de Registro en Planta)
st.sidebar.header("📝 Registrar Nueva Inspección")
operario = st.sidebar.text_input("Nombre del Inspector:", value="Ing. Carlos Pérez")
producto = st.sidebar.selectbox("Producto:", ["Carne de Res", "Pescado Fresco", "Lácteos", "Vegetales"])
temperatura = st.sidebar.number_input("Temperatura registrada (°C):", value=3.5, step=0.1)

# Lógica de Inocuidad (Límites Críticos HACCP)
limite_critico = 4.0
if temperatura <= limite_critico:
    estado = "✅ APROBADO"
    color_alerta = "green"
else:
    estado = "❌ RECHAZADO (PCC Superado)"
    color_alerta = "red"

# Botón para guardar
if st.sidebar.button("Guardar Registro"):
    st.sidebar.success("¡Registro guardado localmente!")

# 2. PANEL VISUAL (Dashboard Principal)
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Temperatura Actual", value=f"{temperatura} °C", delta=f"{temperatura - limite_critico:.1f} °C respecto al límite")

with col2:
    st.markdown(f"### Estado de la Carga:\n<h2 style='color:{color_alerta};'>{estado}</h2>", unsafe_allow_html=True)

with col3:
    st.metric(label="Límite Crítico HACCP", value="4.0 °C Máx")

# 3. TABLA DE HISTÓRICO SIMULADO
st.markdown("---")
st.subheader("📊 Historial Reciente de Recepción")

datos_simulados = {
    "Fecha/Hora": [datetime.now().strftime("%Y-%m-%d %H:%M"), "2026-06-29 14:20", "2026-06-29 11:15", "2026-06-29 08:30"],
    "Inspector": [operario, "Dra. Ana Gómez", "Ing. Carlos Pérez", "Ing. Luis Merino"],
    "Producto": [producto, "Lácteos", "Carne de Res", "Pescado Fresco"],
    "Temperatura (°C)": [temperatura, 3.8, 5.2, 2.1],
    "Decisión": [estado, "✅ APROBADO", "❌ RECHAZADO", "✅ APROBADO"]
}

df = pd.DataFrame(datos_simulados)
st.dataframe(df, use_container_width=True)
