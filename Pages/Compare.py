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
countries = ['Algeria', 'Angola', 'Argentina', 'Australia', 'Austria', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Belarus', 'Belgium', 'Benin', 'Bolivia', 'Botswana', 'Brazil', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Chad', 'Chile', 'China', 'Colombia', 'DR Congo', 'Costa Rica', 'Ivory Coast', 'Czech Republic', 'Denmark', 'Dominican Rep.', 'Ecuador', 'Egypt', 'El Salvador', 'Ethiopia', 'Finland', 'France', 'Germany', 'Ghana', 'Greece', 'Guatemala', 'Guinea', 'Haiti', 'Honduras', 'Hungary', 'India', 'Indonesia', 'Ireland', 'Israel', 'Italy', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kuwait', 'Laos', 'Madagascar', 'Malawi', 'Malaysia', 'Mali', 'Mexico', 'Morocco', 'Mozambique', 'Myanmar', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Panama', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saudi Arabia', 'Senegal', 'Serbia', 'Sierra Leone', 'Singapore', 'Slovakia', 'South Africa', 'South Korea', 'Spain', 'Sri Lanka', 'Sudan', 'Sweden', 'Switzerland', 'Syria', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tunisia', 'Turkey', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States of America', 'Uruguay', 'Uzbekistan', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia']
print("total Countries = "+ str(len(countries)))
print(countries)
alldata1 = pd.read_csv("finalCapital.csv")
alldata1 = alldata1[alldata1["Country"].isin(countries)]
# alldata1 = alldata1.replace({'United States':'United States of America',
#                             'Dominican Rep.':'Dominican Republic'})
# print(alldata1.head())
# if l in ['HDI', 'Proportion of Undernourished', 'Proportion of food insecure','Food Systems Resilience Score']:

# countries = ['Algeria', 'Angola', 'Argentina', 'Australia', 'Austria', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Belarus', 'Belgium', 'Benin', 'Bolivia', 'Botswana', 'Brazil', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Chad', 'Chile', 'China', 'Colombia', 'DR Congo', 'Costa Rica', 'Ivory Coast', 'Czech Republic', 'Denmark', 'Dominican Rep.', 'Ecuador', 'Egypt', 'El Salvador', 'Ethiopia', 'Finland', 'France', 'Germany', 'Ghana', 'Greece', 'Guatemala', 'Guinea', 'Haiti', 'Honduras', 'Hungary', 'India', 'Indonesia', 'Ireland', 'Israel', 'Italy', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kuwait', 'Laos', 'Madagascar', 'Malawi', 'Malaysia', 'Mali', 'Mexico', 'Morocco', 'Mozambique', 'Myanmar', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Panama', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saudi Arabia', 'Senegal', 'Serbia', 'Sierra Leone', 'Singapore', 'Slovakia', 'South Africa', 'South Korea', 'Spain', 'Sri Lanka', 'Sudan', 'Sweden', 'Switzerland', 'Syria', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tunisia', 'Turkey', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States of America', 'Uruguay', 'Uzbekistan', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia']


alldata_pivot = alldata1.pivot(index = ["Country", "Capital"],columns="Year",values="value").reset_index()
print("Printing Pivot PD")
print(alldata_pivot.head())

# capitalsOnly = pd.read_csv("finalCapital.csv")

other = ["HDI","Proportion of Undernourished", "Proportion of food insecure"]
other_db = {}
total_country = {}
other_db["HDI"] = pd.read_csv('HDI.csv')
total_country["HDI"] = other_db["HDI"].shape[0]
other_db["Proportion of Undernourished"]  = pd.read_csv('Proportion of Undernourished.csv')
total_country["Proportion of Undernourished"] = other_db["Proportion of Undernourished"].shape[0]
other_db["Proportion of food insecure"]  = pd.read_csv('Proportion of food insecure.csv')
total_country["Proportion of food insecure"] = other_db["Proportion of food insecure"].shape[0]
total_country["Food Systems Resilience Score"] = len(alldata1["Country"].unique())
total_country["Natural Capital"] = len(alldata1["Country"].unique())
total_country["Human Capital"] = len(alldata1["Country"].unique())
total_country["Social Capital"] = len(alldata1["Country"].unique())
total_country["Financial Capital"] = len(alldata1["Country"].unique())
total_country["Manufactured Capital"] = len(alldata1["Country"].unique())

# countries = alldata1["Country"].unique()
# alldata1 = alldata1[alldata1["Country"].isin(countries)]


