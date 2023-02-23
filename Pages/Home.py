import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import panel as pn


flags = {
   'Afghanistan': 'af', 'Albania': 'al', 'Algeria': 'dz', 'American Samoa': 'as', 'Andorra': 'ad', 'Angola': 'ao', 'Anguilla': 'ai', 'Antarctica': 'aq', 'Antigua and Barbuda': 'ag', 'Argentina': 'ar', 'Armenia': 'am', 'Aruba': 'aw', 'Australia': 'au', 'Austria': 'at', 'Azerbaijan': 'az', 'Bahamas': 'bs', 'Bahrain': 'bh', 'Bangladesh': 'bd', 'Barbados': 'bb', 'Belarus': 'by', 'Belgium': 'be', 'Belize': 'bz', 'Benin': 'bj', 'Bermuda': 'bm', 'Bhutan': 'bt', 'Bolivia, Plurinational State of': 'bo', 'Bolivia': 'bo', 'Bosnia and Herzegovina': 'ba', 'Botswana': 'bw', 'Bouvet Island': 'bv', 'Brazil': 'br', 'British Indian Ocean Territory': 'io', 'Brunei Darussalam': 'bn', 'Brunei': 'bn', 'Bulgaria': 'bg', 'Burkina Faso': 'bf', 'Burundi': 'bi', 'Cambodia': 'kh', 'Cameroon': 'cm', 'Canada': 'ca', 'Cape Verde': 'cv', 'Cayman Islands': 'ky', 'Central African Republic': 'cf', 'Chad': 'td', 'Chile': 'cl', 'China': 'cn', 'Christmas Island': 'cx', 'Cocos (Keeling) Islands': 'cc', 'Colombia': 'co', 'Comoros': 'km', 'Congo': 'cg', 'DR Congo':'cd','Congo, the Democratic Republic of the': 'cd', 'Cook Islands': 'ck', 'Costa Rica': 'cr', "Côte d'Ivoire": 'ci', 'Ivory Coast': 'ci', 'Croatia': 'hr', 'Cuba': 'cu', 'Cyprus': 'cy', 'Czech Republic': 'cz', 'Denmark': 'dk', 'Djibouti': 'dj', 'Dominica': 'dm', 'Dominican Republic': 'do', 'Ecuador': 'ec', 'Egypt': 'eg', 'El Salvador': 'sv', 'Equatorial Guinea': 'gq', 'Eritrea': 'er', 'Estonia': 'ee', 'Ethiopia': 'et', 'Falkland Islands (Malvinas)': 'fk', 'Faroe Islands': 'fo', 'Fiji': 'fj', 'Finland': 'fi', 'France': 'fr', 'French Guiana': 'gf', 'French Polynesia': 'pf', 'French Southern Territories': 'tf', 'Gabon': 'ga', 'Gambia': 'gm', 'Georgia': 'ge', 'Germany': 'de', 'Ghana': 'gh', 'Gibraltar': 'gi', 'Greece': 'gr', 'Greenland': 'gl', 'Grenada': 'gd', 'Guadeloupe': 'gp', 'Guam': 'gu', 'Guatemala': 'gt', 'Guernsey': 'gg', 'Guinea': 'gn', 'Guinea-Bissau': 'gw', 'Guyana': 'gy', 'Haiti': 'ht', 'Heard Island and McDonald Islands': 'hm', 'Holy See (Vatican City State)': 'va', 'Honduras': 'hn', 'Hong Kong': 'hk', 'Hungary': 'hu', 'Iceland': 'is', 'India': 'in', 'Indonesia': 'id', 'Iran, Islamic Republic of': 'ir', 'Iraq': 'iq', 'Ireland': 'ie', 'Isle of Man': 'im', 'Israel': 'il', 'Italy': 'it', 'Jamaica': 'jm', 'Japan': 'jp', 'Jersey': 'je', 'Jordan': 'jo', 'Kazakhstan': 'kz', 'Kenya': 'ke', 'Kiribati': 'ki', "Korea, Democratic People's Republic of": 'kp', 'Korea, Republic of': 'kr', 'South Korea': 'kr', 'Kuwait': 'kw', 'Kyrgyzstan': 'kg', "Lao People's Democratic Republic": 'la', 'Latvia': 'lv', 'Lebanon': 'lb', 'Lesotho': 'ls', 'Liberia': 'lr', 'Libyan Arab Jamahiriya': 'ly', 'Libya': 'ly', 'Liechtenstein': 'li', 'Lithuania': 'lt', 'Luxembourg': 'lu', 'Macao': 'mo', 'Macedonia, the former Yugoslav Republic of': 'mk', 'Madagascar': 'mg', 'Malawi': 'mw', 'Malaysia': 'my', 'Maldives': 'mv', 'Mali': 'ml', 'Malta': 'mt', 'Marshall Islands': 'mh', 'Martinique': 'mq', 'Mauritania': 'mr', 'Mauritius': 'mu', 'Mayotte': 'yt', 'Mexico': 'mx', 'Micronesia, Federated States of': 'fm', 'Moldova, Republic of': 'md', 'Monaco': 'mc', 'Mongolia': 'mn', 'Montenegro': 'me', 'Montserrat': 'ms', 'Morocco': 'ma', 'Mozambique': 'mz', 'Myanmar': 'mm', 'Burma': 'mm', 'Namibia': 'na', 'Nauru': 'nr', 'Nepal': 'np', 'Netherlands': 'nl', 'Netherlands Antilles': 'an', 'New Caledonia': 'nc', 'New Zealand': 'nz', 'Nicaragua': 'ni', 'Niger': 'ne', 'Nigeria': 'ng', 'Niue': 'nu', 'Norfolk Island': 'nf', 'Northern Mariana Islands': 'mp', 'Norway': 'no', 'Oman': 'om', 'Pakistan': 'pk', 'Palau': 'pw', 'Palestinian Territory, Occupied': 'ps', 'Panama': 'pa', 'Papua New Guinea': 'pg', 'Paraguay': 'py', 'Peru': 'pe', 'Philippines': 'ph', 'Pitcairn': 'pn', 'Poland': 'pl', 'Portugal': 'pt', 'Puerto Rico': 'pr', 'Qatar': 'qa', 'Réunion': 're', 'Romania': 'ro', 'Russian Federation': 'ru', 'Russia': 'ru', 'Rwanda': 'rw', 'Saint Helena, Ascension and Tristan da Cunha': 'sh', 'Saint Kitts and Nevis': 'kn', 'Saint Lucia': 'lc', 'Saint Pierre and Miquelon': 'pm', 'Saint Vincent and the Grenadines': 'vc', 'Saint Vincent & the Grenadines': 'vc', 'St. Vincent and the Grenadines': 'vc', 'Samoa': 'ws', 'San Marino': 'sm', 'Sao Tome and Principe': 'st', 'Saudi Arabia': 'sa', 'Senegal': 'sn', 'Serbia': 'rs', 'Seychelles': 'sc', 'Sierra Leone': 'sl', 'Singapore': 'sg', 'Slovakia': 'sk', 'Slovenia': 'si', 'Solomon Islands': 'sb', 'Somalia': 'so', 'South Africa': 'za', 'South Georgia and the South Sandwich Islands': 'gs', 'South Sudan': 'ss', 'Spain': 'es', 'Sri Lanka': 'lk', 'Sudan': 'sd', 'Suriname': 'sr', 'Svalbard and Jan Mayen': 'sj', 'Swaziland': 'sz', 'Sweden': 'se', 'Switzerland': 'ch', 'Syrian Arab Republic': 'sy', 'Taiwan, Province of China': 'tw', 'Taiwan': 'tw', 'Tajikistan': 'tj', 'Tanzania': 'tz', 'Thailand': 'th', 'Timor-Leste': 'tl', 'Togo': 'tg', 'Tokelau': 'tk', 'Tonga': 'to', 'Trinidad and Tobago': 'tt', 'Tunisia': 'tn', 'Turkey': 'tr', 'Turkmenistan': 'tm', 'Turks and Caicos Islands': 'tc', 'Tuvalu': 'tv', 'Uganda': 'ug', 'Ukraine': 'ua', 'United Arab Emirates': 'ae', 'United Kingdom': 'gb', 'United States': 'us', 'United States of America':'us','United States Minor Outlying Islands': 'um', 'Uruguay': 'uy', 'Uzbekistan': 'uz', 'Vanuatu': 'vu', 'Venezuela, Bolivarian Republic of': 've', 'Venezuela': 've', 'Viet Nam': 'vn', 'Vietnam': 'vn', 'Virgin Islands, British': 'vg', 'Virgin Islands, U.S.': 'vi', 'Wallis and Futuna': 'wf', 'Western Sahara': 'eh', 'Yemen': 'ye', 'Zambia': 'zm', 'Zimbabwe': 'zw'
   }



