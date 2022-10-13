
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

# st.sidebar.title("Control Center")ff
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


incomeCat=pd.read_csv("IncomeCat.csv")
# print(incomeCat.head())

# capitals = ['Score','natural','human','social','financial','manufactured']
years = range(2012,2023)
# capitals = ['FSRS','Natural','Human','Social','Financial','Manufactured']
alldata1 = pd.read_csv("FinalData.csv")
alldata1 = alldata1.replace({'United States':'United States of America',
                            'Dominican Rep.':'Dominican Republic'})
countries = alldata1["Country"].unique()
# print(countries)
dataColl = {}
for i in years:
    # abc = pd.read_csv(str(i)+'.csv',index_col= 'Country').transpose()
    # dataColl[i] = pd.read_csv(DATA_URL + "\\"+str(i)+'.csv',index_col= 'Country')
    dataColl[i] = alldata1[alldata1["Year"]==i]

org_data=dataColl[2022]
alldata_pivot = alldata1.pivot(["Country","Indicator"],columns="Year",values="value").reset_index()
# print("Printing Pivot PD")
# print(alldata_pivot.head())
flags = {
   'Afghanistan': 'af', 'Albania': 'al', 'Algeria': 'dz', 'American Samoa': 'as', 'Andorra': 'ad', 'Angola': 'ao', 'Anguilla': 'ai', 'Antarctica': 'aq', 'Antigua and Barbuda': 'ag', 'Argentina': 'ar', 'Armenia': 'am', 'Aruba': 'aw', 'Australia': 'au', 'Austria': 'at', 'Azerbaijan': 'az', 'Bahamas': 'bs', 'Bahrain': 'bh', 'Bangladesh': 'bd', 'Barbados': 'bb', 'Belarus': 'by', 'Belgium': 'be', 'Belize': 'bz', 'Benin': 'bj', 'Bermuda': 'bm', 'Bhutan': 'bt', 'Bolivia, Plurinational State of': 'bo', 'Bolivia': 'bo', 'Bosnia and Herzegovina': 'ba', 'Botswana': 'bw', 'Bouvet Island': 'bv', 'Brazil': 'br', 'British Indian Ocean Territory': 'io', 'Brunei Darussalam': 'bn', 'Brunei': 'bn', 'Bulgaria': 'bg', 'Burkina Faso': 'bf', 'Burundi': 'bi', 'Cambodia': 'kh', 'Cameroon': 'cm', 'Canada': 'ca', 'Cape Verde': 'cv', 'Cayman Islands': 'ky', 'Central African Republic': 'cf', 'Chad': 'td', 'Chile': 'cl', 'China': 'cn', 'Christmas Island': 'cx', 'Cocos (Keeling) Islands': 'cc', 'Colombia': 'co', 'Comoros': 'km', 'Congo': 'cg', 'DR Congo':'cd','Congo, the Democratic Republic of the': 'cd', 'Cook Islands': 'ck', 'Costa Rica': 'cr', "Côte d'Ivoire": 'ci', 'Ivory Coast': 'ci', 'Croatia': 'hr', 'Cuba': 'cu', 'Cyprus': 'cy', 'Czech Republic': 'cz', 'Denmark': 'dk', 'Djibouti': 'dj', 'Dominica': 'dm', 'Dominican Republic': 'do', 'Ecuador': 'ec', 'Egypt': 'eg', 'El Salvador': 'sv', 'Equatorial Guinea': 'gq', 'Eritrea': 'er', 'Estonia': 'ee', 'Ethiopia': 'et', 'Falkland Islands (Malvinas)': 'fk', 'Faroe Islands': 'fo', 'Fiji': 'fj', 'Finland': 'fi', 'France': 'fr', 'French Guiana': 'gf', 'French Polynesia': 'pf', 'French Southern Territories': 'tf', 'Gabon': 'ga', 'Gambia': 'gm', 'Georgia': 'ge', 'Germany': 'de', 'Ghana': 'gh', 'Gibraltar': 'gi', 'Greece': 'gr', 'Greenland': 'gl', 'Grenada': 'gd', 'Guadeloupe': 'gp', 'Guam': 'gu', 'Guatemala': 'gt', 'Guernsey': 'gg', 'Guinea': 'gn', 'Guinea-Bissau': 'gw', 'Guyana': 'gy', 'Haiti': 'ht', 'Heard Island and McDonald Islands': 'hm', 'Holy See (Vatican City State)': 'va', 'Honduras': 'hn', 'Hong Kong': 'hk', 'Hungary': 'hu', 'Iceland': 'is', 'India': 'in', 'Indonesia': 'id', 'Iran, Islamic Republic of': 'ir', 'Iraq': 'iq', 'Ireland': 'ie', 'Isle of Man': 'im', 'Israel': 'il', 'Italy': 'it', 'Jamaica': 'jm', 'Japan': 'jp', 'Jersey': 'je', 'Jordan': 'jo', 'Kazakhstan': 'kz', 'Kenya': 'ke', 'Kiribati': 'ki', "Korea, Democratic People's Republic of": 'kp', 'Korea, Republic of': 'kr', 'South Korea': 'kr', 'Kuwait': 'kw', 'Kyrgyzstan': 'kg', "Lao People's Democratic Republic": 'la', 'Latvia': 'lv', 'Lebanon': 'lb', 'Lesotho': 'ls', 'Liberia': 'lr', 'Libyan Arab Jamahiriya': 'ly', 'Libya': 'ly', 'Liechtenstein': 'li', 'Lithuania': 'lt', 'Luxembourg': 'lu', 'Macao': 'mo', 'Macedonia, the former Yugoslav Republic of': 'mk', 'Madagascar': 'mg', 'Malawi': 'mw', 'Malaysia': 'my', 'Maldives': 'mv', 'Mali': 'ml', 'Malta': 'mt', 'Marshall Islands': 'mh', 'Martinique': 'mq', 'Mauritania': 'mr', 'Mauritius': 'mu', 'Mayotte': 'yt', 'Mexico': 'mx', 'Micronesia, Federated States of': 'fm', 'Moldova, Republic of': 'md', 'Monaco': 'mc', 'Mongolia': 'mn', 'Montenegro': 'me', 'Montserrat': 'ms', 'Morocco': 'ma', 'Mozambique': 'mz', 'Myanmar': 'mm', 'Burma': 'mm', 'Namibia': 'na', 'Nauru': 'nr', 'Nepal': 'np', 'Netherlands': 'nl', 'Netherlands Antilles': 'an', 'New Caledonia': 'nc', 'New Zealand': 'nz', 'Nicaragua': 'ni', 'Niger': 'ne', 'Nigeria': 'ng', 'Niue': 'nu', 'Norfolk Island': 'nf', 'Northern Mariana Islands': 'mp', 'Norway': 'no', 'Oman': 'om', 'Pakistan': 'pk', 'Palau': 'pw', 'Palestinian Territory, Occupied': 'ps', 'Panama': 'pa', 'Papua New Guinea': 'pg', 'Paraguay': 'py', 'Peru': 'pe', 'Philippines': 'ph', 'Pitcairn': 'pn', 'Poland': 'pl', 'Portugal': 'pt', 'Puerto Rico': 'pr', 'Qatar': 'qa', 'Réunion': 're', 'Romania': 'ro', 'Russian Federation': 'ru', 'Russia': 'ru', 'Rwanda': 'rw', 'Saint Helena, Ascension and Tristan da Cunha': 'sh', 'Saint Kitts and Nevis': 'kn', 'Saint Lucia': 'lc', 'Saint Pierre and Miquelon': 'pm', 'Saint Vincent and the Grenadines': 'vc', 'Saint Vincent & the Grenadines': 'vc', 'St. Vincent and the Grenadines': 'vc', 'Samoa': 'ws', 'San Marino': 'sm', 'Sao Tome and Principe': 'st', 'Saudi Arabia': 'sa', 'Senegal': 'sn', 'Serbia': 'rs', 'Seychelles': 'sc', 'Sierra Leone': 'sl', 'Singapore': 'sg', 'Slovakia': 'sk', 'Slovenia': 'si', 'Solomon Islands': 'sb', 'Somalia': 'so', 'South Africa': 'za', 'South Georgia and the South Sandwich Islands': 'gs', 'South Sudan': 'ss', 'Spain': 'es', 'Sri Lanka': 'lk', 'Sudan': 'sd', 'Suriname': 'sr', 'Svalbard and Jan Mayen': 'sj', 'Swaziland': 'sz', 'Sweden': 'se', 'Switzerland': 'ch', 'Syrian Arab Republic': 'sy', 'Taiwan, Province of China': 'tw', 'Taiwan': 'tw', 'Tajikistan': 'tj', 'Tanzania': 'tz', 'Thailand': 'th', 'Timor-Leste': 'tl', 'Togo': 'tg', 'Tokelau': 'tk', 'Tonga': 'to', 'Trinidad and Tobago': 'tt', 'Tunisia': 'tn', 'Turkey': 'tr', 'Turkmenistan': 'tm', 'Turks and Caicos Islands': 'tc', 'Tuvalu': 'tv', 'Uganda': 'ug', 'Ukraine': 'ua', 'United Arab Emirates': 'ae', 'United Kingdom': 'gb', 'United States': 'us', 'United States of America':'us','United States Minor Outlying Islands': 'um', 'Uruguay': 'uy', 'Uzbekistan': 'uz', 'Vanuatu': 'vu', 'Venezuela, Bolivarian Republic of': 've', 'Venezuela': 've', 'Viet Nam': 'vn', 'Vietnam': 'vn', 'Virgin Islands, British': 'vg', 'Virgin Islands, U.S.': 'vi', 'Wallis and Futuna': 'wf', 'Western Sahara': 'eh', 'Yemen': 'ye', 'Zambia': 'zm', 'Zimbabwe': 'zw'
   }

