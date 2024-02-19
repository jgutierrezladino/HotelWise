import streamlit as st

img_logo_sin_fondo = "_src/HotelWiseLogo.Horizontal.png"


def logo_sin_fondo():
    img_style = """
    <style>
        [data-testid=stImage] {
            text-align: right;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """

    # Aplicar los estilos CSS a la imagen
    st.markdown(img_style, unsafe_allow_html=True)
    st.image("_src/HotelWiseLogo.Horizontal.png")
