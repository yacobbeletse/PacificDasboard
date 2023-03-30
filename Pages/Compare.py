
import streamlit as st
from Pages.CountryProfile import linePlot
import pandas as pd
import plotly.express as px
import numpy as np
from Pages.Home import alldata1,typology

pillars = ["Availability","Accessibility","Utilization","Stability"]

countries = alldata1["Country"].dropna().unique()

flags = {
   'Afghanistan': 'af', 'Albania': 'al', 'Algeria': 'dz', 'American Samoa': 'as', 'Andorra': 'ad', 'Angola': 'ao', 'Anguilla': 'ai', 'Antarctica': 'aq', 'Antigua and Barbuda': 'ag', 'Argentina': 'ar', 'Armenia': 'am', 'Aruba': 'aw', 'Australia': 'au', 'Austria': 'at', 'Azerbaijan': 'az', 'Bahamas': 'bs', 'Bahrain': 'bh', 'Bangladesh': 'bd', 'Barbados': 'bb', 'Belarus': 'by', 'Belgium': 'be', 'Belize': 'bz', 'Benin': 'bj', 'Bermuda': 'bm', 'Bhutan': 'bt', 'Bolivia, Plurinational State of': 'bo', 'Bolivia': 'bo', 'Bosnia and Herzegovina': 'ba', 'Botswana': 'bw', 'Bouvet Island': 'bv', 'Brazil': 'br', 'British Indian Ocean Territory': 'io', 'Brunei Darussalam': 'bn', 'Brunei': 'bn', 'Bulgaria': 'bg', 'Burkina Faso': 'bf', 'Burundi': 'bi', 'Cambodia': 'kh', 'Cameroon': 'cm', 'Canada': 'ca', 'Cape Verde': 'cv', 'Cayman Islands': 'ky', 'Central African Republic': 'cf', 'Chad': 'td', 'Chile': 'cl', 'China': 'cn', 'Christmas Island': 'cx', 'Cocos (Keeling) Islands': 'cc', 'Colombia': 'co', 'Comoros': 'km', 'Congo': 'cg', 'Congo, the Democratic Republic of the': 'cd', 'Cook Islands': 'ck', 'Costa Rica': 'cr', "Côte d'Ivoire": 'ci', 'Ivory Coast': 'ci', 'Croatia': 'hr', 'Cuba': 'cu', 'Cyprus': 'cy', 'Czech Republic': 'cz', 'Denmark': 'dk', 'Djibouti': 'dj', 'Dominica': 'dm', 'Dominican Republic': 'do', 'Ecuador': 'ec', 'Egypt': 'eg', 'El Salvador': 'sv', 'Equatorial Guinea': 'gq', 'Eritrea': 'er', 'Estonia': 'ee', 'Ethiopia': 'et', 'Falkland Islands (Malvinas)': 'fk', 'Faroe Islands': 'fo', 'Fiji': 'fj', 'Finland': 'fi', 'France': 'fr', 'French Guiana': 'gf', 'French Polynesia': 'pf', 'French Southern Territories': 'tf', 'Gabon': 'ga', 'Gambia': 'gm', 'Georgia': 'ge', 'Germany': 'de', 'Ghana': 'gh', 'Gibraltar': 'gi', 'Greece': 'gr', 'Greenland': 'gl', 'Grenada': 'gd', 'Guadeloupe': 'gp', 'Guam': 'gu', 'Guatemala': 'gt', 'Guernsey': 'gg', 'Guinea': 'gn', 'Guinea-Bissau': 'gw', 'Guyana': 'gy', 'Haiti': 'ht', 'Heard Island and McDonald Islands': 'hm', 'Holy See (Vatican City State)': 'va', 'Honduras': 'hn', 'Hong Kong': 'hk', 'Hungary': 'hu', 'Iceland': 'is', 'India': 'in', 'Indonesia': 'id', 'Iran, Islamic Republic of': 'ir', 'Iraq': 'iq', 'Ireland': 'ie', 'Isle of Man': 'im', 'Israel': 'il', 'Italy': 'it', 'Jamaica': 'jm', 'Japan': 'jp', 'Jersey': 'je', 'Jordan': 'jo', 'Kazakhstan': 'kz', 'Kenya': 'ke', 'Kiribati': 'ki', "Korea, Democratic People's Republic of": 'kp', 'Korea, Republic of': 'kr', 'South Korea': 'kr', 'Kuwait': 'kw', 'Kyrgyzstan': 'kg', "Lao People's Democratic Republic": 'la', 'Latvia': 'lv', 'Lebanon': 'lb', 'Lesotho': 'ls', 'Liberia': 'lr', 'Libyan Arab Jamahiriya': 'ly', 'Libya': 'ly', 'Liechtenstein': 'li', 'Lithuania': 'lt', 'Luxembourg': 'lu', 'Macao': 'mo', 'Macedonia, the former Yugoslav Republic of': 'mk', 'Madagascar': 'mg', 'Malawi': 'mw', 'Malaysia': 'my', 'Maldives': 'mv', 'Mali': 'ml', 'Malta': 'mt', 'Marshall Islands': 'mh', 'Martinique': 'mq', 'Mauritania': 'mr', 'Mauritius': 'mu', 'Mayotte': 'yt', 'Mexico': 'mx', 'Micronesia, Federated States of': 'fm', 'Moldova, Republic of': 'md', 'Monaco': 'mc', 'Mongolia': 'mn', 'Montenegro': 'me', 'Montserrat': 'ms', 'Morocco': 'ma', 'Mozambique': 'mz', 'Myanmar': 'mm', 'Burma': 'mm', 'Namibia': 'na', 'Nauru': 'nr', 'Nepal': 'np', 'Netherlands': 'nl', 'Netherlands Antilles': 'an', 'New Caledonia': 'nc', 'New Zealand': 'nz', 'Nicaragua': 'ni', 'Niger': 'ne', 'Nigeria': 'ng', 'Niue': 'nu', 'Norfolk Island': 'nf', 'Northern Mariana Islands': 'mp', 'Norway': 'no', 'Oman': 'om', 'Pakistan': 'pk', 'Palau': 'pw', 'Palestinian Territory, Occupied': 'ps', 'Panama': 'pa', 'Papua New Guinea': 'pg', 'Paraguay': 'py', 'Peru': 'pe', 'Philippines': 'ph', 'Pitcairn': 'pn', 'Poland': 'pl', 'Portugal': 'pt', 'Puerto Rico': 'pr', 'Qatar': 'qa', 'Réunion': 're', 'Romania': 'ro', 'Russian Federation': 'ru', 'Russia': 'ru', 'Rwanda': 'rw', 'Saint Helena, Ascension and Tristan da Cunha': 'sh', 'Saint Kitts and Nevis': 'kn', 'Saint Lucia': 'lc', 'Saint Pierre and Miquelon': 'pm', 'Saint Vincent and the Grenadines': 'vc', 'Saint Vincent & the Grenadines': 'vc', 'St. Vincent and the Grenadines': 'vc', 'Samoa': 'ws', 'San Marino': 'sm', 'Sao Tome and Principe': 'st', 'Saudi Arabia': 'sa', 'Senegal': 'sn', 'Serbia': 'rs', 'Seychelles': 'sc', 'Sierra Leone': 'sl', 'Singapore': 'sg', 'Slovakia': 'sk', 'Slovenia': 'si', 'Solomon Islands': 'sb', 'Somalia': 'so', 'South Africa': 'za', 'South Georgia and the South Sandwich Islands': 'gs', 'South Sudan': 'ss', 'Spain': 'es', 'Sri Lanka': 'lk', 'Sudan': 'sd', 'Suriname': 'sr', 'Svalbard and Jan Mayen': 'sj', 'Swaziland': 'sz', 'Sweden': 'se', 'Switzerland': 'ch', 'Syrian Arab Republic': 'sy', 'Taiwan, Province of China': 'tw', 'Taiwan': 'tw', 'Tajikistan': 'tj', 'Tanzania': 'tz', 'Thailand': 'th', 'Timor-Leste': 'tl', 'Togo': 'tg', 'Tokelau': 'tk', 'Tonga': 'to', 'Trinidad and Tobago': 'tt', 'Tunisia': 'tn', 'Turkey': 'tr', 'Turkmenistan': 'tm', 'Turks and Caicos Islands': 'tc', 'Tuvalu': 'tv', 'Uganda': 'ug', 'Ukraine': 'ua', 'United Arab Emirates': 'ae', 'United Kingdom': 'gb', 'United States of America':'us','United States': 'us', 'United States Minor Outlying Islands': 'um', 'Uruguay': 'uy', 'Uzbekistan': 'uz', 'Vanuatu': 'vu', 'Venezuela, Bolivarian Republic of': 've', 'Venezuela': 've', 'Viet Nam': 'vn', 'Vietnam': 'vn', 'Virgin Islands, British': 'vg', 'Virgin Islands, U.S.': 'vi', 'Wallis and Futuna': 'wf', 'Western Sahara': 'eh', 'Yemen': 'ye', 'Zambia': 'zm', 'Zimbabwe': 'zw'
   }

