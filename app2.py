# libraries import
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# data import
#file1 = st.file_uploader("df44", type=["csv"]) # this is if the user wants to apload data
#file2 = st.file_uploader("df5", type=["csv"])
#file3 = st.file_uploader("df6", type=["csv"])
df4 = pd.read_csv("df44.csv")
df5 = pd.read_csv("df5.csv")
df6 = pd.read_csv("df6.csv")

# interface
st.title("Analitical Dashboard")
st.sidebar.header("Selection of Visualizations") 

# Graphics
opcion = st.sidebar.radio("Select a graphic:", [
    "Rentability of different sizes of products",
    "x"
])
# Gráfico 1: Rentability of different sizes of products
if opcion == "Rentability of different sizes of products":
    st.subheader("Rentability of different sizes of products")
    tamaño = df6["space"]
    porcentaje = df6["rentability_percentage"]

    # Crear gráfico
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(tamaño, porcentaje, color="blue")

    # Etiquetas
    ax.set_xlabel("Space that a product occupies")
    ax.set_ylabel("Rentability (%)")
    ax.set_title("Rentability by size of products")

    st.pyplot(fig)