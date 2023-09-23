import streamlit as st
from PIL import Image
from collections import defaultdict
import webcolors
from colorthief import ColorThief
import numpy as np

def closest_color_name(requested_color):
    min_colors = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_color[0]) ** 2
        gd = (g_c - requested_color[1]) ** 2
        bd = (b_c - requested_color[2]) ** 2
        min_colors[(rd + gd + bd)] = name
    return min_colors[min(min_colors.keys())]

def generalize_color_name(color_name):
    color_map = {
        'blue': ['aliceblue', 'lightcyan', 'lightblue', 'skyblue', 'deepskyblue', 'dodgerblue', 'cornflowerblue', 'royalblue', 'mediumblue', 'darkblue', 'midnightblue', 'navy', 'steelblue', 'cadetblue', 'mediumslateblue', 'slateblue', 'darkslateblue'],
        'red': ['indianred', 'lightcoral', 'salmon', 'darksalmon', 'lightsalmon', 'crimson', 'red', 'firebrick', 'darkred'],
        'pink': ['pink', 'lightpink', 'hotpink', 'deeppink', 'mediumvioletred', 'palevioletred'],
        'orange': ['coral', 'tomato', 'orangered', 'gold', 'orange', 'darkorange'],
        'yellow': ['yellow', 'lightyellow', 'lemonchiffon', 'lightgoldenrodyellow', 'papayawhip', 'moccasin', 'peachpuff', 'palegoldenrod', 'khaki', 'darkkhaki'],
        'green': ['lawngreen', 'chartreuse', 'limegreen', 'lime', 'forestgreen', 'green', 'darkgreen', 'greenyellow', 'yellowgreen', 'springgreen', 'mediumspringgreen', 'lightgreen', 'palegreen', 'darkseagreen', 'mediumseagreen', 'seagreen', 'olive', 'darkolivegreen', 'olivedrab'],
        'cyan': ['aqua', 'cyan', 'lightcyan', 'paleturquoise', 'aquamarine', 'turquoise', 'mediumturquoise', 'darkturquoise', 'lightseagreen', 'cadetblue', 'darkcyan', 'teal'],
        'purple': ['lavender', 'thistle', 'plum', 'violet', 'orchid', 'fuchsia', 'magenta', 'mediumorchid', 'mediumpurple', 'blueviolet', 'darkviolet', 'darkorchid', 'darkmagenta', 'purple', 'indigo'],
        'brown': ['cornsilk', 'blanchedalmond', 'bisque', 'navajowhite', 'wheat', 'burlywood', 'tan', 'rosybrown', 'sandybrown', 'goldenrod', 'darkgoldenrod', 'peru', 'chocolate', 'saddlebrown', 'sienna', 'brown', 'maroon'],
        'white': ['white', 'snow', 'honeydew', 'mintcream', 'azure', 'aliceblue', 'ghostwhite', 'whitesmoke', 'seashell', 'beige', 'oldlace', 'floralwhite', 'ivory', 'antiquewhite', 'linen', 'lavenderblush', 'mistyrose'],
        # 'gray': ['gainsboro', 'lightgray', 'silver', 'darkgray', 'gray', 'dimgray', 'lightslategray', 'slategray', 'darkslategray', 'black']
    }
    for general_color, specific_colors in color_map.items():
        if color_name in specific_colors:
            return general_color
    return color_name

def extract_colors(uploaded_file, n_colors=5):
    color_thief = ColorThief(uploaded_file)
    dominant_colors = color_thief.get_palette(color_count=n_colors)

    named_colors = [closest_color_name(color) for color in dominant_colors]
    generalized_colors = [generalize_color_name(color) for color in named_colors]

    return generalized_colors

