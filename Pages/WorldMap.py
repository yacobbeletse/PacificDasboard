import streamlit as st
import geopandas
import pandas as pd
import plotly.express as px
import numpy as np

capitals = ['Food Systems Resilience Score','Natural','Human','Social','Financial','Manufactured']

natural = ['Agricultural Water Quality','Agricultural Water Quantity','Biodiversity and Habitat','Ecosystem Services','Forest Change','Green House Emission Per Capita','Land Degradation','Natural Hazard Exposure','Soil Organic Content']
human = ['Access to Agricultural Resources','Food Dietary Diversity','Food Loss','Food Safety','Food Supply Sufficiency','Labor Force Participation Rate','Literacy Rate','Micronutrient Availability','Population Growth Rate','Poverty Population','Protein Quality']
social = ['Agricultural Women Empowerment','Armed Conflict','Community Organizations','Corruption','Dependency on Chronic Food Aid','Food Safety Net Programs','Food Security Policy Commitment','Gender Equality','Nutritional Standards','Political Stability Risk']
financial = ['Access to Diversified Financial Services','Access to Financial Services','Agricultural GDP','Agricultural Production Volatility','Agricultural Trade','Food Price Volatility','Income Inequality','Per Capita GDP']
manufactured = ['Agricultural R&D','Crop Storage Facilities','Disaster Risk Management','Early Warning Measures','Irrigation Infrastructure','KOFGI Globalization Index','Supply Chain Infrastructure','Sustainable Agriculture','Telecommunications']

natural1 = ["Natural Capital",'Agricultural Water Quality','Agricultural Water Quantity','Biodiversity and Habitat','Ecosystem Services','Forest Change','Green House Emission Per Capita','Land Degradation','Natural Hazard Exposure','Soil Organic Content']
human1 = ["Human Capital",'Access to Agricultural Resources','Food Dietary Diversity','Food Loss','Food Safety','Food Supply Sufficiency','Labor Force Participation Rate','Literacy Rate','Micronutrient Availability','Population Growth Rate','Poverty Population','Protein Quality']
social1 = ["Social Capital",'Agricultural Women Empowerment','Armed Conflict','Community Organizations','Corruption','Dependency on Chronic Food Aid','Food Safety Net Programs','Food Security Policy Commitment','Gender Equality','Nutritional Standards','Political Stability Risk']
financial1 = ["Financial Capital",'Access to Diversified Financial Services','Access to Financial Services','Agricultural GDP','Agricultural Production Volatility','Agricultural Trade','Food Price Volatility','Income Inequality','Per Capita GDP']
manufactured1 = ["Manufactured Capital",'Agricultural R&D','Crop Storage Facilities','Disaster Risk Management','Early Warning Measures','Irrigation Infrastructure','KOFGI Globalization Index','Supply Chain Infrastructure','Sustainable Agriculture','Telecommunications']

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
world = world[(world.pop_est>0) & (world.name!="Antarctica")].drop(columns =["pop_est","continent","iso_a3","gdp_md_est"])
world['name'] = world['name'].str.lower() 
print("Number of Countries = "+str(len(world['name'].unique())))

alldata1 = pd.read_csv("FinalData.csv")
# alldata1["Natural Capital"] = alldata1[[natural]].mean()
# alldata1["Human Capital"] = np.round(alldata1[[natural]].mean(),2)
# alldata1["Social Capital"] = np.round(alldata1[[natural]].mean(),2)
# alldata1["Financial Capital"] = np.round(alldata1[[natural]].mean(),2)
# alldata1["Manufactured Capital"] = np.round(alldata1[[natural]].mean(),2)
alldata1 = alldata1.replace({'United States':'United States of America'})

alldata_pivot = alldata1.pivot(["Country","Indicator"],columns="Year",values="value").reset_index()
print("Printing Pivot PD")
print(alldata_pivot.head())