def linePlot(df,countrySelect):
  # print(df.head())
  #Function for lineplot
  #df - dataframe
  #countrySelect - selected country in the dashboard

  if(len(countrySelect)!=0):
    # df = df[df["Country"].isin(countrySelect)]
    # temp = df[df["Indicator"]==indicator1].dropna()
    # # print(temp.head())
    # print(temp)
    st.sidebar.header("FOOD SECURITY PILLARS")
    for i in pillars:
      data = df[df["Pillar"]==i]
      # print(data)
      if not data.empty:
        st.header(i.upper(),anchor=i)
        refPillar ="<div style ='height:10px'> <a href = '#{}'><h2><b> {}</b></h2></div> <br>".format(i,i.upper())
        st.sidebar.markdown(refPillar,unsafe_allow_html=True)
        # c = st.columns(len(aspects))
        c = st.columns(2)
        k=0

        temp_data = data.copy()
        for j in temp_data["Indicator"].unique():
          data_df = temp_data[temp_data["Indicator"]==j]
          # print(data_df)
          avg_data = data_df.groupby(["Indicator","Year"])["Value"].mean().reset_index()
          # print(avg_data)
          # print(data_df.columns)
          if not data_df.empty:
            fig_ind = px.line(data_df,x="Year",y='Value',color = "Country",color_discrete_sequence =px.colors.qualitative.Antique,markers=True,symbol="Country")
            fig_ind.add_scatter(x = avg_data["Year"], y = avg_data["Value"], name = "Selected Countries (Average)",line=dict(color = 'purple'))
            fig_ind.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
            fig_ind.update_layout(
                      yaxis_title= None if pd.isnull(data_df["Unit"].iloc[0]) else data_df["Unit"].iloc[0],
                      xaxis_title = None,
                      xaxis_tickformat = 'd',
                  legend_title=None,
                  font=dict(
                      family="Arial Black",
                      size=12,
                  ))
            fig_ind.update_layout(shapes=[
        dict(
            type='line',
            xref='paper',
            x0=0,
            x1=1,
            yref='y',
            y0=data_df["Baseline"].iloc[0],
            y1=data_df["Baseline"].iloc[0],
            line=dict(
                color='black',
                width=1,
                dash='dash'
            )
             )
    ]
)
            c[k].subheader(j)
            c[k].write(typology[typology["Indicator"]==j]["About"].iloc[0])
            c[k].plotly_chart(fig_ind)
          else:
            c[k].subheader(j)
            c[k].write("No data for "+j)
          k+=1
          if k >1:
              k=0
      else:
            st.subheader(i)
            st.write("No data for "+i)

    

