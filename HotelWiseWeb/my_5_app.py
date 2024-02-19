import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title='Prueba NavBAR')
st.set_option('deprecation.showPyplotGlobalUse', False)

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
    <a class="navbar-brand" href="#" style="margin-left: 20px">
        <img src="/_src/HotelWiseLogo.Horizontal.jpg" height="40" class="d-inline-block align-top" alt="Logo">
    </a>
    <nav class="navbar navbar-expand-lg navbar-light " style="background-color: #FFF2CC">
        <a class="navbar-brand" href="#" style="margin-left: 20px">
            <img src="_src/HotelWiseLogo.Horizontal.png" height="40" class="d-inline-block align-top" alt="">
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

st.info(
    'Credit: HotelWise ([Project GitHub](https://github.com/jgutierrezladino/HotelWise))')
