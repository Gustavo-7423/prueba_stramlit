# Configuración de la barra lateral
st.sidebar.title("Esta es una prueba")
st.sidebar.header("Hola esto es una barra lateral")
st.sidebar.write("Barra lateral")

# Cargar y mostrar una imagen en la barra lateral
st.sidebar.image("madrir.png")

# Botón en la barra lateral que muestra un mensaje cuando se hace clic
if st.sidebar.button("Clik en la barra lateral"):
    st.sidebar.write("Hice un botón lateral")

# Campo de texto en la barra lateral donde el usuario puede escribir algo
user_input = st.sidebar.text_input("Escribe algo en la barra")
st.sidebar.write("Escribiste en la barra:", user_input)

# Configuración de la página principal
st.title("Esta es mi primera página")
st.header("Mi primera página")
st.image("madrir.png")

# Cargar archivo CSV
uploaded_file = st.file_uploader("Datos_de_la_bolsa_500", type=["csv"])
if uploaded_file is not None:
    # Leer el archivo CSV
    df = pd.read_csv(uploaded_file, sep=';')
    
    # Mostrar los datos del archivo CSV
    st.write("Datos_de_la_bolsa_500:")
    st.dataframe(df)

    # Selección de columnas para el gráfico
    st.write("Seleccione las columnas para el gráfico:")
    x_column = st.selectbox("Columna para el eje X", df.columns)
    y_column = st.selectbox("Columna para el eje Y", df.columns)

    # Crear el gráfico si ambas columnas están seleccionadas
    if x_column and y_column:
        fig, ax = plt.subplots()
        ax.plot(df[x_column], df[y_column], label=f"{y_column} vs {x_column}", color="blue")
        ax.set_title(f"{y_column} vs {x_column}")
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        ax.legend()

        # Mostrar el gráfico en Streamlit
        st.pyplot(fig)
