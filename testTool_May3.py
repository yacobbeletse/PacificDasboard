from re import T
from matplotlib.axis import XAxis
from matplotlib.colors import hexColorPattern
import streamlit as st
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from streamlit import caching
import streamlit.components.v1 as components, html
from google1 import main as mn


import copy

from pathlib import Path
import seaborn as sns
import geopandas
from mpl_toolkits.axes_grid1 import make_axes_locatable

import plotly.express as px
from PIL import Image
import plotly.graph_objects as go


# import SessionState 
# session = SessionState.get(run_id=0)

spreadsheets = ['Best Interventions']

damages = {
    'Drought': [1,4,7,10,12.36,13.83,14.62,15.24,15.59,16.33],
    'Earthquake':[1,6,10,12.39,13.34,14.24,15.12,15.82,16.18,16.79],
    'Flood':[1,5,10,12.54,14.94,15.79,16.12,16.63,17.04,17.58],
    'Landslide':[1,2.5,4,5.5,7,8.5,9.12,11.24,12.26,13.69],
    'Storm':[1,8,11.9,13.3,13.99,15.45,15.93,16.49,17.17,17.93],
    'Volcanic Activity':[1,2,3,4,5,6,7,9.5,11.39,13.09],
    'Wildfire':[1,4,7,8.46,11.77,12.96,13.94,14.61,15.19,15.89],
    'Economic Crises':[1,3,5,7,9,11,13,15,17,19,21]
    # 'Political Conflict':[1,3,5,7,9,11,13,15,17,19,21]
}



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
    'foodsafe': 'Food Safetly',
     'drinking':'Drinking Water',
     'Micro': 'Micronutrient Availability',
     'Protein': 'Protein Quality',
     'Diversity': 'Food Diversity Score',


     'social': 'Social',
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


     'Social':'social' ,
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

plt_style = 'bmh'
# plt_style = 'fivethirtyeight'

# 
st.set_page_config(layout="wide")
# components.html('<head> <script src="https://embed-cdn.surveyhero.com/popup/user/main.ukeampdx.js" async></script> </head>', width=200, height=200)

# components.iframe(html_string)

# components.html(
#     """
#     <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
#     <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
#     <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
#     <div id="accordion">
#       <div class="card">
#         <div class="card-header" id="headingOne">
#           <h5 class="mb-0">
#             <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
#             Collapsible Group Item #1
#             </button>
#           </h5>
#         </div>
#         <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
#           <div class="card-body">
#             Collapsible Group Item #1 content
#           </div>
#         </div>
#       </div>
#       <div class="card">
#         <div class="card-header" id="headingTwo">
#           <h5 class="mb-0">
#             <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
#             Collapsible Group Item #2
#             </button>
#           </h5>
#         </div>
#         <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
#           <div class="card-body">
#             Collapsible Group Item #2 content
#             <script src="https://embed-cdn.surveyhero.com/popup/user/main.ukeampdx.js" async></script>
#           </div>
#         </div>
#       </div>
#     </div>
#     """,
#     height=600,
# )
st.title("Five Capitals Food System Resilience Score (5CFSRS) Analysis Tool")
st.markdown('The 5CFSRS gives the scores for several food system resilience indicators based on the performance of the countries.')
st.markdown('This Dashboard is the preliminary version of a diagnostic tool for rapidly scanning food stresses and shocks.')




@st.cache(persist=True)
def load_data(data_url):
    data=pd.read_csv(data_url)
    return data

DATA_URL = r"C:\Users\kc003\OneDrive - CSIRO\Projects\Composite Score\masterDataset\Yearwisedata"


years = range(2012,2021)
dataColl = {}
for i in years:
    abc = pd.read_csv(str(i)+'.csv',index_col= 'Country').transpose()
    # dataColl[i] = pd.read_csv(DATA_URL + "\\"+str(i)+'.csv',index_col= 'Country')
    dataColl[i] = abc
# org_data=pd.read_csv(DATA_URL + "\\"+str(2012)+'.csv',index_col= 'Country')
org_data=dataColl[2020]
trans_data = org_data.transpose()




## *********** FUNCTIONS ***********
def showOption():

    opts = ['Country','Indicator']
    op = st.sidebar.selectbox('Analysis by:',opts)
    return op

def showPlot(df,c1,c2,index = "country",visType="Des",check="nice"):
    # print(df)
    # df=df.transpose()
    # c1.write(df)
    # df.index.name=None
    plt.style.use(plt_style)
    for i in df.columns:
        # print(i)
        if i in all_factors1.keys():
            c1.write(str.upper(all_factors1[i]))
        else:
            c1.write(str.upper(i))

        # fig,axs = plt.subplots(figsize=(6,4))
        # df[i].sort_values(ascending= False).head(10).plot.barh()
        # plt.xlim([0,100])
        # # plt.show()
        # c1.pyplot(fig)

        # px.bar()
        # print(df[i])



        print(df.head())



        if index!="country":
            df["var_name"] = [all_factors1[i] for i in df.index]
        else:
             df["var_name"]  = df.index
            
    
       
        best_10 = df.sort_values(i,ascending = False).head(10)

        print(best_10)

        fig1 = px.bar(best_10, x = i,y = "var_name",orientation='h')
        # print(best_10)
        
        # print(best_10)
        # if check=="indx":
        #     fig1 = px.bar(best_10, x = i,y = "var_name",orientation='h')
        # else:
        #     #fig1 = px.bar(best_10, x = i,y = best_10.index,orientation='h')
        #     fig1 = px.bar(best_10, x = i,y = "var_name",orientation='h')

        fig1.update_layout(xaxis_range=[0,100],yaxis_title=None, xaxis_title=None)
        fig1.update_xaxes(tickfont=dict(size =15, family = "Arial Black"))
        fig1.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))
        # c1.write("Most Resilient Nations")
        c1.plotly_chart(fig1)

        if i in all_factors1.keys():
            c2.write(str.upper(all_factors1[i]))
        else:
            c2.write(str.upper(i))

        worst_10 = df.sort_values(i,ascending = True).head(10)
        print(worst_10)

        fig2 = px.bar(worst_10, x = i,y = "var_name",orientation='h')

        # if check=="indx":
        #     fig2 = px.bar(worst_10, x = i,y = "var_name",orientation='h')
        # else:
        #     fig2 = px.bar(worst_10, x = i,y = worst_10.index,orientation='h')

        # fig2 = px.bar(worst_10, x = i,y = worst_10.index,orientation='h')

        fig2.update_layout(xaxis_range=[0,100],yaxis_title=None, xaxis_title=None)
        fig2.update_xaxes(tickfont=dict(size =15, family = "Arial Black"))
        fig2.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))

        if(visType=="Des"):
            fig2.update_layout(xaxis_range=[0,100],yaxis_title=None, xaxis_title=None)
        else:
            fig2.update_layout(xaxis_range=[-100,5],yaxis_title=None, xaxis_title=None)
        # c1.write("Most Resilient Nations")
        c2.plotly_chart(fig2)
            
        
        # c1.write(df[i].sort_values(ascending= False).head(10))
 
        
        # # c2.write(df[i].sort_values(ascending= True).head(10))
        # fig1,axs1 = plt.subplots(figsize=(6,4))
        # # plt.style.use(plt_style)
        # # c1.write(df[i].sort_values(ascending= False).head(10))
        # df[i].sort_values(ascending= True).head(10).plot.barh()
        # if(visType=="Des"):
        #     plt.xlim([0,100])
        # else:
        #     plt.xlim([-50,5])
        # plt.ylabel(None)
        # # plt.show()
        # c2.pyplot(fig1)