flags = {
   'Afghanistan': 'af', 'Albania': 'al', 'Algeria': 'dz', 'American Samoa': 'as', 'Andorra': 'ad', 'Angola': 'ao', 'Anguilla': 'ai', 'Antarctica': 'aq', 'Antigua and Barbuda': 'ag', 'Argentina': 'ar', 'Armenia': 'am', 'Aruba': 'aw', 'Australia': 'au', 'Austria': 'at', 'Azerbaijan': 'az', 'Bahamas': 'bs', 'Bahrain': 'bh', 'Bangladesh': 'bd', 'Barbados': 'bb', 'Belarus': 'by', 'Belgium': 'be', 'Belize': 'bz', 'Benin': 'bj', 'Bermuda': 'bm', 'Bhutan': 'bt', 'Bolivia, Plurinational State of': 'bo', 'Bolivia': 'bo', 'Bosnia and Herzegovina': 'ba', 'Botswana': 'bw', 'Bouvet Island': 'bv', 'Brazil': 'br', 'British Indian Ocean Territory': 'io', 'Brunei Darussalam': 'bn', 'Brunei': 'bn', 'Bulgaria': 'bg', 'Burkina Faso': 'bf', 'Burundi': 'bi', 'Cambodia': 'kh', 'Cameroon': 'cm', 'Canada': 'ca', 'Cape Verde': 'cv', 'Cayman Islands': 'ky', 'Central African Republic': 'cf', 'Chad': 'td', 'Chile': 'cl', 'China': 'cn', 'Christmas Island': 'cx', 'Cocos (Keeling) Islands': 'cc', 'Colombia': 'co', 'Comoros': 'km', 'Congo': 'cg', 'Congo, the Democratic Republic of the': 'cd', 'Cook Islands': 'ck', 'Costa Rica': 'cr', "Côte d'Ivoire": 'ci', 'Ivory Coast': 'ci', 'Croatia': 'hr', 'Cuba': 'cu', 'Cyprus': 'cy', 'Czech Republic': 'cz', 'Denmark': 'dk', 'Djibouti': 'dj', 'Dominica': 'dm', 'Dominican Republic': 'do', 'Ecuador': 'ec', 'Egypt': 'eg', 'El Salvador': 'sv', 'Equatorial Guinea': 'gq', 'Eritrea': 'er', 'Estonia': 'ee', 'Ethiopia': 'et', 'Falkland Islands (Malvinas)': 'fk', 'Faroe Islands': 'fo', 'Fiji': 'fj', 'Finland': 'fi', 'France': 'fr', 'French Guiana': 'gf', 'French Polynesia': 'pf', 'French Southern Territories': 'tf', 'Gabon': 'ga', 'Gambia': 'gm', 'Georgia': 'ge', 'Germany': 'de', 'Ghana': 'gh', 'Gibraltar': 'gi', 'Greece': 'gr', 'Greenland': 'gl', 'Grenada': 'gd', 'Guadeloupe': 'gp', 'Guam': 'gu', 'Guatemala': 'gt', 'Guernsey': 'gg', 'Guinea': 'gn', 'Guinea-Bissau': 'gw', 'Guyana': 'gy', 'Haiti': 'ht', 'Heard Island and McDonald Islands': 'hm', 'Holy See (Vatican City State)': 'va', 'Honduras': 'hn', 'Hong Kong': 'hk', 'Hungary': 'hu', 'Iceland': 'is', 'India': 'in', 'Indonesia': 'id', 'Iran, Islamic Republic of': 'ir', 'Iraq': 'iq', 'Ireland': 'ie', 'Isle of Man': 'im', 'Israel': 'il', 'Italy': 'it', 'Jamaica': 'jm', 'Japan': 'jp', 'Jersey': 'je', 'Jordan': 'jo', 'Kazakhstan': 'kz', 'Kenya': 'ke', 'Kiribati': 'ki', "Korea, Democratic People's Republic of": 'kp', 'Korea, Republic of': 'kr', 'South Korea': 'kr', 'Kuwait': 'kw', 'Kyrgyzstan': 'kg', "Lao People's Democratic Republic": 'la', 'Latvia': 'lv', 'Lebanon': 'lb', 'Lesotho': 'ls', 'Liberia': 'lr', 'Libyan Arab Jamahiriya': 'ly', 'Libya': 'ly', 'Liechtenstein': 'li', 'Lithuania': 'lt', 'Luxembourg': 'lu', 'Macao': 'mo', 'Macedonia, the former Yugoslav Republic of': 'mk', 'Madagascar': 'mg', 'Malawi': 'mw', 'Malaysia': 'my', 'Maldives': 'mv', 'Mali': 'ml', 'Malta': 'mt', 'Marshall Islands': 'mh', 'Martinique': 'mq', 'Mauritania': 'mr', 'Mauritius': 'mu', 'Mayotte': 'yt', 'Mexico': 'mx', 'Micronesia, Federated States of': 'fm', 'Moldova, Republic of': 'md', 'Monaco': 'mc', 'Mongolia': 'mn', 'Montenegro': 'me', 'Montserrat': 'ms', 'Morocco': 'ma', 'Mozambique': 'mz', 'Myanmar': 'mm', 'Burma': 'mm', 'Namibia': 'na', 'Nauru': 'nr', 'Nepal': 'np', 'Netherlands': 'nl', 'Netherlands Antilles': 'an', 'New Caledonia': 'nc', 'New Zealand': 'nz', 'Nicaragua': 'ni', 'Niger': 'ne', 'Nigeria': 'ng', 'Niue': 'nu', 'Norfolk Island': 'nf', 'Northern Mariana Islands': 'mp', 'Norway': 'no', 'Oman': 'om', 'Pakistan': 'pk', 'Palau': 'pw', 'Palestinian Territory, Occupied': 'ps', 'Panama': 'pa', 'Papua New Guinea': 'pg', 'Paraguay': 'py', 'Peru': 'pe', 'Philippines': 'ph', 'Pitcairn': 'pn', 'Poland': 'pl', 'Portugal': 'pt', 'Puerto Rico': 'pr', 'Qatar': 'qa', 'Réunion': 're', 'Romania': 'ro', 'Russian Federation': 'ru', 'Russia': 'ru', 'Rwanda': 'rw', 'Saint Helena, Ascension and Tristan da Cunha': 'sh', 'Saint Kitts and Nevis': 'kn', 'Saint Lucia': 'lc', 'Saint Pierre and Miquelon': 'pm', 'Saint Vincent and the Grenadines': 'vc', 'Saint Vincent & the Grenadines': 'vc', 'St. Vincent and the Grenadines': 'vc', 'Samoa': 'ws', 'San Marino': 'sm', 'Sao Tome and Principe': 'st', 'Saudi Arabia': 'sa', 'Senegal': 'sn', 'Serbia': 'rs', 'Seychelles': 'sc', 'Sierra Leone': 'sl', 'Singapore': 'sg', 'Slovakia': 'sk', 'Slovenia': 'si', 'Solomon Islands': 'sb', 'Somalia': 'so', 'South Africa': 'za', 'South Georgia and the South Sandwich Islands': 'gs', 'South Sudan': 'ss', 'Spain': 'es', 'Sri Lanka': 'lk', 'Sudan': 'sd', 'Suriname': 'sr', 'Svalbard and Jan Mayen': 'sj', 'Swaziland': 'sz', 'Sweden': 'se', 'Switzerland': 'ch', 'Syrian Arab Republic': 'sy', 'Taiwan, Province of China': 'tw', 'Taiwan': 'tw', 'Tajikistan': 'tj', 'Tanzania': 'tz', 'Thailand': 'th', 'Timor-Leste': 'tl', 'Togo': 'tg', 'Tokelau': 'tk', 'Tonga': 'to', 'Trinidad and Tobago': 'tt', 'Tunisia': 'tn', 'Turkey': 'tr', 'Turkmenistan': 'tm', 'Turks and Caicos Islands': 'tc', 'Tuvalu': 'tv', 'Uganda': 'ug', 'Ukraine': 'ua', 'United Arab Emirates': 'ae', 'United Kingdom': 'gb', 'United States of America':'us','United States': 'us', 'United States Minor Outlying Islands': 'um', 'Uruguay': 'uy', 'Uzbekistan': 'uz', 'Vanuatu': 'vu', 'Venezuela, Bolivarian Republic of': 've', 'Venezuela': 've', 'Viet Nam': 'vn', 'Vietnam': 'vn', 'Virgin Islands, British': 'vg', 'Virgin Islands, U.S.': 'vi', 'Wallis and Futuna': 'wf', 'Western Sahara': 'eh', 'Yemen': 'ye', 'Zambia': 'zm', 'Zimbabwe': 'zw'
   }