# @st.cache(suppress_st_warning=True)
def visualizeMap1(gdf):


    #  fig = px.choropleth(gdf, geojson=gdf.geometry, locations=gdf.index, color="Value", width = 1000,color_continuous_scale="RdYlGn",range_color=(0, 100),
    #  hover_name=gdf.index,animation_frame="Year")
     fig = px.choropleth(gdf, geojson=gdf.geometry, locations=gdf.index, color="value", width = 1000,color_continuous_scale="RdYlGn",range_color=(0, 100),
     hover_name=gdf.index)
     fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
     fig.update_geos(fitbounds="locations", visible=False, landcolor = 'lightgray',showland = True,showcountries=True, countrycolor="gray")
     fig.update_traces(marker_line_width=2)
    #  cb_ax = fig.axes[1] 
    #  cb_ax.tick_params(labelsize=5)


    #  fig.colorbar.lim(0,100)
     st.plotly_chart(fig)
# @st.cache(suppress_st_warning=True)
years =[*range(2012,2023)]
years.sort(reverse=True)
print(years)


def app():
    # print(alldata1)
    Year = st.sidebar.selectbox("Year",years)
    capital = st.sidebar.selectbox('FSRS/Capital',capitals)
    indicator1=None
    if capital=="Natural":
      indicator1 = st.sidebar.selectbox("Indicator",natural1)
    elif capital=="Human":
      indicator1 = st.sidebar.selectbox("Indicator",human1)
    elif capital=="Social":
      indicator1 = st.sidebar.selectbox("Indicator",social1)
    elif capital=="Financial":
      indicator1 = st.sidebar.selectbox("Indicator",financial1)
    elif capital=="Manufactured":
      indicator1 = st.sidebar.selectbox("Indicator",manufactured1)
    else:
      indicator1 = "Food System Resilience Score"



    # print(indicator1)
   
    df = pd.DataFrame()
    # indicator = all_factors[indicator1]
    if(indicator1=="Food System Resilience Score"):
      df = alldata_pivot[["Country","Indicator",Year]].groupby("Country")[Year].mean().reset_index()
      df["Indicator"] = indicator1
      df =df.rename(columns={Year:"value"})
    elif(indicator1=="Natural Capital"):
      df = alldata_pivot.loc[alldata_pivot["Indicator"].isin(natural),["Country","Indicator",Year]].groupby("Country")[Year].mean().reset_index()
      df =df.rename(columns={Year:"value"})
    elif(indicator1=="Human Capital"):
      df = alldata_pivot.loc[alldata_pivot["Indicator"].isin(human),["Country","Indicator",Year]].groupby("Country")[Year].mean().reset_index()
      df =df.rename(columns={Year:"value"})
    elif(indicator1=="Social Capital"):
      df = alldata_pivot.loc[alldata_pivot["Indicator"].isin(social),["Country","Indicator",Year]].groupby("Country")[Year].mean().reset_index()
      df =df.rename(columns={Year:"value"})
    elif(indicator1=="Financial Capital"):
      df = alldata_pivot.loc[alldata_pivot["Indicator"].isin(financial),["Country","Indicator",Year]].groupby("Country")[Year].mean().reset_index()
      df =df.rename(columns={Year:"value"})
    elif(indicator1=="Manufactured Capital"):
      df = alldata_pivot.loc[alldata_pivot["Indicator"].isin(manufactured),["Country","Indicator",Year]].groupby("Country")[Year].mean().reset_index()
      df =df.rename(columns={Year:"value"})
    else:
      df = alldata1[(alldata1["Year"]==Year) & (alldata1["Indicator"]==indicator1)]
      # print(df)
      # df = df[(df["Year"]==Year) & (df["Indicator"]==indicator1)]
      # print(df)
    # if indicator1 in capitals:
    #   if indicator1==
    print(df)
    df["Country"]=df["Country"].str.lower()
    # df["Year"] = df["Year"].astype("int")
    # print("alldata country = "+ str(len(df["Country"].unique())))
    # print(df["Country"].unique())
    merged = pd.merge(left = world, right = df, right_on = "Country", left_on = 'name', how = 'right')

    gdf = geopandas.GeoDataFrame(merged, geometry="geometry")

    print(gdf)
    gdf.index = gdf.name
    # gdf["Year"]=gdf["Year"].astype("int")
    st.subheader(str.upper(indicator1))
    visualizeMap1(gdf)
    
