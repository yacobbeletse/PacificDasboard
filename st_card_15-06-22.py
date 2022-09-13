import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from streamlit import caching
import streamlit.components.v1 as components, html
from google1 import main as mn
import plotly.express as px
import base64


import copy

from pathlib import Path
import seaborn as sns
import geopandas

# import plotly.express as px
from PIL import Image
import plotly.graph_objects as go


spreadsheets = ['Best Interventions', 'Experience']


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
st.set_page_config(layout="wide")

st.title("Five Capitals Food System Resilience Score (5CFSRS) Analysis Tool")
st.markdown('The 5CFSRS gives the scores for several food system resilience indicators based on the performance of the countries.')
st.markdown('This Dashboard is the preliminary version of a diagnostic tool for rapidly scanning food stresses and shocks.')




@st.cache(persist=True)
def load_data(data_url):
    data=pd.read_csv(data_url)
    return data

DATA_URL = r"C:\Users\kc003\OneDrive - CSIRO\Projects\Composite Score\masterDataset\Yearwisedata"

alldata = pd.read_csv("LL1.csv")

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

def displayPDF(file,st):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1200" height="1000" type="application/pdf"></iframe>'

    # Displaying File
    st.write(pdf_display, unsafe_allow_html=True)


def showOption():

    opts = ['Country','Indicator']
    op = st.sidebar.selectbox('Analysis by:',opts)
    return op

def showPlot(df,conPlots,index = "country",visType="Des",check="nice",present=pd.DataFrame()):
    # print(df)
    # df=df.transpose()
    # c1.write(df)
    # df.index.name=None
    plt.style.use(plt_style)
    for i in df.columns:
        # print(i)
        
        d1,d2 = conPlots.columns(2)

        if i in all_factors1.keys():
            d1.subheader(str.upper(all_factors1[i]))
        else:
            d1.subheader(str.upper(i))
        
        # if i in all_factors1.keys():
        #     d2.subheader(str.upper(all_factors1[i]))
        # else:
        #     d2.subheader(str.upper(i))

        

        print(df.head())



        if index!="country":
            df["var_name"] = [all_factors1[i] for i in df.index]
        else:
             df["var_name"]  = df.index

        if(index!="country"):
            a1,a2,a3,a4,a5,a6 = conPlots.columns(6)

            if(present.empty):       

                a1.metric(label="Food System Resilience Score",value=df.loc[df["var_name"]=="Food System Resilience Score",i])
                a2.metric(label="Natural Capital",value=df.loc[df["var_name"]=="Natural Capital",i])
                a3.metric(label="Human Capital",value=df.loc[df["var_name"]=="Human Capital",i])
                a4.metric(label="Social Capital",value=df.loc[df["var_name"]=="Social Capital",i])
                a5.metric(label="Financial Capital",value=df.loc[df["var_name"]=="Financial Capital",i])
                a6.metric(label="Manufactured Capital",value=df.loc[df["var_name"]=="Manufactured Capital",i])
            else:
                print(present.head())
                print("OKOK")
                print(df.head())
                # a1.metric(label="Food System Resilience Score",value=10,delta=str(np.round(df.loc[df["var_name"]=="Food System Resilience Score",i][0],2))+" %")
                # a2.metric(label="Natural Capital",value=10,delta=str(np.round(df.loc[df["var_name"]=="Natural Capital",i][0],2))+" %")
                # a3.metric(label="Human Capital",value=10,delta=str(np.round(df.loc[df["var_name"]=="Human Capital",i][0],2))+" %")
                # a4.metric(label="Social Capital",value=10,delta=str(np.round(df.loc[df["var_name"]=="Social Capital",i][0],2))+" %")
                # a5.metric(label="Financial Capital",value=10,delta=str(np.round(df.loc[df["var_name"]=="Financial Capital",i][0],2))+" %")
                # a6.metric(label="Manufactured Capital",value=10,delta=str(np.round(df.loc[df["var_name"]=="Manufactured Capital",i][0],2)) +" %")               
                
                #
                a1.metric(label="Food System Resilience Score",value=present.loc[present.index=="Score",i][0],delta=str(np.round(df.loc[df["var_name"]=="Food System Resilience Score",i][0],2)))
                a2.metric(label="Natural Capital",value=present.loc[present.index=="natural",i][0],delta=str(np.round(df.loc[df["var_name"]=="Natural Capital",i][0],2)))
                a3.metric(label="Human Capital",value=present.loc[present.index=="human",i][0],delta=str(np.round(df.loc[df["var_name"]=="Human Capital",i][0],2)))
                a4.metric(label="Social Capital",value=present.loc[present.index=="social",i][0],delta=str(np.round(df.loc[df["var_name"]=="Social Capital",i][0],2)))
                a5.metric(label="Financial Capital",value=present.loc[present.index=="financial",i][0],delta=str(np.round(df.loc[df["var_name"]=="Financial Capital",i][0],2)))
                a6.metric(label="Manufactured Capital",value=present.loc[present.index=="manufactured",i][0],delta=str(np.round(df.loc[df["var_name"]=="Manufactured Capital",i][0],2)))   
            
       
        best_10 = df.sort_values(i,ascending = False).head(10)

        print(best_10)

        c1,c2 = conPlots.columns(2)

        # st.metric(label="Food System Resilience Score",value=df.loc[df["var_name"]=="Food System Resilience Score",i])

        fig1 = px.bar(best_10, x = i,y = "var_name",orientation='h')
        
        fig1.update_layout(xaxis_range=[0,100],yaxis_title=None, xaxis_title=None)
        fig1.update_xaxes(tickfont=dict(size =15, family = "Arial Black"))
        fig1.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))
        # c1.write("Most Resilient Nations")
        # c1.markdown('__STRENGTHS__')
    
        c1.plotly_chart(fig1)



        worst_10 = df.sort_values(i,ascending = True).head(10)
        print(worst_10)

        fig2 = px.bar(worst_10, x = i,y = "var_name",orientation='h')


        fig2.update_layout(xaxis_range=[0,100],yaxis_title=None, xaxis_title=None)
        fig2.update_xaxes(tickfont=dict(size =15, family = "Arial Black"))
        fig2.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))

        if(visType=="Des"):
            fig2.update_layout(xaxis_range=[0,100],yaxis_title=None, xaxis_title=None)
        else:
            fig2.update_layout(xaxis_range=[-100,5],yaxis_title=None, xaxis_title=None)
        # c1.write("Most Resilient Nations")
        # c2.markdown('__WEAKNESSES__')
        c2.plotly_chart(fig2)

        del d1,d2,c1,c2

        if index!="country":
            del a1,a2,a3,a4,a5,a6
            
        
        
