from audioop import reverse
from email.policy import default
from glob import glob
from re import T
from matplotlib.colors import hexColorPattern
from numpy.core.fromnumeric import prod
from pandas.core.indexes import base
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from streamlit import caching
from validators import length

import copy
from statsmodels.tsa.arima_process import ArmaProcess 
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller 
from statsmodels.tsa.arima_model import ARMA
import statsmodels.api as sm
from pathlib import Path
import seaborn as sns
import geopandas
from mpl_toolkits.axes_grid1 import make_axes_locatable

import plotly.express as px


# import SessionState 
# session = SessionState.get(run_id=0)

all_factors = {
    'X': 'Score',

    '1':'natural',
    '1_1': 'BDH.new',
    '1_2': 'ECS',
    '1_3': 'Sealevel',
    '1_4': 'Forest',
    '1_5': 'Land',
    '1_6': 'energy',
    '1_7': 'Water',
    '1_8': 'GHP.new',
    '1_9': 'WaterQuant',
    '1_10': 'WaterQual',

    '2': 'human',
    '2_1':'Demographics',
    '2_2': 'literacy',
    '2_3':'HDI',
    '2_4': 'labrate',
    '2_5': 'agprod',
    '2_6': 'agVol',
    '2_7': 'obesity',
    '2_8': 'foodsafe',
    '2_9': 'drinking',
    '2_11': 'Micro',
    '2_12': 'Protein',
    '2_13': 'Diversity',


    '3': 'social',
    '3_1': 'urbancap',
    '3_2': 'safetynet',
    '3_3': 'policyfood',
    '3_4': 'nutritional',
    '3_5': 'gender',
    '3_6': 'political',
    '3_7': 'corruption',
    '3_8': 'conflict',

    '4': 'financial',
    '4_1': 'perCapita',
    '4_2': 'edu',
    '4_3': 'tariff',
    '4_4': 'agGDP',
    '4_5': 'finance',
    '4_6': 'priceVol',
    '4_7': 'foodloss',

    '5': 'manufactured',
    '5_1': 'kofgi',
    '5_2': 'agadaptpolicy',
    '5_3': 'climatesma',
    '5_4': 'disman',
    '5_5': 'Nindex',
    '5_6': 'RND',
    '5_7': 'mobile',
    '5_8': 'transport',
    '5_9': 'storage'
}


# natural = [ 'BDH.new',
#      'ECS',
#     'Sealevel',
#     'Forest',
#     'Land',
#     'energy',
#     'Water',
#     'GHP.new',
#     'WaterQuant',
#     'WaterQual']
natural = ['BDH.new', 'ECS', 'Sealevel', 'Forest', 'Land', 'energy', 'Water', 'GHP.new', 'WaterQuant', 'WaterQual']
human = ['Demographics', 'literacy', 'HDI', 'labrate', 'agprod', 'agVol', 'obesity', 'foodsafe', 'drinking', 'Micro', 'Protein', 'Diversity']
social = ['urbancap', 'safetynet', 'policyfood', 'nutritional', 'gender', 'political', 'corruption', 'conflict']
financial = ['perCapita', 'edu', 'tariff', 'agGDP', 'finance', 'priceVol', 'foodloss']
manufactured = ['kofgi', 'agadaptpolicy', 'climatesma', 'disman', 'Nindex', 'RND', 'mobile', 'transport', 'storage']

plt_style = 'bmh'
# plt_style = 'fivethirtyeight'

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


years = range(2012,2021)
dataColl = {}
for i in years:
    abc = pd.read_csv(DATA_URL + "\\"+str(i)+'.csv',index_col= 'Country').transpose()
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

def showPlot(df,c1,c2,visType="Des"):
    # df=df.transpose()
    # c1.write(df)
    df.index.name=None
    plt.style.use(plt_style)
    for i in df.columns:
        c1.write(str.upper(i))
        fig,axs = plt.subplots(figsize=(6,4))
            
        
        # c1.write(df[i].sort_values(ascending= False).head(10))
        df[i].sort_values(ascending= False).head(10).plot.barh()
        plt.xlim([0,100])
        # plt.show()
        c1.pyplot(fig)

        c2.write(str.upper(i))
        # c2.write(df[i].sort_values(ascending= True).head(10))
        fig1,axs1 = plt.subplots(figsize=(6,4))
        # plt.style.use(plt_style)
        # c1.write(df[i].sort_values(ascending= False).head(10))
        df[i].sort_values(ascending= True).head(10).plot.barh()
        if(visType=="Des"):
            plt.xlim([0,100])
        else:
            plt.xlim([-50,5])
        # plt.show()
        c2.pyplot(fig1)