def linePlot(df,countrySelect,c1,c2):
    df.index.name=None
    # c1.write(df)
    
    if(len(countrySelect)!=0):
        df =df[df.index.isin(countrySelect)]
        check = df.reset_index().set_index("Year")
        print(check)
        # c1.write(df)
        plt.style.use(plt_style)
        for i in range(int(len(df.columns)/2)):

            if(df.columns[2*i] in all_factors1.keys()):
        
                c1.write(str.upper(all_factors1[df.columns[2*i]]))


            # fig = px.line(check.groupby("index")[check.columns[2*i]])

            # c1.plotly_chart(fig)

            fig,axs = plt.subplots(figsize=(6,4))
                
            
            # c1.write(df[i].sort_values(ascending= False).head(10))
            # df[i].sort_values(ascending= False).head(10).plot.barh()
            df.reset_index().set_index("Year").groupby("index")[df.columns[2*i]].plot(legend = True,style='.-')

            plt.ylim([0,100])
            plt.legend(loc='lower left')
            # plt.show()
            c1.pyplot(fig)

            # c2.write(str.upper(df.columns[2*i+1]))
            c2.write(str.upper(all_factors1[df.columns[2*i+1]]))
            # c2.write(df[i].sort_values(ascending= True).head(10))
            fig1,axs1 = plt.subplots(figsize=(6,4))
            plt.style.use(plt_style)
            # c1.write(df[i].sort_values(ascending= False).head(10))
            df.reset_index().set_index("Year").groupby("index")[df.columns[2*i+1]].plot(legend = True,style='.-')
            plt.ylim([0,100])
            plt.legend(loc='lower left')
            # plt.show()
            c2.pyplot(fig1)

def linePlot1(df,countrySelect,conPlots,capital):
    # print(df)
    # df1 =df[df.index.isin(countrySelect)]
    # # c1.write(df)
    
    # df["Country"]=df.index
    
    # df.reset_index(inplace =True,drop=True)


    # conPlots.pyplot(df.plot())
    # conPlots.write(df)
    # print(df.columns)
    # if(len(countrySelect)!=0):
    #     fig2,axs = plt.subplots(figsize=(4,2))
    #     # df.reset_index().set_index("Year").plot()
    #     sns.lineplot(data=df,x = "Year",y = [df.columns])
    #     plt.legend(loc='lower left')
    #     plt.ylim([0,100])
    #     conPlots.pyplot(fig2)
    # print(df)
    # print(countrySelect)
    # print(df)
    # print(countrySelect)
    ltitle = []
    if capital=="Natural":
        ltitle = natural1
    elif capital=="Human":
        ltitle = human1
    elif capital=="Social":
        ltitle = social1
    elif capital=="Financial":
        ltitle = financial1
    else:
        ltitle = manufactured1
    
    if(len(countrySelect)!=0):
        for i in countrySelect:
            df1=df[df.index==i]
            print(df1)
            conPlots.write(str.upper(i))
        


            fig2,axs = plt.subplots(figsize=(6,2.5))
            # fig2,axs = plt.subplots()
            
                    
            plt.style.use(plt_style)
            # c1.write(df[i].sort_values(ascending= False).head(10))
            # df[i].sort_values(ascending= False).head(10).plot.barh()
            # df.reset_index().set_index("Year").plot(legend = True,style='.-')
            dfm =df1.melt('Year',var_name="Capitals",value_name="Score")
            sns.lineplot(x="Year", y="Score", hue = "Capitals", markers=True, data = dfm)
            plt.ylabel(None)
            plt.ylim([-5,105])
            plt.legend(ltitle,loc='center left',bbox_to_anchor=(1.1, 0.5),prop={'size': 5})
            plt.show()
            conPlots.pyplot(fig2)
            




def visualizeMap(c1,c2,conPlots):
     global dataColl  
     yearChoice =  st.sidebar.selectbox('Year',sorted(list(years),reverse=True))
     indicator1 = st.sidebar.selectbox('Indicator',all_factors.keys())
     indicator = all_factors[indicator1]
     df = dataColl[yearChoice][indicator]
     df.index = df.index.str.lower()
     
     world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
     world = world[(world.pop_est>0) & (world.name!="Antarctica")] 
     world['name'] = world['name'].str.lower()  
     merged = pd.merge(left = world, right = df, right_on = df.index, left_on = 'name', how = 'left').drop(["pop_est","continent","iso_a3","gdp_md_est"],1)
     print(merged)
     conPlots.write(str.upper(indicator1))
    #  conPlots.write(merged) 
    #  fig, ax = plt.subplots(figsize=(5,2.5))
    # #  ax.legend(fontsize=5,prop={'size': 2})
     gdf = geopandas.GeoDataFrame(merged, geometry="geometry")
     gdf.index = gdf.name
    # #  divider = make_axes_locatable(ax)
    # #  cax = divider.append_axes("right", size="5%", pad=0.1)
    #  gdf.plot(column=indicator, ax=ax, colormap='BuPu',vmin =0, vmax = 100,legend=True,legend_kwds={
    #                     'orientation': "horizontal",'shrink': 0.6, 'aspect':15},edgecolor='black',missing_kwds={
    #     "color": "lightgrey",
    #     "edgecolor": "black",
    #     # "hatch": "///",
    #     "label": "Missing values",
    #  })
    
    #  ax.axis('off')

     fig = px.choropleth(gdf, geojson=gdf.geometry, locations=gdf.index, color=indicator, width = 1200,color_continuous_scale="viridis",range_color=(0, 100),
     hover_name=gdf.index)
     fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
     fig.update_geos(fitbounds="locations", visible=False)
     fig.update_traces(marker_line_width=2)
    #  cb_ax = fig.axes[1] 
    #  cb_ax.tick_params(labelsize=5)


    #  fig.colorbar.lim(0,100)
     conPlots.plotly_chart(fig)






