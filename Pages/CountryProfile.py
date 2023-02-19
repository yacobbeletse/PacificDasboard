
from turtle import color
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

pillars = ["Availability","Accessibility","Utilization","Stability"]
aspects = ["Exposure","Capacity"]

# st.sidebar.title("Control Center")ff
typology = pd.read_csv("Typology.csv")
alldata1 = pd.read_csv("Data1.csv")

countries = alldata1["Country"].dropna().unique()
# print(countries)
# print("Coutnry = "+str(len(countries)))


flags = {
   'Afghanistan': 'af', 'Albania': 'al', 'Algeria': 'dz', 'American Samoa': 'as', 'Andorra': 'ad', 'Angola': 'ao', 'Anguilla': 'ai', 'Antarctica': 'aq', 'Antigua and Barbuda': 'ag', 'Argentina': 'ar', 'Armenia': 'am', 'Aruba': 'aw', 'Australia': 'au', 'Austria': 'at', 'Azerbaijan': 'az', 'Bahamas': 'bs', 'Bahrain': 'bh', 'Bangladesh': 'bd', 'Barbados': 'bb', 'Belarus': 'by', 'Belgium': 'be', 'Belize': 'bz', 'Benin': 'bj', 'Bermuda': 'bm', 'Bhutan': 'bt', 'Bolivia, Plurinational State of': 'bo', 'Bolivia': 'bo', 'Bosnia and Herzegovina': 'ba', 'Botswana': 'bw', 'Bouvet Island': 'bv', 'Brazil': 'br', 'British Indian Ocean Territory': 'io', 'Brunei Darussalam': 'bn', 'Brunei': 'bn', 'Bulgaria': 'bg', 'Burkina Faso': 'bf', 'Burundi': 'bi', 'Cambodia': 'kh', 'Cameroon': 'cm', 'Canada': 'ca', 'Cape Verde': 'cv', 'Cayman Islands': 'ky', 'Central African Republic': 'cf', 'Chad': 'td', 'Chile': 'cl', 'China': 'cn', 'Christmas Island': 'cx', 'Cocos (Keeling) Islands': 'cc', 'Colombia': 'co', 'Comoros': 'km', 'Congo': 'cg', 'DR Congo':'cd','Congo, the Democratic Republic of the': 'cd', 'Cook Islands': 'ck', 'Costa Rica': 'cr', "Côte d'Ivoire": 'ci', 'Ivory Coast': 'ci', 'Croatia': 'hr', 'Cuba': 'cu', 'Cyprus': 'cy', 'Czech Republic': 'cz', 'Denmark': 'dk', 'Djibouti': 'dj', 'Dominica': 'dm', 'Dominican Republic': 'do', 'Ecuador': 'ec', 'Egypt': 'eg', 'El Salvador': 'sv', 'Equatorial Guinea': 'gq', 'Eritrea': 'er', 'Estonia': 'ee', 'Ethiopia': 'et', 'Falkland Islands (Malvinas)': 'fk', 'Faroe Islands': 'fo', 'Fiji': 'fj', 'Finland': 'fi', 'France': 'fr', 'French Guiana': 'gf', 'French Polynesia': 'pf', 'French Southern Territories': 'tf', 'Gabon': 'ga', 'Gambia': 'gm', 'Georgia': 'ge', 'Germany': 'de', 'Ghana': 'gh', 'Gibraltar': 'gi', 'Greece': 'gr', 'Greenland': 'gl', 'Grenada': 'gd', 'Guadeloupe': 'gp', 'Guam': 'gu', 'Guatemala': 'gt', 'Guernsey': 'gg', 'Guinea': 'gn', 'Guinea-Bissau': 'gw', 'Guyana': 'gy', 'Haiti': 'ht', 'Heard Island and McDonald Islands': 'hm', 'Holy See (Vatican City State)': 'va', 'Honduras': 'hn', 'Hong Kong': 'hk', 'Hungary': 'hu', 'Iceland': 'is', 'India': 'in', 'Indonesia': 'id', 'Iran, Islamic Republic of': 'ir', 'Iraq': 'iq', 'Ireland': 'ie', 'Isle of Man': 'im', 'Israel': 'il', 'Italy': 'it', 'Jamaica': 'jm', 'Japan': 'jp', 'Jersey': 'je', 'Jordan': 'jo', 'Kazakhstan': 'kz', 'Kenya': 'ke', 'Kiribati': 'ki', "Korea, Democratic People's Republic of": 'kp', 'Korea, Republic of': 'kr', 'South Korea': 'kr', 'Kuwait': 'kw', 'Kyrgyzstan': 'kg', "Lao People's Democratic Republic": 'la', 'Latvia': 'lv', 'Lebanon': 'lb', 'Lesotho': 'ls', 'Liberia': 'lr', 'Libyan Arab Jamahiriya': 'ly', 'Libya': 'ly', 'Liechtenstein': 'li', 'Lithuania': 'lt', 'Luxembourg': 'lu', 'Macao': 'mo', 'Macedonia, the former Yugoslav Republic of': 'mk', 'Madagascar': 'mg', 'Malawi': 'mw', 'Malaysia': 'my', 'Maldives': 'mv', 'Mali': 'ml', 'Malta': 'mt', 'Marshall Islands': 'mh', 'Martinique': 'mq', 'Mauritania': 'mr', 'Mauritius': 'mu', 'Mayotte': 'yt', 'Mexico': 'mx', 'Micronesia, Federated States of': 'fm', 'Moldova, Republic of': 'md', 'Monaco': 'mc', 'Mongolia': 'mn', 'Montenegro': 'me', 'Montserrat': 'ms', 'Morocco': 'ma', 'Mozambique': 'mz', 'Myanmar': 'mm', 'Burma': 'mm', 'Namibia': 'na', 'Nauru': 'nr', 'Nepal': 'np', 'Netherlands': 'nl', 'Netherlands Antilles': 'an', 'New Caledonia': 'nc', 'New Zealand': 'nz', 'Nicaragua': 'ni', 'Niger': 'ne', 'Nigeria': 'ng', 'Niue': 'nu', 'Norfolk Island': 'nf', 'Northern Mariana Islands': 'mp', 'Norway': 'no', 'Oman': 'om', 'Pakistan': 'pk', 'Palau': 'pw', 'Palestinian Territory, Occupied': 'ps', 'Panama': 'pa', 'Papua New Guinea': 'pg', 'Paraguay': 'py', 'Peru': 'pe', 'Philippines': 'ph', 'Pitcairn': 'pn', 'Poland': 'pl', 'Portugal': 'pt', 'Puerto Rico': 'pr', 'Qatar': 'qa', 'Réunion': 're', 'Romania': 'ro', 'Russian Federation': 'ru', 'Russia': 'ru', 'Rwanda': 'rw', 'Saint Helena, Ascension and Tristan da Cunha': 'sh', 'Saint Kitts and Nevis': 'kn', 'Saint Lucia': 'lc', 'Saint Pierre and Miquelon': 'pm', 'Saint Vincent and the Grenadines': 'vc', 'Saint Vincent & the Grenadines': 'vc', 'St. Vincent and the Grenadines': 'vc', 'Samoa': 'ws', 'San Marino': 'sm', 'Sao Tome and Principe': 'st', 'Saudi Arabia': 'sa', 'Senegal': 'sn', 'Serbia': 'rs', 'Seychelles': 'sc', 'Sierra Leone': 'sl', 'Singapore': 'sg', 'Slovakia': 'sk', 'Slovenia': 'si', 'Solomon Islands': 'sb', 'Somalia': 'so', 'South Africa': 'za', 'South Georgia and the South Sandwich Islands': 'gs', 'South Sudan': 'ss', 'Spain': 'es', 'Sri Lanka': 'lk', 'Sudan': 'sd', 'Suriname': 'sr', 'Svalbard and Jan Mayen': 'sj', 'Swaziland': 'sz', 'Sweden': 'se', 'Switzerland': 'ch', 'Syrian Arab Republic': 'sy', 'Taiwan, Province of China': 'tw', 'Taiwan': 'tw', 'Tajikistan': 'tj', 'Tanzania': 'tz', 'Thailand': 'th', 'Timor-Leste': 'tl', 'Togo': 'tg', 'Tokelau': 'tk', 'Tonga': 'to', 'Trinidad and Tobago': 'tt', 'Tunisia': 'tn', 'Turkey': 'tr', 'Turkmenistan': 'tm', 'Turks and Caicos Islands': 'tc', 'Tuvalu': 'tv', 'Uganda': 'ug', 'Ukraine': 'ua', 'United Arab Emirates': 'ae', 'United Kingdom': 'gb', 'United States': 'us', 'United States of America':'us','United States Minor Outlying Islands': 'um', 'Uruguay': 'uy', 'Uzbekistan': 'uz', 'Vanuatu': 'vu', 'Venezuela, Bolivarian Republic of': 've', 'Venezuela': 've', 'Viet Nam': 'vn', 'Vietnam': 'vn', 'Virgin Islands, British': 'vg', 'Virgin Islands, U.S.': 'vi', 'Wallis and Futuna': 'wf', 'Western Sahara': 'eh', 'Yemen': 'ye', 'Zambia': 'zm', 'Zimbabwe': 'zw'
   }



