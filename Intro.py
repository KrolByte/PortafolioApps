import streamlit as st
from PIL import Image
st.title("Aplicaciones de nuestro curso.")

with st.sidebar:
  st.subheader("Potafolio: Mis apps.")
  parrafo = (
    "En este portafolio encontrarás todas las apps que hemos desarrollado durante el curso, "
    "aquí abordamos diferentes temas y en base a ellos desarrollamos una app para entender "
    "su funcionamiento, de igual manera respondiendo a frutas sobre las mismas."
  )
  st.write(parrafo)

url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("Aquí encontramos todos los contenidos tratado y trabajados durante el curso.")
st.write(f"Conoce más aquí: [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("Detector de anomalías")
 image = Image.open('txt_to_audio2.png')
 st.image(image, width=190)
 st.write("En esta app vemos Lógica + Big-O + NumPy, mediante medidores de humedad y temperatura, combinando ambas preposiciones") 
 url = "https://logicabig-o-pbu88wfn75nojzhtelapvt.streamlit.app/"
 st.write(f"Mira la app: [Enlace]({url})")

 st.subheader("Predictor de lluvia")
 image = Image.open('txt_to_audio.png')
 st.image(image, width=200)
 st.write("En esta app vemos regresión logística interactiva, combinando nuevamente las preposiciones de humedad y temperatura junto con la calidad del aire") 
 url = "https://predictorlluvia-k4r0l.streamlit.app/"
 st.write(f"Mira la app: [Enlace]({url})")

 st.subheader("Estación Marco CORNARE")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En esta app tenemos el resumen de la estación 5 con respecto a diferentes datos de una problematica con el nivel de ríos y quebradas") 
 url = "https://r2tscwbzp2jqldpkdrydmk.streamlit.app/"
 st.write(f"Mira la app: [Enlace]({url})")

with col2: 
 st.subheader("Predictor de sensación térmica")
 image = Image.open('OIG8.jpg')
 st.image(image, width=200)
 st.write("En esta app tenemos datos reales de temperatura y humedad tomados por un sensor IoT, para entrenar un modelo de regresión lineal que predice la sensación térmica") 
 url = "https://sensaciontermica-k4r0l.streamlit.app/"
 st.write(f"Mira la app: [Enlace]({url})")

 st.subheader("Series de tiempo")
 image = Image.open('data_analisis.png')
 st.image(image, width=190)
 st.write("En esta app medimos la tendencia, estacionalidad y ruido de los datos mediante la media móvil, suavizado exponencial y modelo ARIMA") 
 url = "https://serietiempo-k4r0l.streamlit.app/"
 st.write(f"Mira la app: [Enlace]({url})")

 st.subheader("Predictor de la calidad del aire")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 st.write("En esta app medimos la calidad del aire mediante archivos con registros con datos anteriores, nos sirve para predecir el clima") 
 url = "https://prediccionaire-k4r0l.streamlit.app/"
 st.write(f"Mira la app: [Enlace]({url})")


with col3: 
 st.subheader("Descenso del gradiente interactivo")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En esta app exploramos en vivo cómo la tasa de aprendizaje y el punto inicial afectan la convergencia del descenso de gradiente") 
 url = "https://gradiente-g6jnvjyglj6jgjuy8j5t4y.streamlit.app/"
 st.write(f"Mira la app: [Enlace]({url})")

 st.subheader("KNN con suelos de AGROSAVIA")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("Esta app es como cuando eliges un restaurante preguntando a amigos con gustos parecidos, KNN clasifica un suelo nuevo según sus k vecinos más cercanos, que votan") 
 url = "https://knnsuelos-k4r0l.streamlit.app/"
 st.write(f"Mira la app: [Enlace]({url})")
 
 st.subheader("¿Qué fruta es más parecida?")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En esta app de acuerdo a variables de peso, diámetro y dulzor, predecimos a qué otra fruta es similar la actual por medio de vectores y distancias") 
 url = "https://7y4nmxfxjcrj56kyjdeawq.streamlit.app/"
 st.write(f"Mira la app: [Enlace]({url})")


