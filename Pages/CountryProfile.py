
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from Pages.Home import alldata1,typology

pillars = ["Availability","Accessibility","Utilization","Stability"]
aspects = ["Mitigator","Amplifier"]
trend = ["Availability trend", "Accessibility trend", "Utilization trend"]

# st.sidebar.title("Control Center")ff
# typology = pd.read_csv("Typology.csv")
# alldata1 = pd.read_csv("Data1.csv")

countries = alldata1["Country"].dropna().unique()
# print(countries)
# print("Coutnry = "+str(len(countries)))


flags = {
   'Afghanistan': 'af', 'Albania': 'al', 'Algeria': 'dz', 'American Samoa': 'as', 'Andorra': 'ad', 'Angola': 'ao', 'Anguilla': 'ai', 'Antarctica': 'aq', 'Antigua and Barbuda': 'ag', 'Argentina': 'ar', 'Armenia': 'am', 'Aruba': 'aw', 'Australia': 'au', 'Austria': 'at', 'Azerbaijan': 'az', 'Bahamas': 'bs', 'Bahrain': 'bh', 'Bangladesh': 'bd', 'Barbados': 'bb', 'Belarus': 'by', 'Belgium': 'be', 'Belize': 'bz', 'Benin': 'bj', 'Bermuda': 'bm', 'Bhutan': 'bt', 'Bolivia, Plurinational State of': 'bo', 'Bolivia': 'bo', 'Bosnia and Herzegovina': 'ba', 'Botswana': 'bw', 'Bouvet Island': 'bv', 'Brazil': 'br', 'British Indian Ocean Territory': 'io', 'Brunei Darussalam': 'bn', 'Brunei': 'bn', 'Bulgaria': 'bg', 'Burkina Faso': 'bf', 'Burundi': 'bi', 'Cambodia': 'kh', 'Cameroon': 'cm', 'Canada': 'ca', 'Cape Verde': 'cv', 'Cayman Islands': 'ky', 'Central African Republic': 'cf', 'Chad': 'td', 'Chile': 'cl', 'China': 'cn', 'Christmas Island': 'cx', 'Cocos (Keeling) Islands': 'cc', 'Colombia': 'co', 'Comoros': 'km', 'Congo': 'cg', 'DR Congo':'cd','Congo, the Democratic Republic of the': 'cd', 'Cook Islands': 'ck', 'Costa Rica': 'cr', "Côte d'Ivoire": 'ci', 'Ivory Coast': 'ci', 'Croatia': 'hr', 'Cuba': 'cu', 'Cyprus': 'cy', 'Czech Republic': 'cz', 'Denmark': 'dk', 'Djibouti': 'dj', 'Dominica': 'dm', 'Dominican Republic': 'do', 'Ecuador': 'ec', 'Egypt': 'eg', 'El Salvador': 'sv', 'Equatorial Guinea': 'gq', 'Eritrea': 'er', 'Estonia': 'ee', 'Ethiopia': 'et', 'Falkland Islands (Malvinas)': 'fk', 'Faroe Islands': 'fo', 'Fiji': 'fj', 'Finland': 'fi', 'France': 'fr', 'French Guiana': 'gf', 'French Polynesia': 'pf', 'French Southern Territories': 'tf', 'Gabon': 'ga', 'Gambia': 'gm', 'Georgia': 'ge', 'Germany': 'de', 'Ghana': 'gh', 'Gibraltar': 'gi', 'Greece': 'gr', 'Greenland': 'gl', 'Grenada': 'gd', 'Guadeloupe': 'gp', 'Guam': 'gu', 'Guatemala': 'gt', 'Guernsey': 'gg', 'Guinea': 'gn', 'Guinea-Bissau': 'gw', 'Guyana': 'gy', 'Haiti': 'ht', 'Heard Island and McDonald Islands': 'hm', 'Holy See (Vatican City State)': 'va', 'Honduras': 'hn', 'Hong Kong': 'hk', 'Hungary': 'hu', 'Iceland': 'is', 'India': 'in', 'Indonesia': 'id', 'Iran, Islamic Republic of': 'ir', 'Iraq': 'iq', 'Ireland': 'ie', 'Isle of Man': 'im', 'Israel': 'il', 'Italy': 'it', 'Jamaica': 'jm', 'Japan': 'jp', 'Jersey': 'je', 'Jordan': 'jo', 'Kazakhstan': 'kz', 'Kenya': 'ke', 'Kiribati': 'ki', "Korea, Democratic People's Republic of": 'kp', 'Korea, Republic of': 'kr', 'South Korea': 'kr', 'Kuwait': 'kw', 'Kyrgyzstan': 'kg', "Lao People's Democratic Republic": 'la', 'Latvia': 'lv', 'Lebanon': 'lb', 'Lesotho': 'ls', 'Liberia': 'lr', 'Libyan Arab Jamahiriya': 'ly', 'Libya': 'ly', 'Liechtenstein': 'li', 'Lithuania': 'lt', 'Luxembourg': 'lu', 'Macao': 'mo', 'Macedonia, the former Yugoslav Republic of': 'mk', 'Madagascar': 'mg', 'Malawi': 'mw', 'Malaysia': 'my', 'Maldives': 'mv', 'Mali': 'ml', 'Malta': 'mt', 'Marshall Islands': 'mh', 'Martinique': 'mq', 'Mauritania': 'mr', 'Mauritius': 'mu', 'Mayotte': 'yt', 'Mexico': 'mx', 'Micronesia, Federated States of': 'fm', 'Moldova, Republic of': 'md', 'Monaco': 'mc', 'Mongolia': 'mn', 'Montenegro': 'me', 'Montserrat': 'ms', 'Morocco': 'ma', 'Mozambique': 'mz', 'Myanmar': 'mm', 'Burma': 'mm', 'Namibia': 'na', 'Nauru': 'nr', 'Nepal': 'np', 'Netherlands': 'nl', 'Netherlands Antilles': 'an', 'New Caledonia': 'nc', 'New Zealand': 'nz', 'Nicaragua': 'ni', 'Niger': 'ne', 'Nigeria': 'ng', 'Niue': 'nu', 'Norfolk Island': 'nf', 'Northern Mariana Islands': 'mp', 'Norway': 'no', 'Oman': 'om', 'Pakistan': 'pk', 'Palau': 'pw', 'Palestinian Territory, Occupied': 'ps', 'Panama': 'pa', 'Papua New Guinea': 'pg', 'Paraguay': 'py', 'Peru': 'pe', 'Philippines': 'ph', 'Pitcairn': 'pn', 'Poland': 'pl', 'Portugal': 'pt', 'Puerto Rico': 'pr', 'Qatar': 'qa', 'Réunion': 're', 'Romania': 'ro', 'Russian Federation': 'ru', 'Russia': 'ru', 'Rwanda': 'rw', 'Saint Helena, Ascension and Tristan da Cunha': 'sh', 'Saint Kitts and Nevis': 'kn', 'Saint Lucia': 'lc', 'Saint Pierre and Miquelon': 'pm', 'Saint Vincent and the Grenadines': 'vc', 'Saint Vincent & the Grenadines': 'vc', 'St. Vincent and the Grenadines': 'vc', 'Samoa': 'ws', 'San Marino': 'sm', 'Sao Tome and Principe': 'st', 'Saudi Arabia': 'sa', 'Senegal': 'sn', 'Serbia': 'rs', 'Seychelles': 'sc', 'Sierra Leone': 'sl', 'Singapore': 'sg', 'Slovakia': 'sk', 'Slovenia': 'si', 'Solomon Islands': 'sb', 'Somalia': 'so', 'South Africa': 'za', 'South Georgia and the South Sandwich Islands': 'gs', 'South Sudan': 'ss', 'Spain': 'es', 'Sri Lanka': 'lk', 'Sudan': 'sd', 'Suriname': 'sr', 'Svalbard and Jan Mayen': 'sj', 'Swaziland': 'sz', 'Sweden': 'se', 'Switzerland': 'ch', 'Syrian Arab Republic': 'sy', 'Taiwan, Province of China': 'tw', 'Taiwan': 'tw', 'Tajikistan': 'tj', 'Tanzania': 'tz', 'Thailand': 'th', 'Timor-Leste': 'tl', 'Togo': 'tg', 'Tokelau': 'tk', 'Tonga': 'to', 'Trinidad and Tobago': 'tt', 'Tunisia': 'tn', 'Turkey': 'tr', 'Turkmenistan': 'tm', 'Turks and Caicos Islands': 'tc', 'Tuvalu': 'tv', 'Uganda': 'ug', 'Ukraine': 'ua', 'United Arab Emirates': 'ae', 'United Kingdom': 'gb', 'United States': 'us', 'United States of America':'us','United States Minor Outlying Islands': 'um', 'Uruguay': 'uy', 'Uzbekistan': 'uz', 'Vanuatu': 'vu', 'Venezuela, Bolivarian Republic of': 've', 'Venezuela': 've', 'Viet Nam': 'vn', 'Vietnam': 'vn', 'Virgin Islands, British': 'vg', 'Virgin Islands, U.S.': 'vi', 'Wallis and Futuna': 'wf', 'Western Sahara': 'eh', 'Yemen': 'ye', 'Zambia': 'zm', 'Zimbabwe': 'zw'
   }



