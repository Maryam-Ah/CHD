import streamlit as st
from PIL import Image

# Include the functions: closest_color, extract_colors, and interpret_colors here

st.title('Child Drawing Analysis')

uploaded_file = st.file_uploader("Choose a drawing...", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Drawing.', use_column_width=True)
    
    dominant_colors = extract_colors(image)
    interpretations = interpret_colors(dominant_colors)
    
    st.write(f"Dominant Colors: {', '.join(dominant_colors)}")
    for interpretation in interpretations:
        st.write(f"→ {interpretation}")
