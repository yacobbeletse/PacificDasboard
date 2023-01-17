from turtle import width
import streamlit as st
import pandas as pd
import plotly.express as px
import geopandas
import numpy as np
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
import plotly.graph_objects as go



dataColl = {}
dataColl = {}
alldata1 = pd.read_csv("FinalData.csv")
alldata1["Year"] = alldata1["Year"].astype("int")
years = range(2012,2023)
for i in years:
    # abc = pd.read_csv(str(i)+'.csv',index_col= 'Country').transpose()
    # dataColl[i] = pd.read_csv(DATA_URL + "\\"+str(i)+'.csv',index_col= 'Country')
    dataColl[i] = alldata1[alldata1["Year"]==i]

org_data=dataColl[2022]
alldata_pivot = alldata1.pivot(["Country","Indicator"],columns="Year",values="value").reset_index()
countries = org_data["Country"].unique()
# print("Printing DFF")
# print(dff)

capitalsOnly = pd.read_csv("finalCapital.csv")

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


countries = ['Algeria', 'Angola', 'Argentina', 'Australia', 'Austria', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Belarus', 'Belgium', 'Benin', 'Bolivia', 'Botswana', 'Brazil', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Chad', 'Chile', 'China', 'Colombia', 'Costa Rica', 'Czech Republic', 'DR Congo', 'Denmark', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Ethiopia', 'Finland', 'France', 'Germany', 'Ghana', 'Greece', 'Guatemala', 'Guinea', 'Haiti', 'Honduras', 'Hungary', 'India', 'Indonesia', 'Ireland', 'Israel', 'Italy', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kuwait', 'Madagascar', 'Malawi', 'Malaysia', 'Mali', 'Mexico', 'Morocco', 'Mozambique', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Panama', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saudi Arabia', 'Senegal', 'Serbia', 'Sierra Leone', 'Singapore', 'South Africa', 'South Korea', 'Spain', 'Sudan', 'Sweden', 'Switzerland', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tunisia', 'Turkey', 'Uganda', 'United Arab Emirates', 'United Kingdom', 'United States of America', 'Uruguay', 'Uzbekistan']
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
world = world[(world.pop_est>0) & (world.name!="Antarctica")].drop(columns =["pop_est","continent","iso_a3","gdp_md_est"])
world['name'] = world['name'].str.lower() 

flags = {
   'Afghanistan': 'af', 'Albania': 'al', 'Algeria': 'dz', 'American Samoa': 'as', 'Andorra': 'ad', 'Angola': 'ao', 'Anguilla': 'ai', 'Antarctica': 'aq', 'Antigua and Barbuda': 'ag', 'Argentina': 'ar', 'Armenia': 'am', 'Aruba': 'aw', 'Australia': 'au', 'Austria': 'at', 'Azerbaijan': 'az', 'Bahamas': 'bs', 'Bahrain': 'bh', 'Bangladesh': 'bd', 'Barbados': 'bb', 'Belarus': 'by', 'Belgium': 'be', 'Belize': 'bz', 'Benin': 'bj', 'Bermuda': 'bm', 'Bhutan': 'bt', 'Bolivia, Plurinational State of': 'bo', 'Bolivia': 'bo', 'Bosnia and Herzegovina': 'ba', 'Botswana': 'bw', 'Bouvet Island': 'bv', 'Brazil': 'br', 'British Indian Ocean Territory': 'io', 'Brunei Darussalam': 'bn', 'Brunei': 'bn', 'Bulgaria': 'bg', 'Burkina Faso': 'bf', 'Burundi': 'bi', 'Cambodia': 'kh', 'Cameroon': 'cm', 'Canada': 'ca', 'Cape Verde': 'cv', 'Cayman Islands': 'ky', 'Central African Republic': 'cf', 'Chad': 'td', 'Chile': 'cl', 'China': 'cn', 'Christmas Island': 'cx', 'Cocos (Keeling) Islands': 'cc', 'Colombia': 'co', 'Comoros': 'km', 'Congo': 'cg', 'DR Congo':'cd','Congo, the Democratic Republic of the': 'cd', 'Cook Islands': 'ck', 'Costa Rica': 'cr', "Côte d'Ivoire": 'ci', 'Ivory Coast': 'ci', 'Croatia': 'hr', 'Cuba': 'cu', 'Cyprus': 'cy', 'Czech Republic': 'cz', 'Denmark': 'dk', 'Djibouti': 'dj', 'Dominica': 'dm', 'Dominican Republic': 'do', 'Ecuador': 'ec', 'Egypt': 'eg', 'El Salvador': 'sv', 'Equatorial Guinea': 'gq', 'Eritrea': 'er', 'Estonia': 'ee', 'Ethiopia': 'et', 'Falkland Islands (Malvinas)': 'fk', 'Faroe Islands': 'fo', 'Fiji': 'fj', 'Finland': 'fi', 'France': 'fr', 'French Guiana': 'gf', 'French Polynesia': 'pf', 'French Southern Territories': 'tf', 'Gabon': 'ga', 'Gambia': 'gm', 'Georgia': 'ge', 'Germany': 'de', 'Ghana': 'gh', 'Gibraltar': 'gi', 'Greece': 'gr', 'Greenland': 'gl', 'Grenada': 'gd', 'Guadeloupe': 'gp', 'Guam': 'gu', 'Guatemala': 'gt', 'Guernsey': 'gg', 'Guinea': 'gn', 'Guinea-Bissau': 'gw', 'Guyana': 'gy', 'Haiti': 'ht', 'Heard Island and McDonald Islands': 'hm', 'Holy See (Vatican City State)': 'va', 'Honduras': 'hn', 'Hong Kong': 'hk', 'Hungary': 'hu', 'Iceland': 'is', 'India': 'in', 'Indonesia': 'id', 'Iran, Islamic Republic of': 'ir', 'Iraq': 'iq', 'Ireland': 'ie', 'Isle of Man': 'im', 'Israel': 'il', 'Italy': 'it', 'Jamaica': 'jm', 'Japan': 'jp', 'Jersey': 'je', 'Jordan': 'jo', 'Kazakhstan': 'kz', 'Kenya': 'ke', 'Kiribati': 'ki', "Korea, Democratic People's Republic of": 'kp', 'Korea, Republic of': 'kr', 'South Korea': 'kr', 'Kuwait': 'kw', 'Kyrgyzstan': 'kg', "Lao People's Democratic Republic": 'la', 'Latvia': 'lv', 'Lebanon': 'lb', 'Lesotho': 'ls', 'Liberia': 'lr', 'Libyan Arab Jamahiriya': 'ly', 'Libya': 'ly', 'Liechtenstein': 'li', 'Lithuania': 'lt', 'Luxembourg': 'lu', 'Macao': 'mo', 'Macedonia, the former Yugoslav Republic of': 'mk', 'Madagascar': 'mg', 'Malawi': 'mw', 'Malaysia': 'my', 'Maldives': 'mv', 'Mali': 'ml', 'Malta': 'mt', 'Marshall Islands': 'mh', 'Martinique': 'mq', 'Mauritania': 'mr', 'Mauritius': 'mu', 'Mayotte': 'yt', 'Mexico': 'mx', 'Micronesia, Federated States of': 'fm', 'Moldova, Republic of': 'md', 'Monaco': 'mc', 'Mongolia': 'mn', 'Montenegro': 'me', 'Montserrat': 'ms', 'Morocco': 'ma', 'Mozambique': 'mz', 'Myanmar': 'mm', 'Burma': 'mm', 'Namibia': 'na', 'Nauru': 'nr', 'Nepal': 'np', 'Netherlands': 'nl', 'Netherlands Antilles': 'an', 'New Caledonia': 'nc', 'New Zealand': 'nz', 'Nicaragua': 'ni', 'Niger': 'ne', 'Nigeria': 'ng', 'Niue': 'nu', 'Norfolk Island': 'nf', 'Northern Mariana Islands': 'mp', 'Norway': 'no', 'Oman': 'om', 'Pakistan': 'pk', 'Palau': 'pw', 'Palestinian Territory, Occupied': 'ps', 'Panama': 'pa', 'Papua New Guinea': 'pg', 'Paraguay': 'py', 'Peru': 'pe', 'Philippines': 'ph', 'Pitcairn': 'pn', 'Poland': 'pl', 'Portugal': 'pt', 'Puerto Rico': 'pr', 'Qatar': 'qa', 'Réunion': 're', 'Romania': 'ro', 'Russian Federation': 'ru', 'Russia': 'ru', 'Rwanda': 'rw', 'Saint Helena, Ascension and Tristan da Cunha': 'sh', 'Saint Kitts and Nevis': 'kn', 'Saint Lucia': 'lc', 'Saint Pierre and Miquelon': 'pm', 'Saint Vincent and the Grenadines': 'vc', 'Saint Vincent & the Grenadines': 'vc', 'St. Vincent and the Grenadines': 'vc', 'Samoa': 'ws', 'San Marino': 'sm', 'Sao Tome and Principe': 'st', 'Saudi Arabia': 'sa', 'Senegal': 'sn', 'Serbia': 'rs', 'Seychelles': 'sc', 'Sierra Leone': 'sl', 'Singapore': 'sg', 'Slovakia': 'sk', 'Slovenia': 'si', 'Solomon Islands': 'sb', 'Somalia': 'so', 'South Africa': 'za', 'South Georgia and the South Sandwich Islands': 'gs', 'South Sudan': 'ss', 'Spain': 'es', 'Sri Lanka': 'lk', 'Sudan': 'sd', 'Suriname': 'sr', 'Svalbard and Jan Mayen': 'sj', 'Swaziland': 'sz', 'Sweden': 'se', 'Switzerland': 'ch', 'Syrian Arab Republic': 'sy', 'Taiwan, Province of China': 'tw', 'Taiwan': 'tw', 'Tajikistan': 'tj', 'Tanzania': 'tz', 'Thailand': 'th', 'Timor-Leste': 'tl', 'Togo': 'tg', 'Tokelau': 'tk', 'Tonga': 'to', 'Trinidad and Tobago': 'tt', 'Tunisia': 'tn', 'Turkey': 'tr', 'Turkmenistan': 'tm', 'Turks and Caicos Islands': 'tc', 'Tuvalu': 'tv', 'Uganda': 'ug', 'Ukraine': 'ua', 'United Arab Emirates': 'ae', 'United Kingdom': 'gb', 'United States': 'us', 'United States of America':'us','United States Minor Outlying Islands': 'um', 'Uruguay': 'uy', 'Uzbekistan': 'uz', 'Vanuatu': 'vu', 'Venezuela, Bolivarian Republic of': 've', 'Venezuela': 've', 'Viet Nam': 'vn', 'Vietnam': 'vn', 'Virgin Islands, British': 'vg', 'Virgin Islands, U.S.': 'vi', 'Wallis and Futuna': 'wf', 'Western Sahara': 'eh', 'Yemen': 'ye', 'Zambia': 'zm', 'Zimbabwe': 'zw'
   }

countryRename = {
    'Bahamas (the)': 'Bahamas',
    'Bolivia (Plurinational State of)': 'Bolivia',
    'Brunei Darussalam': 'Brunei',
    "CÃ´te dÂ’Ivoire": 'Ivory Coast',
    'Cayman Islands (the)': 'Cayman Islands',
    'Comoros (the)': 'Comoros',
    'Congo (the Democratic Republic of the)': 'DR Congo',
    'Congo (the)': 'Congo Republic',
    'Czech Republic (the)': 'Czech Republic',
    'Dominican Republic (the)': 'Dominican Republic',
    'Gambia (the)': 'Gambia',
    'Iran (Islamic Republic of)': 'Iran',
    "Korea (the Democratic People's Republic of)": 'North Korea',
    'Korea (the Republic of)': 'South Korea',
    "Lao People's Democratic Republic (the)": 'Laos',
    'Moldova (the Republic of)': 'Moldova',
    'Netherlands (the)': 'Netherlands',
    'Niger (the)': 'Niger',
    'Palestine, State of': 'Palestine',
    'Philippines (the)': 'Philippines',
    'Russian Federation (the)':'Russia',
    'Sudan (the)': 'Sudan',
    'Syrian Arab Republic': 'Syria',
    'Tanzania, United Republic of':'Tanzania',
    'United Arab Emirates (the)': 'United Arab Emirates',
    'United Kingdom of Great Britain and Northern Ireland (the)': 'United Kingdom',
    'United States':'United States of America',
    'Venezuela (Bolivarian Republic of)': 'Venezuela',
    'Viet Nam': 'Vietnam',
    'Yemen Arab Rep': 'Yemen'
}


def coloredPlot(df,c1,i):
    df = df.sort_values(by="Value",ascending=True)
    df.index =df.index.str.title()
    df["Value"] = np.round(df["Value"],2)
    fig1 = px.bar(df, x = i,y = df.index,orientation='h',text = i)
    
    # fig1.update_layout(xaxis_range=[0,100],yaxis_title=None, xaxis_title=None,width = 285)
    # fig1.update_layout(yaxis_title=None, xaxis_title=None,width = 400,height =400)
    fig1.update_layout(yaxis_title=None, xaxis_title=None,height =400)
    fig1.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
    # # fig1['layout']['xaxis'].update(autorange = True)
    fig1.update_xaxes(tickfont=dict(size =12, family = "Arial Black"))
    fig1.update_yaxes(tickfont=dict(size =12,family = "Arial Black"))
    fig1.layout.showlegend = False
    # fig1.update_traces(textposition='outside')
    # c1.subheader(capital) 
    # a1.metric(label="Food System Resilience Score",value=df.loc[df["var_name"]=="Food System Resilience Score",i])
    # if i not in all_factors1.keys():
    #     c1.metric(label=capital+" Capital",value=(np.round(df[i].mean(),1)))
    # else:
    #     c1.subheader(capital)

    c1.plotly_chart(fig1,use_container_width=True)
def visualizeMap1(gdf):


    #  fig = px.choropleth(gdf, geojson=gdf.geometry, locations=gdf.index, color="Value", width = 1000,color_continuous_scale="RdYlGn",range_color=(0, 100),
    #  hover_name=gdf.index,animation_frame="Year")
     fig = px.choropleth(gdf, geojson=gdf.geometry, locations=gdf.index, color="Value",color_continuous_scale="RdYlGn_r",
     hover_name=gdf.index)
     fig = px.choropleth(gdf, geojson=gdf.geometry, locations=gdf.index, color="Value",color_continuous_scale="RdYlGn_r",
     hover_name=gdf.index)
     fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
     fig.update_geos(fitbounds="locations", visible=False,landcolor = 'lightgray',showland = True,showcountries=True, countrycolor="gray")
     fig.update_traces(marker_line_width=2)
    #  cb_ax = fig.axes[1] 
    #  cb_ax.tick_params(labelsize=5)


    #  fig.colorbar.lim(0,100)
     col1, col2, col3= st.columns([4,1,2])
     col1.plotly_chart(fig,use_container_width=True)
     col3.subheader("Top 10 countries worst-hit by "+ gdf["Disaster Type"].unique()[0])
    #  col2.write(gdf[["name","Value"]].sort_values("Value",ascending=False).head(10))
     coloredPlot(gdf[["name","Value"]].sort_values("Value",ascending=False).head(10),col3,"Value")
# @st.cache(suppress_st_warning=True)

def linePlot(df,i,var,c1,shock=None):
  print(df)

  fig = make_subplots(specs=[[{"secondary_y": True}]])

  # Add traces
  fig.add_trace(
      go.Scatter(x=df["Year"], y=df[i], name=i),
      secondary_y=False,
  )
  for k in var:
    # if k!="Count":
    #     name1 = 

    fig.add_trace(
        go.Scatter(x=df["Year"], y=df[k], name=k.split("_")[0]),
        secondary_y=True,
    )

    fig.update_yaxes(title_text = "Score for Indicator",secondary_y = False)
    fig.update_yaxes(title_text = "Standardized Value for the Shock",secondary_y = True)
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')

    fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
))
  c1.subheader("Influence of "+shock +" on " +  i)

  # fig.add_trace(
  #     go.Scatter(x=df["Year"], y=df[col], name=col),
  #     secondary_y=True,
  # )

  fig.update_xaxes(tickfont=dict(size =15, family = "Arial Black"))
  fig.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))
  # fig.update_traces(mode = "markers")