def linePlot(df,countrySelect,conPlots):
    df.index.name=None
    # c1.write(df)
    c1,c2 = conPlots.columns(2)
    if(len(countrySelect)!=0):
        df =df[df.index.isin(countrySelect)]
        check = df.reset_index().set_index("Year")
        print(check)
        # c1.write(df)
        plt.style.use(plt_style)
        for i in range(int(len(df.columns)/2)):

            if(df.columns[2*i] in all_factors1.keys()):
        
                c1.subheader(str.upper(all_factors1[df.columns[2*i]]))


            fig,axs = plt.subplots(figsize=(6,4))

            df.reset_index().set_index("Year").groupby("index")[df.columns[2*i]].plot(legend = True,style='.-')

            plt.ylim([0,100])
            plt.legend(loc='lower left')
            # plt.show()
            c1.pyplot(fig)

            # c2.write(str.upper(df.columns[2*i+1]))
            c2.subheader(str.upper(all_factors1[df.columns[2*i+1]]))
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
            conPlots.subheader(str.upper(i))
        


            fig2,axs = plt.subplots(figsize=(6,2.5))
            # fig2,axs = plt.subplots()
            
                    
            plt.style.use(plt_style)

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
     print(df.head())
     df.index = df.index.str.lower()
     
     world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
     world = world[(world.pop_est>0) & (world.name!="Antarctica")] 
     world['name'] = world['name'].str.lower()  
     merged = pd.merge(left = world, right = df, right_on = df.index, left_on = 'name', how = 'left').drop(columsn =["pop_est","continent","iso_a3","gdp_md_est"])
     print(merged)
     conPlots.write(str.upper(indicator1))

     gdf = geopandas.GeoDataFrame(merged, geometry="geometry")
     gdf.index = gdf.name

     fig = px.choropleth(gdf, geojson=gdf.geometry, locations=gdf.index, color=indicator, width = 1200,color_continuous_scale="viridis",range_color=(0, 100),
     hover_name=gdf.index)
     fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
     fig.update_geos(fitbounds="locations", visible=False)
     fig.update_traces(marker_line_width=2)

     conPlots.plotly_chart(fig)


