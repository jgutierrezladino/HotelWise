import streamlit as st


def page_layout():
    st.set_page_config(
        layout="wide",
        initial_sidebar_state="collapsed",
        page_title='HotelWise',
        page_icon="_src/HotelWiseLogo.Icon.png",)
    st.set_option('deprecation.showPyplotGlobalUse', False)

    hide_streamlit_style = """
    <style>
        MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
    </style>

    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    page_bg_img = f"""
        <style>
            [data-testid="stAppViewContainer"] > .main
            {{
                
                background-image: url("https://i.postimg.cc/4xgNnkfX/Untitled-design.png");
                background-size: cover;
                background-position: center;
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
