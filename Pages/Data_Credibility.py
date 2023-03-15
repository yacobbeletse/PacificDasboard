import streamlit as st
import pandas as pd
import numpy as np
from Pages.Home import alldata1,typology
import plotly.express as px




pillars = ["Overall","Availability", "Accessibility","Utilization","Stability"]
aspects = ["Mitigator", "Amplifier"]

trend = ["Availability trend", "Accessibility trend", "Utilization trend"]

countries = alldata1["Country"].dropna().unique()
countries = np.insert(countries,0,"Overall")
flags = {
   'Afghanistan': 'af', 'Albania': 'al', 'Algeria': 'dz', 'American Samoa': 'as', 'Andorra': 'ad', 'Angola': 'ao', 'Anguilla': 'ai', 'Antarctica': 'aq', 'Antigua and Barbuda': 'ag', 'Argentina': 'ar', 'Armenia': 'am', 'Aruba': 'aw', 'Australia': 'au', 'Austria': 'at', 'Azerbaijan': 'az', 'Bahamas': 'bs', 'Bahrain': 'bh', 'Bangladesh': 'bd', 'Barbados': 'bb', 'Belarus': 'by', 'Belgium': 'be', 'Belize': 'bz', 'Benin': 'bj', 'Bermuda': 'bm', 'Bhutan': 'bt', 'Bolivia, Plurinational State of': 'bo', 'Bolivia': 'bo', 'Bosnia and Herzegovina': 'ba', 'Botswana': 'bw', 'Bouvet Island': 'bv', 'Brazil': 'br', 'British Indian Ocean Territory': 'io', 'Brunei Darussalam': 'bn', 'Brunei': 'bn', 'Bulgaria': 'bg', 'Burkina Faso': 'bf', 'Burundi': 'bi', 'Cambodia': 'kh', 'Cameroon': 'cm', 'Canada': 'ca', 'Cape Verde': 'cv', 'Cayman Islands': 'ky', 'Central African Republic': 'cf', 'Chad': 'td', 'Chile': 'cl', 'China': 'cn', 'Christmas Island': 'cx', 'Cocos (Keeling) Islands': 'cc', 'Colombia': 'co', 'Comoros': 'km', 'Congo': 'cg', 'DR Congo':'cd','Congo, the Democratic Republic of the': 'cd', 'Cook Islands': 'ck', 'Costa Rica': 'cr', "Côte d'Ivoire": 'ci', 'Ivory Coast': 'ci', 'Croatia': 'hr', 'Cuba': 'cu', 'Cyprus': 'cy', 'Czech Republic': 'cz', 'Denmark': 'dk', 'Djibouti': 'dj', 'Dominica': 'dm', 'Dominican Republic': 'do', 'Ecuador': 'ec', 'Egypt': 'eg', 'El Salvador': 'sv', 'Equatorial Guinea': 'gq', 'Eritrea': 'er', 'Estonia': 'ee', 'Ethiopia': 'et', 'Falkland Islands (Malvinas)': 'fk', 'Faroe Islands': 'fo', 'Fiji': 'fj', 'Finland': 'fi', 'France': 'fr', 'French Guiana': 'gf', 'French Polynesia': 'pf', 'French Southern Territories': 'tf', 'Gabon': 'ga', 'Gambia': 'gm', 'Georgia': 'ge', 'Germany': 'de', 'Ghana': 'gh', 'Gibraltar': 'gi', 'Greece': 'gr', 'Greenland': 'gl', 'Grenada': 'gd', 'Guadeloupe': 'gp', 'Guam': 'gu', 'Guatemala': 'gt', 'Guernsey': 'gg', 'Guinea': 'gn', 'Guinea-Bissau': 'gw', 'Guyana': 'gy', 'Haiti': 'ht', 'Heard Island and McDonald Islands': 'hm', 'Holy See (Vatican City State)': 'va', 'Honduras': 'hn', 'Hong Kong': 'hk', 'Hungary': 'hu', 'Iceland': 'is', 'India': 'in', 'Indonesia': 'id', 'Iran, Islamic Republic of': 'ir', 'Iraq': 'iq', 'Ireland': 'ie', 'Isle of Man': 'im', 'Israel': 'il', 'Italy': 'it', 'Jamaica': 'jm', 'Japan': 'jp', 'Jersey': 'je', 'Jordan': 'jo', 'Kazakhstan': 'kz', 'Kenya': 'ke', 'Kiribati': 'ki', "Korea, Democratic People's Republic of": 'kp', 'Korea, Republic of': 'kr', 'South Korea': 'kr', 'Kuwait': 'kw', 'Kyrgyzstan': 'kg', "Lao People's Democratic Republic": 'la', 'Latvia': 'lv', 'Lebanon': 'lb', 'Lesotho': 'ls', 'Liberia': 'lr', 'Libyan Arab Jamahiriya': 'ly', 'Libya': 'ly', 'Liechtenstein': 'li', 'Lithuania': 'lt', 'Luxembourg': 'lu', 'Macao': 'mo', 'Macedonia, the former Yugoslav Republic of': 'mk', 'Madagascar': 'mg', 'Malawi': 'mw', 'Malaysia': 'my', 'Maldives': 'mv', 'Mali': 'ml', 'Malta': 'mt', 'Marshall Islands': 'mh', 'Martinique': 'mq', 'Mauritania': 'mr', 'Mauritius': 'mu', 'Mayotte': 'yt', 'Mexico': 'mx', 'Micronesia, Federated States of': 'fm', 'Moldova, Republic of': 'md', 'Monaco': 'mc', 'Mongolia': 'mn', 'Montenegro': 'me', 'Montserrat': 'ms', 'Morocco': 'ma', 'Mozambique': 'mz', 'Myanmar': 'mm', 'Burma': 'mm', 'Namibia': 'na', 'Nauru': 'nr', 'Nepal': 'np', 'Netherlands': 'nl', 'Netherlands Antilles': 'an', 'New Caledonia': 'nc', 'New Zealand': 'nz', 'Nicaragua': 'ni', 'Niger': 'ne', 'Nigeria': 'ng', 'Niue': 'nu', 'Norfolk Island': 'nf', 'Northern Mariana Islands': 'mp', 'Norway': 'no', 'Oman': 'om', 'Pakistan': 'pk', 'Palau': 'pw', 'Palestinian Territory, Occupied': 'ps', 'Panama': 'pa', 'Papua New Guinea': 'pg', 'Paraguay': 'py', 'Peru': 'pe', 'Philippines': 'ph', 'Pitcairn': 'pn', 'Poland': 'pl', 'Portugal': 'pt', 'Puerto Rico': 'pr', 'Qatar': 'qa', 'Réunion': 're', 'Romania': 'ro', 'Russian Federation': 'ru', 'Russia': 'ru', 'Rwanda': 'rw', 'Saint Helena, Ascension and Tristan da Cunha': 'sh', 'Saint Kitts and Nevis': 'kn', 'Saint Lucia': 'lc', 'Saint Pierre and Miquelon': 'pm', 'Saint Vincent and the Grenadines': 'vc', 'Saint Vincent & the Grenadines': 'vc', 'St. Vincent and the Grenadines': 'vc', 'Samoa': 'ws', 'San Marino': 'sm', 'Sao Tome and Principe': 'st', 'Saudi Arabia': 'sa', 'Senegal': 'sn', 'Serbia': 'rs', 'Seychelles': 'sc', 'Sierra Leone': 'sl', 'Singapore': 'sg', 'Slovakia': 'sk', 'Slovenia': 'si', 'Solomon Islands': 'sb', 'Somalia': 'so', 'South Africa': 'za', 'South Georgia and the South Sandwich Islands': 'gs', 'South Sudan': 'ss', 'Spain': 'es', 'Sri Lanka': 'lk', 'Sudan': 'sd', 'Suriname': 'sr', 'Svalbard and Jan Mayen': 'sj', 'Swaziland': 'sz', 'Sweden': 'se', 'Switzerland': 'ch', 'Syrian Arab Republic': 'sy', 'Taiwan, Province of China': 'tw', 'Taiwan': 'tw', 'Tajikistan': 'tj', 'Tanzania': 'tz', 'Thailand': 'th', 'Timor-Leste': 'tl', 'Togo': 'tg', 'Tokelau': 'tk', 'Tonga': 'to', 'Trinidad and Tobago': 'tt', 'Tunisia': 'tn', 'Turkey': 'tr', 'Turkmenistan': 'tm', 'Turks and Caicos Islands': 'tc', 'Tuvalu': 'tv', 'Uganda': 'ug', 'Ukraine': 'ua', 'United Arab Emirates': 'ae', 'United Kingdom': 'gb', 'United States': 'us', 'United States of America':'us','United States Minor Outlying Islands': 'um', 'Uruguay': 'uy', 'Uzbekistan': 'uz', 'Vanuatu': 'vu', 'Venezuela, Bolivarian Republic of': 've', 'Venezuela': 've', 'Viet Nam': 'vn', 'Vietnam': 'vn', 'Virgin Islands, British': 'vg', 'Virgin Islands, U.S.': 'vi', 'Wallis and Futuna': 'wf', 'Western Sahara': 'eh', 'Yemen': 'ye', 'Zambia': 'zm', 'Zimbabwe': 'zw'
   }

