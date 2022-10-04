from tkinter.tix import Tree
import streamlit as st
import geopandas
import pandas as pd
import plotly.express as px
import numpy as np

capitals1 = ['Food Systems Resilience Score','Natural Capital','Human Capital','Social Capital','Financial Capital','Manufactured Capital']

capitals = ['fsrs','natural','human','social','financial','manufactured']

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

# world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
# world = world[(world.pop_est>0) & (world.name!="Antarctica")].drop(columns =["pop_est","continent","iso_a3","gdp_md_est"])
# world['name'] = world['name'].str.lower() 
# print("Number of Countries = "+str(len(world['name'].unique())))

alldata1 = pd.read_csv("finalCapital.csv")
alldata1 = alldata1.replace({'United States':'United States of America'})
print(alldata1.head())

# countries = ['Algeria', 'Angola', 'Argentina', 'Australia', 'Austria', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Belarus', 'Belgium', 'Benin', 'Bolivia', 'Botswana', 'Brazil', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Chad', 'Chile', 'China', 'Colombia', 'DR Congo', 'Costa Rica', 'Ivory Coast', 'Czech Republic', 'Denmark', 'Dominican Rep.', 'Ecuador', 'Egypt', 'El Salvador', 'Ethiopia', 'Finland', 'France', 'Germany', 'Ghana', 'Greece', 'Guatemala', 'Guinea', 'Haiti', 'Honduras', 'Hungary', 'India', 'Indonesia', 'Ireland', 'Israel', 'Italy', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kuwait', 'Laos', 'Madagascar', 'Malawi', 'Malaysia', 'Mali', 'Mexico', 'Morocco', 'Mozambique', 'Myanmar', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Panama', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saudi Arabia', 'Senegal', 'Serbia', 'Sierra Leone', 'Singapore', 'Slovakia', 'South Africa', 'South Korea', 'Spain', 'Sri Lanka', 'Sudan', 'Sweden', 'Switzerland', 'Syria', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tunisia', 'Turkey', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States of America', 'Uruguay', 'Uzbekistan', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia']
countries = alldata1["Country"].unique()
alldata1 = alldata1[alldata1["Country"].isin(countries)]

alldata_pivot = alldata1.pivot(["Country","Capital"],columns="Year",values="value").reset_index()
print("Printing Pivot PD")
print(alldata_pivot.head())


other = ["HDI","Proportion of Undernourished", "Proportion of food insecure"]
other_db = {}
other_db["HDI"] = pd.read_csv('HDI.csv')
other_db["Proportion of Undernourished"]  = pd.read_csv('Proportion of Undernourished.csv')
other_db["Proportion of food insecure"]  = pd.read_csv('Proportion of food insecure.csv')


