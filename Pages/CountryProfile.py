
from turtle import color
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

# st.sidebar.title("Control Center")ff

qualities = ["Robustness", "Redundancy", "Resourcefulness","Rapidity"]
years = range(2012,2023)
capitals = ['Food Systems Resilience Score','Natural Capital','Human Capital','Social Capital','Financial Capital','Manufactured Capital']

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

notCountry = ['World','Lower middle income' 'Upper middle income' 'High income' 'Low income','Middle East & North Africa' 'Sub-Saharan Africa'
 'Latin America & Caribbean' 'East Asia & Pacific' 'Europe & Central Asia'
 'South Asia' 'North America']
incomeCat=pd.read_csv("IncomeCat.csv")

years = range(2012,2023)
# capitals = ['FSRS','Natural','Human','Social','Financial','Manufactured']
alldata1 = pd.read_csv("allIndicatorData11.csv")
# print(alldata1.head())
alldata1["Color"] = 'green'
alldata1.loc[alldata1['value']<40,'Color'] = "red"
alldata1.loc[(alldata1['value']>=40) & (alldata1['value']<60),"Color"] = "orange"
alldata1.loc[(alldata1['value']>=60) & (alldata1['value']<80),"Color"] = "yellow"
# print(alldata1["Income Group"].dropna().unique())
# print(alldata1["Region"].dropna().unique())
# alldata1 = alldata1.merge(incomeCat,on="Country",how="left")
# incomeAvg = pd.read_csv('income.csv')
# regionAvg = pd.read_csv('region.csv')
# worldAvg = incomeAvg.groupby(["Year","Indicator"]).mean().round(1).reset_index()
# worldAvg = worldAvg.rename(columns = {"Avg_Income":"World"})


# # alldata1 = alldata1.replace({'United States':'United States of America',
#                             'Dominican Rep.':'Dominican Republic',
#                             "Korea, Dem People's Rep":"North Korea",
#                             "St. Kitts and Nevis":"St Kitts and Nevis",
#                             "Saint Kitts and Nevis":"St Kitts and Nevis",
#                             "St. Vincent and the Grenadines": "St Vincent and the Grenadines",
#                             "Saint Vincent and the Grenadines": "St Vincent and the Grenadines",
#                             "St. Lucia": "St Lucia",
#                             "Saint Lucia": "St Lucia",
#                             "Micronesia, Fed. Sts.":"Mirconesia",
#                             "Micronesia, Fed Sts":"Micronesia",
#                             "Virgin Islands(U.S.)": "Virgin Islands (US)",
#                             "Sint Marteen": "Sint Marteen (Dutch part)"})
countries = alldata1[~alldata1["Country"].isin(notCountry)]["Country"].unique()
# print(countries)
# dataColl = {}
# for i in years:
#     # abc = pd.read_csv(str(i)+'.csv',index_col= 'Country').transpose()
#     # dataColl[i] = pd.read_csv(DATA_URL + "\\"+str(i)+'.csv',index_col= 'Country')
#     dataColl[i] = alldata1[alldata1["Year"]==i]