def visualizeMap1(gdf,conPlots):

    #  global alldata
    #  df = alldata.copy()
    # #  print(df.head())
    # #  yearChoice =  st.sidebar.selectbox('Year',sorted(list(years),reverse=True))
    #  indicator1 = st.sidebar.selectbox('Indicator',all_factors.keys())
    #  indicator = all_factors[indicator1]
    #  df = df[["Year","Country",indicator]]
    # #  print(df.columns)
     
    # #  df.index = df.index.str.lower()
    #  df["Country"]=df["Country"].str.lower()
    #  df["Year"] = df["Year"].astype("int")
    #  print(df.head())
     
    #  world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
    #  world = world[(world.pop_est>0) & (world.name!="Antarctica")] 
    #  world['name'] = world['name'].str.lower()  
    #  merged = pd.merge(left = world, right = df, right_on = "Country", left_on = 'name', how = 'left').drop(["pop_est","continent","iso_a3","gdp_md_est"],1)
    # #  print(merged)
    #  conPlots.write(str.upper(indicator1))
    # #  conPlots.write(merged) 
    # #  fig, ax = plt.subplots(figsize=(5,2.5))
    # # #  ax.legend(fontsize=5,prop={'size': 2})
    #  gdf = geopandas.GeoDataFrame(merged, geometry="geometry").dropna()
    #  gdf.index = gdf.name
    #  gdf["Year"]=gdf["Year"].astype("int")

     fig = px.choropleth(gdf, geojson=gdf.geometry, locations=gdf.index, color=indicator, width = 1250,color_continuous_scale="plasma",range_color=(0, 100),
     hover_name=gdf.index,animation_frame="Year")
     fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
     fig.update_geos(fitbounds="locations", visible=False)
     fig.update_traces(marker_line_width=2)
    #  cb_ax = fig.axes[1] 
    #  cb_ax.tick_params(labelsize=5)


    #  fig.colorbar.lim(0,100)
     conPlots.plotly_chart(fig)


def visualizeMapan(c1,c2,conPlots):
    df = pd.read_csv('alldisaster.csv')
    print(df.head())
    fd = df.groupby(["Year","Country"])["AdjustedDamages_new"].sum().reset_index()
    print(fd.head())

    fig = px.choropleth(fd, locations="Country", color="AdjustedDamages_new", width = 1200,color_continuous_scale="viridis",range_color=(0, 100),
                     hover_name="Country",
                     animation_frame="Year",
                     projection="equirectangular")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0},)
    fig.update_yaxes(visible=False)
    # fig.update_geos(fitbounds="locations", visible=False)
    fig.update_traces(marker_line_width=2)
    
    conPlots.plotly_chart(fig)
    



def visualizeOp(op,conPlots,yearChoice=2020):
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

    # c1.markdown('__STRENGTHS__')
    # c2.markdown('__WEAKNESSES__')
    if op=="Country":
        countrySelect = st.sidebar.multiselect('Select Country(ies)',countries)
        print("choice of year = " + str(yearChoice))
        # abc = abc.append(i for i in countrySelect)
        # org_data=pd.read_csv(DATA_URL + "\\"+str(yearChoice)+'.csv',index_col= 'Country')
        org_data=dataColl[yearChoice]
        # df = org_data[countrySelect]
        df = org_data[org_data.index.isin(countrySelect)].transpose()
        print(df)

        showPlot(df,conPlots,index='indicator')
     
    else:
        indSelect1 = st.sidebar.multiselect('Select indicator(s)',all_factors.keys())
        # trans_data=pd.read_csv(DATA_URL + "\\"+str(yearChoice)+'.csv',index_col= 'Country').transpose()
        indSelect = [all_factors[i] for i in indSelect1]
        print("choice of year = " + str(yearChoice))
        trans_data=dataColl[yearChoice]
        df1 = trans_data[indSelect]
        # print(df1)
        showPlot(df1,conPlots,index='country')
  

