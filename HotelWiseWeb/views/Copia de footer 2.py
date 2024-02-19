import streamlit as st
import base64
from pathlib import Path


def load_bootstrap():
    return st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)


def page_footer1():
    st.markdown("""
    <style>
        .container {
            display: flex;
        }

        .box {
            flex-grow: 1; 
            width: 100px;
            height: 100px;
            background-color: rgba(0, 0, 0, 0.05);
        }
    </style>
    <div class="container">
        <div class="box">Div 1</div>
        <div class="box">Div 2</div>
        <div class="box">Div 3</div>
    </div>
""", unsafe_allow_html=True)


def page_footer():
    # img_to_bytes and img_to_html inspired from https://pmbaumgartner.github.io/streamlitopedia/sizing-and-images.html

    load_bootstrap()

    def img_to_bytes(img_path):
        img_bytes = Path(img_path).read_bytes()
        encoded = base64.b64encode(img_bytes).decode()
        return encoded

    def img_to_html(img_path):
        img_html = "<img src='data:image/png;base64,{}' class='img-fluid'>".format(
            img_to_bytes(img_path)
        )
        return img_html

    st.markdown(
        """<div class="rounded-div text-center p-4" style="background-color: rgba(0, 0, 0, 0.05);">
            © 2024 Copyright:
            <a class="text-reset fw-bold" href="{% url 'home' %}">HotelWise.com</a>
        </div>""", unsafe_allow_html=True)


def page_footer2():
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
                    <img src="/static/imagenes/HenryLogo.svg" class="img-responsive" width="150%" alt="Responsive image">
                </a>
            </div>
        </section>

        <div class="rounded-div text-center p-4" style="background-color: rgba(0, 0, 0, 0.05);">
            © 2024 Copyright:
            <a class="text-reset fw-bold" href="{% url 'home' %}">HotelWise.com</a>
        </div>
        """, unsafe_allow_html=True)
