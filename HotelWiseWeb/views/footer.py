import streamlit as st

img_logo_con_fondo = "_src/HotelWiseLogo.Horizontal.Fondo.png"
img_logo_henry = "_src/LogoHenry.png"


def page_footer():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Carrera Data Science PT")

    with col2:
        st.image(img_logo_con_fondo)

    with col3:
        st.image(img_logo_henry, width=50)

    st.markdown(""" 
        <style>
            .rounded-section {
                border-radius: 10px;
            }

            .rounded-div {
                border-radius: 10px;
            }
        </style>
        """, unsafe_allow_html=True)

    st.markdown("""
        <div class="rounded-div text-center p-4" style="background-color: rgba(0, 0, 0, 0.05);">
            © 2024 Copyright:
            <a class="text-reset fw-bold" href="{% url 'home' %}">HotelWise.com</a>
            <img src="https://github.com/jgutierrezladino/HotelWise/blob/HotelWiseWeb/HotelWiseWeb/static/imagenes/HotelWiseLogo.Horizontal.png" ,width="10%">
        </div>
        """, unsafe_allow_html=True)