def linePlot(df,c,width = False):
    # print(df.head())
    #function to visualize lineplot.
    if not df.empty:
        # print(df)
        fig = px.line(df,x="Year",y="Value",color = "Country",markers=True,symbol="Country")
        fig.update_layout(
        # yaxis_range=[0,100],
        # yaxis_title="Score",
        yaxis_title=None,
        xaxis_title = None,
        xaxis_tickformat = 'd',
    font=dict(
        family="Arial Black",
        size=12,
    ),
    legend = dict(
        orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1,
    title = None
    )
    )
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
        c.plotly_chart(fig,use_container_width = width)


def wrap_long_text(text):
    words = text.split(" ")
    line1 = ""
    line2 = ""
    line3 = ""
    for word in words:
        if len(line1) + len(word) < 20:
            line1 += word + " "
        else:
            if len(line2) + len(word) < 20:
                line2 += word + " "
            else:
                line3+= word+" "
    return line1 + "<br>" + line2 + "<br>" + line3




def visualizeOp(df,country):
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
        
    # print(df)
    # country = data["Country"].unique()[0]
    country_data = df[df["Country"]==country]
    # print(country_data)
    # data = df.copy()
    # data["Color"] = "gray"
    # print(data)
    present = country_data.dropna(subset = "Value").sort_values("Year").drop_duplicates(["Country", "Indicator"], keep = "last")
    present_rad = df.dropna(subset = "Value").sort_values("Year").drop_duplicates(["Country", "Indicator"], keep = "last")
    # print("************RAD DATA************")
    # print(present_rad)
    # print(present)
    try:
        st.image("Con_Flags/"+flags[country]+".png",width=100)
        st.subheader(str.upper(country))
    except:
        st.subheader(str.upper(country))

    style_text=""
    for i in range(4):
        colors = ['red','yellow','green','gray']
        legend = ['Weak ' , 'Fine ', 'Excellent', 'Data Missing']
        style_text+= "<div><div class='rectangle {}'></div> {}</div>".format(colors[i],legend[i])
    st.sidebar.markdown(style_text,unsafe_allow_html=True)
    st.sidebar.subheader("INDICATORS")
    
    for i in range(len(pillars)):
        color_discrete_map= {country:"red", "Pacific":"blue"}
        
        # st.sidebar.header(pillars[i])
        st.header(pillars[i])
        showhide = st.checkbox("Show Trends for Indicators!",key = i)
        temp = df[df["Pillar"]==pillars[i]].dropna(subset = "Value")
        rad_data = present_rad[present_rad["Pillar"]==pillars[i]]
        rad_data.loc[rad_data["Indicator"]=="Agriculture orientation Index for Government Expenditures","Value"]*=100
        # print(rad_data[["Country","Indicator","Value"]])

        c = st.columns(len(rad_data["Aspect"].unique()))
        # cat_order = None
        # if pillars[i]=="Stability":
        #     cat_order = ["Control of Corruption","Reulatory Quality","Rule of Law", "score for adoption and implementation of disaster reduction strategies", "Voice and Accountability"]
        # t_fig=None


        for k in range(len(aspects)):
            bac =rad_data[rad_data["Aspect"]==aspects[k]].sort_values("Indicator").sort_values("Country",ascending=False)
            print(bac[["Country","Indicator","Value"]])
            if len(bac[bac["Country"]==country]["Indicator"].unique())<3:
            # t_fig = px.bar_polar(rad_data[rad_data["Aspect"]==aspects[k]],r = "Value",theta="Indicator", color = "Country",line_close=True)
                t_fig = px.bar_polar(bac,r = "Value",theta="Indicator", color = "Country",color_discrete_map=color_discrete_map)
            else:
                t_fig = px.line_polar(bac,r = "Value",theta="Indicator",color = "Country",color_discrete_map=color_discrete_map,line_close=True,line_shape = 'spline')
            # t_fig.update_yaxes(tickangle=90)
                t_fig.update_traces(fill='toself')
            t_fig.update_layout(
                font=dict(
        family="Arial Black",
        size=12
    ),
    polar=dict(
        angularaxis=dict(
            ticktext=[wrap_long_text(text) for text in bac["Indicator"]],
            tickvals=bac["Indicator"]
        )
    )
            )
            # t_fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')

            c[k].plotly_chart(t_fig)
        # st.plotly_chart(fig1)
        # print(temp)
        # print(temp["Indicator"].dropna().unique())
        # print(temp["Country"].unique())
        if showhide:
            st.sidebar.header(pillars[i])
            for j in temp["Indicator"].unique():
                # st.header(j)
                present_df = present[present["Indicator"]==j]
                # print(present_df["Color"])
                presentValue = 'NA'
                color = ''
                try:
                    color = present_df['Color'].iloc[0]
                    presentValue = present_df['Value'].iloc[0]
                except:
                    color = 'gray'
                    presentValue = 'NA'

                st.subheader(j,anchor=j.replace(' ',''))
                st.write(typology[typology["Indicator"]==j]["About"].iloc[0])
                anchor_text="<div><div class = 'rectangle {}'></div><a href = '#{}'>{}</div> <br>".format(color,j.replace(' ',''),j)
                # print(anchor_text)
                
                st.text('Unit: {}'.format(temp[temp["Indicator"]==j]['Unit'].iloc[0]))
                st.text('Value: {}'.format(presentValue))
                linePlot(temp[temp["Indicator"]==j],st)
                st.sidebar.markdown(anchor_text,unsafe_allow_html=True)


def app():
    country = st.sidebar.selectbox("Select a Country:",countries)
    choice = ["Exposure","Capacity"]
    if st.sidebar.checkbox("Visualization by Aspect",value=False):
        choice1 = st.sidebar.selectbox("Visualization by:",["Exposure","Capacity"])
        choice = choice1.split()
        # print(choice)
    df = alldata1.merge(typology, on = "Indicator", how = "left")
    df =df[df["Country"].isin(["Pacific",country])]
    # print(df.head())
    visualizeOp(df[df["Aspect"].isin(choice)],country)