#   fig.update_layout(width = 800)
  fig.update_layout(
    # title="Plot Title",
    # xaxis_title="X Axis Title",
    # yaxis_title="Y Axis Title",
    # legend_title="Legend Title",
    font=dict(
        family="Arial Black",
        size=9,
    ))

  
  c1.plotly_chart(fig,use_container_width=True)

capitals = ['Food Systems Resilience Score','Natural Capital','Human Capital','Social Capital','Financial Capital','Manufactured Capital']




def app():
    global dataColl
    df = pd.read_csv("alldisaster.csv")
    print(df.head())
    disasters = df["Disaster Type"].dropna().unique()
    # df = df.replace(countryRename)
    years_df = df['Year'].unique()
    low = min(years_df)
    high = max(years_df)
    # print(df['Country'].unique())
    scale = st.sidebar.selectbox('Select a scale',["Global","Country"])
    # country=None
    
    # shock = st.sidebar.selectbox('Select a shock',damages.keys())
    # # intensity_score = st.sidebar.slider('Enter the shock intensity', min_value=0,max_value=10,value=0)
    # ranger = st.sidebar.slider('Choose the range!', min_value=int(low),max_value=int(high),value=(2000,2022))
    # # print(intensity_score,ranger)
    # df = df[(df["Year"]>=ranger[0]) & (df["Year"]<=ranger[1])]
    # print(df.head())

    if (scale=="Global"):
        shock = st.sidebar.selectbox('Select a shock',disasters)
        choice = st.sidebar.selectbox("Choose a Disaster Impact",["Deaths","Total Affected","Economic Damages"])
        # intensity_score = st.sidebar.slider('Enter the shock intensity', min_value=0,max_value=10,value=0)
        ranger = st.sidebar.slider('Choose the range!', min_value=int(low),max_value=int(high),value=(2000,2022))

        capital = st.sidebar.selectbox('FSRS/Capital',capitals)
        indicator1=None
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
     
        df = df[(df["Year"]>=ranger[0]) & (df["Year"]<=ranger[1])]
   
        df = df[df["Disaster Type"]==shock]
        print(df.head())
        if df.empty:
            st.subheader("No "+shock+" reported globally in the selected range "+str(ranger[0]) +" and " + str(ranger[1]))
        else:

            fd = df.groupby(["Country","Disaster Type"])[["Total Deaths_new","Total Affected_new", "AdjustedDamages_new"]].sum().reset_index()
            # print(fd)

            fd1 = df[df["Year"].isin(years)].groupby(["Disaster Type","Year"])[["Total Deaths_new","Total Affected_new", "AdjustedDamages_new"]].sum().reset_index()

            fd11 = df[df["Year"].isin(years)].groupby(["Disaster Type","Year"])["Total Deaths_new"].count().reset_index()
            fd11 = fd11.rename(columns = {"Total Deaths_new":"Count"})
            print("Years")
            print(fd11)
            if choice=="Deaths":
                df1 = fd[["Country","Disaster Type","Total Deaths_new"]]
            elif choice=="Total Affected":
                df1 = fd[["Country","Disaster Type","Total Affected_new"]]
            else:
                df1 = fd[["Country","Disaster Type","AdjustedDamages_new"]]
            print(df1)

            df1 = df1.replace({"United States":"United States of America"})
            df1["Country"]=df1["Country"].str.lower()
            # df["Year"] = df["Year"].astype("int")
            merged = pd.merge(left = world, right = df1, right_on = "Country", left_on = 'name', how = 'left')
            # print(world['name'].unique())
            # print(df1['Country'].unique())
            

            gdf = geopandas.GeoDataFrame(merged, geometry="geometry").dropna()
            # print(gdf.head())

            
            gdf.index = gdf.name
            gdf = gdf.rename(columns = {gdf.columns[4]:"Value"})
            print(gdf.head())
            # gdf["Year"]=gdf["Year"].astype("int")
            st.subheader(str.upper(choice))
            
            gdf = gdf.replace({"United States":"United States of America"})
            print(gdf.sort_values(by = "Value", ascending = False))

            visualizeMap1(gdf)
            
            print(alldata1.head())

