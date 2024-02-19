import streamlit as st
import numpy as np
import pandas as pd
from streamlit_extras.stylable_container import stylable_container


#############################################################################################
# remover barra lateral

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

st.image('_src/HotelWiseLogo.Horizontal.Fondo.png')
#############################################################################################
# remover barra lateral
# st.set_page_config(initial_sidebar_state="collapsed")

st.markdown(
    """
<style>
    div [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    div [data-testid=stTitle]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)
#############################################################################################
st.markdown(
    """
    <link rel="stylesheet" type="text/css" href="https://www.example.com/style.css">
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://www.example.com/image.jpg");
    }
   </style>
    """,
    unsafe_allow_html=True
)
#############################################################################################
hide_streamlit_style = """
<style>
MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
#############################################################################################

hide_streamlit_style = """
<style>
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}
</style>

"""
st.title("Test")
if st.checkbox('Remove padding'):
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
#############################################################################################
st.markdown("<h1 style='text-align: center; color: red;'>Some title</h1>",
            unsafe_allow_html=True)
st.title("This is outside the container")
#############################################################################################
with stylable_container(
    key="green_button",
    css_styles="""
        button {
            background-color: green;
            color: white;
            border-radius: 20px;
        }
        """,
):
    st.button("Green button")

st.button("Normal button")

with stylable_container(
    key="container_with_border",
    css_styles="""
        {
            border: 1px solid rgba(49, 51, 63, 0.2);
            border-radius: 0.5rem;
            padding: calc(1em - 1px);
            background-color: rgb(255, 242, 204)
        }
        """,
):
    st.markdown("This is a container with a border.")
with stylable_container(
    key="container_with_no_border",
    css_styles="""
        {
            background-color: rgb(255, 242, 204)
        }
        """,
):
    st.markdown("This is a container")
#############################################################################################
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://i.postimg.cc/4xgNnkfX/Untitled-design.png");
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
#############################################################################################
with st.container():
    st.title("This is inside the container")
    st.markdown("<h1 style='text-align: center; color: red;'>Some title</h1>",
                unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg")

    with col2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg")

    with col3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg")

    st.title("This is inside the container")

#############################################################################################

# You can call any Streamlit command, including custom components:

st.bar_chart(np.random.randn(50, 3))
st.write("This is outside the container")

#############################################################################################
