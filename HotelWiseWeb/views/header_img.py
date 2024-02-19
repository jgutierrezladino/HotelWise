import streamlit as st

img_logo_sin_fondo = "_src/HotelWiseLogo.Horizontal.png"
img_logo_con_fondo = "_src/HotelWiseLogo.Horizontal.Fondo.png"


def logo_sin_fondo():
    img_style = """
    <style>
        [data-testid=stImage] {
            justify-content: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            border-radius: 30%;
            width: 100%;
        }
    </style>
    """
    st.markdown(img_style, unsafe_allow_html=True)
    st.image(img_logo_con_fondo)

    image_url = "https://people.com/thmb/TzDJt_cDuFa_EShaPF1WzqC8cy0=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc():focal(216x0:218x2)/michael-jordan-435-3-4fc019926b644905a27a3fc98180cc41.jpg"
    style_image1 = """
    width: auto;
    max-width: 850px;
    height: auto;
    max-height: 750px;
    display: block;
    justify-content: center;
    border-radius: 20%;
    """
    st.markdown(
        f'<img src="{image_url}" style="{style_image1}">',
        unsafe_allow_html=True,
    )
    image_url = "https://github.com/jgutierrezladino/HotelWise/blob/HotelWiseWeb/HotelWiseWeb/_src/HotelWiseLogo.Horizontal.Fondo.png"
    style_image2 = """
    width: auto;
    max-width: 850px;
    height: auto;
    max-height: 750px;
    display: block;
    justify-content: center;
    border-radius: 20%;
    """
    st.markdown(
        f'<img src="{image_url}" style="{style_image2}">',
        unsafe_allow_html=True,
    )
