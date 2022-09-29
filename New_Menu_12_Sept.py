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

from Pages import About,WorldMap, Diagnostics, TimeSeries, Disaster

import copy
from pathlib import Path
import seaborn as sns
import geopandas

# import plotly.express as px
from PIL import Image
import plotly.graph_objects as go


spreadsheets = ['Best Interventions', 'Experience']


# damages = {
#     'Drought': [1,4,7,10,12.36,13.83,14.62,15.24,15.59,16.33],
#     'Earthquake':[1,6,10,12.39,13.34,14.24,15.12,15.82,16.18,16.79],
#     'Flood':[1,5,10,12.54,14.94,15.79,16.12,16.63,17.04,17.58],
#     'Landslide':[1,2.5,4,5.5,7,8.5,9.12,11.24,12.26,13.69],
#     'Storm':[1,8,11.9,13.3,13.99,15.45,15.93,16.49,17.17,17.93],
#     'Volcanic Activity':[1,2,3,4,5,6,7,9.5,11.39,13.09],
#     'Wildfire':[1,4,7,8.46,11.77,12.96,13.94,14.61,15.19,15.89],
#     'Economic Crises':[1,3,5,7,9,11,13,15,17,19,21]
#     # 'Political Conflict':[1,3,5,7,9,11,13,15,17,19,21]
# }


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


natural = ['BDH.new', 'ECS', 'Sealevel', 'Forest', 'Land', 'energy', 'Water', 'GHP.new', 'WaterQuant', 'WaterQual']
human = ['Demographics', 'literacy', 'HDI', 'labrate', 'agprod', 'agVol', 'obesity', 'foodsafe', 'drinking', 'Micro', 'Protein', 'Diversity']
social = ['urbancap', 'safetynet', 'policyfood', 'nutritional', 'gender', 'political', 'corruption', 'conflict']
financial = ['perCapita', 'edu', 'tariff', 'agGDP', 'finance', 'priceVol', 'foodloss']
manufactured = ['kofgi', 'agadaptpolicy', 'climatesma', 'disman', 'Nindex', 'RND', 'mobile', 'transport', 'storage']

natural1 = [all_factors1[i] for i in ['BDH.new', 'ECS', 'Sealevel', 'Forest', 'Land', 'energy', 'Water', 'GHP.new', 'WaterQuant', 'WaterQual']]
human1 = [all_factors1[i] for i in ['Demographics', 'literacy', 'HDI', 'labrate', 'agprod', 'agVol', 'obesity', 'foodsafe', 'drinking', 'Micro', 'Protein', 'Diversity']]
social1 = [all_factors1[i] for i in ['urbancap', 'safetynet', 'policyfood', 'nutritional', 'gender', 'political', 'corruption', 'conflict']]
financial1 = [all_factors1[i] for i in ['perCapita', 'edu', 'tariff', 'agGDP', 'finance', 'priceVol', 'foodloss']]
manufactured1 = [all_factors1[i] for i in ['kofgi', 'agadaptpolicy', 'climatesma', 'disman', 'Nindex', 'RND', 'mobile', 'transport', 'storage']]

capitals = ['Score','natural','human','social','financial','manufactured']

plt_style = 'bmh'


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
    {"func": Disaster.app, "title": "Disaster Vulnerability", "icon": "radioactive"}
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

DATA_URL = r"C:\Users\kc003\OneDrive - CSIRO\Projects\Composite Score\masterDataset\Yearwisedata"

alldata = pd.read_csv("LL1.csv")

alldata1 = pd.read_csv("restructure.csv")

years = range(2012,2021)
dataColl = {}
for i in years:
    abc = pd.read_csv(str(i)+'.csv',index_col= 'Country').transpose()
    # dataColl[i] = pd.read_csv(DATA_URL + "\\"+str(i)+'.csv',index_col= 'Country')
    dataColl[i] = abc

org_data=dataColl[2020]
trans_data = org_data.transpose()


    
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

