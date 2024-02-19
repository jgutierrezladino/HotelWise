import streamlit as st


def page_footer():
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
        <section class="rounded-section d-flex justify-content-center justify-content-lg-between p-4 border-bottom">
            <div class="me-5 d-none d-md-block" style="margin-left: 1cm;">
                <span>Carrera Data Science PT</span>
            </div>
            <div class="text-md-center" style="margin-right: 1.5cm;">
                <a href="https://www.soyhenry.com/">
                    <img src="https://github.com/jgutierrezladino/HotelWise/blob/HotelWiseWeb/HotelWiseWeb/static/imagenes/HotelWiseLogo.Horizontal.png" width="150%">
                </a>
            </div>
        </section>

        <div class="rounded-div text-center p-4" style="background-color: rgba(0, 0, 0, 0.05);">
            © 2024 Copyright:
            <a class="text-reset fw-bold" href="{% url 'home' %}">HotelWise.com</a>
            <img src="https://github.com/jgutierrezladino/HotelWise/blob/HotelWiseWeb/HotelWiseWeb/static/imagenes/HotelWiseLogo.Horizontal.png" width="150%">
        </div>
        """, unsafe_allow_html=True)