# org_data=dataColl[2022]
# alldata_pivot = alldata1.pivot(["Country","Indicator"],columns="Year",values="value").reset_index()
# print("Printing Pivot PD")
# print(alldata_pivot.head())
flags = {
   'Afghanistan': 'af', 'Albania': 'al', 'Algeria': 'dz', 'American Samoa': 'as', 'Andorra': 'ad', 'Angola': 'ao', 'Anguilla': 'ai', 'Antarctica': 'aq', 'Antigua and Barbuda': 'ag', 'Argentina': 'ar', 'Armenia': 'am', 'Aruba': 'aw', 'Australia': 'au', 'Austria': 'at', 'Azerbaijan': 'az', 'Bahamas': 'bs', 'Bahrain': 'bh', 'Bangladesh': 'bd', 'Barbados': 'bb', 'Belarus': 'by', 'Belgium': 'be', 'Belize': 'bz', 'Benin': 'bj', 'Bermuda': 'bm', 'Bhutan': 'bt', 'Bolivia, Plurinational State of': 'bo', 'Bolivia': 'bo', 'Bosnia and Herzegovina': 'ba', 'Botswana': 'bw', 'Bouvet Island': 'bv', 'Brazil': 'br', 'British Indian Ocean Territory': 'io', 'Brunei Darussalam': 'bn', 'Brunei': 'bn', 'Bulgaria': 'bg', 'Burkina Faso': 'bf', 'Burundi': 'bi', 'Cambodia': 'kh', 'Cameroon': 'cm', 'Canada': 'ca', 'Cape Verde': 'cv', 'Cayman Islands': 'ky', 'Central African Republic': 'cf', 'Chad': 'td', 'Chile': 'cl', 'China': 'cn', 'Christmas Island': 'cx', 'Cocos (Keeling) Islands': 'cc', 'Colombia': 'co', 'Comoros': 'km', 'Congo': 'cg', 'DR Congo':'cd','Congo, the Democratic Republic of the': 'cd', 'Cook Islands': 'ck', 'Costa Rica': 'cr', "Côte d'Ivoire": 'ci', 'Ivory Coast': 'ci', 'Croatia': 'hr', 'Cuba': 'cu', 'Cyprus': 'cy', 'Czech Republic': 'cz', 'Denmark': 'dk', 'Djibouti': 'dj', 'Dominica': 'dm', 'Dominican Republic': 'do', 'Ecuador': 'ec', 'Egypt': 'eg', 'El Salvador': 'sv', 'Equatorial Guinea': 'gq', 'Eritrea': 'er', 'Estonia': 'ee', 'Ethiopia': 'et', 'Falkland Islands (Malvinas)': 'fk', 'Faroe Islands': 'fo', 'Fiji': 'fj', 'Finland': 'fi', 'France': 'fr', 'French Guiana': 'gf', 'French Polynesia': 'pf', 'French Southern Territories': 'tf', 'Gabon': 'ga', 'Gambia': 'gm', 'Georgia': 'ge', 'Germany': 'de', 'Ghana': 'gh', 'Gibraltar': 'gi', 'Greece': 'gr', 'Greenland': 'gl', 'Grenada': 'gd', 'Guadeloupe': 'gp', 'Guam': 'gu', 'Guatemala': 'gt', 'Guernsey': 'gg', 'Guinea': 'gn', 'Guinea-Bissau': 'gw', 'Guyana': 'gy', 'Haiti': 'ht', 'Heard Island and McDonald Islands': 'hm', 'Holy See (Vatican City State)': 'va', 'Honduras': 'hn', 'Hong Kong': 'hk', 'Hungary': 'hu', 'Iceland': 'is', 'India': 'in', 'Indonesia': 'id', 'Iran, Islamic Republic of': 'ir', 'Iraq': 'iq', 'Ireland': 'ie', 'Isle of Man': 'im', 'Israel': 'il', 'Italy': 'it', 'Jamaica': 'jm', 'Japan': 'jp', 'Jersey': 'je', 'Jordan': 'jo', 'Kazakhstan': 'kz', 'Kenya': 'ke', 'Kiribati': 'ki', "Korea, Democratic People's Republic of": 'kp', 'Korea, Republic of': 'kr', 'South Korea': 'kr', 'Kuwait': 'kw', 'Kyrgyzstan': 'kg', "Lao People's Democratic Republic": 'la', 'Latvia': 'lv', 'Lebanon': 'lb', 'Lesotho': 'ls', 'Liberia': 'lr', 'Libyan Arab Jamahiriya': 'ly', 'Libya': 'ly', 'Liechtenstein': 'li', 'Lithuania': 'lt', 'Luxembourg': 'lu', 'Macao': 'mo', 'Macedonia, the former Yugoslav Republic of': 'mk', 'Madagascar': 'mg', 'Malawi': 'mw', 'Malaysia': 'my', 'Maldives': 'mv', 'Mali': 'ml', 'Malta': 'mt', 'Marshall Islands': 'mh', 'Martinique': 'mq', 'Mauritania': 'mr', 'Mauritius': 'mu', 'Mayotte': 'yt', 'Mexico': 'mx', 'Micronesia, Federated States of': 'fm', 'Moldova, Republic of': 'md', 'Monaco': 'mc', 'Mongolia': 'mn', 'Montenegro': 'me', 'Montserrat': 'ms', 'Morocco': 'ma', 'Mozambique': 'mz', 'Myanmar': 'mm', 'Burma': 'mm', 'Namibia': 'na', 'Nauru': 'nr', 'Nepal': 'np', 'Netherlands': 'nl', 'Netherlands Antilles': 'an', 'New Caledonia': 'nc', 'New Zealand': 'nz', 'Nicaragua': 'ni', 'Niger': 'ne', 'Nigeria': 'ng', 'Niue': 'nu', 'Norfolk Island': 'nf', 'Northern Mariana Islands': 'mp', 'Norway': 'no', 'Oman': 'om', 'Pakistan': 'pk', 'Palau': 'pw', 'Palestinian Territory, Occupied': 'ps', 'Panama': 'pa', 'Papua New Guinea': 'pg', 'Paraguay': 'py', 'Peru': 'pe', 'Philippines': 'ph', 'Pitcairn': 'pn', 'Poland': 'pl', 'Portugal': 'pt', 'Puerto Rico': 'pr', 'Qatar': 'qa', 'Réunion': 're', 'Romania': 'ro', 'Russian Federation': 'ru', 'Russia': 'ru', 'Rwanda': 'rw', 'Saint Helena, Ascension and Tristan da Cunha': 'sh', 'Saint Kitts and Nevis': 'kn', 'Saint Lucia': 'lc', 'Saint Pierre and Miquelon': 'pm', 'Saint Vincent and the Grenadines': 'vc', 'Saint Vincent & the Grenadines': 'vc', 'St. Vincent and the Grenadines': 'vc', 'Samoa': 'ws', 'San Marino': 'sm', 'Sao Tome and Principe': 'st', 'Saudi Arabia': 'sa', 'Senegal': 'sn', 'Serbia': 'rs', 'Seychelles': 'sc', 'Sierra Leone': 'sl', 'Singapore': 'sg', 'Slovakia': 'sk', 'Slovenia': 'si', 'Solomon Islands': 'sb', 'Somalia': 'so', 'South Africa': 'za', 'South Georgia and the South Sandwich Islands': 'gs', 'South Sudan': 'ss', 'Spain': 'es', 'Sri Lanka': 'lk', 'Sudan': 'sd', 'Suriname': 'sr', 'Svalbard and Jan Mayen': 'sj', 'Swaziland': 'sz', 'Sweden': 'se', 'Switzerland': 'ch', 'Syrian Arab Republic': 'sy', 'Taiwan, Province of China': 'tw', 'Taiwan': 'tw', 'Tajikistan': 'tj', 'Tanzania': 'tz', 'Thailand': 'th', 'Timor-Leste': 'tl', 'Togo': 'tg', 'Tokelau': 'tk', 'Tonga': 'to', 'Trinidad and Tobago': 'tt', 'Tunisia': 'tn', 'Turkey': 'tr', 'Turkmenistan': 'tm', 'Turks and Caicos Islands': 'tc', 'Tuvalu': 'tv', 'Uganda': 'ug', 'Ukraine': 'ua', 'United Arab Emirates': 'ae', 'United Kingdom': 'gb', 'United States': 'us', 'United States of America':'us','United States Minor Outlying Islands': 'um', 'Uruguay': 'uy', 'Uzbekistan': 'uz', 'Vanuatu': 'vu', 'Venezuela, Bolivarian Republic of': 've', 'Venezuela': 've', 'Viet Nam': 'vn', 'Vietnam': 'vn', 'Virgin Islands, British': 'vg', 'Virgin Islands, U.S.': 'vi', 'Wallis and Futuna': 'wf', 'Western Sahara': 'eh', 'Yemen': 'ye', 'Zambia': 'zm', 'Zimbabwe': 'zw'
   }