flags = {
   'Afghanistan': 'af', 'Albania': 'al', 'Algeria': 'dz', 'American Samoa': 'as', 'Andorra': 'ad', 'Angola': 'ao', 'Anguilla': 'ai', 'Antarctica': 'aq', 'Antigua and Barbuda': 'ag', 'Argentina': 'ar', 'Armenia': 'am', 'Aruba': 'aw', 'Australia': 'au', 'Austria': 'at', 'Azerbaijan': 'az', 'Bahamas': 'bs', 'Bahrain': 'bh', 'Bangladesh': 'bd', 'Barbados': 'bb', 'Belarus': 'by', 'Belgium': 'be', 'Belize': 'bz', 'Benin': 'bj', 'Bermuda': 'bm', 'Bhutan': 'bt', 'Bolivia, Plurinational State of': 'bo', 'Bolivia': 'bo', 'Bosnia and Herzegovina': 'ba', 'Botswana': 'bw', 'Bouvet Island': 'bv', 'Brazil': 'br', 'British Indian Ocean Territory': 'io', 'Brunei Darussalam': 'bn', 'Brunei': 'bn', 'Bulgaria': 'bg', 'Burkina Faso': 'bf', 'Burundi': 'bi', 'Cambodia': 'kh', 'Cameroon': 'cm', 'Canada': 'ca', 'Cape Verde': 'cv', 'Cayman Islands': 'ky', 'Central African Republic': 'cf', 'Chad': 'td', 'Chile': 'cl', 'China': 'cn', 'Christmas Island': 'cx', 'Cocos (Keeling) Islands': 'cc', 'Colombia': 'co', 'Comoros': 'km', 'Congo': 'cg', 'Congo, the Democratic Republic of the': 'cd', 'Cook Islands': 'ck', 'Costa Rica': 'cr', "Côte d'Ivoire": 'ci', 'Ivory Coast': 'ci', 'Croatia': 'hr', 'Cuba': 'cu', 'Cyprus': 'cy', 'Czech Republic': 'cz', 'Denmark': 'dk', 'Djibouti': 'dj', 'Dominica': 'dm', 'Dominican Republic': 'do', 'Ecuador': 'ec', 'Egypt': 'eg', 'El Salvador': 'sv', 'Equatorial Guinea': 'gq', 'Eritrea': 'er', 'Estonia': 'ee', 'Ethiopia': 'et', 'Falkland Islands (Malvinas)': 'fk', 'Faroe Islands': 'fo', 'Fiji': 'fj', 'Finland': 'fi', 'France': 'fr', 'French Guiana': 'gf', 'French Polynesia': 'pf', 'French Southern Territories': 'tf', 'Gabon': 'ga', 'Gambia': 'gm', 'Georgia': 'ge', 'Germany': 'de', 'Ghana': 'gh', 'Gibraltar': 'gi', 'Greece': 'gr', 'Greenland': 'gl', 'Grenada': 'gd', 'Guadeloupe': 'gp', 'Guam': 'gu', 'Guatemala': 'gt', 'Guernsey': 'gg', 'Guinea': 'gn', 'Guinea-Bissau': 'gw', 'Guyana': 'gy', 'Haiti': 'ht', 'Heard Island and McDonald Islands': 'hm', 'Holy See (Vatican City State)': 'va', 'Honduras': 'hn', 'Hong Kong': 'hk', 'Hungary': 'hu', 'Iceland': 'is', 'India': 'in', 'Indonesia': 'id', 'Iran, Islamic Republic of': 'ir', 'Iraq': 'iq', 'Ireland': 'ie', 'Isle of Man': 'im', 'Israel': 'il', 'Italy': 'it', 'Jamaica': 'jm', 'Japan': 'jp', 'Jersey': 'je', 'Jordan': 'jo', 'Kazakhstan': 'kz', 'Kenya': 'ke', 'Kiribati': 'ki', "Korea, Democratic People's Republic of": 'kp', 'Korea, Republic of': 'kr', 'South Korea': 'kr', 'Kuwait': 'kw', 'Kyrgyzstan': 'kg', "Lao People's Democratic Republic": 'la', 'Latvia': 'lv', 'Lebanon': 'lb', 'Lesotho': 'ls', 'Liberia': 'lr', 'Libyan Arab Jamahiriya': 'ly', 'Libya': 'ly', 'Liechtenstein': 'li', 'Lithuania': 'lt', 'Luxembourg': 'lu', 'Macao': 'mo', 'Macedonia, the former Yugoslav Republic of': 'mk', 'Madagascar': 'mg', 'Malawi': 'mw', 'Malaysia': 'my', 'Maldives': 'mv', 'Mali': 'ml', 'Malta': 'mt', 'Marshall Islands': 'mh', 'Martinique': 'mq', 'Mauritania': 'mr', 'Mauritius': 'mu', 'Mayotte': 'yt', 'Mexico': 'mx', 'Micronesia, Federated States of': 'fm', 'Moldova, Republic of': 'md', 'Monaco': 'mc', 'Mongolia': 'mn', 'Montenegro': 'me', 'Montserrat': 'ms', 'Morocco': 'ma', 'Mozambique': 'mz', 'Myanmar': 'mm', 'Burma': 'mm', 'Namibia': 'na', 'Nauru': 'nr', 'Nepal': 'np', 'Netherlands': 'nl', 'Netherlands Antilles': 'an', 'New Caledonia': 'nc', 'New Zealand': 'nz', 'Nicaragua': 'ni', 'Niger': 'ne', 'Nigeria': 'ng', 'Niue': 'nu', 'Norfolk Island': 'nf', 'Northern Mariana Islands': 'mp', 'Norway': 'no', 'Oman': 'om', 'Pakistan': 'pk', 'Palau': 'pw', 'Palestinian Territory, Occupied': 'ps', 'Panama': 'pa', 'Papua New Guinea': 'pg', 'Paraguay': 'py', 'Peru': 'pe', 'Philippines': 'ph', 'Pitcairn': 'pn', 'Poland': 'pl', 'Portugal': 'pt', 'Puerto Rico': 'pr', 'Qatar': 'qa', 'Réunion': 're', 'Romania': 'ro', 'Russian Federation': 'ru', 'Russia': 'ru', 'Rwanda': 'rw', 'Saint Helena, Ascension and Tristan da Cunha': 'sh', 'Saint Kitts and Nevis': 'kn', 'Saint Lucia': 'lc', 'Saint Pierre and Miquelon': 'pm', 'Saint Vincent and the Grenadines': 'vc', 'Saint Vincent & the Grenadines': 'vc', 'St. Vincent and the Grenadines': 'vc', 'Samoa': 'ws', 'San Marino': 'sm', 'Sao Tome and Principe': 'st', 'Saudi Arabia': 'sa', 'Senegal': 'sn', 'Serbia': 'rs', 'Seychelles': 'sc', 'Sierra Leone': 'sl', 'Singapore': 'sg', 'Slovakia': 'sk', 'Slovenia': 'si', 'Solomon Islands': 'sb', 'Somalia': 'so', 'South Africa': 'za', 'South Georgia and the South Sandwich Islands': 'gs', 'South Sudan': 'ss', 'Spain': 'es', 'Sri Lanka': 'lk', 'Sudan': 'sd', 'Suriname': 'sr', 'Svalbard and Jan Mayen': 'sj', 'Swaziland': 'sz', 'Sweden': 'se', 'Switzerland': 'ch', 'Syrian Arab Republic': 'sy', 'Taiwan, Province of China': 'tw', 'Taiwan': 'tw', 'Tajikistan': 'tj', 'Tanzania': 'tz', 'Thailand': 'th', 'Timor-Leste': 'tl', 'Togo': 'tg', 'Tokelau': 'tk', 'Tonga': 'to', 'Trinidad and Tobago': 'tt', 'Tunisia': 'tn', 'Turkey': 'tr', 'Turkmenistan': 'tm', 'Turks and Caicos Islands': 'tc', 'Tuvalu': 'tv', 'Uganda': 'ug', 'Ukraine': 'ua', 'United Arab Emirates': 'ae', 'United Kingdom': 'gb', 'United States of America':'us','United States': 'us', 'United States Minor Outlying Islands': 'um', 'Uruguay': 'uy', 'Uzbekistan': 'uz', 'Vanuatu': 'vu', 'Venezuela, Bolivarian Republic of': 've', 'Venezuela': 've', 'Viet Nam': 'vn', 'Vietnam': 'vn', 'Virgin Islands, British': 'vg', 'Virgin Islands, U.S.': 'vi', 'Wallis and Futuna': 'wf', 'Western Sahara': 'eh', 'Yemen': 'ye', 'Zambia': 'zm', 'Zimbabwe': 'zw'
   }
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
    st.header('RANK COMPARISON')

    # print(hdi.columns)
    # print(alldata1)
    yearChoice = int(st.sidebar.selectbox("Year",years))
    countrySelect = st.sidebar.multiselect('Select Country(ies)',countries)
    print("choice of year = " + str(type(yearChoice)))

    df = alldata_pivot[["Country","Capital",yearChoice]]

    print(df.columns)



    # df_hdi = hdi.filter(["Country",yearChoice],axis =1)
    # df_hdi = hdi[["Country",yearChoice]]

    fd = pd.DataFrame()
    for i in df["Capital"].unique():
      temp = df[df["Capital"]==i]
      temp["rank"] = temp[yearChoice].rank(ascending = False).astype(int)
      fd = fd.append(temp,ignore_index=False)
    print(fd.head())
    d = st.columns(4)

    k=0
    for i in countrySelect:
      data = fd[fd["Country"]==i]
      # d1,d2 = d[k].columns([1,10])
      d[k].image("Con_Flags/"+flags[i]+".png",width=50)
      d[k].subheader(str.upper(i))

      for m in range(len(capitals1)):
        rank = int(data.loc[(data["Capital"]==capitals[m]),"rank"])

        if(capitals[m]=="fsrs"):
           d[k].subheader(capitals1[m]+ ' : ' + str(rank))
        else:
          d[k].write(capitals1[m]+ ' : ' + str(rank))

      for m in other:
        print(m)
        other_data = other_db[m].filter(["Country",str(yearChoice)])
        other_data = other_data[other_data["Country"].isin(countries)]

        print(other_data.head())
      
        if (m=="HDI"):
          other_data["rank"] = other_data[str(yearChoice)].rank(ascending=False).astype(int) if not other_data[str(yearChoice)].dropna().empty else "NA"
        else:
          # print(other_data[str(yearChoice)].rank())
          other_data["rank"] = other_data[str(yearChoice)].rank(ascending=True) 
          if not other_data[str(yearChoice)].dropna().empty:
            other_data["rank"] = other_data["rank"].fillna(0).astype(int)
            other_data["rank"] = other_data["rank"].replace({0:'NA'})
          else:
            other_data["rank"] = 'NA'

      
        print(other_data.head())
        d[k].subheader( m + ": "+ str((other_data.loc[other_data["Country"]==i,"rank"].iloc[0])))
      k = k+1
    
    
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
   
    df = pd.DataFrame()
    # indicator = all_factors[indicator1]
    # if(indicator1=="Food System Resilience Score"):
    #   df = alldata_pivot[["Country","Indicator",Year]].groupby("Country")[Year].mean().reset_index()
    #   df["Indicator"] = indicator1
    #   df =df.rename(columns={Year:"value"})
    # elif(indicator1=="Natural Capital"):
    #   df = alldata_pivot.loc[alldata_pivot["Indicator"].isin(natural),["Country","Indicator",Year]].groupby("Country")[Year].mean().reset_index()
    #   df =df.rename(columns={Year:"value"})
    # elif(indicator1=="Human Capital"):
    #   df = alldata_pivot.loc[alldata_pivot["Indicator"].isin(human),["Country","Indicator",Year]].groupby("Country")[Year].mean().reset_index()
    #   df =df.rename(columns={Year:"value"})
    # elif(indicator1=="Social Capital"):
    #   df = alldata_pivot.loc[alldata_pivot["Indicator"].isin(social),["Country","Indicator",Year]].groupby("Country")[Year].mean().reset_index()
    #   df =df.rename(columns={Year:"value"})
    # elif(indicator1=="Financial Capital"):
    #   df = alldata_pivot.loc[alldata_pivot["Indicator"].isin(financial),["Country","Indicator",Year]].groupby("Country")[Year].mean().reset_index()
    #   df =df.rename(columns={Year:"value"})
    # elif(indicator1=="Manufactured Capital"):
    #   df = alldata_pivot.loc[alldata_pivot["Indicator"].isin(manufactured),["Country","Indicator",Year]].groupby("Country")[Year].mean().reset_index()
    #   df =df.rename(columns={Year:"value"})
    # else:
    #   df = alldata1[(alldata1["Year"]==Year) & (alldata1["Indicator"]==indicator1)]
    #   # print(df)
      # df = df[(df["Year"]==Year) & (df["Indicator"]==indicator1)]
      # print(df)
    # if indicator1 in capitals:
    #   if indicator1==
    # print(df)
    # df["Country"]=df["Country"].str.lower()
    # # df["Year"] = df["Year"].astype("int")
    # # print("alldata country = "+ str(len(df["Country"].unique())))
    # # print(df["Country"].unique())
    # merged = pd.merge(left = world, right = df, right_on = "Country", left_on = 'name', how = 'right')

    # gdf = geopandas.GeoDataFrame(merged, geometry="geometry")

    # print(gdf)
    # gdf.index = gdf.name
    # # gdf["Year"]=gdf["Year"].astype("int")
    # st.subheader(str.upper(indicator1))
    # visualizeMap1(gdf)
    