# st.image("Con_Flags/"+flags['Afghanistan']+".png",width=50)
# flags = pd.read_csv('Flag.csv',index_col="Country").T.to_dict("index")
# print(flags)
capitalsOnly = pd.read_csv("finalCapital.csv")



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
    print(df1[index].unique())
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






def showOption():
    opts = ['Country','Indicator']
    op = st.sidebar.selectbox('Analysis by:',opts)
    return op

def visualizeOp(op,yearChoice=2022):
    global dataColl
    if(isinstance(yearChoice,list)):
        if(len(yearChoice)==1):
            yearChoice = yearChoice[0]
        else:
            yearChoice=2022
    trans_data=dataColl[yearChoice]
    if op=="Country":
        countrySelect = st.sidebar.multiselect('Select Country(ies)',countries)
        print("choice of year = " + str(yearChoice))
        # abc = abc.append(i for i in countrySelect)
        # org_data=pd.read_csv(DATA_URL + "\\"+str(yearChoice)+'.csv',index_col= 'Country')
        org_data=dataColl[yearChoice]
        print(org_data.shape)
        # df = org_data[countrySelect]
        # df = org_data[org_data.index.isin(countrySelect)].transpose()
        df = org_data.loc[org_data["Country"].isin(countrySelect),:]
        # print(df)
        traffic(df,index = "Country")
        # showPlot(df,index='indicator')

     
    else:
        vistype = st.sidebar.selectbox("Visualization by:",["Overall", "Income Category","Region"])
        capital = st.sidebar.selectbox('FSRS/Capital',capitals)
        # indicator1=None
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
        # indSelect1 = st.sidebar.multiselect('Select indicator(s)',all_factors.keys())
        # # trans_data=pd.read_csv(DATA_URL + "\\"+str(yearChoice)+'.csv',index_col= 'Country').transpose()
        # indSelect = [all_factors[i] for i in indSelect1]
        # print("choice of year = " + str(yearChoice))
        
        # print(trans_data)
        # print(all_factors[indicator1])
        # df1 = trans_data.loc[:,[all_factors[indicator1]]]
        # print(df1)
        # df = pd.DataFrame()
        df = pd.DataFrame()
        print("indicator = "+indicator1)
        Year = yearChoice
        if(indicator1 in capitals):
            df = capitalsOnly[(capitalsOnly["Capital"]==indicator1) & (capitalsOnly['Year']==Year)]
            print(df.head())

        else:
            dff = alldata_pivot[["Country","Indicator",Year]].groupby(["Country", "Indicator"])[Year].mean().round(1).reset_index()
            df = dff[dff["Indicator"]==indicator1]
            print(df.head())


        df["Indicator"] = indicator1
        df =df.rename(columns={Year:"value"})
    # indicator = all_factors[indicator1]
        # Year = yearChoice
        # if(indicator1=="Food Systems Resilience Score"):
        #     df = alldata_pivot[["Country","Indicator",Year]].groupby("Country")[Year].mean().reset_index()
        #     df["Indicator"] = indicator1
        #     df =df.rename(columns={Year:"value"})
        # elif(indicator1=="Natural Capital"):
        #     df = alldata_pivot.loc[alldata_pivot["Indicator"].isin(natural),["Country","Indicator",Year]].groupby("Country")[Year].mean().reset_index()
        #     df =df.rename(columns={Year:"value"})
        # elif(indicator1=="Human Capital"):
        #     df = alldata_pivot.loc[alldata_pivot["Indicator"].isin(human),["Country","Indicator",Year]].groupby("Country")[Year].mean().reset_index()
        #     df =df.rename(columns={Year:"value"})
        # elif(indicator1=="Social Capital"):
        #     df = alldata_pivot.loc[alldata_pivot["Indicator"].isin(social),["Country","Indicator",Year]].groupby("Country")[Year].mean().reset_index()
        #     df =df.rename(columns={Year:"value"})
        # elif(indicator1=="Financial Capital"):
        #     df = alldata_pivot.loc[alldata_pivot["Indicator"].isin(financial),["Country","Indicator",Year]].groupby("Country")[Year].mean().reset_index()
        #     df =df.rename(columns={Year:"value"})
        # elif(indicator1=="Manufactured Capital"):
        #     df = alldata_pivot.loc[alldata_pivot["Indicator"].isin(manufactured),["Country","Indicator",Year]].groupby("Country")[Year].mean().reset_index()
        #     df =df.rename(columns={Year:"value"})
        # else:
        #     df = alldata1[(alldata1["Year"]==Year) & (alldata1["Indicator"]==indicator1)]
        # print(df)
        # df = df[(df["Year"]==Year) & (df["Indicator"]==indicator1)]
        # print(df)
        # if indicator1 in capitals:
        #   if indicator1==
        print(df)

        showPlot(df,index='Country',visType=vistype,indicator=indicator1)



def app():
    yearChoice =  st.sidebar.selectbox('Select Year(s)',sorted(list(years),reverse=True))
    op =showOption()
    visualizeOp(op,yearChoice)