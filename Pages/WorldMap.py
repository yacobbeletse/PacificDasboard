from turtle import color
import streamlit as st
import geopandas
import pandas as pd
import plotly.express as px
import numpy as np

# countryRename = {
#  'Dem. Rep. Congo': 'DR Congo',
#  'Dominican Rep.': 'Dominican Republic',
#  "Côte d'Ivoire": 'Ivory Coast',
#  'Central African Rep.': 'Central African Republic',
#   'Congo':'Congo Republic',
#  'Solomon Is.': 'Solomon Island',
#  'Czechia':'Czech Republic',
#  'Bosnia and Herz.': 'Bosnia and Herzegovina',
# }

qualities = ["Robustness", "Redundancy", "Resourcefulness","Rapidity"]

capitals = ['Food Systems Resilience Score','Natural Capital','Human Capital','Social Capital','Financial Capital','Manufactured Capital']
capitals1 = ['Natural Capital','Human Capital','Social Capital','Financial Capital','Manufactured Capital']

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
# world = world.replace(countryRename)
# print(world["name"].unique())
world['name'] = world['name'].str.upper() 
# print("Number of Countries = "+str(len(world['name'].unique())))

alldata1 = pd.read_csv("allIndicatorData11.csv")


alldata1 = alldata1.replace({'United States':'United States of America'})

alldata_pivot = alldata1.pivot(["Country","Indicator"],columns="Year",values="value").reset_index()
# capitalsOnly = pd.read_csv("finalCapital.csv")
# print("Printing Pivot PD")
# print(alldata_pivot.head())



# @st.cache(suppress_st_warning=True)
def visualizeMap1(gdf):


    #  fig = px.choropleth(gdf, geojson=gdf.geometry, locations=gdf.index, color="Value", width = 1000,color_continuous_scale="RdYlGn",range_color=(0, 100),
    #  hover_name=gdf.index,animation_frame="Year")
     fig = px.choropleth(gdf, geojson=gdf.geometry, locations=gdf.index, color="value",color_continuous_scale="RdYlGn",width = 1600,height = 400,range_color=(0, 100),
     hover_data = ['value'],labels={"index": "Country",
                                      "value": gdf["Indicator"].unique()[0]})
     fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
     fig.update_geos(fitbounds="locations", visible=False, landcolor = 'lightgray',showland = True,showcountries=True, countrycolor="gray")
     fig.update_traces(marker_line_width=2)

    #  st.plotly_chart(fig, use_container_width=True)
     st.plotly_chart(fig, use_container_width=False)
# @st.cache(suppress_st_warning=True)
years =[*range(2012,2023)]
years.sort(reverse=True)
# print(years)

def app():
    Year = st.sidebar.selectbox("Year",years)
    option = st.sidebar.selectbox("Visualization by: ", ["FSRS/Capital", "Quality"])
    indicator1=None
    if option=="Quality":
      indicator1 = st.sidebar.selectbox('Quality',qualities)
    
    else:
      capital = st.sidebar.selectbox('FSRS/Capital',capitals)
      
      if capital=="Natural Capital":
        indicator1 = st.sidebar.selectbox("Indicator",natural1)
      elif capital=="Human Capital":
        indicator1 = st.sidebar.selectbox("Indicator",human1)
      elif capital=="Social Capital":
        indicator1 = st.sidebar.selectbox("Indicator",social1)
      elif capital=="Financial Capital":
        indicator1 = st.sidebar.selectbox("Indicator",financial1)
      elif capital=="Manufactured Capital":
        indicator1 = st.sidebar.selectbox("Indicator",manufactured1)
      else:
        indicator1 = "Food Systems Resilience Score"



    # df = pd.DataFrame()
    print("indicator = "+indicator1)
    # print(alldata1["Indicator"].unique())
    # print(len(alldata1["Indicator"].unique()))
    # if(indicator1 in capitals):
    #   df = capitalsOnly[(capitalsOnly["Capital"]==indicator1) & (capitalsOnly['Year']==Year)]
    #   print(df.head())

    # else:
    #   dff = alldata_pivot[["Country","Indicator",Year]].groupby(["Country", "Indicator"])[Year].mean().round(1).reset_index()
    #   df = dff[dff["Indicator"]==indicator1]
    #   print(df.head())
    # print(alldata_pivot.head())
    # print(alldata1)
    # dff = alldata_pivot[["Country","Indicator",Year]].groupby(["Country", "Indicator"])[Year].mean().round(1).reset_index()
    df = alldata1.loc[(alldata1["Year"]==Year) & (alldata1["Indicator"]==indicator1),["Country","Indicator","value"]]
    # df = dff[dff["Indicator"]==indicator1]
    # df["Indicator"] = indicator1
    # df =df.rename(columns={Year:"value"})

    
    df["Country"]=df["Country"].str.upper()
    # print(df)
    # print(df["value"].mean(skipna = True).round(1))

    merged = pd.merge(left = world, right = df, right_on = "Country", left_on = 'name', how = 'right')

    gdf = geopandas.GeoDataFrame(merged, geometry="geometry")

    # # print(gdf)
    gdf.index = gdf.name

    st.subheader(str.upper(indicator1))
    if not gdf["value"].dropna().empty:
      st.write('Global Average: ' + str(df["value"].mean(skipna = True).round(1)))
      st.write('Countries Covered: ' + str(len(df.dropna()["Country"].unique())))
      with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
      # c = st.columns(4)
      # colors = ['red','orange','yellow','green']
      # legend = ['Weak [0-40]' , 'Moderate [40-60]', 'Good [60-80]', 'Very Good [80 -100]' ]
      # for i in range(4):
      #   style_text = "<div span class = 'rectangle {}'></span></div> {}".format(colors[i],legend[i])
      #   print(style_text)
      #   c[i].markdown(style_text,unsafe_allow_html=True)
      # style_text=""
      # for i in range(4):
      #   colors = ['red','orange','yellow','green']
      #   legend = ['Weak [0-40]' , 'Moderate [40-60]', 'Good [60-80]', 'Very Good [80 -100]' ]
      #   style_text+= "<div><div class='rectangle {}'></div> {}</div>".format(colors[i],legend[i])
      # print(style_text)
      # st.markdown(style_text,unsafe_allow_html=True)

      visualizeMap1(gdf)
    else:
      st.write("No Data Available for " + indicator1 + " for "+ str(Year))
    