@st.cache(show_spinner=False)
def load_data(url):
    df = pd.read_csv(url)
    return df


typology = load_data("Typology.csv")
alldata1 =load_data("Data1.csv")

# cluster_ref = alldata1.merge(typology, on = "Indicator", how = "left")

# availability = [i for i in cluster_ref[cluster_ref["Pillar"]=="Availability"]["Indicator"].unique()]
# accessibility = [i for i in cluster_ref[cluster_ref["Pillar"]=="Accessibility"]["Indicator"].unique()]
# utilization = [i for i in cluster_ref[cluster_ref["Pillar"]=="Utilization"]["Indicator"].unique()]
# stability = [i for i in cluster_ref[cluster_ref["Pillar"]=="Stability"]["Indicator"].unique()]

# def wrap_long_text(text):
#     words = text.split(" ")
#     line1 = ""
#     line2 = ""
#     line3 = ""
#     for word in words:
#         if len(line1) + len(word) < 20:
#             line1 += word + " "
#         else:
#             if len(line2) + len(word) < 20:
#                 line2 += word + " "
#             else:
#                 line3+= word+" "
#     return line1 + "<br>" + line2 + "<br>" + line3
def clockData(df):
    clockmap = {"red": -1, "green": 1, "gray": 0}
    temp = df.copy()
    temp["colValue"] =  temp["Color"].map(clockmap)
    clockData = temp.groupby(["Country","Pillar"])["colValue"].sum().reset_index()
    return clockData


