import streamlit as st
import pandas as pd
import plotly.express as px

# Encabezado de la app
st.header("Análisis exploratorio de anuncios de autos en EE.UU.")

# Cargar el dataset
df = pd.read_csv("vehicles_us.csv")

# Mostrar una vista previa
st.subheader("Vista previa del dataset")
st.write(df.head())

st.markdown("---")

# Checkbox para histograma
if st.checkbox("Mostrar histograma del kilometraje"):
    fig_hist = px.histogram(
        df,
        x="odometer",
        title="Distribución del kilometraje de los vehículos"
    )
    st.plotly_chart(fig_hist)

# Checkbox para gráfico de dispersión
if st.checkbox("Mostrar gráfico Precio vs Kilometraje"):
    fig_scatter = px.scatter(
        df,
        x="odometer",
        y="price",
        title="Relación entre precio y kilometraje"
    )
    st.plotly_chart(fig_scatter)