def visualizeOp(op,c1,c2,yearChoice=2020):
    global dataColl
    # countries = dataColl[yearChoice].index
    # global conPlots
    # conPlots.write("The default year is 2020")
    # print(type(yearChoice))
    if(isinstance(yearChoice,list)):
        if(len(yearChoice)==1):
            yearChoice = yearChoice[0]
        else:
            yearChoice=2020
        # if(len(yearChoice)==0):
        #     yearChoice = 2020
        # else:
        #     for i in yearChoice:
        #         dataColl[i] = pd.read_csv(DATA_URL + "\\"+str(i)+'.csv',index_col= 'Country')


    if op=="Country":
        countrySelect = st.sidebar.multiselect('Select Country(ies)',countries)
        print("choice of year = " + str(yearChoice))
        # abc = abc.append(i for i in countrySelect)
        # org_data=pd.read_csv(DATA_URL + "\\"+str(yearChoice)+'.csv',index_col= 'Country')
        org_data=dataColl[yearChoice]
        # df = org_data[countrySelect]
        df = org_data[org_data.index.isin(countrySelect)].transpose()
        print(df)

        showPlot(df,c1,c2,index='indicator')
     
    else:
        indSelect1 = st.sidebar.multiselect('Select indicator(s)',all_factors.keys())
        # trans_data=pd.read_csv(DATA_URL + "\\"+str(yearChoice)+'.csv',index_col= 'Country').transpose()
        indSelect = [all_factors[i] for i in indSelect1]
        print("choice of year = " + str(yearChoice))
        trans_data=dataColl[yearChoice]
        df1 = trans_data[indSelect]
        # print(df1)
        showPlot(df1,c1,c2,index='country')
  

def visualizeComp(op,c1,c2,conPlots,choiceDiff):
    global dataColl
    # global conPlots
    # conPlots.write("The default year is 2020")
    # print(type(yearChoice))
    yearChoice = []
    if choiceDiff=="1-year Analysis":
        yearChoice=[2020,2019]
    elif choiceDiff=="5-year Analysis":
        yearChoice=[2020,2015]
    elif choiceDiff == "YTD Analysis":
         yearChoice=[2020,2012]
    else:
        yearChoice=[i for i in range(2012,2021)]

    if op=="Country":
        countrySelect = st.sidebar.multiselect('Select Country(ies)',countries)
        # abc = abc.append(i for i in countrySelect)
        # df = dataColl[yearChoice[0]].subtract(dataColl[yearChoice[1]])[countrySelect]
        df = dataColl[yearChoice[0]].subtract(dataColl[yearChoice[1]])
        df = df[df.index.isin(countrySelect)].transpose()
        # df = org_data[countrySelect]
        print(df)
        showPlot(df,c1,c2,"Comp","indx")
    elif op =="Countryvs":
        countrySelect = st.sidebar.multiselect('Select Country(ies)',countries)
        indexes = ["Score","natural","human","social","financial","manufactured","Year"]
        tempData ={}
        df = pd.DataFrame()
        for i in yearChoice:
            abc = dataColl[i]
            abc["Year"]=i
            tempData[i]=abc
            df =pd.concat([df,tempData[i]])
        # print(df)
        df1= df[indexes]
        linePlot(df1,countrySelect,c1,c2)

    elif op =="Capitals":
        capital = st.sidebar.selectbox("Choose a capital", ["Natural", "Human","Social","Financial","Manufactured"])
        countrySelect = st.sidebar.multiselect('Select Country(ies)',countries)
        indexes=[]
        if capital=="Natural":
            indexes = natural
        elif capital=="Human":
            indexes = human
        elif capital=="Social":
            indexes = social
        elif capital=="Financial":
            indexes = financial
        else:
            indexes = manufactured
        indexes.append("Year")
        # print(indexes)
        tempData ={}
        df = pd.DataFrame()
        # print(yearChoice)
        for i in yearChoice:
            abc = dataColl[i]
            # print(abc)
            abc = abc[abc.index.isin(countrySelect)]
            abc["Year"]=i
            tempData[i]=abc
            df =pd.concat([df,tempData[i]])
        # print(df)
        df1= df[indexes]
        # print(df1)
        # df1 = df1.reset_index()
        # print(df1.index)
        linePlot1(df1,countrySelect,conPlots,capital)

    else:
        indSelect1 = st.sidebar.multiselect('Select indicator(s)',all_factors.keys())
        indSelect = [all_factors[i] for i in indSelect1]
        df1 = dataColl[yearChoice[0]].subtract(dataColl[yearChoice[1]])[indSelect]
        print(df1)
        showPlot(df1,c1,c2,index="country",visType="Comp")