def showLegend(st):
    c1,c2 = st.columns([1,8])
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
    style_text=""
    for i in range(3):
        colors = ['red','green','gray']
        legend = ['Amplifier ' , 'Mitigator', 'Data Missing']
        style_text+= "<div><div class='rectangle {}'></div> {}</div>".format(colors[i],legend[i])
    c1.subheader("LEGEND")
    c1.markdown(style_text,unsafe_allow_html=True)


def clockMeter(df,country,pillar):
    data = df[(df["Country"]==country) & (df["Pillar"]==pillar)]
    value = 0
    if not data.empty:
        value = data["colValue"].iloc[0]
    # fig1 = pn.indicators.Gauge(name='Food Security', value=value, bounds=(-25, 25),format='{value}',
    #                            colors=[(0.4, 'red'), (0.7, 'yellow'), (1, 'green')])
        
    fig1 = go.Figure(go.Indicator(
    number = {'font': {'size': 20}},
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = value,
    mode = "gauge+number",
    # number ={'suffix': "%"},
    # title = {'text': names[0]},
# delta = {'reference': 380},
    gauge = {'axis': {'range': [-25, 25]},
             'bar': {'color': "darkblue"},
            'steps' : [
                {'range': [-25, -10], 'color': "red"},
                {'range': [-9, 10], 'color': "yellow"},
                {'range': [11, 25], 'color': "green"}],
            # 'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.8, 'value': 100}
            }))
    # fig1.update_layout(
    #     height = 250
    # )

    return fig1

