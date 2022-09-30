import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from streamlit import caching
import streamlit.components.v1 as components, html
from google1 import main as mn
import plotly.express as px
import base64
from streamlit_option_menu import option_menu

from Pages import About,WorldMap, Diagnostics, TimeSeries, Disaster, Compare

import copy

from pathlib import Path
import seaborn as sns
import geopandas

# import plotly.express as px
from PIL import Image
import plotly.graph_objects as go



all_factors1 = {
    'Score': 'Food System Resilience Score',

    'natural': 'Natural Capital',
    'BDH.new': 'Biodiversity and Habitat',
    'ECS': 'Ecosystem Status',
    'Sealevel': "Sealevel Rise",
    'Forest': 'Forest Area',
    'Land':'Land Degradation',
     'energy': 'Energy Footprint',
     'Water': 'Water Footprint',
    'GHP.new': 'Greenhouse emission per capita',
    'WaterQuant': 'Agricultural water quantity',
    'WaterQual': 'Agricultural water quality',

    'human': 'Human Capital',
    'Demographics': 'Population Growth',
   'literacy': 'Literacy Rate',
    'HDI': 'HDI Score',
     'labrate': 'Labor Participation Rate',
     'agprod':'Agricultural Production Index',
     'agVol':'Agricultural Production Volatility',
    'obesity':'Obsesity Prevelance',
    'foodsafe': 'Food Safety',
     'drinking':'Drinking Water',
     'Micro': 'Micronutrient Availability',
     'Protein': 'Protein Quality',
     'Diversity': 'Food Diversity Score',


     'social': 'Social Capital',
     'urbancap':'Urban Absorption Capacity',
     'safetynet': 'Presence of SafetyNet',
    'policyfood': 'Food Policy Score',
   'nutritional': 'Nutritional Standards',
    'gender': 'Gender Equity',
    'political': 'Political Stability',
     'corruption': 'Corruption',
   'conflict':'Conflict',

     'financial': 'Financial Capital',
     'perCapita': 'Per-Capita Income',
   'edu': 'Agricultural Education and Resources',
    'tariff': 'Agricultural Import Tariff',
     'agGDP': 'Agricultural GDP',
     'finance': 'Access to finance for farmers',
    'priceVol': 'Food Price Volatility',
    'foodloss': 'Food Loss and Waste',

    'manufactured': 'Manufactured Capital',
    'kofgi': 'Index of Globalization',
    'agadaptpolicy': 'Adaptation of agricultural policy',
    'climatesma': 'Climate smart agriculture',
    'disman': 'Disaster Mangement',
    'Nindex':'Sustainable use of Nitrogen',
    'RND': 'Agricultural R&D',
    'mobile': 'Mobile access to farmers',
    'transport': 'Transportation',
    'storage': 'Food Storage Facilities'
}