# st.image("Con_Flags/"+flags['Afghanistan']+".png",width=50)
# flags = pd.read_csv('Flag.csv',index_col="Country").T.to_dict("index")
# print(flags)
# capitalsOnly = pd.read_csv("finalCapital.csv")



def coloredPlot(df,c1,capital,i,height =600):
    df[i] = np.round(df[i],1)
    print(df.head())
    df = df.sort_values(i,ascending = True).fillna("NA")
    fig1 = px.bar(df, x = i,y = df.index,orientation='h', color = "Color",text = i,color_discrete_map={"yellow":"Yellow", "green":"green", "red":"red", "orange": "#FFA500"})
    
    fig1.update_layout(xaxis_range=[0,100],yaxis_title=None, xaxis_title=None,height =height)
    # fig1.update_layout(yaxis_title=None, xaxis_title=None)
    fig1.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
    # # fig1['layout']['xaxis'].update(autorange = True)
    fig1.update_xaxes(tickfont=dict(size =9, family = "Arial Black"))
    fig1.update_yaxes(tickfont=dict(size =8,family = "Arial Black"))
    fig1.layout.showlegend = False
    # fig1.update_traces(textposition='outside')
    # c1.subheader(capital) 
    # a1.metric(label="Food System Resilience Score",value=df.loc[df["var_name"]=="Food System Resilience Score",i])
    # if i not in all_factors1.keys():
    #     c1.metric(label=capital+" Capital",value=(np.round(df[i].mean(),1)))
    # else:
    #   
    df = df.replace({"NA":np.nan})
    with c1:
        c1.metric(label=str(capital),value=(np.round(df[i].mean(),1)))  
        # c1.subheader(capital+ " Capital")
        c1.plotly_chart(fig1,use_container_width=True)