def app():
    
    color = {"red":"red","green":"green","gray":"gray"}
    info = {"red":"Amplifier","green":"Mitigator", "gray":"Data Missing"}

    data = alldata1.dropna(subset="Value").drop_duplicates(["Country","Indicator"],keep="last")
    # print(data)

    dataClock = clockData(data.merge(typology, on = "Indicator", how = "left"))
    # print(dataClock)
    df = data.dropna(subset=["Country"]).pivot(index=["Indicator"], columns=["Country"],values='Color')
    df = df.merge(typology, on = "Indicator", how = "left")
    df[(df.isna()) | df.isnull()] = 'gray'
    df["Bar"]=5
    # print(df)

    st.sidebar.subheader("Select this to view the amplifiers and mitigators.")
    viewOption = st.sidebar.checkbox("Amplifier/Mitigator")

    # num_vars = len(df.index.unique())
    # print(num_vars)
    # angles = np.linspace(0, 360, num_vars, endpoint=False)
    # print(angles)
    # c = st.columns(4)
    # k=0
    # for i in df.columns:
    #     if i not in ["Bar","Indicator", "About","Unit","Aspect","Pillar"]:
    #         df1 = df.copy()
    #         df1.loc[:,"Status"] = df1[i].map(info)
    #         print(df1)
    #         fig = px.sunburst(df1, path = ["Pillar","Aspect","Indicator"],values = "Bar", color=i,color_discrete_map=color, custom_data=["Indicator","Status"] )
    #                 # fig = px.bar_polar(df1, r = "Bar", theta="Indicator",color=i,color_discrete_map=color, hover_name=None,
    #                 #                     custom_data=["Indicator","Status"])
    #         fig.update_traces(hovertemplate='<b>%{customdata[0]}</b> <br>Status: %{customdata[1]}')
    #         fig.update_layout(showlegend=False)
    #         c[k].plotly_chart(fig,use_container_width = True)
    #         k+=1
    #         if k>3:
    #             k=0


    # c1,c2 = st.columns([1,8])
    


    

    # st.markdown("""
    # <style>
    #     .chart-container {
    #         height: 500px;
    #     }
    # </style>
    # """, unsafe_allow_html=True)

    c = st.columns([1,2,2,2,2])
    # c[0].subheader('COUNTRY')
    # for i in df.columns:
    #     if i not in  [ "Bar", "About","Unit","Aspect","Pillar","Indicator", "Pacific"]:
    #         try:
    #             st.markdown("<div class='chart-container'>")
    #             c[0].image("Con_Flags/"+flags[i]+".png", width = 100)
    #             c[0].write(str.upper(i))
    #             st.markdown("</div>")
    #         except:
    #             st.markdown("<div class='chart-container'>")
    #             c[0].write(str.upper(i))
    #             st.markdown("</div>")
    k=0
    st.sidebar.subheader('COUNTRY')
    for j in ["Country","Availability","Accessibility", "Utilization","Stability"]:
        c[k].subheader(j)
        
        for i in df.columns:
            if i not in  [ "Bar", "About","Unit","Aspect","Pillar","Indicator", "Pacific"]:
                if j=='Country':
                    c[0].subheader(' ', anchor = i)
                    c[0].write("<h3 style='height: 232px;'>{}</h3>".format(i), unsafe_allow_html=True)
                    
                    refCountry ="<div style ='height:2px'> <a href = '#{}'><h2><b> {}</b></h2></div> <br>".format(i,i.upper())
                    st.sidebar.markdown(refCountry,unsafe_allow_html=True)
                    # c[0].image("Con_Flags/"+flags[i]+".png", width = 100)
                    # html_string = ""
                    # try:
                    #     html_string = '<div style="height:{}px;display:flex;flex-direction:column;align-items:center;justify-content:center;">'.format(270)
                    #     html_string += '<img src="Con_Flags/{}.png" style="height:50%;width:auto;">'.format(flags[i])
                    #     html_string += '<p>{}</p>'.format(i)
                    #     html_string += '</div>'
                    #     print(html_string)
                    #     c[0].markdown(html_string, unsafe_allow_html = True)
                    # except:
                    #     c[0].write("<h2 style='height: 278px;'>{}</h2>".format(i), unsafe_allow_html=True)
                    # try:
                    #     fig = go.Figure()
                    #     fig.add_layout_image(
                    #         dict(
                    #             source = "Con_Flags/"+flags[i]+".png"
                    #         )
                    #     )
                    #     # img = cv2.imread("Con_Flags/"+flags[i]+".png")
                    #     # pic = px.imshow(img)
                    #     # pic.update_xaxes(showticklabels=False)
                    #     # pic.update_yaxes(showticklabels=False)
                    #     # pic.update_layout(
                    #     # height =200
                    #     # )
                    #     # img = Image.open("Con_Flags/"+flags[i]+".png")
                    #     # c[0].image("Con_Flags/"+flags[i]+".png")
                    #     # fig = px.imshow(img)
                    #     fig.update_xaxes(showticklabels=False)
                    #     fig.update_yaxes(showticklabels=False)
                    #     fig.update_layout(
                    #     height =200
                    #     )
                    #     c[0].plotly_chart(fig)

                    #     c[0].write(i)
                    #     # c[0].image("Con_Flags/"+flags[i]+".png")
                        
                    # except:
                    #     c[0].write(i)
                    #     # print("NTH")

                else:
                    df1 = df[df["Pillar"]==j].copy()
                    df1.loc[:,"Status"] = df1[i].copy().map(info)
                    fig = None
                    # df1["Status"] = df1["Status"].replace(info)
                    # df1.loc[:,"Status"] = df1.loc[:,i].replace(info)
                    # print(df1)
                    # for i in df1.columns:
                        # if i not in  [ "Bar", "About","Unit","Aspect","Pillar","Indicator", "Pacific"]:
                            # print(df[i])
                    # fig = px.sunburst(df1, path = ["Status","Indicator"],values = "Bar", color=i,color_discrete_map=color, custom_data=["Indicator","Status"] )
                    if viewOption:
                        fig = px.bar_polar(df1, r = "Bar", theta="Indicator",color=i,color_discrete_map=color, hover_name=None,custom_data=["Indicator","Status"])
                        fig.update_traces(hovertemplate='<b>%{customdata[0]}</b> <br>Status: %{customdata[1]}')
                        # fig.update_traces(labels=['',] * len(fig.data[0]['labels']))
                        fig.update_layout(showlegend=False)
                        fig.update_layout(
                            font=dict(
                    family="Arial Black",
                    size=8
                ),
                    polar=dict(
                    angularaxis=dict(
                        showticklabels = False,
                        # ticktext=[wrap_long_text(text) for text in df1["Indicator"]],
                        # tickvals=df1["Indicator"]
                    ),
                    radialaxis = dict(
                        showticklabels = False,
                        visible = False
                    ) 
                        )
                        )
                        # fig.update_layout(
                        #     height =250,
                        #     margin=dict(l=0, r=150, t=10, b=100)
                        # )
                        
                    else:
                        fig = clockMeter(dataClock,i,j)
                        # c[k].bokeh_chart(fig)
                    # st.markdown("<div class='chart-container'>")
                    fig.update_layout(
                            height =230,
                            margin=dict(l=5, r=50, t=20, b=50)
                        )
                    c[k].plotly_chart(fig,use_container_width = True)
                    # st.plotly_chart(fig)
                    
        k+=1
        if k >4:
            k=1

  


