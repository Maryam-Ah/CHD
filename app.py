# app.py
import streamlit as st
from PIL import Image
from sklearn.cluster import KMeans
import webcolors
from colorthief import ColorThief

# Function to get the closest CSS3 color name
def closest_color(requested_color):
    min_colors = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_color[0]) ** 2
        gd = (g_c - requested_color[1]) ** 2
        bd = (b_c - requested_color[2]) ** 2
        min_colors[(rd + gd + bd)] = name
    return min_colors[min(min_colors.keys())]

# Function to extract the dominant colors from an image
def extract_colors(uploaded_file, n_colors=5):
    color_thief = ColorThief(uploaded_file)
    dominant_colors = color_thief.get_palette(color_count=n_colors)

    named_colors = []
    for color in dominant_colors:
        named_color = closest_color(color)
        named_colors.append(named_color)

    return named_colors

# Function to interpret the dominant colors
def interpret_colors(dominant_colors):
    interpretations = []

    if 'green' in dominant_colors:
        interpretations.append("The child might be expressing contentment, peace, or a connection with nature.")
    if 'red' in dominant_colors:
        interpretations.append("The child might be experiencing strong emotions such as anger, love, or fear.")
    # ... add more interpretations based on other colors

    if not interpretations:
        return ["No specific interpretation available."]
    
    return interpretations

# Streamlit UI
st.title('Child Drawing Analysis')
st.text("Unhappiness, shyness, empathy or repressed anger are some of the feelings you can identify in your children's drawings. Find out how to interpret the colors your children draw with.")

          
uploaded_file = st.file_uploader("Choose a drawing...", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Drawing.', use_column_width=True)
    
    dominant_colors = extract_colors(uploaded_file)
    interpretations = interpret_colors(dominant_colors)
    
    st.write(f"Dominant Colors: {', '.join(dominant_colors)}")
    for interpretation in interpretations:
        st.write(f"→ {interpretation}")