def doSA(scale,shock,intensity,duration,c1,c2,country=None,con=None):
    global dataColl
    disinfo = pd.read_csv('disInfo.csv',index_col ='index')
    yearChoice = 2020
    if scale=="Global":
        temp = pd.DataFrame(disinfo[shock])
        print(temp.head())
        con.write('Global Vulnerability of {}'.format(shock))

        best_10 = temp.sort_values(shock, ascending = False).head(10)
        fig1 = px.bar(best_10, x =shock , y = best_10.index,orientation='h', text = shock)
        fig1.update_layout(xaxis_range=[0,110],yaxis_title=None,xaxis_title ='Standardized Impact')
        fig1.update_xaxes(tickfont=dict(size =15, family = "Arial Black"))
        fig1.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))
        fig1.update_traces(textposition='outside')
        # c1.write("Most Resilient Nations")
        c1.plotly_chart(fig1)

        worst_10 = temp[temp>0].sort_values(shock, ascending = True).head(10)
        fig2 = px.bar(worst_10, x = shock, y = worst_10.index,orientation='h',text = shock)
        fig2.update_layout(xaxis_range=[0,110],yaxis_title=None,xaxis_title ='Standardized Impact')
        fig2.update_xaxes(tickfont=dict(size =15, family = "Arial Black"))
        fig2.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))
        fig2.update_traces(textposition='outside')
        # c2.write("Most Vulnerable Nations")
        c2.plotly_chart(fig2)







        effect = pd.read_csv('globalscale.csv',index_col='index')
        df_effect = effect[shock]
        print(df_effect.head())
        df = dataColl[yearChoice]
        df=df[['Score']]
    
        # df = df1.transpose()
        print(df.head())
        # print(df1.head())
        data = pd.merge(df,df_effect, right_on = df_effect.index, left_on=df.index, how = "left")
        print(data.head())
        plot_data = pd.DataFrame()
        plot_data["Country"] = df.index

        plot_data["Score"] = data['Score'] - intensity*duration*data[shock]
    
        # plot_data[plot_data>0]=100        

        # for i in df.index:
        #     plot_data[i] = data[i] - intensity*duration*data[shock]
        plot_data =plot_data.set_index("Country")
        plot_data[plot_data<0]=0
        plot_data[plot_data>100]=100
 

        # # for i in df1.index:
        # #     plot_data[i] = data[i] - intensity*duration*data[shock]
        # # plot_data =plot_data.set_index("Country")
        # # plot_data[plot_data<0]=0
        
        print(plot_data.head())

        # plot_d = plot_data.T
        # print(plot_d)
        # plot_d['natural'] = plot_d[natural].mean(axis =1)
        # plot_d['human'] = plot_d[human].mean(axis =1)
        # plot_d['social'] = plot_d[social].mean(axis =1)
        # plot_d['financial'] = plot_d[financial].mean(axis =1)
        # plot_d['manufactured'] = plot_d[manufactured].mean(axis =1)
        # plot_d['Score'] = np.round(plot_d[['natural','human','social', 'financial','manufactured']].mean(axis =1),1)
        # # print(plot_d)
        # # df['Score'] = np.round(df.mean(axis=1),1)
        # # print('printing df after score')
        # # print(df1)

        plot_d = plot_data.copy()

        plot_d['diff'] = np.round(plot_data['Score']-df['Score'],1)

        # print(plot_d)

        # plot_d[plot_d>100]=100

        best_10 = plot_d.sort_values("Score", ascending = False).head(10)
        fig1 = px.bar(best_10, x ="Score" , y = best_10.index,orientation='h', text = "diff")
        fig1.update_layout(xaxis_range=[0,110],yaxis_title=None)
        fig1.update_xaxes(tickfont=dict(size =15, family = "Arial Black"))
        fig1.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))
        fig1.update_traces(textposition='outside')
        c1.write("Most Resilient Nations")
        c1.plotly_chart(fig1)

        worst_10 = plot_d.sort_values("Score", ascending = True).head(10)
        fig2 = px.bar(worst_10, x = "Score", y = worst_10.index,orientation='h',text = "diff")
        fig2.update_layout(xaxis_range=[0,110],yaxis_title=None)
        fig2.update_xaxes(tickfont=dict(size =15, family = "Arial Black"))
        fig2.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))
        fig2.update_traces(textposition='outside')
        c2.write("Most Vulnerable Nations")
        c2.plotly_chart(fig2)


    elif(scale=="Country"):
        effect = pd.read_csv('Country/{}.csv'.format(country),index_col='index')
        
        try:
            disdata = disinfo[disinfo.index==country].transpose().reset_index()
            print(disdata.head())
            # con.write("Historical Impact Analysis of Shocks")
            fig3 = px.bar(disdata.sort_values(by=country,ascending=False), y =country , x = 'index',orientation='v',text = country)
            fig3.update_layout(yaxis_range=[0,max(disdata[country])+3],yaxis_title='Standardized Impact Score',xaxis_title=None, font = dict(
                size =18,
            )
            )
            fig3.update_xaxes(tickfont=dict(size =15, family = "Arial Black"))
            fig3.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))
            fig3.update_traces(textposition='outside')
            con.plotly_chart(fig3)
        except:
            con.write("No food shocks reported in {}".format(country))


        




        df_effect1 = effect[shock]
        print(df_effect1.head())

        # df_effect = df_effect1[df_effect1>0]
        # df_effect = df_effect1[df_effect1>0].sort_values(shock, ascending= False)
        
        df_effect = df_effect1.copy()

        df1 = dataColl[yearChoice]
        print(df1.head())

        print("prinding ddf1")

        df = df1[df1.index==country].transpose()
        # print(df.transpose().index)
    
        data = pd.merge(df_effect,df, left_on = df_effect.index, right_on=df.index, how = "left")
        # print(data)
        plot_data = pd.DataFrame()
        plot_data["Indicator"] = df_effect.index
        # print(plot_data)

        

        for i in df.transpose().index:
            plot_data[i] = data[i] - intensity*duration*data[shock]
        plot_data =plot_data.set_index("Indicator")
        plot_data[plot_data>100]=100

        plot_d = plot_data
        plot_d["var_name"] = [all_factors1[i] for i in plot_d.index]
        # print(plot_d)
        # print(plot_data.sort_values(country, ascending=False))
        # plot_d['natural'] = plot_d[natural].mean(axis =1)
        # plot_d['human'] = plot_d[human].mean(axis =1)
        # plot_d['social'] = plot_d[social].mean(axis =1)
        # plot_d['financial'] = plot_d[financial].mean(axis =1)
        # plot_d['manufactured'] = plot_d[manufactured].mean(axis =1)
        # plot_d['Score'] = np.round(plot_d[['natural','human','social', 'financial','manufactured']].mean(axis =1),1)
        # print(plot_d)
        plot_d['diff'] = np.round(plot_d[country]-df[country],1)
        
        best_10 = plot_d[plot_d[country]>0].sort_values(country, ascending = False).head(10)
        # fig1 = px.bar(best_10, x =country , y = best_10.index,orientation='h')
        fig1 = px.bar(best_10, x =country , y = "var_name",orientation='h',text = "diff")
        fig1.update_layout(xaxis_range=[0,120],yaxis_title=None)
        fig1.update_xaxes(tickfont=dict(size =15, family = "Arial Black"))
        fig1.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))
        fig1.update_traces(textposition='outside')
        c1.write("Most Resilient Indicators")
        # c1.write(country)
        c1.plotly_chart(fig1)

        worst_10 = plot_d[plot_d[country]>0].sort_values(country, ascending = True).head(10)
        # fig2 = px.bar(worst_10, x = country, y = worst_10.index,orientation='h')
        fig2 = px.bar(worst_10, x = country, y = "var_name",orientation='h',text = "diff")
        fig2.update_layout(xaxis_range=[0,120],yaxis_title=None)
        fig2.update_xaxes(tickfont=dict(size =15, family = "Arial Black"))
        fig2.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))
        fig2.update_traces(textposition='outside')
        c2.write("Most Vulnerable Indicators")
        # c2.write(country)
        c2.plotly_chart(fig2)
      
        # print(plot_data)
        
        # plot_d = plot_data.T
        # print(plot_d)
        # plot_d['natural'] = plot_d[natural].mean(axis =1)
        # plot_d['human'] = plot_d[human].mean(axis =1)
        # plot_d['social'] = plot_d[social].mean(axis =1)
        # plot_d['financial'] = plot_d[financial].mean(axis =1)
        # plot_d['manufactured'] = plot_d[manufactured].mean(axis =1)
        # plot_d['Score'] = np.round(plot_d[['natural','human','social', 'financial','manufactured']].mean(axis =1),1)
        # print(plot_d)

        # best_10 = plot_d.sort_values("Score", ascending = False).head(10)
        # fig1 = px.bar(best_10, x ="Score" , y = best_10.index,orientation='h')
        # fig1.update_layout(xaxis_range=[0,100],yaxis_title=None)
        # c1.write("Most Resilient Nations")
        # c1.plotly_chart(fig1)

        # worst_10 = plot_d.sort_values("Score", ascending = True).head(10)
        # fig2 = px.bar(worst_10, x = "Score", y = worst_10.index,orientation='h')
        # fig2.update_layout(xaxis_range=[0,100],yaxis_title=None)
        # c2.write("Most Vulnerable Nations")
        # c2.plotly_chart(fig2)
    
    else:
        print("nth")