def linePlot(df,c,width = False):
    print(df[["Country","Year","Indicator","Value","Baseline","UpDown"]])
    if df["Indicator"].iloc[0]!="Average protein supply":
        df["Baseline"] =df["Baseline"].astype(float)
    #function to visualize lineplot.
    if not df.empty:
        # print(df)
        fig = px.line(df,x="Year",y="Value",color_discrete_sequence =px.colors.qualitative.Antique,color = "Country",markers=True,symbol="Country")
        fig.add_hline(y=df["Baseline"].iloc[0], line_width=2, line_dash="dash", line_color="black")
        if (df["UpDown"].iloc[0]=="Down" and (df["Baseline"].iloc[0]<100 | width)):
            fig.add_hrect(y0=min(df["Value"].min(), df["Baseline"].iloc[0]), y1=df["Baseline"].iloc[0], line_width=0, fillcolor="green", opacity=0.1)
            fig.add_hrect(y0=df["Baseline"].iloc[0], y1=max(df["Value"].max(),df["Baseline"].iloc[0])*1.2, line_width=0, fillcolor="red", opacity=0.1)

            # fig.add_trace(
            # go.Scatter(
            #     x=[df["Year"].min(),df["Year"].max()], y=[df["Baseline"].iloc[0],df["Baseline"].iloc[0]], mode='lines',
            #     fill='tozeroy', line = dict(color='rgba(0,176,0,0.5)'),fillcolor='rgba(0, 176, 0, 0.2)',showlegend=False
            # )
            #     )
            # fig.add_trace(
            # go.Scatter(
            #     x=[df["Year"].min(),df["Year"].max()], y=[df["Baseline"].iloc[0],df["Baseline"].iloc[0]], mode='lines',
            #     fill='tozeroy', line = dict(color='rgba(176,0,0,0.5)'),fillcolor='rgba(176, 0, 0, 0.2)',showlegend=False
            # )
            #     )
        else:
            if width:
                fig.add_hrect(y0=min(df["Value"].min(), df["Baseline"].iloc[0]), y1=df["Baseline"].iloc[0], line_width=0, fillcolor="red", opacity=0.1)
                fig.add_hrect(y0=df["Baseline"].iloc[0], y1=max(df["Value"].max(),df["Baseline"].iloc[0])*1.2, line_width=0, fillcolor="green", opacity=0.1)

            else:
                if df["Indicator"].iloc[0]=="Average protein supply":
                    print(int(df["Baseline"].iloc[0].split(',')[0]))
                    fig.add_hrect(y0=40, y1=int(df["Baseline"].iloc[0].split(',')[0]), line_width=0, fillcolor="red", opacity=0.1)
                    fig.add_hrect(y0=int(df["Baseline"].iloc[0].split(',')[-1]), y1=df["Value"].max()*1.2, line_width=0, fillcolor="red", opacity=0.1)
                    fig.add_hrect(y0=int(df["Baseline"].iloc[0].split(',')[0]),y1=int(df["Baseline"].iloc[0].split(',')[-1]), line_width=0, fillcolor="green", opacity=0.1)
                else:
                    print(df.info())
                    fig.add_hrect(y0=min(df["Value"].min(), df["Baseline"].iloc[0]), y1=df["Baseline"].iloc[0], line_width=0, fillcolor="red", opacity=0.1)
                    fig.add_hrect(y0=df["Baseline"].iloc[0], y1=max(df["Value"].max(),df["Baseline"].iloc[0])*1.2, line_width=0, fillcolor="green", opacity=0.1)

    #     fig.add_trace(
    #     go.Scatter(
    #          x=[df["Year"].min(),df["Year"].max()], y=[max(df["Value"].max(),df["Baseline"].iloc[0]),max(df["Value"].max(),df["Baseline"].iloc[0])], mode='lines',
    #         fill='tonexty', fillcolor='rgba(176, 0, 0, 0.2)',showlegend=False
    #     )
    # )

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
#         fig.update_layout(
#     shapes=[
#         dict(
#             type='line',
#             xref='paper',
#             x0=0,
#             x1=1,
#             yref='y',
#             y0=df["Baseline"].iloc[0],
#             y1=df["Baseline"].iloc[0],
#             line=dict(
#                 color='black',
#                 width=2,
#                 dash='dash'
#             )
#         )
#     ]
    