def visualizeComp(op,conPlots,choiceDiff):
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
        original = dataColl[yearChoice[0]][dataColl[yearChoice[0]].index.isin(countrySelect)].transpose()
        # df = org_data[countrySelect]
        print('*****')
        print(original.head())
        showPlot(df,conPlots,"Comp","indx",present = original)
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
        linePlot(df1,countrySelect,conPlots)

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
        showPlot(df1,conPlots,index="country",visType="Comp")



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

        plot_data =plot_data.set_index("Country")
        plot_data[plot_data<0]=0
        plot_data[plot_data>100]=100

        print(plot_data.head())


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
      

    
    else:
        print("nth")

def doSA1(dff,scale,shock,intensity,duration,conPlots,c1,c2,country=None):
    # print(df.head(10))
    # conPlots = st.container()
    # c1,c2 = conPlots.columns(2)
    temp = dff.copy()
    temp['intensity'] = temp['intensity'].apply(np.round)
    print(temp.head())
    
    # print(temp.head())

    global dataColl
    # disinfo = pd.read_csv('disInfo.csv',index_col ='index')
    yearChoice = 2020
    if scale=="Global":
        temp = temp.rename(columns = {'intensity':shock})
        temp[shock] = temp[shock].astype("float").apply(np.round)
        # temp = pd.DataFrame(disinfo[shock])
        # print(temp.head())
        with conPlots:
            st.subheader('Global Vulnerability of {}'.format(shock))

        best_10 = temp.sort_values(shock, ascending = False).head(10)
        print(best_10)
        fig1 = px.bar(best_10, x =shock , y = "Country",orientation='h', text = shock)
        fig1.update_layout(xaxis_range=[0,110],yaxis_title=None,xaxis_title ='Standardized Impact')
        fig1.update_xaxes(tickfont=dict(size =15, family = "Arial Black"))
        fig1.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))
        fig1.update_traces(textposition='outside')
        c1.subheader("Most Affected Nations")
        c1.plotly_chart(fig1)

        worst_10 = temp[temp[shock]>0].sort_values(shock, ascending = True).head(10)
        fig2 = px.bar(worst_10, x = shock, y ="Country",orientation='h',text = shock)
        fig2.update_layout(xaxis_range=[0,110],yaxis_title=None,xaxis_title ='Standardized Impact')
        fig2.update_xaxes(tickfont=dict(size =15, family = "Arial Black"))
        fig2.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))
        fig2.update_traces(textposition='outside')
        c2.subheader("Least Affected Nations")
        c2.plotly_chart(fig2)







        effect = pd.read_csv('globalscale.csv',index_col='Country')
        df_effect = effect[shock]
        print(df_effect.index)
        print(df_effect.head())
        df = dataColl[yearChoice].reset_index()
    
        df = df[['index','Score']]

        # df=df[['Country','Score']]
        df = df.set_index("index")
    
        # df = df1.transpose()
        print(df.index)
        print(df.head())
        # print(df1.head())
        data = pd.merge(df,df_effect, right_on = df_effect.index, left_on=df.index, how = "left")
        plot_data = data.rename(columns = {'key_0':'Country'})
        print(plot_data.head())


        print('intensity = '+str(intensity))
        print(plot_data[shock])
        plot_data["diff"] = plot_data['Score'] - plot_data['Score']* intensity/10*plot_data[shock]
        plot_data[plot_data["diff"]<0]["diff"]=0
        plot_data[plot_data["diff"]>100]["diff"]=100
        plot_data["diff"] = plot_data["diff"].apply(np.round)
        plot_data["delta"] = np.round(( plot_data["diff"]-plot_data["Score"])/plot_data["Score"]*100,1)
    
        # # plot_data[plot_data>0]=100        

        # for i in df.index:
        #     plot_data[i] = data[i] - intensity*duration*data[shock]
        plot_data =plot_data.set_index("Country")
        # plot_data[plot_data<0]=0
        # plot_data[plot_data>100]=100

        print(plot_data.head())
 


        plot_d = plot_data.copy()

        best_10 = plot_d.sort_values("Score", ascending = False).head(10)
        fig1 = px.bar(best_10, x ="Score" , y = best_10.index,orientation='h', text = "delta")
        fig1.update_layout(xaxis_range=[0,110],yaxis_title=None)
        fig1.update_xaxes(tickfont=dict(size =15, family = "Arial Black"))
        fig1.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))
        fig1.update_traces(textposition='outside')
        c1.subheader("Most Resilient Nations")
        c1.plotly_chart(fig1)

        worst_10 = plot_d.sort_values("Score", ascending = True).head(10)
        fig2 = px.bar(worst_10, x = "Score", y = worst_10.index,orientation='h',text = "delta")
        fig2.update_layout(xaxis_range=[0,110],yaxis_title=None)
        fig2.update_xaxes(tickfont=dict(size =15, family = "Arial Black"))
        fig2.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))
        fig2.update_traces(textposition='outside')
        c2.subheader("Most Vulnerable Nations")
        c2.plotly_chart(fig2)


    elif(scale=="Country"):
        effect = pd.read_csv('Country/{}.csv'.format(country),index_col='index')
        print(effect.head())
        disdata = temp.copy()
        print(disdata)
        # con.write("Historical Impact Analysis of Shocks")
        
        try:
            # disdata = disinfo[disinfo.index==country].transpose().reset_index()
            fig3 = px.bar(disdata.sort_values(by="intensity",ascending=False), x ="Disaster Type" , y = 'intensity',orientation='v',text = 'intensity')
            fig3.update_layout(yaxis_range=[0,max(disdata['intensity'])+3],yaxis_title='Standardized Impact Score',xaxis_title=None, font = dict(
                size =18,
        )
        )
            fig3.update_xaxes(tickfont=dict(size =15, family = "Arial Black"))
            fig3.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))
            fig3.update_traces(textposition='outside')
            conPlots.subheader("Impacts of Food Shocks")
            conPlots.plotly_chart(fig3)
         

        except:
            conPlots.write("No food shocks reported in {}".format(country))


    
        print("trying")
        print(disdata.loc[disdata["Disaster Type"]==shock,"intensity"])
        # if (disdata.loc[disdata["Disaster Type"]==shock,"intensity"]==0):
        if (disdata[disdata["Disaster Type"]==shock]["intensity"].sum()==0):
            conPlots.markdown("Note: No {} reported in {}, Indicators unlikely to change so far!!!".format(shock,country))
        df_effect1 = effect[shock]
        print(df_effect1.head())



        df1 = dataColl[yearChoice]

        df = df1[df1.index==country].transpose()
        # print(df.transpose().index)
        print(df.head())
        
        data = pd.merge(df_effect1,df, left_on = df_effect1.index, right_on=df.index, how = "left")
        

        data = data[~data["key_0"].isin(capitals)].replace(all_factors1)
        
        data['new'] = np.round(data[country] - data[country]*intensity/10*data[shock],1)
        data['delta'] = np.round((data['new'] - data[country])/data[country]*100,1 )
        print(data.head())


        try:
            print("trying")
            df_effect1 = effect[shock]
            print(df_effect1.head())


            df1 = dataColl[yearChoice]

            df = df1[df1.index==country].transpose()
            # print(df.transpose().index)
            print(df.head())
            
            data = pd.merge(df_effect1,df, left_on = df_effect1.index, right_on=df.index, how = "left")
            

            data = data[~data["key_0"].isin(capitals)].replace(all_factors1)
            
            data['new'] = np.round(data[country] - data[country]*intensity/10*data[shock],1)
            data['delta'] = np.round((data['new'] - data[country])/data[country]*100,1 )

            data.loc[data["new"]<0,"new"]=0
            data.loc[data["new"]>100,"new"]=100
        
            
            print(data.head())
            
            plot_d = data.copy()
            best_10 = plot_d[plot_d[country]>0].sort_values('new', ascending = False).head(10)
            # fig1 = px.bar(best_10, x =country , y = best_10.index,orientation='h')
            fig1 = px.bar(best_10, x ='new' , y = "key_0",orientation='h',text = "delta")
            fig1.update_layout(xaxis_range=[0,120],yaxis_title=None)
            fig1.update_xaxes(tickfont=dict(size =15, family = "Arial Black"))
            fig1.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))
            fig1.update_traces(textposition='outside')
            c1.subheader("Most Resilient Indicators")
            # c1.write(country)
            c1.plotly_chart(fig1)

            worst_10 = plot_d[plot_d[country]>0].sort_values(country, ascending = True).head(10)
            # fig2 = px.bar(worst_10, x = country, y = worst_10.index,orientation='h')
            fig2 = px.bar(worst_10, x = country, y = "key_0",orientation='h',text = "delta")
            fig2.update_layout(xaxis_range=[0,120],yaxis_title=None)
            fig2.update_xaxes(tickfont=dict(size =15, family = "Arial Black"))
            fig2.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))
            fig2.update_traces(textposition='outside')
            c2.subheader("Most Vulnerable Indicators")
            # c2.write(country)
            c2.plotly_chart(fig2)
        


        except:
            c1.write("No {} reported in {}".format(shock,country))
            df1 = dataColl[yearChoice]
            df = df1[df1.index==country].transpose().reset_index()
            df = df[~df["Country"].isin(capitals)]
            df = df.replace(all_factors1)
            print(df.head())

            plot_d = df.copy()
            best_10 = plot_d[plot_d[country]>0].sort_values(country, ascending = False).head(10)
            # fig1 = px.bar(best_10, x =country , y = best_10.index,orientation='h')
            fig1 = px.bar(best_10, x =country , y = "Country",orientation='h')
            fig1.update_layout(xaxis_range=[0,120],yaxis_title=None)
            fig1.update_xaxes(tickfont=dict(size =15, family = "Arial Black"))
            fig1.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))
            fig1.update_traces(textposition='outside')
            c1.subheader("Most Resilient Indicators")
            # c1.write(country)
            c1.plotly_chart(fig1)

            worst_10 = plot_d[plot_d[country]>0].sort_values(country, ascending = True).head(10)
            # fig2 = px.bar(worst_10, x = country, y = worst_10.index,orientation='h')
            fig2 = px.bar(worst_10, x = country, y = "Country",orientation='h')
            fig2.update_layout(xaxis_range=[0,120],yaxis_title=None)
            fig2.update_xaxes(tickfont=dict(size =15, family = "Arial Black"))
            fig2.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))
            fig2.update_traces(textposition='outside')
            c2.subheader("Most Vulnerable Indicators")
            # c2.write(country)
            c2.plotly_chart(fig2)
        

        
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