# @st.cache(suppress_st_warning=True)
# def visualizeMap1(gdf):


#     #  fig = px.choropleth(gdf, geojson=gdf.geometry, locations=gdf.index, color="Value", width = 1000,color_continuous_scale="RdYlGn",range_color=(0, 100),
#     #  hover_name=gdf.index,animation_frame="Year")
#      fig = px.choropleth(gdf, geojson=gdf.geometry, locations=gdf.index, color="value", width = 1000,color_continuous_scale="RdYlGn",range_color=(0, 100),
#      hover_name=gdf.index)
#      fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
#      fig.update_geos(fitbounds="locations", visible=False, landcolor = 'lightgray',showland = True,showcountries=True, countrycolor="gray")
#      fig.update_traces(marker_line_width=2)
#     #  cb_ax = fig.axes[1] 
#     #  cb_ax.tick_params(labelsize=5)


#     #  fig.colorbar.lim(0,100)
#      st.plotly_chart(fig)
# @st.cache(suppress_st_warning=True)
years =[*range(2012,2023)]
years.sort(reverse=True)
print(years)

def tryconvert(x):
  try:
    return(int(x))
  except:
    return("NA")

def app():
    st.header('RANK COMPARISON')


    # print(hdi.columns)
    # print(alldata1)
    yearChoice = int(st.sidebar.selectbox("Year",years))
    countrySelect = st.sidebar.multiselect('Select Country(ies)',countries)
    print(countrySelect)
    print("choice of year = " + str(yearChoice))

    df = alldata_pivot[["Country","Capital",yearChoice]].pivot("Country",columns = "Capital", values = yearChoice)

    print(df.head())

    if  len(countrySelect)!=0:
      legend = "<b> Legend  </b> <span class = 'highlight green tab'> Q1 </span> <span class = 'highlight yellow'> Q2 </span> <span class = 'highlight orange'> Q3 </span> <span class = 'highlight red'> Q4 </span><br><br>"
      print(legend)
      st.markdown(legend,unsafe_allow_html=True)
    # df_hdi = hdi.filter(["Country",yearChoice],axis =1)
    # df_hdi = hdi[["Country",yearChoice]]
    # fd = pd.DataFrame()
    for i in df.columns:
      # temp = df[[df.index]]
      # if i in ["Proportion of Undernourished", "Proportion of food insecure"]:
      #   df["rank_"+i] = df[i].dropna().rank(ascending = True).astype(int) if not df[i].dropna().empty else 'NA'
      # else:
      df["rank_"+i] = df[i].dropna().rank(ascending = False).astype(int) if not df[i].dropna().empty else 'NA'
      df = df.drop(columns = [i])
      # fd = fd.append(temp,ignore_index=False)
    fd =df.reset_index()
    print(fd.head())


    compare_data = fd.copy()

    d = st.columns(3)

    for m in other:
        print(m)
        other_data = other_db[m].filter(["Country",str(yearChoice)])
        other_data = other_data.rename(columns = {str(yearChoice):m})
        other_data = other_data[other_data["Country"].isin(countries)]
        # other_data["rank_"+m] = other_data[m].dropna().rank(ascending = False) if not other_data[m].dropna().empty else 'NA'
        if m in ["Proportion of Undernourished", "Proportion of food insecure"]:
          other_data["rank_"+m] = other_data[m].dropna().rank(ascending = True) 
        else:
          other_data["rank_"+m] = other_data[m].dropna().rank(ascending = False)
        other_data = other_data.drop(columns = [m])
        compare_data = pd.merge(compare_data,other_data, on="Country",how = "inner")
    print(compare_data.head())

    k=0
    for j in countrySelect:
      data = compare_data[compare_data["Country"]==j].melt("Country", value_vars=[i for i in compare_data.columns if i not in [ "Country", "Capital"]],var_name="Indicators", value_name="Rank")
      # d1,d2 = d[k].columns([1,10])
      print(data.head())
      # data["Rank"] = data["Rank"].apply(lambda x: int(x) if  not (x.isnull()) else "NA")
      # data["Rank"].apply(lambda x: tryconvert(x))
      # data["Rank"] = data["Rank"].astype('Int64')
      # if (type(x)=="int" or type(x)=="float") else "NA"
      print(data)
      renameCols = {}
      for i in data["Indicators"].unique():
          renameCols[i] = i.split("_")[1]
      data = data.replace(renameCols)
      try:
        d[k].image("Con_Flags/"+flags[j]+".png",width=50)
        d[k].subheader(str.upper(j))
      except:
        d[k].subheader(str.upper(j))
      # print(data)

      catOrder = [ 'HDI', 'Proportion of Undernourished', 'Proportion of food insecure','Food Systems Resilience Score','Natural Capital',
                  'Human Capital','Social Capital','Financial Capital', 'Manufactured Capital']
      with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
      for l in catOrder:
        rank = tryconvert(data.loc[data["Indicators"]==l,"Rank"].iloc[0])
        color = "" 
        if rank!="NA":
          if rank > total_country[l]/2 and rank <=total_country[l]*3/4:
            color = "orange"
          elif rank > total_country[l]/4 and rank <=total_country[l]/2:
            color = "yellow"
          elif rank <= total_country[l]/4:
            color = "green"
          else:
            color = "red"
          style_text =" "
          if l in ['HDI', 'Proportion of Undernourished', 'Proportion of food insecure','Food Systems Resilience Score']:
            style_text = "<div> <b style='font-size:25px;'> {} : </b> <span class = 'highlight {}' > {} / {} </span><br><br>".format(l,color,rank,total_country[l])
          else:
            style_text = "<div style = 'text-indent: 40px'> <b style='font-size:20px;'> {} : </b> <span class = 'highlight {}' > {} / {} </span>".format(l,color,rank,total_country[l])
          
            
          print(style_text)
          d[k].markdown(style_text, unsafe_allow_html=True)
        else:

          if l in ['HDI', 'Proportion of Undernourished', 'Proportion of food insecure','Food Systems Resilience Score']:
            d[k].subheader(l+" : "+ str(rank)+" / " + str(total_country[l])) 
          else:
            d[k].write(l+" : "+ str(rank))

      k = k+1
      if k >2:
        k=0



      # fig3 = px.bar(data, x ="Rank" , y = 'Indicators',orientation='h',text = 'Rank')
      # fig3.update_layout(xaxis_title=None, yaxis_title = None, font = dict(
      #         size =18
      # ), width = 500
      # )
      # fig3.update_xaxes(showticklabels = False)
      # fig3.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))
      # fig3.update_traces(textposition='auto')
      # fig3.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
      # # st.subheader("Impacts of Food Shocks")
      # d[k].plotly_chart(fig3)
      # k = k+1
      # if(k>2):
      #   k=0
      # for m in capitals1:
      #   rank = int(data.loc[(data["Capital"]==m),"rank"])

      #   if(capitals[m]=="fsrs"):
      #      d[k].subheader(capitals1[m]+ ' : ' + str(rank))
      #   else:
      #     d[k].write(capitals1[m]+ ' : ' + str(rank))

      
      
      #   if (m=="HDI"):
      #     other_data["rank"] = other_data[str(yearChoice)].rank(ascending=False).astype(int) if not other_data[str(yearChoice)].dropna().empty else "NA"
      #   else:
      #     # print(other_data[str(yearChoice)].rank())
      #     other_data["rank"] = other_data[str(yearChoice)].rank(ascending=True) 
      #     if not other_data[str(yearChoice)].dropna().empty:
      #       other_data["rank"] = other_data["rank"].fillna(0).astype(int)
      #       other_data["rank"] = other_data["rank"].replace({0:'NA'})
      #     else:
      #       other_data["rank"] = 'NA'

      
      #   print(other_data.head())
      #   d[k].subheader( m + ": "+ str((other_data.loc[other_data["Country"]==i,"rank"].iloc[0])))
      # k = k+1
    

    # for i in countrySelect:
    #   data = fd[fd["Country"]==i]
    #   # d1,d2 = d[k].columns([1,10])
    #   try:
    #     d[k].image("Con_Flags/"+flags[i]+".png",width=50)
    #     d[k].subheader(str.upper(i))
    #   except:
    #     d[k].subheader(str.upper(i))

    #   for m in range(len(capitals1)):
    #     rank = int(data.loc[(data["Capital"]==capitals[m]),"rank"])

    #     if(capitals[m]=="fsrs"):
    #        d[k].subheader(capitals1[m]+ ' : ' + str(rank))
    #     else:
    #       d[k].write(capitals1[m]+ ' : ' + str(rank))

      
      
    #     if (m=="HDI"):
    #       other_data["rank"] = other_data[str(yearChoice)].rank(ascending=False).astype(int) if not other_data[str(yearChoice)].dropna().empty else "NA"
    #     else:
    #       # print(other_data[str(yearChoice)].rank())
    #       other_data["rank"] = other_data[str(yearChoice)].rank(ascending=True) 
    #       if not other_data[str(yearChoice)].dropna().empty:
    #         other_data["rank"] = other_data["rank"].fillna(0).astype(int)
    #         other_data["rank"] = other_data["rank"].replace({0:'NA'})
    #       else:
    #         other_data["rank"] = 'NA'

      
    #     print(other_data.head())
    #     d[k].subheader( m + ": "+ str((other_data.loc[other_data["Country"]==i,"rank"].iloc[0])))
    #   k = k+1
    
    
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
   
    # df = pd.DataFrame()
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
    
