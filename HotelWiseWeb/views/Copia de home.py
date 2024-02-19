import streamlit as st
import pandas as pd

logo = "_src/HotelWiseLogo.Horizontal.png"

st.set_page_config(
    layout="wide", initial_sidebar_state="collapsed", page_title='HOME')
st.set_option('deprecation.showPyplotGlobalUse', False)

hide_streamlit_style = """
<style>
    MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

left_co, cent_co, last_co = st.columns(3)
with cent_co:
    st.image(logo, use_column_width=True)

st.image("_src/HotelWiseLogo.Horizontal.png")
background = Image.open("_src/HotelWiseLogo.Horizontal.png")
col1, col2, col3 = st.columns([0.2, 5, 0.2])
col2.image(background, use_column_width=True)
st.markdown(
    """
    <style>
        button[title^=Exit]+div [data-testid=stImage]{
            text-align: center;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True
)
st.image("_src/HotelWiseLogo.Horizontal.png")


page_bg_img = f"""
    <style>
        [data-testid="stAppViewContainer"] > .main 
        {{
            background-image: url("https://i.postimg.cc/4xgNnkfX/Untitled-design.png");
            background-size: cover;
            background-position: center center;
            background-repeat: no-repeat;
            background-attachment: local;
        }}
        [data-testid="stHeader"]
        {{
            background: rgba(0,0,0,0);
        }}
    </style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar navbar-expand-lg navbar-light " style="background-color: #FFF2CC">
    <a class="navbar-brand" href="#" style="margin-left: 20px">
        <img src="HotelWiseLogo.Horizontal.png" height="40" class="d-inline-block align-top" alt="logo">
    </a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
            <li class="nav-item active">
            <a class="nav-link" href="{% url 'home' %}">Acerca De <span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
            <a class="nav-link" href="{% url 'reviews' %}">Reviews</a>
            </li>
            <li class="nav-item">
            <a class="nav-link" href="{% url 'home' %}">Busqueda</a>
            </li>
            <li class="nav-item">
            <a class="nav-link " href="{% url 'home' %}">Contacto</a>
            </li>
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Dropdown
                </a>
                <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Action</a></li>
                <li><a class="dropdown-item" href="#">Another action</a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">Something else here</a></li>
                </ul>
            </li>
        </ul>
        <form class="d-flex" role="search">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success" type="submit">Search</button>
        </form>                    
    </div>
</nav>
""", unsafe_allow_html=True)

st.image('_src/HotelWiseLogo.Horizontal.Fondo.png')
st.markdown("""
<footer class="text-center text-lg-start bg-light text-muted">
    <section
        class="d-flex justify-content-center justify-content-lg-between
        p-4 border-bottom">
        <div class="me-5 d-none d-md-block" style="margin-left: 1cm;">
            <span>Carrera
                Data Science PT</span>
        </div>
        <div class="text-md-center" style="margin-right: 1.5cm;">
            <a href="https://www.soyhenry.com/">
                <img src="/static/imagenes/HenryLogo.svg"
                    class="img-responsive" width="150%"
                    alt="Responsive image">
            </a>
        </div>
    </section>
    <div class="text-center p-4" style="background-color: rgba(0, 0, 0,
        0.05);">
        © 2024 Copyright:
        <a class="text-reset fw-bold" href="{% url 'home' %}">HotelWise.com</a>
    </div>
</footer>
""", unsafe_allow_html=True)
st.info(
    'Credit: HotelWise ([Project GitHub](https://github.com/jgutierrezladino/HotelWise))')