def top_used_colors(uploaded_file, dominant_colors, top_n=3):
    img = Image.open(uploaded_file).convert("RGB")
    pixels = list(img.getdata())

    dominant_rgb_colors = [webcolors.name_to_rgb(color) for color in dominant_colors]

    color_counts = defaultdict(int)
    
    white_rgb = np.array([255, 255, 255])
    gray_rgb = np.array([128, 128, 128])
    threshold_white = 100
    threshold_gray = 100  # Adjust this threshold if necessary

    for pixel in pixels:
        pixel_array = np.array(pixel)
        
        # Exclude white and grayish pixels
        if np.linalg.norm(pixel_array - white_rgb) < threshold_white or np.linalg.norm(pixel_array - gray_rgb) < threshold_gray:
            continue

        closest_dom_color = dominant_rgb_colors[np.argmin([np.sum((pixel_array - np.array(col))**2) for col in dominant_rgb_colors])]
        color_counts[closest_dom_color] += 1

    sorted_colors = sorted(color_counts.items(), key=lambda x: x[1], reverse=True)
    
    top_colors_rgb = [color[0] for color in sorted_colors[:top_n]]
    top_colors_names = [generalize_color_name(closest_color_name(rgb)) for rgb in top_colors_rgb]

    return top_colors_names

def interpret_colors(colors):
    interpretations = []
    if 'green' in colors:
        interpretations.append("green :The child might be expressing contentment, peace, or a connection with nature.")
    if 'red' in colors:
        interpretations.append("red :Red is a color that attracts kids’ attention because of its intensity. You can interpret its use in two different ways: If the child uses it often, he might be a hostile child with feelings of repressed anger. If the child uses it moderately, it can describe vitality and energy.")
    if 'blue' in colors:
        interpretations.append("Blue :This color is associated with calmness, well-being and relaxation. It’s usually the favorite of calm or timid children. In addition, it awakens the sense of creativity and sensitivity in kids. Specialists estimate that children who use this color also develop self-control at younger ages. In addition, some children who use this color often have a condition called enuresis, a disorder that we also call “wetting the bed.")
    if 'black' in colors:
        interpretations.append("Black :Contrary to popular belief, it’s a color that isn’t always linked to negative or depressed feelings. It actually describes a child with good self-esteem and self-confidence.")
    if 'brown' in colors:
        interpretations.append("Brown :This color represents responsibility. In that sense, when children choose it, they show that they’re diligent and prudent. However, using it excessively shows that they’re overwhelmed by daily activities.")
    if 'yellow' in colors:
        interpretations.append("Yellow :Yellow is synonymous with energy, dynamism, joy and sociability. It’s a color that shows happy children. In addition, you see all of the virtues associated with childhood. However, using it frequently in drawings shows problems with authority figures.")
    if 'purple' in colors:
        interpretations.append("Purple :Using this color shows that the child feels melancholic, dissatisfied and restless for some reason. When used with yellow in drawings, it can mean that the child is overwhelmed by some type of pressure.")
    # if 'gray' in colors:
    #     interpretations.append("red :The child might be experiencing strong emotions such as anger, love, or fear.")

    # if 'gray' in colors:
    #     interpretations.append("Gray :Gray is the color of restrained and quiet children. They should receive support in every endeavor. Give your child more attention so that his gray drawings become colored with all the colors of the rainbow..")
    
    if not interpretations:
        return ["No specific interpretation available."]
    return interpretations

st.title('Child Drawing Analysis')
st.markdown("Unhappiness, shyness, empathy or repressed anger are some of the feelings you can identify in your children's drawings. Find out how to interpret the colors your children draw with.")

uploaded_file = st.file_uploader("Choose a drawing...", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Drawing.', use_column_width=True)
    
    dominant_colors = extract_colors(uploaded_file)
    top_colors = top_used_colors(uploaded_file, dominant_colors)

    st.write(f"Dominant Colors: {', '.join(dominant_colors)}")
    st.write(f"Most Used Colors in Order: {', '.join(top_colors)}")

    interpretations = interpret_colors(top_colors)
    for interpretation in interpretations:
        st.write(f"→ {interpretation}")