def traffic(df1,index = "Country",visType="Des",check="nice",present=pd.DataFrame()):
    df1 = df1.replace({0:0.1})
    # df=df.transpose()
    # c1.write(df)
    # df.index.name=None
    # plt.style.use(plt_style)
    # print(df1[index].unique())
    for i in df1[index].unique():
        print(i)
        df = df1[(df1[index]==i)].replace({0:0.1})
        d1,d2 = st.columns([1,15])
        try:
            st.image("Con_Flags/"+flags[i]+".png",width=50)
            st.subheader(str.upper(i))
        except:
            st.subheader(str.upper(i))
        
        st.metric("Food Systems Resilience Score", np.round(df["value"].mean(),2))

        c1,c2,c3,c4,c5 = st.columns(5)
        colored = df.sort_values("value",ascending=True).copy().set_index("Indicator")
        print(colored)
        
        colored["Color"] = "green"
        colored.loc[colored["value"]<40,"Color"] = "red"
        colored.loc[(colored["value"]>=40) & (colored["value"]<60),"Color"]= "orange"
        colored.loc[(colored["value"]>=60) & (colored["value"]<80),"Color"]= "yellow"
        # colored.index = colored.index.map(all_factors1)

        print(colored)
               
        nat = colored[colored.index.isin(natural)]
        hum =colored[colored.index.isin(human)]
        soc = colored[colored.index.isin(social)]
        fin = colored[colored.index.isin(financial)]
        man = colored[colored.index.isin(manufactured)]
        print(nat)
        coloredPlot(nat,c1,"Natural Capital","value")
        coloredPlot(hum,c2,"Human Capital","value")
        coloredPlot(soc,c3,"Social Capital","value")
        coloredPlot(fin,c4,"Financial Capital","value")
        coloredPlot(man,c5,"Manufactured Capital","value")


def showPlot(df,index = "Country",visType="Des",indicator="nice",present=pd.DataFrame()):
    
    st.subheader(indicator)


    df11 =df.merge(incomeCat,on="Country",how="left").dropna()
    print(df11.head())

    print("Income = "+ str(len(df11["Income Group"].unique())))
    print("region = "+ str(len(df11["Region"].unique())))
    # c = []
    # c = st.columns(4)


        

    if visType == "Income Category":
        c = st.columns(4)
        k=0
        for j in df11["Income Group"].unique():
            print(j)
            print(df11.head())
        
            fd = df11[df11["Income Group"]==j].sort_values("value",ascending=True)
            fd.index = fd["Country"]
            fd["Color"]="green"
            fd.loc[fd["value"]<40,"Color"] = "red"
            fd.loc[(fd["value"]>=40) & (fd["value"]<60),"Color"]= "orange"
            fd.loc[(fd["value"]>=60) & (fd["value"]<80),"Color"]= "yellow"
            # print(c)
            coloredPlot(fd.dropna(),c[k],j,"value",height = 1000)
            k=k+1
    elif(visType=="Region"):
        k=0
        c = st.columns(4)
        for j in df11["Region"].unique():
        
            fd = df11[df11["Region"]==j].sort_values("value",ascending=True)
            fd.index = fd["Country"]
            fd["Color"]="green"
            fd.loc[fd["value"]<40,"Color"] = "red"
            fd.loc[(fd["value"]>=40) & (fd["value"]<60),"Color"]= "orange"
            fd.loc[(fd["value"]>=60) & (fd["value"]<80),"Color"]= "yellow"
            # print(c)
            coloredPlot(fd,c[k],j,"value",height=1000)
            k=k+1

            if(k>3):
                k=0
    else:
        print(df.head())
        c1,c2,c3,c4 = st.columns(4)
        fd = df.dropna()
        fd.index = fd["Country"]
        fd["Color"]="green"
        fd.loc[fd["value"]<40,"Color"] = "red"
        fd.loc[(fd["value"]>=40) & (fd["value"]<80),"Color"]= "yellow"
        # bottom = fd.sort_values("value",ascending = True).head(20)
        # print(bottom.sort_values("value",ascending=True))
        # print(c)
        coloredPlot(fd.sort_values("value",ascending = True).tail(15),c1,"Top Ranked Countries","value",height=1000)
        coloredPlot(fd.sort_values("value",ascending=False).tail(15),c3,"Bottom Ranked Countries","value",height=1000)