# displayPDF("About.pdf",st)



st.sidebar.image("icon.png",width =150)

# if (st.sidebar.button("About")):
#     st.empty()
#     displayPDF("About.pdf",st)
st.sidebar.title('Control Center')
# st.sidebar.markdown('Control Parameters Here')
# st.sidebar.checkbox("Select a Country", True, key=1)

analysisType = st.sidebar.radio(
     "Visualization By:",
     ("About/Help",'World Map','Descriptive Analysis', 'Comparative Analysis','Scenario Analysis',"Best Interventions"),index =1)
# print(analysisType)

countries = org_data.index

conPlots = st.container()


c1,c2 = st.columns(2)
# col1, col2 = conPlots.columns((0.85,1))

# conSliders = st.container()

# global c1,c2

# c1,c2 = conSliders.columns(2)
# c1,c2 = conPlots.columns(2)

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
world = world[(world.pop_est>0) & (world.name!="Antarctica")].drop(columns =["pop_est","continent","iso_a3","gdp_md_est"])
world['name'] = world['name'].str.lower() 

if(analysisType=="World Map"):
    df = alldata.copy()
    # visualizeMap(c1,c2,conPlots)    
    indicator1 = st.sidebar.selectbox('Indicator',all_factors.keys())
    indicator = all_factors[indicator1]
    df = df[["Year","Country",indicator]]

    df["Country"]=df["Country"].str.lower()
    df["Year"] = df["Year"].astype("int")
    # world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
    # world = world[(world.pop_est>0) & (world.name!="Antarctica")] 
    # world['name'] = world['name'].str.lower()  
    # merged = pd.merge(left = world, right = df, right_on = "Country", left_on = 'name', how = 'left').drop(columns =["pop_est","continent","iso_a3","gdp_md_est"])
    merged = pd.merge(left = world, right = df, right_on = "Country", left_on = 'name', how = 'left')

    gdf = geopandas.GeoDataFrame(merged, geometry="geometry").dropna()
    gdf.index = gdf.name
    gdf["Year"]=gdf["Year"].astype("int")
    conPlots.subheader(str.upper(indicator1))
    visualizeMap1(gdf,conPlots)