# )
#         fig.add_annotation(
#     x=0.5,
#     y=df["Baseline"].iloc[0],
#     xref='paper',
#     yref='y',
#     text='Baseline',
#     showarrow=False,
#     font=dict(
#         size=14,
#         color='black'
#     )
# )
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
            if len(line2) + len(word) < 25:
                line2 += word + " "
            else:
                line3+= word+" "
    return line1 + "<br>" + line2 + "<br>" + line3


def visualizeOp(df,country):
    info = {'red':-1,'green':1,'gray':0}
    
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
        
    # print(df)
    # country = data["Country"].unique()[0]
    country_data = df[df["Country"]==country]
    # print(country_data)


    # print(country_data)
    # data = df.copy()
    # data["Color"] = "gray"
    # print(data)
    present = country_data.dropna(subset = "Value").sort_values("Year").drop_duplicates(["Country", "Indicator"], keep = "last")
    
    mitigators = [i for i in present.loc[present["Status"]=="Mitigator","Indicator"].unique()]
    amplifier = [i for i in present.loc[present["Status"]=="Amplifier","Indicator"].unique()]
    # print(mitigators)
    # print(amplifier)
    present_rad = df.dropna(subset = "Value").sort_values("Year").drop_duplicates(["Country", "Indicator"], keep = "last")
    # print("************RAD DATA************")
    # print(present_rad)
    # print(present)
    try:
        st.image("Con_Flags/"+flags[country]+".png",width=100)
        st.subheader(str.upper(country))
    except:
        st.subheader(str.upper(country))
    showhide = st.sidebar.checkbox("Show Trends for Indicators!")
    style_text=""
    # for i in range(4):
    #     colors = ['red','yellow','green','gray']
    #     legend = ['Weak ' , 'Fine ', 'Excellent', 'Data Missing']
    #     style_text+= "<div><div class='rectangle {}'></div> {}</div>".format(colors[i],legend[i])
    colors = ['redop','greenop','red','green']
    legend = ['Amplifier Zone ' , 'Mitigator Zone', "Amplifer","Mitigator"]
    for i in range(len(colors)):
        style_text+= "<div><div class='rectangle {}'></div> {}</div>".format(colors[i],legend[i])
    st.sidebar.subheader("LEGEND")
    st.sidebar.markdown(style_text,unsafe_allow_html=True)
    
    st.sidebar.subheader("INDICATORS")
    score_data = present_rad[present_rad["Country"]==country].copy()
    score_data["colVal"] = score_data["Color"].map(info)
    score = score_data.groupby("Country")["colVal"].sum().reset_index()
    st.header('Food Security Score: {}'.format(score["colVal"].iloc[0]))
    st.write('Investment/Funding Areas: **{}**'.format(amplifier))
    for i in range(len(pillars)):
        color_discrete_map= {country:"purple", "Pacific":"blue"}
        
        # st.sidebar.header(pillars[i])
        st.header(pillars[i].upper(),anchor=pillars[i])

        # showhide = st.checkbox("Show Trends for Indicators!",key = i)
        if showhide:
            # st.sidebar.subheader(pillars[i])
            refPillar ="<div style ='height:2px'> <a href = '#{}'><h2><b> {}</b></h2></div> <br>".format(pillars[i],pillars[i].upper())
            st.sidebar.markdown(refPillar,unsafe_allow_html=True)
        temp = df[df["Pillar"]==pillars[i]]
        rad_data = present_rad[present_rad["Pillar"]==pillars[i]]
        # print(rad_data)
        # rad_data.loc[rad_data["Indicator"]=="Agriculture orientation Index for Government Expenditures","Value"]*=100
        # print(rad_data[["Country","Indicator","Status","Value"]])
        # print(rad_data.columns)
        score = 0
        if not score_data[score_data["Pillar"]==pillars[i]].empty:
            score = score_data[score_data["Pillar"]==pillars[i]].groupby("Country")["colVal"].sum().reset_index()["colVal"].iloc[0]
        st.write('Score: {}'.format(score))
        
        c = st.columns(2)
    
        # print(len(rad_data["Status"].unique()))
        # cat_order = None
        # if pillars[i]=="Stability":
        #     cat_order = ["Control of Corruption","Reulatory Quality","Rule of Law", "score for adoption and implementation of disaster reduction strategies", "Voice and Accountability"]
        # t_fig=None


        for k in range(len(aspects)):
            indList = [i for i in present.loc[(present["Pillar"]==pillars[i])& (present["Status"]==aspects[k]),"Indicator"].unique()]
            indList.sort()
            # print(indList)
            bac =rad_data[rad_data["Indicator"].isin(indList)].sort_values("Indicator")
            # print(bac["Indicator"])
            # cat = len(indList)
            if not bac.empty:
                # step = 360/cat
                # nbar_group = len(bac["Country"].unique())
                # small_step = step/(nbar_group+1)
                # theta = [0.5*(2*k-1)*step+small_step*(j+1)  for k in range(cat) for j in range(nbar_group)]
                # tickvals=[k*step for k in range(cat)]
                # ticktext=[wrap_long_text(text) for text in indList]
                # t_fig = px.bar_polar(bac,r = "Value",theta=theta, color = "Country",color_discrete_map=color_discrete_map,custom_data=["Country","Indicator","Value"])
                
                
                t_fig = px.bar(bac,x = "Value", y = 'Indicator', color = "Country", orientation = 'h',color_discrete_sequence =px.colors.qualitative.Antique,barmode = 'group',custom_data=["Country","Indicator","Value"])
                # t_fig.update_layout(barmode='group')
                # t_fig.update_traces(text = bac["Indicator"],hovertemplate='%{theta}: %{r}')
                # if len(bac[bac["Country"]==country]["Indicator"].unique())<3:
                # # t_fig = px.bar_polar(rad_data[rad_data["Aspect"]==aspects[k]],r = "Value",theta="Indicator", color = "Country",line_close=True)
                #     t_fig = px.bar_polar(bac,r = "Value",theta="Indicator", color = "Country",color_discrete_map=color_discrete_map, custom_data=["Country","Indicator","Value"])
                # else:
                #     t_fig = px.line_polar(bac,r = "Value",theta="Indicator",color = "Country",color_discrete_map=color_discrete_map,line_close=True,line_shape = 'spline',custom_data=["Country","Indicator","Value"])
                # # t_fig.update_yaxes(tickangle=90)
                #     t_fig.update_traces(fill='toself')
                t_fig.update_traces(hovertemplate='<b>%{customdata[0]}</b> <br>Indicator: %{customdata[1]} <br>Value: %{customdata[2]:.2f}')
                # t_fig.update_layout(polar=dict(angularaxis=dict(tickvals=tickvals, ticktext=ticktext)))
                t_fig.update_layout(
                    font=dict(
                    family="Arial Black",
                    size=11
                ))
                t_fig.update_yaxes(
                    title = '',
                    tickmode='array',
                    ticktext = [wrap_long_text(text) for text in indList],
                    tickvals = indList
                    # showticklabels = False,
                )
                t_fig.update_xaxes(
                    title = ''
                )

                t_fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