def linePlot(df,countrySelect,c1,c2):
    df.index.name=None
    # c1.write(df)
    # print(df)
    if(len(countrySelect)!=0):
        df =df[df.index.isin(countrySelect)]
        # c1.write(df)
        plt.style.use(plt_style)
        for i in range(int(len(df.columns)/2)):
            c1.write(str.upper(df.columns[2*i]))
            fig,axs = plt.subplots(figsize=(6,4))
                
            
            # c1.write(df[i].sort_values(ascending= False).head(10))
            # df[i].sort_values(ascending= False).head(10).plot.barh()
            df.reset_index().set_index("Year").groupby("index")[df.columns[2*i]].plot(legend = True,style='.-')
            plt.ylim([0,100])
            plt.legend(loc='lower left')
            # plt.show()
            c1.pyplot(fig)

            c2.write(str.upper(df.columns[2*i+1]))
            # c2.write(df[i].sort_values(ascending= True).head(10))
            fig1,axs1 = plt.subplots(figsize=(6,4))
            plt.style.use(plt_style)
            # c1.write(df[i].sort_values(ascending= False).head(10))
            df.reset_index().set_index("Year").groupby("index")[df.columns[2*i+1]].plot(legend = True,style='.-')
            plt.ylim([0,100])
            plt.legend(loc='lower left')
            # plt.show()
            c2.pyplot(fig1)

def linePlot1(df,countrySelect,conPlots):
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
            plt.ylim([-5,105])
            plt.legend(loc='center left',bbox_to_anchor=(1.1, 0.5),prop={'size': 5})
            plt.show()
            conPlots.pyplot(fig2)
            




def visualizeMap(c1,c2,conPlots):
     global dataColl  
     yearChoice =  st.sidebar.selectbox('Year',sorted(list(years),reverse=True))
     indicator = st.sidebar.selectbox('Indicator',all_factors.values())
     df = dataColl[yearChoice][indicator]
     df.index = df.index.str.lower()
     
     world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
     world = world[(world.pop_est>0) & (world.name!="Antarctica")] 
     world['name'] = world['name'].str.lower()  
     merged = pd.merge(left = world, right = df, right_on = df.index, left_on = 'name', how = 'left').drop(["pop_est","continent","iso_a3","gdp_md_est"],1)
     print(merged)
     conPlots.write(str.upper(indicator))
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

        showPlot(df,c1,c2)
     
    else:
        indSelect = st.sidebar.multiselect('Select indicator(s)',all_factors.values())
        # trans_data=pd.read_csv(DATA_URL + "\\"+str(yearChoice)+'.csv',index_col= 'Country').transpose()
        print("choice of year = " + str(yearChoice))
        trans_data=dataColl[yearChoice]
        df1 = trans_data[indSelect]
        print(df1)
        showPlot(df1,c1,c2)
  

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
        showPlot(df,c1,c2,"Comp")
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
        linePlot1(df1,countrySelect,conPlots)

    else:
        indSelect = st.sidebar.multiselect('Select indicator(s)',all_factors.values())
        df1 = dataColl[yearChoice[0]].subtract(dataColl[yearChoice[1]])[indSelect]
        showPlot(df1,c1,c2,"Comp")





###### SIDEBAR *****************




# countries = org_data.drop('Indicator',1).columns
countries = org_data.index
st.sidebar.title('Control Center')
# st.sidebar.markdown('Control Parameters Here')
# st.sidebar.checkbox("Select a Country", True, key=1)

analysisType = st.sidebar.radio(
     "Visualization By:",
     ('World Map','Descriptive Analysis', 'Comparative Analysis','Scenario Analysis'))
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


else:
    shock = st.sidebar.selectbox('Select a hazard',["Flood","Drought", "Storm", "Pandemic", "Civil War", "Economic Crisis","Earthquake"])
    intensity = st.sidebar.slider('Intensity of Shock', min_value = 0, max_value = 10,value = 0)
    conPlots.write("Page will be up and running soon.... Hang on!!!")










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