elif(analysisType=="Descriptive Analysis"):
    # c1.markdown('__STRENGTHS__')
    # c2.markdown('__WEAKNESSES__')
    yearChoice =  st.sidebar.selectbox('Select Year(s)',sorted(list(years),reverse=True))
    print(type(yearChoice))
    op =showOption()
    # if len(yearChoice)==0:
    #     # conPlots.write("If the year is empty, the default year is 2020")
    #     visualizeOp(op,c1,c2)
    # else:
    #     visualizeOp(op,c1,c2,yearChoice)
    visualizeOp(op,conPlots,yearChoice)


elif(analysisType=="Comparative Analysis"):
    
    choiceDiff =  st.sidebar.selectbox('Select a type',["1-year Analysis","5-Year Analysis", "YTD Analysis", "Country vs Country", "Capitals"])
    if choiceDiff in ["1-year Analysis","5-Year Analysis", "YTD Analysis",]:
        op =showOption()
    elif choiceDiff== "Country vs Country":
        op = "Countryvs"
    else:
        op = choiceDiff
    visualizeComp(op,conPlots,choiceDiff)


elif((analysisType=="Scenario Analysis")):
    # effect = pd.read_csv('effect1.csv', index_col = "Variables")
    # effect = {}
    df = pd.read_csv("alldisaster.csv")
    years_df = df['Year'].unique()
    low = min(years_df)
    high = max(years_df)
    print(low,high)
    scale = st.sidebar.selectbox('Select a scale',["Global","Country"])
    country=None
    
    shock = st.sidebar.selectbox('Select a shock',damages.keys())
    intensity_score = st.sidebar.slider('Enter the shock intensity', min_value=0,max_value=10,value=0)
    ranger = st.sidebar.slider('Choose the range!', min_value=int(low),max_value=int(high),value=(2000,2022))
    print(intensity_score,ranger)
    df = df[(df["Year"]>=ranger[0]) & (df["Year"]<=ranger[1])]
    print(df.head())

    if (scale=="Global"):

        df = df[df["Disaster Type"]==shock]

    else:
        country = conPlots.selectbox('Select a country',countries)
        df = df[df["Country"]==country]
        # conPlots.write(country)
    print(df.head())
    fd = df.groupby(["Country","Disaster Type"])[["Total Deaths_new","Total Affected_new", "AdjustedDamages_new"]].sum()
    fd = fd.assign(intensity=lambda x: x[['Total Deaths_new','Total Affected_new','AdjustedDamages_new']].mean(axis=1)).reset_index()
    fd = fd[["Country","Disaster Type","intensity"]]
   
    doSA1(fd,scale,shock,intensity_score,1,conPlots,c1,c2,country=country)
    # st.markdown("# _Page will be up and running soon.... Hang on!!!_")