def app():
    countrySelect = st.sidebar.multiselect('Select Country(ies)',countries)
    info = {'red':-1,'green':1,'gray':0} #This will be used to calculated the overall score for the dimensions and food security. +1 for mitigator and -1 for amplifier.
    df = alldata1.merge(typology, on = "Indicator", how = "left")
    
    df1 = df[(df["Country"].isin(countrySelect))]
    df1["Color"] = df1["Color"].map(info)
    if not df1.empty:
      temp_df = df1.dropna(subset = ["Value"]).drop_duplicates(["Country","Indicator"], keep= "last")
      fund = temp_df.groupby("Country")["Color"].sum().reset_index().sort_values("Color")
      # print(fund)
      st.header("Investment Priority")
      st.subheader("Food Security Score")
      for k in fund["Country"].unique():
        st.subheader('{} : {}'.format(k,fund[fund["Country"]==k]["Color"].iloc[0]) )
      st.write('Better Country for investment/fundings: **{}**'.format(fund["Country"].iloc[0]))
      st.subheader("Investment/Funding Areas")
      c = st.columns(4)
      m=0
      # print(temp_df.info())
      amp =temp_df[(temp_df["Country"]==fund["Country"].iloc[0]) & (temp_df["Color"]==-1)]
      #-1 is the value for amplifier
    
      for k in pillars:
          c[m].subheader(k)
          if not amp[amp["Pillar"]==k].empty:
              for l in amp[amp["Pillar"]==k]["Indicator"].unique():
                  c[m].write(l)
          else:
              c[m].write("No indicators in {}".format(k))
          m+=1
          if(m>3):
              m=0

  
    
      linePlot(df1,countrySelect)