def legend(c):
    with open('style.css') as f:
        c.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
    style_text=""
    for i in range(2):
        colors = ['red','green']
        legend = ['Amplifier' , 'Mitigator']
        style_text+= "<div><div class='rectangle {}'></div> {}</div>".format(colors[i],legend[i])

    c.subheader("STATUS")
    c.markdown(style_text,unsafe_allow_html=True)

def app():
    info = {"red":"Amplifier","green":"Mitigator", "gray":"Data Missing"}
    color = {"Amplifier":"red", "Mitigator":"green","Data Missing":"gray"}
    choice = st.sidebar.selectbox("Data Check by: ", ["Country","Indicator"])
    data_temp = alldata1.merge(typology, on = "Indicator", how = 'right')
    
    if choice=="Country":
        country = st.sidebar.selectbox("Country: ", countries)
        # df = alldata1[alldata1['Country']==country].drop_duplicates(["Country","Indicator"],keep='last').drop(columns = ["value","Income Group","Region"])
        if country=='Overall':
            df = data_temp.dropna(subset=["Value"]).drop_duplicates(["Country","Indicator"],keep='last')
            df["Status"] = df["Color"].map(info)
            # print(df.columns)
            df_count1 = df.groupby(["Country","Status"])["Value"].count().reset_index()
            print(df_count1)

            df_total = df.groupby("Country").agg(Total = ("Value",'count')).reset_index(0)
            df_count = df_count1.merge(df_total, on ="Country", how = "left")
            print(df_total)
            fig = px.bar(df_count.sort_values('Total'), x = "Value", y = "Country", text = "Value",color = "Status",color_discrete_map  = color,custom_data=["Country","Value"], orientation = "h")
            fig.update_yaxes(title = '')
            fig.update_xaxes(title = 'Indicators Covered')
            fig.update_traces(hovertemplate='<b>%{customdata[0]}</b> <br>Indicators Countries: %{customdata[1]:.2f}')
    
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',height = 700)
            fig.update_layout(
                        font=dict(
                        family="Arial Black",
                        size=11
                    ),
                    )
            fig.update_traces(textposition='inside')
            st.plotly_chart(fig)
        else:

            df = data_temp.dropna(subset=["Value"])[data_temp['Country']==country].drop_duplicates(["Country","Indicator"],keep='last')
            df["Status"] = df["Color"].map(info)
            # print(df["Indicator"].unique())
            # print(df)

            # print(df.columns)
        
            # df = alldata1.dropna()[alldata1['Country']==country].drop_duplicates(["Country","Indicator"],keep='last').drop(columns = ["Income Group","Region"])
            # print(df)
            try:
                st.image("Con_Flags/"+flags[country]+".png",width=100)
                st.subheader(str.upper(country))
            except:
                st.subheader(str.upper(country))
            # print(df["Indicator"].unique())
            st.subheader("Available Indicators: "+ str(len(df["Indicator"].unique())))
            st.write("Note: The trend indicators for the first three pillars - availability, accessibility, and utilization are derived indicators and are available only for one year.")
            
            
            for i in pillars:
                if i!="Overall":
                    st.header(i.upper())
                    temp = df[df["Pillar"]==i].dropna(subset=["Value"])
                    # print(temp)
                    # temp["Year"] = temp["Year"].astype('int')
                    if temp.empty:
                        st.write("No data for {}".format(i))
                    else:
                        c = st.columns(len(aspects))
                        for k in range(len(aspects)):
                            c[k].subheader(aspects[k])
                            data_fd = temp[temp["Status"]==aspects[k]]
                            if data_fd.empty:
                                c[k].write("No data for {}".format(aspects[k]))
                            else:
                                for j in data_fd["Indicator"].unique():
                                    data_df = data_fd[data_fd["Indicator"]==j]
                                    if data_df.empty:
                                        c[k].write("No data for {}".format(j))
                                    else:
                                        if j in trend:
                                            c[k].write(j)
                                        else:
                                            c[k].write(j+', '+str(temp[temp["Indicator"]==j]["Year"].iloc[0]))

        
    else:
        pillar = st.sidebar.selectbox('Pillar',pillars)
        if pillar=='Overall':
            df = data_temp.dropna(subset= "Value").drop_duplicates(["Country","Indicator"],keep='last')
            df =df[df["Country"]!="Pacific"]
            df["Status"] = df["Color"].map(info)
            # print(df.columns)
            df_count1 = df.groupby(["Indicator","Status"])["Value"].count().reset_index()
            # print(df_count1)

            df_total = df.groupby("Indicator").agg(Total = ("Value",'count')).reset_index()
            df_count = df_count1.merge(df_total, on ="Indicator", how = "left")
            print(df_count.sort_values('Total',ascending=False))
            # df_count = df.groupby("Indicator")["Value"].count().reset_index()
            # df_count['Value'] = df_count['Value']-1
            #-1 done to discount Pacific as a county
            fig = px.bar(df_count.sort_values('Total'), x = "Value", y = "Indicator", color = "Status", color_discrete_map  = color,text = "Value",custom_data=["Indicator","Value"], orientation = "h")
            fig.update_yaxes(title = '')
            fig.update_xaxes(title = 'Contries Covered')
            fig.update_traces(hovertemplate='<b>%{customdata[0]}</b> <br>Covered Countries: %{customdata[1]:.0f}')
    
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',height = 700,width = 1000,legend_title_text="#Countries with indicator status")
            fig.update_layout(
                        font=dict(
                        family="Arial Black",
                        size=11
                    ),
                    )
            fig.update_traces(textposition='inside')
            st.plotly_chart(fig)
        else:

            # aspect = st.sidebar.selectbox('Miti',data_temp["Aspect"].unique())
            indicator = st.sidebar.selectbox("Indicator", data_temp[(data_temp["Pillar"]==pillar)]["Indicator"].dropna().unique())
            # df = data_temp[(data_temp["Pillar"]==pillar) & (data_temp["Aspect"]==aspect)& (data_temp["Indicator"]==indicator)]
            df = data_temp[(data_temp["Indicator"]==indicator)]
            # print(df)
            # print(data_temp["Indicator"].unique())
            st.header(indicator)
            st.write(df['About'].iloc[0])
            st.subheader('Unit: {}'.format(df["Unit"].iloc[0]))
            st.markdown("<h3> Source: <a href ='{}'>{}</h1>".format(df["Link"].iloc[0], df["Source"].iloc[0]),unsafe_allow_html=True)
            st.subheader("Countries covered: {}".format(len(df.dropna(subset = "Value")["Country"].unique())-1))
            data = df.dropna(subset= "Value").drop_duplicates(["Country","Indicator"],keep='last')
            if indicator not in trend:
                data["Year"] = data["Year"].astype('int')
            c1,c2 = st.columns([1,1.5])
            for i in data["Country"].dropna().unique():
                if i!="Pacific":
                    c1.write(i + ", Latest Data Available: " + str(data[data["Country"]==i]["Year"].iloc[0]) )
            # print(data.columns)
            legend(c2)
            # fig = px.box(data, y = "Value", points="all", custom_data=["Country","Value"], color = "Color",color_discrete_map=info)
            print(data["Color"])
            fig = px.bar(data[data["Country"]!="Pacific"].sort_values("Value"), x = "Value", y = "Country", custom_data=["Country","Value"], orientation = "h",color = "Color",color_discrete_map={'red':'red','green':'green'})
            
            fig.add_vline(x=data[data["Country"]=="Pacific"]["Value"].iloc[0],line_dash="dash",annotation_text="{} (Pacific Average)".format(np.round(data[data["Country"]=="Pacific"]["Value"].iloc[0],2)),annotation_position = "bottom right")
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
            fig.update_layout(
                        font=dict(
                        family="Arial Black",
                        size=11
                    ),
                    showlegend = False)
            fig.update_yaxes(title = '')
            fig.update_traces(hovertemplate='<b>%{customdata[0]}</b> <br>Value: %{customdata[1]:.2f}')
        

            c2.plotly_chart(fig)



    