elif(analysisType=="Best Interventions"):
    # st.markdown("# _Page will be up and running soon.... Hang on!!!_")
    mn(spreadsheets)
    # temp_df = pd.read_csv('survey_data.csv')
    temp_df = pd.read_csv(spreadsheets[0]+'.csv')
    # print(temp_df)
    user = st.sidebar.selectbox('Select User Type',["Expert","User"])
    shock = st.sidebar.selectbox('Select a shock',damages.keys())
    intensity = st.sidebar.slider('Intensity of Shock', min_value = 0, max_value = 10,value = 0)
    
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
            temp_df = pd.read_csv(spreadsheets[0]+'.csv')
            # temp_df = pd.read_csv('survey_data.csv')
            displayGuage(temp_df,conPlots)


            done=False





    else:
        conPlots.subheader("Top 3 Interventions")
        displayGuage(temp_df,conPlots)

else:
    displayPDF("About.pdf",st)
    
my_html1 = """<h2>Please share your experience of using this tool 
    <a href="https://forms.gle/JpgirdYtypVdiLC27" target="_blank">HERE</a> </h2>
    """

expander = st.expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")
components.html(my_html1)
a,b,c = st.columns(3)

a.image('CSIRO.png',width=150)
b.image('ANU.png',width=150)
c.image('DFAT.png',width=150)
# st
# .write("__Please share your experience here__")