# t_fig.update_layout(margin = dict(l=10,r=10,t=10,b=10))
                # polar=dict(
                #     angularaxis=dict(
                #         ticktext=[wrap_long_text(text) for text in bac["Indicator"]],
                #         tickvals=bac["Indicator"]
                #     )
                # )
                #         )
                        # t_fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
                
                c[k].subheader(aspects[k])
                if aspects[k]=="Mitigator":
                    c[k].write("Mitigators help ease the food insecurity conditions.")
    #                 t_fig.update_layout(
    #     plot_bgcolor='green',
    #     # paper_bgcolor='green'
    # )
                else:
                    c[k].write("Amplifiers worsen the food insecurity conditions.")
                c[k].plotly_chart(t_fig)

                if showhide:
                    st.sidebar.header(aspects[k])
                    # trendData = temp[temp["Status"]==aspects[k]]
                    trendData = temp[temp["Indicator"].isin(indList)]
                    # print(trendData)
                    for j in trendData["Indicator"].unique():
                        # st.header(j)
                        present_df = present[present["Indicator"]==j]
                        # praint(j)
                        # print(present_df["Color"])
                        presentValue = 'NA'
                        color = ''
                        try:
                            color = present_df['Color'].iloc[0]
                            presentValue = present_df['Value'].iloc[0]
                        except:
                            color = 'gray'
                            presentValue = 'NA'

                        c[k].subheader(j,anchor=j.replace(' ',''))
                        c[k].write(typology[typology["Indicator"]==j]["About"].iloc[0])
                        anchor_text="<div><div class = 'rectangle {}'></div><a href = '#{}'>{}</div> <br>".format(color,j.replace(' ',''),j)
                        # print(anchor_text)
                        
                        c[k].text('Unit: {}'.format(temp[temp["Indicator"]==j]['Unit'].iloc[0]))
                        c[k].text('Value: {}'.format(presentValue))

                        if (j in ["Prevalance of undernourishment",'Proportion of children moderately or severely stunted or wasted']): 
                            linePlot(temp[temp["Indicator"]==j],c[k],width = True)
                        elif j in trend:
                             print(temp[temp["Indicator"]==j])
                             t_fig = px.bar(temp[temp["Indicator"]==j],x = "Value", y = 'Year', color = "Country", orientation = 'h',color_discrete_sequence =px.colors.qualitative.Antique,barmode = 'group',custom_data=["Country","Year","Value"])
                             t_fig.update_traces(hovertemplate='<b>%{customdata[0]}</b> <br>Indicator: %{customdata[1]} <br>Value: %{customdata[2]:.2f}')
                             t_fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
                             t_fig.update_xaxes(
                                title = ''
                            )
                             t_fig.update_yaxes(
                                title = ''
                            )
                             t_fig.update_layout(
                                font=dict(
                                family="Arial Black",
                                size=11
                            ))
                             c[k].plotly_chart(t_fig)
                        else:
                            linePlot(temp[temp["Indicator"]==j],c[k])
                        st.sidebar.markdown(anchor_text,unsafe_allow_html=True)
            else:
                c[k].write("No {} for {} in {} pillar of Food Security".format(aspects[k],country,pillars[i]))

        
        # if showhide:
        #     st.sidebar.header(pillars[i])
            
        #     for j in temp["Indicator"].unique():
        #         # st.header(j)
        #         present_df = present[present["Indicator"]==j]
        #         # print(present_df["Color"])
        #         presentValue = 'NA'
        #         color = ''
        #         try:
        #             color = present_df['Color'].iloc[0]
        #             presentValue = present_df['Value'].iloc[0]
        #         except:
        #             color = 'gray'
        #             presentValue = 'NA'

        #         st.subheader(j,anchor=j.replace(' ',''))
        #         st.write(typology[typology["Indicator"]==j]["About"].iloc[0])
        #         anchor_text="<div><div class = 'rectangle {}'></div><a href = '#{}'>{}</div> <br>".format(color,j.replace(' ',''),j)
        #         # print(anchor_text)
                
        #         st.text('Unit: {}'.format(temp[temp["Indicator"]==j]['Unit'].iloc[0]))
        #         st.text('Value: {}'.format(presentValue))
        #         linePlot(temp[temp["Indicator"]==j],st)
        #         st.sidebar.markdown(anchor_text,unsafe_allow_html=True)


def app():
    country = st.sidebar.selectbox("Select a Country:",countries)
    info = {"red":"Amplifier","green":"Mitigator", "gray":"Data Missing"}
    # choice = ["Exposure","Capacity"]
    # if st.sidebar.checkbox("Visualization by Aspect",value=False):
    #     choice1 = st.sidebar.selectbox("Visualization by:",["Exposure","Capacity"])
    #     choice = choice1.split()
        # print(choice)
    df = alldata1.merge(typology, on = "Indicator", how = "left")
    df["Status"] = df["Color"].map(info)
    df =df[df["Country"].isin(["Pacific",country])]
    # print(df.head())
    visualizeOp(df,country)