all_factors = {
    'Food System Resilience Score':'Score',

    'Natural Capital': 'natural',
    'Biodiversity and Habitat':'BDH.new',
    'Ecosystem Status': 'ECS',
    'Sealevel Rise': 'Sealevel',
    'Forest Area':'Forest',
    'Land Degradation':'Land',
     'Energy Footprint':'energy' ,
     'Water Footprint':'Water' ,
    'Greenhouse emission per capita':'GHP.new' ,
    'Agricultural water quantity':'WaterQuant' ,
    'Agricultural water quality':'WaterQual' ,

    'Human Capital':'human' ,
    'Population Growth':'Demographics',
   'Literacy Rate':'literacy' ,
    'HDI Score':'HDI' ,
    'Labor Participation Rate': 'labrate',
    'Agricultural Production Index': 'agprod',
    'Agricultural Production Volatility': 'agVol',
    'Obsesity Prevelance':'obesity',
    'Food Safety':'foodsafe',
     'Drinking Water':'drinking',
     'Micronutrient Availability':'Micro' ,
     'Protein Quality':'Protein' ,
     'Food Diversity Score':'Diversity' ,


     'Social Capital':'social' ,
     'Urban Absorption Capacity':'urbancap',
     'Presence of SafetyNet':'safetynet' ,
    'Food Policy Score':'policyfood',
   'Nutritional Standards':'nutritional' ,
    'Gender Equity':'gender' ,
    'Political Stability':'political' ,
     'Corruption':'corruption' ,
   'Conflict':'conflict',

     'Financial Capital':'financial',
    'Per-Capita Income': 'perCapita' ,
   'Agricultural Education and Resources':'edu' ,
    'Agricultural Import Tariff':'tariff' ,
     'Agricultural GDP':'agGDP' ,
     'Access to finance for farmers':'finance' ,
    'Food Price Volatility':'priceVol' ,
    'Food Loss and Waste':'foodloss' ,

    'Manufactured Capital':'manufactured' ,
    'Index of Globalization':'kofgi' ,
    'Adaptation of agricultural policy':'agadaptpolicy' ,
    'Climate smart agriculture':'climatesma' ,
    'Disaster Mangement':'disman' ,
    'Sustainable use of Nitrogen':'Nindex',
    'Agricultural R&D':'RND' ,
    'Mobile access to farmers':'mobile' ,
    'Transportation':'transport' ,
    'Food Storage Facilities':'storage'
}


# 
# st.set_page_config(layout="wide")
st.set_page_config(page_title="Food Systems Resilience Diagnostics", layout="wide")

a,b,c = st.sidebar.columns([1,5,1])
a.write('')
b.image("FSDR_1.png")
c.write('')


apps = [
    {"func": About.app, "title": "About", "icon": "info-circle"},
    {"func": WorldMap.app, "title": "World Map", "icon": "map"},
    {"func": Diagnostics.app, "title": "Diagnostics", "icon": "tools"},
    {"func": TimeSeries.app, "title": "Time-Series Analysis", "icon": "graph-up-arrow"},
    {"func": Disaster.app, "title": "Disaster Vulnerability", "icon": "radioactive"},
    {"func": Compare.app, "title": "Compare", "icon": "arrow-down-up"}
]

titles = [app["title"] for app in apps]
titles_lower = [title.lower() for title in titles]
icons = [app["icon"] for app in apps]

params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles_lower.index(params["page"][0].lower()))
else:
    default_index = 0


selected = option_menu(
        "Navigation",
        options=titles,
        icons=icons,
        menu_icon="cast",
        default_index=default_index,
        orientation = "horizontal"
    )
if(selected!="About"):
    st.sidebar.title("Control Center")

st.title("Food Systems Resilience Diagnostic (FSRD) Tool")
st.markdown('The FSRD gives the scores for several food system resilience indicators based on the performance of the countries.')
st.markdown('This Dashboard is the preliminary version of a diagnostic tool for rapidly scanning food stresses and shocks.')

for app in apps:
    if app["title"] == selected:
        app["func"]()
        break



@st.cache(persist=True)
def load_data(data_url):
    data=pd.read_csv(data_url)
    return data

alldata1 = pd.read_csv("FinalData.csv")

years = range(2012,2023)
dataColl = {}
for i in years:
    # abc = pd.read_csv(str(i)+'.csv',index_col= 'Country').transpose()
    # dataColl[i] = pd.read_csv(DATA_URL + "\\"+str(i)+'.csv',index_col= 'Country')
    dataColl[i] = alldata1[alldata1["Year"]==i]

org_data=dataColl[2022]


    
my_html1 = """<h3>Please share your experience of using this tool 
    <a href="https://forms.gle/JpgirdYtypVdiLC27" target="_blank">HERE</a> </h3>
    """

    
    





components.html(my_html1)

expander = st.expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")

st.sidebar.write("PARTNERS")
st.sidebar.image('partners.PNG')
# a1,b1,c1 = st.sidebar.columns(3)
# a1.image('CSIRO.png',width=100)
# b1.image('ANU.png',width=100)
# c1.image('DFAT.png',width=100)

# st.write("__Please share your experience here__")

with st.sidebar:
    components.html(my_html1)