#NO MAPS REQUIRED
        df = pd.DataFrame()
        if(indicator1 in capitals):
            df = capitalsOnly[capitalsOnly["Capital"]==indicator1].groupby("Year")["value"].mean().round(1).reset_index()
            print(df.head())

        else:
            df = alldata1[alldata1["Indicator"]==indicator1].groupby("Year")["value"].mean().reset_index()
            print(df.head())


        # df["Indicator"] = indicator1
        # df =df.rename(columns={Year:"value"})
        # if(indicator1=="Food Systems Resilience Score"):
        #     # df = alldata_pivot[["Country","Indicator",Year]].groupby("Country")[Year].mean().reset_index()
        #     df = alldata1.groupby("Year")["value"].mean().reset_index()
           
        #     # df["Indicator"] = indicator1
        #     print(df.head())
        #     # df =df.rename(columns={Year:"value"})
        # elif(indicator1=="Natural Capital"):
        #     df = alldata1[alldata1["Indicator"].isin(natural)].groupby("Year")["value"].mean().reset_index()
        #     print(df.head())
        # elif(indicator1=="Human Capital"):
        #     df = alldata1[alldata1["Indicator"].isin(human)].groupby("Year")["value"].mean().reset_index()
        #     print(df.head())
        # elif(indicator1=="Social Capital"):
        #     df = alldata1[alldata1["Indicator"].isin(social)].groupby("Year")["value"].mean().reset_index()
        #     print(df.head())
        # elif(indicator1=="Financial Capital"):
        #     df = alldata1[alldata1["Indicator"].isin(financial)].groupby("Year")["value"].mean().reset_index()
        #     print(df.head())
        # elif(indicator1=="Manufactured Capital"):
        #     df = alldata1[alldata1["Indicator"].isin(manufactured)].groupby("Year")["value"].mean().reset_index()
        #     print(df.head())
        # else:
        #     # df = alldata1[(alldata1["Indicator"]==indicator1)]
        #     df = alldata1[alldata1["Indicator"]==indicator1].groupby("Year")["value"].mean().reset_index()
        #     # .groupby("Year")[all_factors[indicator1]].mean().reset_index()
        #     print(df)

            # df1= df[indexes]
        df =df.rename(columns = {'value':indicator1})
        merged = fd11.merge(df,on = "Year",how = "left")
        print(merged.head())

        
        c1,c2,c3 = st.columns([1,4,1])
        linePlot(merged,indicator1,["Count"],c2,shock=shock)

      # linePlot(fd11,avgdata,)

      # linePlot()


    else:
        country = st.sidebar.selectbox('Select a country',countries)
        if country == "United States of America":
            country = "United States"
        ranger = st.sidebar.slider('Choose the range!', min_value=int(low),max_value=int(high),value=(2000,2022))
        shock = st.sidebar.selectbox('Select a shock',disasters)
        df = df[(df["Year"]>=ranger[0]) & (df["Year"]<=ranger[1]) & (df["Country"]==country)]
        if df.empty:
            st.subheader("NO DISASTERS REPORTED IN "+country)
        else:
            fd = df.groupby(["Country","Disaster Type"])[["Total Deaths_new","Total Affected_new", "AdjustedDamages_new"]].sum()
            fd = fd.assign(intensity=lambda x: x[['Total Deaths_new','Total Affected_new','AdjustedDamages_new']].mean(axis=1)).reset_index()
            fd = fd[["Country","Disaster Type","intensity"]]
            print(fd)

            fd["intensity"] = fd["intensity"].apply(np.ceil)
            print(fd.head())

            # d1,d2 = st.columns([1,10])
            try:
                st.image("Con_Flags/"+flags[country]+".png",width=50)
                st.subheader(str.upper(country))
            except:
                st.subheader(str.upper(country))
            fig3 = px.bar(fd.sort_values(by="intensity",ascending=False), x ="Disaster Type" , y = 'intensity',orientation='v',text = 'intensity')
            fig3.update_layout(yaxis_range=[0,max(fd['intensity'])+3],yaxis_title='Standardized Impact Score',xaxis_title=None, font = dict(
                    size =18,
            )
            )
            fig3.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
            fig3.update_xaxes(tickfont=dict(size =15, family = "Arial Black"))
            fig3.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))
            fig3.update_traces(textposition='outside')
            st.subheader("Impacts of Food Shocks")
            st.plotly_chart(fig3,use_container_width=False)

            sdf = df[(df["Year"].isin(years)) & (df['Disaster Type']==shock)]
            # print(dff)


            if sdf.empty:
                st.subheader("No "+ shock + " reported in chosen year range "+ str(years[0]) + " and "+  str(years[-1]))

            else:
                fd1 = sdf[sdf["Year"].isin(years)].groupby(["Disaster Type","Year"])[["Total Deaths_new","Total Affected_new", "AdjustedDamages_new"]].sum().reset_index()

                fd11 = sdf[sdf["Year"].isin(years)].groupby(["Disaster Type","Year"])["Total Deaths_new"].count().reset_index()
                print("fd1")
                print(fd1)
                fd11 = fd11.rename(columns = {"Total Deaths_new":"Count"})
                print("fd11")
                print(fd11)

                capital = st.sidebar.selectbox('FSRS/Capital',capitals)
                indicator1=None
                indicator1=None
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
            
                df = df[(df["Year"]>=ranger[0]) & (df["Year"]<=ranger[1])]
        
                df = df[df["Disaster Type"]==shock]
            
        


                print("Country")


                print(alldata1.head())
                df = pd.DataFrame()
                if(indicator1 in capitals):
                    df = capitalsOnly[capitalsOnly["Capital"]==indicator1].groupby("Year")["value"].mean().round(1).reset_index()
                    print(df.head())

                else:
                    df = alldata1[alldata1["Indicator"]==indicator1].groupby("Year")["value"].mean().reset_index()
                    print(df.head())
                # df = pd.DataFrame()
                # if(indicator1=="Food Systems Resilience Score"):
                #     # df = alldata_pivot[["Country","Indicator",Year]].groupby("Country")[Year].mean().reset_index()
                #     df = alldata1.groupby("Year")["value"].mean().reset_index()
                
                #     # df["Indicator"] = indicator1
                #     # print(df.head())
                #     # df =df.rename(columns={Year:"value"})
                # elif(indicator1=="Natural Capital"):
                #     df = alldata1[alldata1["Indicator"].isin(natural)].groupby("Year")["value"].mean().reset_index()
                #     # print(df.head())
                # elif(indicator1=="Human Capital"):
                #     df = alldata1[alldata1["Indicator"].isin(human)].groupby("Year")["value"].mean().reset_index()
                #     # print(df.head())
                # elif(indicator1=="Social Capital"):
                #     df = alldata1[alldata1["Indicator"].isin(social)].groupby("Year")["value"].mean().reset_index()
                #     # print(df.head())
                # elif(indicator1=="Financial Capital"):
                #     df = alldata1[alldata1["Indicator"].isin(financial)].groupby("Year")["value"].mean().reset_index()
                #     # print(df.head())
                # elif(indicator1=="Manufactured Capital"):
                #     df = alldata1[alldata1["Indicator"].isin(manufactured)].groupby("Year")["value"].mean().reset_index()
                #     # print(df.head())
                # else:
                #     # df = alldata1[(alldata1["Indicator"]==indicator1)]
                #     df = alldata1[alldata1["Indicator"]==indicator1].groupby("Year")["value"].mean().reset_index()
                    # .groupby("Year")[all_factors[indicator1]].mean().reset_index()
                    # print(df)

            # df1= df[indexes]
                avgdata =df.rename(columns = {'value':indicator1})
                print(avgdata.head())
                # avgdata = dff[(dff.index==country)][[all_factors[indicator1],"Year"]].groupby("Year")[all_factors[indicator1]].mean().reset_index()
                # .groupby("Year")[all_factors[indicator1]].mean().reset_index()
                # print(avgdata)

                # df1= df[indexes]

                merged = fd11.merge(avgdata,on = "Year",how = "right")
                merged = merged.merge(fd1,on = "Year", how = "left")
                print(merged.head())

                var = ["Count","Total Deaths_new","Total Affected_new","AdjustedDamages_new"]
                # c1,c2,c3 = st.columns([1,8,1])
                linePlot(merged, indicator1,var,st,shock=shock)
          # coll = int(len(var)/2)
          # print("printing coll")
          # print(coll)
          # colst = []
          # colst = st.columns(coll)
          # m  = 0


          # for i in var:
          #   colst[m].subheader(i+", "+indicator1)
          #   linePlot(merged,all_factors[indicator1],i,colst[m])
          #   m = m+1
          #   if m>coll-1:
          #     m=0
        