# def app():
#     color = {"red":"red","yellow":"yellow","green":"green","gray":"gray"}
#     cat = ["Worst","Fine","Excellent","Data Missing"]
#     pillar = st.sidebar.selectbox("Pillar", [ "Availability", "Accessibility", "Utilization", "Stability"])
#     data = alldata1.dropna(subset="Value").drop_duplicates(["Country","Indicator"],keep="last")
#     df = data.dropna(subset=["Country"]).pivot(index=["Indicator"], columns=["Country"],values='Color')
#     df = df.merge(typology, on = "Indicator", how = "left")
#     df = df[df["Pillar"]==pillar]
#     df[(df.isna()) | df.isnull()] = 'gray'
#     df["Bar"]=5

#     # num_vars = len(df.index.unique())
#     # print(num_vars)
#     # angles = np.linspace(0, 360, num_vars, endpoint=False)
#     # print(angles)

#     c1,c2 = st.columns([1,8])
    
#     with open('style.css') as f:
#         st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
#     style_text=""
#     for i in range(4):
#         colors = ['red','yellow','green','gray']
#         legend = ['Weak ' , 'Fine ', 'Excellent', 'Data Missing']
#         style_text+= "<div><div class='rectangle {}'></div> {}</div>".format(colors[i],legend[i])
#     c1.subheader("LEGEND")
#     c1.markdown(style_text,unsafe_allow_html=True)