def displayGuage(temp_df,conPlots):

    print(temp_df['Food System Shock'],shock)
    
    data1 = temp_df[temp_df['Food System Shock']==shock].dropna(axis=1).drop(columns = ["Timestamp","Email Address","Food System Shock", "Impact Intensity"]).reset_index(drop=True)
    # temp = data1.transpose()
    print(data1.transpose(),data1.transpose().columns)
    
    trans_df = data1.transpose()
    trans_df.info()
    trans_df['Avg'] = trans_df.mean(axis=1)
    best_int = trans_df.sort_values(by = "Avg", ascending = False).head(3)
    names = list(best_int.index)
    values = list(best_int["Avg"])
    # trans_df =trans_df.rename(columns = )
    print(best_int)
    print(best_int.index)

    co1, co2,co3 = conPlots.columns(3)
    fig1 = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = values[0],
    mode = "gauge+number",
    # number ={'suffix': "%"},
    title = {'text': names[0]},
# delta = {'reference': 380},
    gauge = {'axis': {'range': [None, 10]},
            'steps' : [
                {'range': [0, 3], 'color': "lightgray"},
                {'range': [3, 6], 'color': "gray"}],
            'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.8, 'value': 100}}))

    fig1.update_layout(width=500)
    fig2 = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value =values[1],
    mode = "gauge+number",
    # number ={'suffix': "%"},
    title = {'text': names[1]},
# delta = {'reference': 380},
    gauge = {'axis': {'range': [None, 10]},
            'steps' : [
                {'range': [0, 3], 'color': "lightgray"},
                {'range': [3, 6], 'color': "gray"}],
            'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.8, 'value': 100}}))    

    fig3 = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = values[2],
    mode = "gauge+number",
    # number ={'suffix': "%"},
    title = {'text': names[2]},
# delta = {'reference': 380},
    gauge = {'axis': {'range': [None, 10]},
            'steps' : [
                {'range': [0, 3], 'color': "lightgray"},
                {'range': [3, 6], 'color': "gray"}],
            'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.8, 'value': 100}}))  


    fig1.update_layout(width=500) 
    fig2.update_layout(width=500)  
    fig3.update_layout(width=500) 
    co1.plotly_chart(fig1)
    co2.plotly_chart(fig2)
    co3.plotly_chart(fig3)




###### SIDEBAR *****************




# countries = org_data.drop('Indicator',1).columns
countries = org_data.index

st.sidebar.image("icon.png",width =150)
st.sidebar.title('Control Center')
# st.sidebar.markdown('Control Parameters Here')
# st.sidebar.checkbox("Select a Country", True, key=1)

analysisType = st.sidebar.radio(
     "Visualization By:",
     ('World Map','Descriptive Analysis', 'Comparative Analysis','Scenario Analysis',"Best Interventions"))
print(analysisType)


conPlots = st.container()
col1, col2 = conPlots.columns((0.85,1))

conSliders = st.container()

# global c1,c2

c1,c2 = conSliders.columns(2)

if(analysisType=="World Map"):
    visualizeMap(c1,c2,conPlots)    



elif(analysisType=="Descriptive Analysis"):
    c1.markdown('__STRENGTHS__')
    c2.markdown('__WEAKNESSES__')
    yearChoice =  st.sidebar.selectbox('Select Year(s)',sorted(list(years),reverse=True))
    print(type(yearChoice))
    op =showOption()
    # if len(yearChoice)==0:
    #     # conPlots.write("If the year is empty, the default year is 2020")
    #     visualizeOp(op,c1,c2)
    # else:
    #     visualizeOp(op,c1,c2,yearChoice)
    visualizeOp(op,c1,c2,yearChoice)


elif(analysisType=="Comparative Analysis"):
    
    choiceDiff =  st.sidebar.selectbox('Select a type',["1-year Analysis","5-Year Analysis", "YTD Analysis", "Country vs Country", "Capitals"])
    if choiceDiff in ["1-year Analysis","5-Year Analysis", "YTD Analysis",]:
        op =showOption()
    elif choiceDiff== "Country vs Country":
        op = "Countryvs"
    else:
        op = choiceDiff
    visualizeComp(op,c1,c2,conPlots,choiceDiff)


elif((analysisType=="Scenario Analysis")):
    # effect = pd.read_csv('effect1.csv', index_col = "Variables")
    # effect = {}
    scale = st.sidebar.selectbox('Select a scale',["Global","Country"])
    country=None
    if (scale=="Country"):
        country = st.sidebar.selectbox('Select a country',countries)
        conPlots.write(country)
    shock = st.sidebar.selectbox('Select a shock',damages.keys())
    intensity_score = st.sidebar.slider('Enter the shock intensity', min_value=0,max_value=10,value=0)
    # print(shock)
    # hazard_score = damages[shock]
    # damageamount = float(st.sidebar.text_input('Please enter possible damages in US $ in millions', value = 0))
    
    # intensity_score = min(max(int(min(hazard_score, key=lambda x:abs(x-damageamount**0.1)))-1,1),10)
    # st.sidebar.text('Estimated Impact Intensity is: '+str(intensity_score))
    # intensity = st.sidebar.slider('Intensity of Shock', min_value = 0, max_value = 10,value = 0)
    # duration = st.sidebar.slider('Duration of Shock', min_value = 1, max_value = 10,value = 0)
    
    doSA(scale,shock,intensity_score,1,c1,c2,country,con=conPlots)
    # st.markdown("# _Page will be up and running soon.... Hang on!!!_")

else:
    # st.markdown("# _Page will be up and running soon.... Hang on!!!_")
    mn(spreadsheets)
    temp_df = pd.read_csv('survey_data.csv')
    # print(temp_df)
    user = st.sidebar.selectbox('Select User Type',["Expert","User"])
    shock = st.sidebar.selectbox('Select a shock',damages.keys())
    intensity = st.sidebar.slider('Intensity of Shock', min_value = 0, max_value = 10,value = 0)
    # duration = st.sidebar.slider('Duration of Shock in days', min_value = 1, max_value = 120,value = 0)
#     co1, co2,co3 = conPlots.columns(3)
#     fig1 = go.Figure(go.Indicator(
#     domain = {'x': [0, 1], 'y': [0, 1]},
#     value = np.round(np.random.rand(),2)*100,
#     mode = "gauge+number",
#     number ={'suffix': "%"},
#     title = {'text': "Intervention 1"},
#    # delta = {'reference': 380},
#     gauge = {'axis': {'range': [None, 100]},
#              'steps' : [
#                  {'range': [0, 25], 'color': "lightgray"},
#                  {'range': [25, 50], 'color': "gray"}],
#              'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.8, 'value': 100}}))


    # components.html('''
    # <div id="medium-widget"></div>
    # <script src="https://medium-widget.pixelpoint.io/widget.js"></script>
    # <script>MediumWidget.Init({renderTo: '#medium-widget', params: {"resource":"https://medium.com/@mehulgupta_7991","postsPerLine":3,"limit":9,"picture":"small","fields":["description","author","claps","publishAt"],"ratio":"landscape"}})</script>''')

    my_html = """
    <a href="https://forms.gle/W8XkFaq28DinvvWU7" target="_blank">Click here to enter your expert opinion</a>
    """
    
    if user=="Expert":
        components.html(my_html)
        conPlots.write("_Please enter Food System Shock as_ **{}** _and Intensity of Shock as_ **{}** _while filling up the form!_".format(shock,intensity))

        done =conPlots.checkbox("Check this box when done with putting your expert opinion / Uncheck the box if you want to enter additional information!")

        if done:
            # conPlots.empty()
            mn(spreadsheets)
            temp_df = pd.read_csv('survey_data.csv')
            displayGuage(temp_df,conPlots)


            done=False





    else:
        displayGuage(temp_df,conPlots)


    #     fig1.update_layout(width=500)
    #     fig2 = go.Figure(go.Indicator(
    #     domain = {'x': [0, 1], 'y': [0, 1]},
    #     value =np.round(np.random.rand(),2)*100,
    #     mode = "gauge+number",
    #     number ={'suffix': "%"},
    #     title = {'text': "Intervention 2"},
    # # delta = {'reference': 380},
    #     gauge = {'axis': {'range': [None, 100]},
    #             'steps' : [
    #                 {'range': [0, 25], 'color': "lightgray"},
    #                 {'range': [25, 50], 'color': "gray"}],
    #             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.8, 'value': 100}}))    

    #     fig3 = go.Figure(go.Indicator(
    #     domain = {'x': [0, 1], 'y': [0, 1]},
    #     value = np.round(np.random.rand(),2)*100,
    #     mode = "gauge+number",
    #     number ={'suffix': "%"},
    #     title = {'text': "Intervention 3"},
    # # delta = {'reference': 380},
    #     gauge = {'axis': {'range': [None, 100]},
    #             'steps' : [
    #                 {'range': [0, 25], 'color': "lightgray"},
    #                 {'range': [25, 50], 'color': "gray"}],
    #             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.8, 'value': 100}}))   
    #     fig1.update_layout(width=500) 
    #     fig2.update_layout(width=500)  
    #     fig3.update_layout(width=500) 
    #     co1.plotly_chart(fig1)
    #     co2.plotly_chart(fig2)
    #     co3.plotly_chart(fig3)

        # conPlots.write(data1)




    # html_string = 'src="https://embed-cdn.surveyhero.com/popup/user/main.ukeampdx.js" async'

    # my_html = f"<script>{my_js}</script>"

    










# ind_only = org_data.drop(['score','natural','human','social','financial','manufactured'],0)
# df = pd.DataFrame()
# df1 =pd.DataFrame()



# col1, col2 = conPlots.columns((0.85,1))

# conSliders = st.container()

# # global c1,c2

# c1,c2 = conSliders.columns(2)



# c1,c2,c3,c4 = conSliders.columns(4)










# c3.markdown('__QUALITY & SAFETY__')
# c4.markdown('__NATURAL RESOURCES & RESILIENCE__')

# for i in df.columns:
#     c1.write(df[i].sort_values(ascending= False).head(10))

# for i in df.columns:
#     c2.write(df[i].sort_values(ascending= True).head(10))

# pDATA_URL = r"C:\Users\kc003\OneDrive - CSIRO\Projects\Bayesian work\DataSet\pro{}.csv".format(countrySelect)

# org_data=load_data(DATA_URL)

# changedfac1 = []

# # global changedfac1 

# def retData(dfk):
#     # print('Performing calculation ...')
#     df = copy.copy(dfk)
#     df['4_7'] = 0.75*df['4_7_1']+0.25*df['4_7_2']
#     df['4_6'] = 0.2*df['4_6_1']+0.2*df['4_6_2']+0.2*df['4_6_3']+0.4*df['4_6_4']
#     df['4_5'] = 0.6*df['4_5_1']+0.4*df['4_5_2']
#     df['4_4'] = 0.5*df['4_4_1']+0.5*df['4_4_2']
#     df['4_3'] = 0.6*df['4_3_1']+0.2*df['4_3_2']+0.2*df['4_3_3']
#     df['4_2'] = 0.8*df['4_2_1']+0.2*df['4_2_2']
#     df['4_1'] = 0.25*df['4_1_1']+0.239*df['4_1_2']+0.208*df['4_1_3']+0.083*df['4_1_4']+0.229*df['4_1_5']
#     df['4'] = 0.211*df['4_1']+0.14*df['4_2']+0.14*df['4_3']+0.123*df['4_4']+0.105*df['4_5']+0.211*df['4_6']+0.07*df['4_7']


#     df['3_5'] = 0.321*df['3_5_1']+0.429*df['3_5_2']+0.25*df['3_5_3'] 
#     df['3_3'] = 1/3*df['3_3_1']+1/3*df['3_3_2']+1/3*df['3_3_3'] 
#     df['3_2'] = 0.265*df['3_2_1']+0.235*df['3_2_2']+0.235*df['3_2_3'] +0.265*df['3_2_4']
#     df['3'] = 0.203*df['3_1']+0.136*df['3_2']+0.254*df['3_3']+0.237*df['3_4']+0.169*df['3_5']

#     df['2_7'] = 0.5*df['2_7_1']+0.5*df['2_7_2']
#     df['2_5'] = 0.294*df['2_5_1']+0.235*df['2_5_2']+0.235*df['2_5_3']+0.235*df['2_5_4']
#     df['2_3'] = 0.176*df['2_3_1']+0.294*df['2_3_2']+0.29*df['2_3_3']+0.235*df['2_3_4']  
#     df['2_2'] = 0.5*df['2_2_1']+0.5*df['2_2_2']
#     df['2_1'] = 0.733*df['2_1_1']+0.267*df['2_1_2']
#     df['2'] = 0.263*df['2_1']+0.091*df['2_2']+0.141*df['2_3']+0.152*df['2_4']+0.121*df['2_5']+0.141*df['2_6']+0.091*df['2_7']     

#     df['1_6'] = 0.353*df['1_6_1']+0.353*df['1_6_2']+0.294*df['1_6_3']
#     df['1_5'] = 0.25*df['1_5_1']+0.25*df['1_5_2']+0.25*df['1_5_3']+0.25*df['1_5_4']
#     df['1'] = 0.204*df['1_1']+0.185*df['1_2']+0.204*df['1_3']+0.093*df['1_4']+0.204*df['1_5']+0.111*df['1_6']

#     df['Overall'] = 0.324*df['1']+0.324*df['2']+0.176*df['3']+0.176*df['4']
                
#     return df

# def nextPlot(Year):
#     global changedfac1
#     # print('ok= {}'.format(changedfac1))
#     df1 = pd.read_csv(pDATA_URL)
#     df1["Year"] = df1["Year"].astype('int')
#     # actual = df1[df1["Year"]<=2020]
#     baseline = df1[df1["Year"]<=Year]
#     prodata =copy.copy(baseline)
#     # print('Changed values = {}'.format(len(changedfac1)))
#     for i in changedfac1:
#         fill = prodata['Year']>2020
#         prodata[i].loc[fill,]= updatedVal[i]
#     prodata = retData(prodata)
#     # print(prodata['1'], baseline['1'])
#     with plt.style.context('fivethirtyeight'):
#         fig1,ax = plt.subplots()

#         ax.set_title("Overall GFSI")

#         l1 = ax.plot(org_data['Year'],org_data['Overall'])
#         l2 = ax.plot(baseline['Year'],baseline['Overall'], color = 'black')
#         l3 = ax.plot(prodata['Year'],prodata['Overall'],color = 'red')
#         plt.legend([l1,l2,l3],labels = ['Actual','Baseline','Forecast'])
#         # plt.legend('upper left')
#         col1.plotly_chart(fig1,use_container_width=False)

#         fig,axs = plt.subplots(2,2)
#         # x_axis = df1['Year']
#         # plt.style.context('ggplot')
#         plt.subplots_adjust(hspace=0.4, wspace=0.15)

#         ax1 = plt.subplot(221)
#         ax1.set_title("Affordability")
#         ll1 = ax1.plot(org_data['Year'],org_data['1'])
#         ll2 = ax1.plot(baseline['Year'],baseline['1'], color = 'black')
#         ll3 = ax1.plot(prodata['Year'],prodata['1'], color = 'red')
        
#         ax2 = plt.subplot(222)
#         ax2.set_title("Availability")
#         ax2.plot(org_data['Year'],org_data['2'])
#         ax2.plot(baseline['Year'],baseline['2'], color = 'black')
#         ax2.plot(prodata['Year'],prodata['2'], color = 'red')
            

#         ax3 = plt.subplot(223)
#         ax3.set_title("Quality and Safety")
#         ax3.plot(org_data['Year'],org_data['3'])
#         ax3.plot(baseline['Year'],baseline['3'], color = 'black')
#         ax3.plot(prodata['Year'],prodata['3'], color = 'red')
            

#         ax4 = plt.subplot(224)
#         ax4.set_title("Natural resources and resilience")
#         ax4.plot(org_data['Year'],org_data['4'])
#         ax4.plot(baseline['Year'],baseline['4'], color = 'black')
#         ax4.plot(prodata['Year'],prodata['4'], color = 'red')

#         # fig1.legend([ll1,ll2,ll3],labels = ['Actual','Baseline','Forecast'], loc = 'center right')
#         # plt.legend()
#         plt.tight_layout()

#         col2.plotly_chart(fig,use_container_width=False)
    

# # fig,axs = plt.subplots(2,2)
# # plt.style.use('tableau-colorblind10')
# # plt.subplots_adjust(hspace=0.4, wspace=0.1)

# # ax1 = plt.subplot(221)
# # ax1.set_title("Affordability")
    
# # l1 =ax1.plot(x_axis,df1['1'])
   
# # ax2 = plt.subplot(222)
# # ax2.set_title("Availability")
# # ax2.plot(x_axis,df1['2'])
    

# # ax3 = plt.subplot(223)
# # ax3.set_title("Quality and Safety")
# # ax3.plot(x_axis,df1['3'])
    

# # ax4 = plt.subplot(224)
# # ax4.set_title("Natural resources and resilience")
# # ax4.plot(x_axis,df1['4'])
    

# # ax5 = plt.subplot(235)
# # ax5.set_title("Overall GFSI")
# # ax5.plot(x_axis,df1['Overall'])
    

# # ax6 = plt.subplot(236)
# # ax6.axis('off')


# # col2.plotly_chart(fig,use_container_width=False)


# # min_date, max_date = preprocessing.retDate(org_data)
# # print(min_date,max_date)

# # # print(df)
# # df = preprocessing.drop_uncol(org_data)

# # df1 = copy.copy(df)

# # prechecked_data = preprocessing.preCheck(df)

# # fixedCol, best_order, best_order_diff = preprocessing.predictData(df,prechecked_data)
# # do_nth = set(fixedCol)- set(best_order.keys())-set(best_order_diff.keys())

# # Year = st.sidebar.slider("Projection Year", 2021,2100, 2030, step = 1)

# # changed = {}

# # visualize.show_plot(Year,changed, data = org_data, data1=df1, best_order= best_order, best_order_diff=best_order_diff, do_nth=do_nth, check_data=prechecked_data)


# # c1.markdown('AFFORDABILITY')
# # c2.markdown('AVAILABILITY')
# # c3.markdown('QUALITY & SAFETY')
# # c4.markdown('NATURAL RESOURCES & RESILIENCE')
# factor1 = [i for i in all_factors.keys() if i.startswith('1') and i not in nonFac]
# factor2 = [i for i in all_factors.keys() if i.startswith('2') and i not in nonFac]
# factor3 = [i for i in all_factors.keys() if i.startswith('3') and i not in nonFac]
# factor4 = [i for i in all_factors.keys() if i.startswith('4') and i not in nonFac]
# updatedVal = {}
# for i in factor1:
#     s1 = c1.slider(all_factors.get(i),0,100, value = int(org_data.tail(1)[i]), step =1)
#     updatedVal[i]=s1
    

# for i in factor2:
#     s2 = c2.slider(all_factors.get(i),0,100, value = int(org_data.tail(1)[i]), step =1)
#     updatedVal[i]=s2

# for i in factor3:
#     s3 = c3.slider(all_factors.get(i),0,100, value = int(org_data.tail(1)[i]), step =1)
#     updatedVal[i]=s3

# for i in factor4:
#     s4 = c4.slider(all_factors.get(i),0,100, value = int(org_data.tail(1)[i]), step =1)
#     updatedVal[i]=s4
# # print(updatedVal)

# #Plotting
# x_axis = org_data['Year']
# #print(x_axis)
# # print(df['Year'].min())
# # iniplot = visualize.initPlot(org_data)





#         # df1= copy.copy(org_data)

# # fig1,ax = plt.subplots(figsize=(7,3))
# # plt.style.use('tableau-colorblind10')

# # ax.set_title("Overall GFSI")
# # ax.plot(x_axis,df1['Overall'])






# # frac1_val = resetval.resVal(data = org_data,st = st)
# # c1,c2,c3,c4 = {}
# # # def disSlider(c1,c2,c3,c4):
# #     global fac1_val
# #     fac1_val = {}

# #     # st.sidebar.write("Variables RESET")
# #     for i in factor1:
# #         if i in nonFac:
# #         s1 = c1.slider(all_factors.get(i),0,100, value = int(org_data.tail(1)[i]), step =1)
# #         fac1_val[i]=s1

# #     for i in factor2:
# #         s2 = c2.slider(all_factors.get(i),0,100, value = int(org_data.tail(1)[i]), step =1)
# #         fac1_val[i]=s2

# #     for i in factor3:
# #         s3 = c3.slider(all_factors.get(i),0,100, value = int(org_data.tail(1)[i]), step =1)
# #         fac1_val[i]=s3

# #     for i in factor4:
# #         s4 = c4.slider(all_factors.get(i),0,100, value = int(org_data.tail(1)[i]), step =1)
# #         fac1_val[i]=s4
#     # st.sidebar.write('fac1_val = {}'.format(len(fac1_val)))
#     # return fac1_val
# # def resSlider(c1,c2,c3,c4):
# #     global fac1_val, placeholder
# #     placeholder.empty()
# #     fac1_val = {}

# #     # st.sidebar.write("Variables RESET")

# #     for i in factor1:
# #         fac1_val[i] = c1.slider(all_factors.get(i),0,100, value = int(org_data.tail(1)[i]), step =1)

# #     for i in factor2:
# #         fac1_val[i] = c2.slider(all_factors.get(i),0,100, value = int(org_data.tail(1)[i]), step =1)
    

# #     for i in factor3:
# #         fac1_val[i] = c3.slider(all_factors.get(i),0,100, value = int(org_data.tail(1)[i]), step =1)


# #     for i in factor4:
# #         fac1_val[i] = c4.slider(all_factors.get(i),0,100, value = int(org_data.tail(1)[i]), step =1)



# # # fac1_val = resetSlider()
# # placeholder = st.empty()


# # disSlider(c1,c2,c3,c4)

# # a1,a2 = st.sidebar.columns(2)
# # # simulate = a1.button('Simulate', on_click = disSlider, args = (c1,c2,c3,c4))
# # if a1.button('Simulate'):
# #     pass
# # # a2.button('Reset Variables', on_click = resSlider, args = (c1,c2,c3,c4))

# # if a2.button("Reset Variables"):
# #     st.caching.clear_cache()
# #     conPlots.empty()
# #     col2.plotly_chart(fig1,use_container_width=False)
# #     # resSlider(c1,c2,c3,c4)

# #Side Bar Stuffs

# # changedfac1 = []

# def printChange():
#     global changedfac1
#     if (len(updatedVal)!=0):
#         # global changedfac1
#         changedfac1 = [i for i in all_factors.keys() if (i not in nonFac.keys() and updatedVal[i]!=int(org_data.tail(1)[i]))]
#         # print('Length of changed frac = {}'.format(len(changedfac1)))

#     if len(changedfac1)!=0 and len(updatedVal)!=0:
#         r1 =st.sidebar
#         # st.sidebar.markdown("You changed the following variables")
#         with r1:
#             r1.write("You changed the following variables")

#         for i in changedfac1:
#             # st.sidebar.markdown('{} changed from {} to {}'.format(all_factors.get(i),int(org_data.tail(1)[i]),fac1_val[i]))
#             with r1:
#                 r1.write('{} changed from {} to {}'.format(all_factors.get(i),int(org_data.tail(1)[i]),updatedVal[i]))

# printChange()
# # if (len(updatedVal)!=0):
# #     # global changedfac1
# #     changedfac1 = [i for i in all_factors.keys() if (i not in nonFac.keys() and updatedVal[i]!=int(org_data.tail(1)[i]))]
# #     # print('Length of changed frac = {}'.format(len(changedfac1)))

# # if len(changedfac1)!=0 and len(updatedVal)!=0:
# #     r1 =st.sidebar
# #     # st.sidebar.markdown("You changed the following variables")
# #     with r1:
# #         r1.write("You changed the following variables")

# #     for i in changedfac1:
# #         # st.sidebar.markdown('{} changed from {} to {}'.format(all_factors.get(i),int(org_data.tail(1)[i]),fac1_val[i]))
# #         with r1:
# #             r1.write('{} changed from {} to {}'.format(all_factors.get(i),int(org_data.tail(1)[i]),updatedVal[i]))
# if Year <=2020:
#     df1= copy.copy(org_data)
#     with plt.style.context('fivethirtyeight'):
#         fig1,ax = displayplot.gfsi(df1)
#         col1.plotly_chart(fig1,use_container_width=False)


#         fig,axs = displayplot.initPlot(df1)
#         col2.plotly_chart(fig,use_container_width=False)
# else:
#     nextPlot(Year)


# if resetBut:
#     with r1:
#         caching.clear_cache()
#         r1.write("OK ")
    # st.empty()
    # st.sidebar.markdown("All Variables reset to Year 2020")

    # session.run_id += 1
    # abc = st.session_state.count+1
    # frac1_val = resetval.resVal(data = org_data,st = st, ok=abc)
    # fac1_val = resetSlider(org_data,st)
    # c1.empty()
# def nextPlot():
#     global changedfac1
#     df1 = pd.read_csv(pDATA_URL)
#     df1["Year"] = df1["Year"].astype('int')
#     # actual = df1[df1["Year"]<=2020]
#     baseline = df1[df1["Year"]<=Year]
#     prodata =copy.copy(baseline)
#     print('Changed values = {}'.format(len(changedfac1)))
#     for i in changedfac1:
#         fill = prodata['Year']>2020
#         prodata[fill][i] = updatedVal[i]
#     prodata = retData(prodata)
#     with plt.style.context('fivethirtyeight'):
#         fig1,ax = plt.subplots()

#         ax.set_title("Overall GFSI")

#         l1 = ax.plot(org_data['Year'],org_data['Overall'])
#         l2 = ax.plot(baseline['Year'],baseline['Overall'], color = 'black')
#         l3 = ax.plot(prodata['Year'],prodata['Overall'], color = 'red')
#         fig1.legend([l1,l2,l3],labels = ['Actual','Baseline','Forecast'], loc = 'center right')
#         col1.plotly_chart(fig1,use_container_width=False)

#         fig,axs = plt.subplots(2,2)
#         # x_axis = df1['Year']
#         # plt.style.context('ggplot')
#         plt.subplots_adjust(hspace=0.4, wspace=0.15)

#         ax1 = plt.subplot(221)
#         ax1.set_title("Affordability")
#         ll1 = ax1.plot(org_data['Year'],org_data['1'])
#         ll2 = ax1.plot(baseline['Year'],baseline['1'], color = 'black')
#         ll3 = ax1.plot(prodata['Year'],prodata['1'], color = 'red')
        
#         ax2 = plt.subplot(222)
#         ax2.set_title("Availability")
#         ax2.plot(org_data['Year'],org_data['2'])
#         ax2.plot(baseline['Year'],baseline['2'], color = 'black')
#         ax2.plot(prodata['Year'],prodata['2'], color = 'red')
            

#         ax3 = plt.subplot(223)
#         ax3.set_title("Quality and Safety")
#         ax3.plot(org_data['Year'],org_data['3'])
#         ax3.plot(baseline['Year'],baseline['3'], color = 'black')
#         ax3.plot(prodata['Year'],prodata['3'], color = 'red')
            

#         ax4 = plt.subplot(224)
#         ax4.set_title("Natural resources and resilience")
#         ax4.plot(org_data['Year'],org_data['3'])
#         ax4.plot(baseline['Year'],baseline['3'], color = 'black')
#         ax4.plot(prodata['Year'],prodata['3'], color = 'red')

#         fig1.legend([ll1,ll2,ll3],labels = ['Actual','Baseline','Forecast'], loc = 'center right')
#         plt.legend()
#         plt.tight_layout()

#         col2.plotly_chart(fig,use_container_width=False)
    

expander = st.expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")