def linePlot(df,c,width = False):
    if not df.empty:
        # print(df)
        fig = px.line(df,x="Year",y="value",color = "Country",markers=True,symbol="Country")
        fig.update_layout(
        # yaxis_range=[0,100],
        yaxis_title="Score",
        xaxis_title = None,
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






def showOption():
    opts = ['Country','Indicator']
    op = st.sidebar.selectbox('Analysis by:',opts)
    return op


dd = {}
dd['Natural Capital'] = ['Agricultural Water Quality','Agricultural Water Quantity','Biodiversity and Habitat','Ecosystem Services','Forest Change','Green House Emission Per Capita','Land Degradation','Natural Hazard Exposure','Soil Organic Content']
dd['Human Capital'] = ['Access to Agricultural Resources','Food Dietary Diversity','Food Loss','Food Safety','Food Supply Sufficiency','Labor Force Participation Rate','Literacy Rate','Micronutrient Availability','Population Growth Rate','Poverty Population','Protein Quality']
dd['Social Capital'] = ['Agricultural Women Empowerment','Armed Conflict','Community Organizations','Corruption','Dependency on Chronic Food Aid','Food Safety Net Programs','Food Security Policy Commitment','Gender Equality','Nutritional Standards','Political Stability Risk']
dd['Financial Capital'] = ['Access to Diversified Financial Services','Access to Financial Services','Agricultural GDP','Agricultural Production Volatility','Agricultural Trade','Food Price Volatility','Income Inequality','Per Capita GDP']
dd['Manufactured Capital'] = ['Agricultural R&D','Crop Storage Facilities','Disaster Risk Management','Early Warning Measures','Irrigation Infrastructure','KOFGI Globalization Index','Supply Chain Infrastructure','Sustainable Agriculture','Telecommunications']



def visualizeOp(df,country):
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
    # country = data["Country"].unique()[0]
    data = df[df["Country"]==country]
    # print(alldata1.head())
    present = data[~data["value"].isna()].sort_values("Year").drop_duplicates(["Country", "Indicator"], keep = "last")
    # print(present)
    try:
        st.image("Con_Flags/"+flags[country]+".png",width=100)
        st.subheader(str.upper(country))
    except:
        st.subheader(str.upper(country))

    c = st.columns(4)
    for i in range(len(qualities)):
        c[i].subheader(qualities[i])
        c[i].text('Score: {}'.format(np.round(present_df['value'].iloc[0],1))) 
        linePlot(df[df["Indicator"]==qualities[i]],c[i],width = True)


#     st.sidebar.markdown('''
# # Sections
# - [Section 1](#NaturalCapital)
# - [Section 2](#section-2)
# ''', unsafe_allow_html=True)
    style_text=""
    for i in range(4):
        colors = ['red','orange','yellow','green']
        legend = ['Weak [0-40]' , 'Moderate [40-60]', 'Good [60-80]', 'Very Good [80 -100]' ]
        style_text+= "<div><div class='rectangle {}'></div> {}</div>".format(colors[i],legend[i])
    # print(style_text)
    st.sidebar.markdown(style_text,unsafe_allow_html=True)
    st.sidebar.subheader("INDICATORS")
    anchor_text = ""
    for i in capitals:
        # print('********'+i)
        dff = df[df["Indicator"]==i]
        # print(dff)
        present_df = present[present["Indicator"]==i]
        try:
            color = present_df['Color'].iloc[0]
        except:
            color = 'gray'
        if not dff[dff["Country"]==country].empty:
            if i=="Food Systems Resilience Score":
                # anchor_text+="[<div><div class = 'rectangle {}'></div>{}](#section-{})</div> <br>".format(color,i,a)
                # anchor_text+='''<div><div class = 'rectangle {}'></div>{}(#{})</div> <br>'''.format(color,i,i)
                st.header(i,i.replace(' ',''))
                anchor_text+="<div><div class = 'rectangle {}'></div><a href = '#{}'>{}</div> <br>".format(color,i.replace(' ',''),i)


                
                st.text('Score: {}'.format(np.round(present_df['value'].iloc[0],1)))
                # st.text('Latest Data Available: {}'.format(present_df['Year'].iloc[0]))
                # st.text('Data Source: Linked Source[]')

                linePlot(dff,st)
                # st.markdown("[{}](#{})".format(i,i))
                # st.metric(label = "",value=present_df["value"].iloc[0])
            else:

                # anchor_text+="<div><div class = 'rectangle {}'></div>[{}](#section-{})</div> <br>".format(color,i,a)
                st.header(i, anchor=i.replace(' ',''))
                anchor_text+="<div><div class = 'rectangle {}'></div><a href = '#{}'>{}</div> <br>".format(color,i.replace(' ',''),i)
                # anchor_text+='''[{}](#section)'''.format(i)
                
                # df_df = df[df["Indicator"].isin(dd[i])]
                # present_df =present[present["Indicator"]==i]
                
                # st.write(present_df)
                # st.subheader('Score: {} \n Latest Data Available Year: {}'.format(np.round(present_df['value'].iloc[0],1),present_df['Year'].iloc[0]))
                st.text('Score: {}'.format(np.round(present_df['value'].iloc[0],1)))
                # st.text('Latest Data Available: {}'.format(present_df['Year'].iloc[0]))
                # st.text('Data Source: Linked Source[]')
                linePlot(dff,st)

                if len(present[present["Indicator"].isin(dd[i])]["Indicator"].unique())!=0:
                    for j in present[present["Indicator"].isin(dd[i])]["Indicator"].unique():
                        # print(j)
                        if i!=j:
                            # print(df['Country'].unique())
                            color = ""
                            df_indicator = df[df["Indicator"]==j]
                            present_indicator = present[present["Indicator"]==j]
                            # print("*********Indicator")
                            # print(df_indicator)
                            try:
                                color = present_indicator['Color'].iloc[0]
                            except:
                                color = "gray"
                            st.subheader(j,anchor = j.replace(' ',''))
                            anchor_text+="<div><div class = 'rectangle {} left'></div><a href = '#{}'>{}</div> <br>".format(color,j.replace(' ',''),j)
                            # st.write(present_indicator)
                            # st.subheader('Score: {} \n Latest Data Available Year: {}'.format(np.round(present_indicator['value'].iloc[0],1),present_indicator['Year'].iloc[0]))
                            st.text('Score: {}'.format(np.round(present_indicator['value'].iloc[0],1)))
                            st.text('Latest Data Available: {}'.format(present_indicator['Year'].iloc[0]))
                            st.text('Data Source: Linked Source[]')
                            # st.write(df)
                            # st.write()
                            linePlot(df_indicator,st)
                #             # anchor_text+= "- [{}](#subsection-{}) <br>".format(j,a)
                            
                #             a+=1
        else:
            st.write("No data available for indicators in "+ i)

    # print(anchor_text)
    st.sidebar.markdown(anchor_text,unsafe_allow_html=True)


def app():

    # print(alldata1.head())
    country = st.sidebar.selectbox("Select a Country:",countries)
    conList = [country, 'World',alldata1.loc[alldata1["Country"]==country, "Region"].iloc[1],alldata1.loc[alldata1["Country"]==country, "Income Group"].iloc[1]]
    # print(conList)
    df = alldata1[alldata1["Country"].isin(conList)].drop(columns = ["Income Group","Region"]).drop_duplicates(["Country","Year","Indicator"])
    visualizeOp(df,country)