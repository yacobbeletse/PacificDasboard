#this is the main hosting file for the dashboard.

import streamlit as st
st.set_page_config(page_title="Pacific Food Security Dashboard", layout="wide")

import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit.components.v1 as components, html
import plotly.express as px
import base64
from streamlit_option_menu import option_menu

from Pages import  Compare, CountryProfile, Data_Credibility,Home


from pathlib import Path


#This is for scrolling to the top
def navigateHeader():

    st.markdown(f"Top", unsafe_allow_html=True)


apps = [
    {"func": Home.app, "title": "Home", "icon": "info-circle"},
    {"func": CountryProfile.app, "title": "Country Profile", "icon": "tools"},
    {"func": Compare.app, "title": "Compare", "icon": "graph-up-arrow"},
   # {"func": Disaster.app, "title": "Disaster Vulnerability", "icon": "radioactive"},
    {"func": Data_Credibility.app, "title": "Data Check", "icon": "file-check"},
    
]

titles = [app["title"] for app in apps]
titles_lower = [title.lower() for title in titles]
icons = [app["icon"] for app in apps]

params = st.experimental_get_query_params()
# print("Params: "+str(params))

if "page" in params:
    default_index = int(titles_lower.index(params["page"][0].lower()))
else:
    default_index =0

with st.sidebar:
    selected = option_menu(
            "Navigation",
            options=titles,
            icons=icons,
            menu_icon="cast",
            default_index=default_index,
            orientation = "vertical"
        )

# button = st.sidebar.button("Top", on_click=navigateHeader)
# st.sidebar.markdown("[Scroll to Top](#Top)")    
#CREATING A TAG FOR SCROLLING TO THE TOP WITH A BUTTON
st.markdown('<a href = "#{}"><button class = "scroll-to-top">Scroll to Top </button>'.format("Top"),unsafe_allow_html=True)

if(selected!="Home"):
    st.sidebar.title("Control Center")

#LOADING THE CSS FILE FOR STYLING THE HTML CONTENT
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

st.title("Pacific Food Security Dashboard",anchor="Top")

st.markdown("## *'You can improve what you can measure!!!'*")

st.markdown('The PFSD visualizes the data of Pacific nations for different indicators in four pillars of food security - availability, accessibility, utilization and stability.',unsafe_allow_html=True)


def chooseapp(selected):
    global apps
    for app in apps:
        if app["title"] == selected:
            app["func"]()
            break

chooseapp(selected)
st.sidebar.subheader(' ')
st.sidebar.subheader("PARTNERS")
st.sidebar.image('partners.PNG')

#THIS HAS A GOOGLE FORM LINKED.
my_html1 = """<h3>Please share your experience of using this tool 
    <a href="https://forms.gle/JpgirdYtypVdiLC27" target="_blank">HERE</a> </h3>
    """

#THIS IS OPTIONAL AND CAN BE REMOVED.
# expander = st.expander("FAQ")
# expander.write("Here you could put in some really, really long explanations...")


components.html(my_html1)