#     c = st.columns(5)
#     k=0
#     for i in df.columns:
#         if i not in  [ "Bar", "About","Unit","Aspect","Pillar","Indicator", "Pacific"]:
#             try:
#                 c[k].image("Con_Flags/"+flags[i]+".png",width=50)
#                 c[k].write(str.upper(i))
#             except:
#                 c[k].write(str.upper(i))

#             # print(df[i])
#             fig = px.bar_polar(df, r = "Bar", theta="Indicator",color=i,color_discrete_map=color )
#             fig.update_layout(showlegend=False)
#             fig.update_layout(
#                 font=dict(
#         family="Arial Black",
#         size=8
#     ),
#         polar=dict(
#         angularaxis=dict(
#             ticktext=[wrap_long_text(text) for text in df["Indicator"]],
#             tickvals=df["Indicator"]
#         ),
#         radialaxis = dict(
#             showticklabels = False,
#             visible = False
#         ) 
#             )
#             )
#             fig.update_layout(
#                 height =250
#             )
#             c[k].plotly_chart(fig,use_container_width = True)
#             k+=1
#             if k >4:
#                 k=0


    



# def app():
#     # color = {"red":"red","yellow":"yellow","green":"green","gray":"gray"}
#     color = {"red":"red","yellow":"yellow","green":"green","gray":"gray"}
#     cat = ["Worst","Fine","Excellent","Data Missing"]
#     data = alldata1.dropna(subset="Value").drop_duplicates(["Country","Indicator"],keep="last")
#     df = data.dropna(subset=["Country"]).pivot(index=["Indicator"], columns=["Country"],values='Color')
#     df[(df.isna()) | df.isnull()] = 'gray'
#     # df["Bar"]=5


#     c1,c2 = st.columns([1,8])
    
#     with open('style.css') as f:
#         st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
#     style_text=""
#     for i in range(4):
#         colors = ['red','yellow','green','gray']
#         legend = ['Weak ' , 'Fine ', 'Excellent', 'Data Missing']
#         style_text+= "<div><div class='rectangle {}'></div> {}</div>".format(colors[i],legend[i])
#     c1.subheader("LEGEND")
#     c1.markdown(style_text,unsafe_allow_html=True)


#     #define a dictionary to map color names to color codes
#     colors = {
#         'red': 1,
#         'yellow': 2,
#         'green': 3,
#         'gray': 4
#     }

#     pillar_dic = {
#         'Availability':availability,
#         'Accessibility':accessibility,
#         'Utilization':utilization,
#         'Stability':stability
#     }

#     # create a new dataframe with color codes
#     df_codes = df.applymap(lambda x: colors[x])
    

#     pillar = st.sidebar.selectbox("Pillar of Food Security",["All","Availability","Accessibility","Utilization","Stability"])

#     df_codes1 = df_codes[df_codes.index.isin(pillar_dic[pillar])] if pillar!="All" else df_codes.copy()
#     print(df_codes1)

#     # create the heatmap
#     fig = px.imshow(df_codes1, color_continuous_scale=["red",'yellow','green','gray'], aspect='auto')

#     fig.update_xaxes(side="top")
#     if pillar=="All":
#         fig.layout.height = 1000
#     else:
#         fig.layout.height = 600
#     fig.layout.width = 1400
#     fig.update_layout(coloraxis_showscale=False)
#     fig.update_layout(
#             # yaxis_range=[0,100],
#             # yaxis_title="Score",
#             yaxis_title=None,
#             xaxis_title = None,
#         font=dict(
#             family="Arial Black",
#             size=14,
#         ))
#     fig.update_xaxes(tickangle=270)

#     c2.plotly_chart(fig)
   

    
