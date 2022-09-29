import streamlit as st
import geopandas
import pandas as pd
import plotly.express as px

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

natural1 = [all_factors1[i] for i in ['natural','BDH.new', 'ECS', 'Sealevel', 'Forest', 'Land', 'energy', 'Water', 'GHP.new', 'WaterQuant', 'WaterQual']]
human1 = [all_factors1[i] for i in ['human','Demographics', 'literacy', 'HDI', 'labrate', 'agprod', 'agVol', 'obesity', 'foodsafe', 'drinking', 'Micro', 'Protein', 'Diversity']]
social1 = [all_factors1[i] for i in ['social','urbancap', 'safetynet', 'policyfood', 'nutritional', 'gender', 'political', 'corruption', 'conflict']]
financial1 = [all_factors1[i] for i in ['financial','perCapita', 'edu', 'tariff', 'agGDP', 'finance', 'priceVol', 'foodloss']]
manufactured1 = [all_factors1[i] for i in ['manufactured','kofgi', 'agadaptpolicy', 'climatesma', 'disman', 'Nindex', 'RND', 'mobile', 'transport', 'storage']]

capitals = ['FSRS','Natural','Human','Social','Financial','Manufactured']

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
world = world[(world.pop_est>0) & (world.name!="Antarctica")].drop(columns =["pop_est","continent","iso_a3","gdp_md_est"])
world['name'] = world['name'].str.lower() 
print("Number of Countries = "+str(len(world['name'].unique())))

alldata1 = pd.read_csv("restructure.csv")
alldata1 = alldata1.replace({'United States':'United States of America'})


# print(df.head())
# # visualizeMap(c1,c2,conPlots)    
# indicator1 = st.sidebar.selectbox('Indicator',all_factors.keys())
# indicator = all_factors[indicator1]
# df = df[["Year","Country",'Indicator',"Value"]][df["Indicator"]==indicator1]
# print(df.head())

# df["Country"]=df["Country"].str.lower()
# df["Year"] = df["Year"].astype("int")
# # world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
# # world = world[(world.pop_est>0) & (world.name!="Antarctica")] 
# # world['name'] = world['name'].str.lower()  
# # merged = pd.merge(left = world, right = df, right_on = "Country", left_on = 'name', how = 'left').drop(columns =["pop_est","continent","iso_a3","gdp_md_est"])
# merged = pd.merge(left = world, right = df, right_on = "Country", left_on = 'name', how = 'left')

# gdf = geopandas.GeoDataFrame(merged, geometry="geometry").dropna()

# print(gdf.head())
# gdf.index = gdf.name
# gdf["Year"]=gdf["Year"].astype("int")
# conPlots.subheader(str.upper(indicator1))
# visualizeMap1(gdf,conPlots)

# @st.cache(suppress_st_warning=True)
def visualizeMap1(gdf):


    #  fig = px.choropleth(gdf, geojson=gdf.geometry, locations=gdf.index, color="Value", width = 1000,color_continuous_scale="RdYlGn",range_color=(0, 100),
    #  hover_name=gdf.index,animation_frame="Year")
     fig = px.choropleth(gdf, geojson=gdf.geometry, locations=gdf.index, color="Value", width = 1000,color_continuous_scale="RdYlGn",range_color=(0, 100),
     hover_name=gdf.index)
     fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
     fig.update_geos(fitbounds="locations", visible=False)
     fig.update_traces(marker_line_width=2)
    #  cb_ax = fig.axes[1] 
    #  cb_ax.tick_params(labelsize=5)


    #  fig.colorbar.lim(0,100)
     st.plotly_chart(fig)
# @st.cache(suppress_st_warning=True)
years =[*range(2012,2021)]
years.sort(reverse=True)
print(years)

def app():
  st.subheader("HERE YOU WILL BE ABLE TO COMPARE THE FOOD SYSTEMS RESILIENCE SCORE AND PERFORMANCE OF INDICATORS AGAINST OTHER EXISTING INDEX SYSTEMS")
    # print(alldata1)
    # df = alldata1.copy()
    # capital = st.sidebar.selectbox('FSRS/Capital',capitals)
    # indicator1=None
    # if capital=="Natural":
    #   indicator1 = st.sidebar.selectbox("Indicator",natural1)
    # elif capital=="Human":
    #   indicator1 = st.sidebar.selectbox("Indicator",human1)
    # elif capital=="Social":
    #   indicator1 = st.sidebar.selectbox("Indicator",social1)
    # elif capital=="Financial":
    #   indicator1 = st.sidebar.selectbox("Indicator",financial1)
    # elif capital=="Manufactured":
    #   indicator1 = st.sidebar.selectbox("Indicator",manufactured1)
    # else:
    #   indicator1 = "Food System Resilience Score"



    # print(indicator1)
    # Year = st.sidebar.selectbox("Year",years)
    # # indicator = all_factors[indicator1]
    # df = df[["Year","Country",'Indicator',"Value"]][(df["Indicator"]==indicator1) & (df["Year"]==Year)]
    # df["Country"]=df["Country"].str.lower()
    # df["Year"] = df["Year"].astype("int")
    # print("alldata country = "+ str(len(df["Country"].unique())))
    # print(df["Country"].unique())
    # merged = pd.merge(left = world, right = df, right_on = "Country", left_on = 'name', how = 'right')

    # gdf = geopandas.GeoDataFrame(merged, geometry="geometry").dropna()

    # print(gdf)
    # gdf.index = gdf.name
    # # gdf["Year"]=gdf["Year"].astype("int")
    # st.subheader(str.upper(indicator1))
    # visualizeMap1(gdf)
    
