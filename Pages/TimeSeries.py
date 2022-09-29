from cmath import acosh
from tkinter.ttk import Style
from turtle import color
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from plotly.subplots import make_subplots
import plotly.graph_objects as go

incomeCat=pd.read_csv("IncomeCat.csv")
plt_style = 'bmh'
natural = ['natural','BDH.new', 'ECS', 'Sealevel', 'Forest', 'Land', 'energy', 'Water', 'GHP.new', 'WaterQuant', 'WaterQual']
human = ['human','Demographics', 'literacy', 'HDI', 'labrate', 'agprod', 'agVol', 'obesity', 'foodsafe', 'drinking', 'Micro', 'Protein', 'Diversity']
social = ['social','urbancap', 'safetynet', 'policyfood', 'nutritional', 'gender', 'political', 'corruption', 'conflict']
financial = ['financial','perCapita', 'edu', 'tariff', 'agGDP', 'finance', 'priceVol', 'foodloss']
manufactured = ['manufactured','kofgi', 'agadaptpolicy', 'climatesma', 'disman', 'Nindex', 'RND', 'mobile', 'transport', 'storage']
flags = {
   'Afghanistan': 'af', 'Albania': 'al', 'Algeria': 'dz', 'American Samoa': 'as', 'Andorra': 'ad', 'Angola': 'ao', 'Anguilla': 'ai', 'Antarctica': 'aq', 'Antigua and Barbuda': 'ag', 'Argentina': 'ar', 'Armenia': 'am', 'Aruba': 'aw', 'Australia': 'au', 'Austria': 'at', 'Azerbaijan': 'az', 'Bahamas': 'bs', 'Bahrain': 'bh', 'Bangladesh': 'bd', 'Barbados': 'bb', 'Belarus': 'by', 'Belgium': 'be', 'Belize': 'bz', 'Benin': 'bj', 'Bermuda': 'bm', 'Bhutan': 'bt', 'Bolivia, Plurinational State of': 'bo', 'Bolivia': 'bo', 'Bosnia and Herzegovina': 'ba', 'Botswana': 'bw', 'Bouvet Island': 'bv', 'Brazil': 'br', 'British Indian Ocean Territory': 'io', 'Brunei Darussalam': 'bn', 'Brunei': 'bn', 'Bulgaria': 'bg', 'Burkina Faso': 'bf', 'Burundi': 'bi', 'Cambodia': 'kh', 'Cameroon': 'cm', 'Canada': 'ca', 'Cape Verde': 'cv', 'Cayman Islands': 'ky', 'Central African Republic': 'cf', 'Chad': 'td', 'Chile': 'cl', 'China': 'cn', 'Christmas Island': 'cx', 'Cocos (Keeling) Islands': 'cc', 'Colombia': 'co', 'Comoros': 'km', 'Congo': 'cg', 'Congo, the Democratic Republic of the': 'cd', 'Cook Islands': 'ck', 'Costa Rica': 'cr', "Côte d'Ivoire": 'ci', 'Ivory Coast': 'ci', 'Croatia': 'hr', 'Cuba': 'cu', 'Cyprus': 'cy', 'Czech Republic': 'cz', 'Denmark': 'dk', 'Djibouti': 'dj', 'Dominica': 'dm', 'Dominican Republic': 'do', 'Ecuador': 'ec', 'Egypt': 'eg', 'El Salvador': 'sv', 'Equatorial Guinea': 'gq', 'Eritrea': 'er', 'Estonia': 'ee', 'Ethiopia': 'et', 'Falkland Islands (Malvinas)': 'fk', 'Faroe Islands': 'fo', 'Fiji': 'fj', 'Finland': 'fi', 'France': 'fr', 'French Guiana': 'gf', 'French Polynesia': 'pf', 'French Southern Territories': 'tf', 'Gabon': 'ga', 'Gambia': 'gm', 'Georgia': 'ge', 'Germany': 'de', 'Ghana': 'gh', 'Gibraltar': 'gi', 'Greece': 'gr', 'Greenland': 'gl', 'Grenada': 'gd', 'Guadeloupe': 'gp', 'Guam': 'gu', 'Guatemala': 'gt', 'Guernsey': 'gg', 'Guinea': 'gn', 'Guinea-Bissau': 'gw', 'Guyana': 'gy', 'Haiti': 'ht', 'Heard Island and McDonald Islands': 'hm', 'Holy See (Vatican City State)': 'va', 'Honduras': 'hn', 'Hong Kong': 'hk', 'Hungary': 'hu', 'Iceland': 'is', 'India': 'in', 'Indonesia': 'id', 'Iran, Islamic Republic of': 'ir', 'Iraq': 'iq', 'Ireland': 'ie', 'Isle of Man': 'im', 'Israel': 'il', 'Italy': 'it', 'Jamaica': 'jm', 'Japan': 'jp', 'Jersey': 'je', 'Jordan': 'jo', 'Kazakhstan': 'kz', 'Kenya': 'ke', 'Kiribati': 'ki', "Korea, Democratic People's Republic of": 'kp', 'Korea, Republic of': 'kr', 'South Korea': 'kr', 'Kuwait': 'kw', 'Kyrgyzstan': 'kg', "Lao People's Democratic Republic": 'la', 'Latvia': 'lv', 'Lebanon': 'lb', 'Lesotho': 'ls', 'Liberia': 'lr', 'Libyan Arab Jamahiriya': 'ly', 'Libya': 'ly', 'Liechtenstein': 'li', 'Lithuania': 'lt', 'Luxembourg': 'lu', 'Macao': 'mo', 'Macedonia, the former Yugoslav Republic of': 'mk', 'Madagascar': 'mg', 'Malawi': 'mw', 'Malaysia': 'my', 'Maldives': 'mv', 'Mali': 'ml', 'Malta': 'mt', 'Marshall Islands': 'mh', 'Martinique': 'mq', 'Mauritania': 'mr', 'Mauritius': 'mu', 'Mayotte': 'yt', 'Mexico': 'mx', 'Micronesia, Federated States of': 'fm', 'Moldova, Republic of': 'md', 'Monaco': 'mc', 'Mongolia': 'mn', 'Montenegro': 'me', 'Montserrat': 'ms', 'Morocco': 'ma', 'Mozambique': 'mz', 'Myanmar': 'mm', 'Burma': 'mm', 'Namibia': 'na', 'Nauru': 'nr', 'Nepal': 'np', 'Netherlands': 'nl', 'Netherlands Antilles': 'an', 'New Caledonia': 'nc', 'New Zealand': 'nz', 'Nicaragua': 'ni', 'Niger': 'ne', 'Nigeria': 'ng', 'Niue': 'nu', 'Norfolk Island': 'nf', 'Northern Mariana Islands': 'mp', 'Norway': 'no', 'Oman': 'om', 'Pakistan': 'pk', 'Palau': 'pw', 'Palestinian Territory, Occupied': 'ps', 'Panama': 'pa', 'Papua New Guinea': 'pg', 'Paraguay': 'py', 'Peru': 'pe', 'Philippines': 'ph', 'Pitcairn': 'pn', 'Poland': 'pl', 'Portugal': 'pt', 'Puerto Rico': 'pr', 'Qatar': 'qa', 'Réunion': 're', 'Romania': 'ro', 'Russian Federation': 'ru', 'Russia': 'ru', 'Rwanda': 'rw', 'Saint Helena, Ascension and Tristan da Cunha': 'sh', 'Saint Kitts and Nevis': 'kn', 'Saint Lucia': 'lc', 'Saint Pierre and Miquelon': 'pm', 'Saint Vincent and the Grenadines': 'vc', 'Saint Vincent & the Grenadines': 'vc', 'St. Vincent and the Grenadines': 'vc', 'Samoa': 'ws', 'San Marino': 'sm', 'Sao Tome and Principe': 'st', 'Saudi Arabia': 'sa', 'Senegal': 'sn', 'Serbia': 'rs', 'Seychelles': 'sc', 'Sierra Leone': 'sl', 'Singapore': 'sg', 'Slovakia': 'sk', 'Slovenia': 'si', 'Solomon Islands': 'sb', 'Somalia': 'so', 'South Africa': 'za', 'South Georgia and the South Sandwich Islands': 'gs', 'South Sudan': 'ss', 'Spain': 'es', 'Sri Lanka': 'lk', 'Sudan': 'sd', 'Suriname': 'sr', 'Svalbard and Jan Mayen': 'sj', 'Swaziland': 'sz', 'Sweden': 'se', 'Switzerland': 'ch', 'Syrian Arab Republic': 'sy', 'Taiwan, Province of China': 'tw', 'Taiwan': 'tw', 'Tajikistan': 'tj', 'Tanzania': 'tz', 'Thailand': 'th', 'Timor-Leste': 'tl', 'Togo': 'tg', 'Tokelau': 'tk', 'Tonga': 'to', 'Trinidad and Tobago': 'tt', 'Tunisia': 'tn', 'Turkey': 'tr', 'Turkmenistan': 'tm', 'Turks and Caicos Islands': 'tc', 'Tuvalu': 'tv', 'Uganda': 'ug', 'Ukraine': 'ua', 'United Arab Emirates': 'ae', 'United Kingdom': 'gb', 'United States': 'us', 'United States Minor Outlying Islands': 'um', 'Uruguay': 'uy', 'Uzbekistan': 'uz', 'Vanuatu': 'vu', 'Venezuela, Bolivarian Republic of': 've', 'Venezuela': 've', 'Viet Nam': 'vn', 'Vietnam': 'vn', 'Virgin Islands, British': 'vg', 'Virgin Islands, U.S.': 'vi', 'Wallis and Futuna': 'wf', 'Western Sahara': 'eh', 'Yemen': 'ye', 'Zambia': 'zm', 'Zimbabwe': 'zw'
   }

all_factors = {
    'Food System Resilience Score':'Score',

    'Natural Capital': 'natural',
    'Biodiversity and Habitat':'BDH.new',
    'Ecosystem Status': 'ECS',
    'Sealevel Rise': 'Sealevel',
    'Forest Area':'Forest',
    'Land Degradation':'Land',
     'Energy Footprint':'energy' ,
     'Water Footprint':'Water' ,
    'Greenhouse emission per capita':'GHP.new' ,
    'Agricultural water quantity':'WaterQuant' ,
    'Agricultural water quality':'WaterQual' ,

    'Human Capital':'human' ,
    'Population Growth':'Demographics',
   'Literacy Rate':'literacy' ,
    'HDI Score':'HDI' ,
    'Labor Participation Rate': 'labrate',
    'Agricultural Production Index': 'agprod',
    'Agricultural Production Volatility': 'agVol',
    'Obsesity Prevelance':'obesity',
    'Food Safety':'foodsafe',
     'Drinking Water':'drinking',
     'Micronutrient Availability':'Micro' ,
     'Protein Quality':'Protein' ,
     'Food Diversity Score':'Diversity' ,


     'Social Capital':'social' ,
     'Urban Absorption Capacity':'urbancap',
     'Presence of SafetyNet':'safetynet' ,
    'Food Policy Score':'policyfood',
   'Nutritional Standards':'nutritional' ,
    'Gender Equity':'gender' ,
    'Political Stability':'political' ,
     'Corruption':'corruption' ,
   'Conflict':'conflict',

     'Financial Capital':'financial',
    'Per-Capita Income': 'perCapita' ,
   'Agricultural Education and Resources':'edu' ,
    'Agricultural Import Tariff':'tariff' ,
     'Agricultural GDP':'agGDP' ,
     'Access to finance for farmers':'finance' ,
    'Food Price Volatility':'priceVol' ,
    'Food Loss and Waste':'foodloss' ,

    'Manufactured Capital':'manufactured' ,
    'Index of Globalization':'kofgi' ,
    'Adaptation of agricultural policy':'agadaptpolicy' ,
    'Climate smart agriculture':'climatesma' ,
    'Disaster Mangement':'disman' ,
    'Sustainable use of Nitrogen':'Nindex',
    'Agricultural R&D':'RND' ,
    'Mobile access to farmers':'mobile' ,
    'Transportation':'transport' ,
    'Food Storage Facilities':'storage'
}


all_factors1 = {
    'Score': 'Food System Resilience Score',

    'natural': 'Natural Capital',
    'BDH.new': 'Biodiversity and Habitat',
    'ECS': 'Ecosystem Status',
    'Sealevel': "Sealevel Rise",
    'Forest': 'Forest Area',
    'Land':'Land Degradation',
     'energy': 'Energy Footprint',
     'Water': 'Water Footprint',
    'GHP.new': 'Greenhouse emission per capita',
    'WaterQuant': 'Agricultural water quantity',
    'WaterQual': 'Agricultural water quality',

    'human': 'Human Capital',
    'Demographics': 'Population Growth',
   'literacy': 'Literacy Rate',
    'HDI': 'HDI Score',
     'labrate': 'Labor Participation Rate',
     'agprod':'Agricultural Production Index',
     'agVol':'Agricultural Production Volatility',
    'obesity':'Obsesity Prevelance',
    'foodsafe': 'Food Safety',
     'drinking':'Drinking Water',
     'Micro': 'Micronutrient Availability',
     'Protein': 'Protein Quality',
     'Diversity': 'Food Diversity Score',


     'social': 'Social Capital',
     'urbancap':'Urban Absorption Capacity',
     'safetynet': 'Presence of SafetyNet',
    'policyfood': 'Food Policy Score',
   'nutritional': 'Nutritional Standards',
    'gender': 'Gender Equity',
    'political': 'Political Stability',
     'corruption': 'Corruption',
   'conflict':'Conflict',

     'financial': 'Financial Capital',
     'perCapita': 'Per-Capita Income',
   'edu': 'Agricultural Education and Resources',
    'tariff': 'Agricultural Import Tariff',
     'agGDP': 'Agricultural GDP',
     'finance': 'Access to finance for farmers',
    'priceVol': 'Food Price Volatility',
    'foodloss': 'Food Loss and Waste',

    'manufactured': 'Manufactured Capital',
    'kofgi': 'Index of Globalization',
    'agadaptpolicy': 'Adaptation of agricultural policy',
    'climatesma': 'Climate smart agriculture',
    'disman': 'Disaster Mangement',
    'Nindex':'Sustainable use of Nitrogen',
    'RND': 'Agricultural R&D',
    'mobile': 'Mobile access to farmers',
    'transport': 'Transportation',
    'storage': 'Food Storage Facilities'
}

natural1 = [all_factors1[i] for i in ['natural','BDH.new', 'ECS', 'Sealevel', 'Forest', 'Land', 'energy', 'Water', 'GHP.new', 'WaterQuant', 'WaterQual']]
human1 = [all_factors1[i] for i in ['human','Demographics', 'literacy', 'HDI', 'labrate', 'agprod', 'agVol', 'obesity', 'foodsafe', 'drinking', 'Micro', 'Protein', 'Diversity']]
social1 = [all_factors1[i] for i in ['social','urbancap', 'safetynet', 'policyfood', 'nutritional', 'gender', 'political', 'corruption', 'conflict']]
financial1 = [all_factors1[i] for i in ['financial','perCapita', 'edu', 'tariff', 'agGDP', 'finance', 'priceVol', 'foodloss']]
manufactured1 = [all_factors1[i] for i in ['manufactured','kofgi', 'agadaptpolicy', 'climatesma', 'disman', 'Nindex', 'RND', 'mobile', 'transport', 'storage']]

# capitals = ['Score','natural','human','social','financial','manufactured']
capitals = ['FSRS','Natural','Human','Social','Financial','Manufactured']

dataColl = {}
years = range(2012,2021)
for i in years:
    abc = pd.read_csv(str(i)+'.csv',index_col= 'Country').transpose()
    # dataColl[i] = pd.read_csv(DATA_URL + "\\"+str(i)+'.csv',index_col= 'Country')
    dataColl[i] = abc
# org_data=pd.read_csv(DATA_URL + "\\"+str(2012)+'.csv',index_col= 'Country')
org_data=dataColl[2020]
trans_data = org_data.transpose()
countries = org_data.index


def showOption():
    opts = ['Country','Indicator']
    op = st.sidebar.selectbox('Analysis by:',opts)
    return op

def coloredPlot(df,c1,capital,i):
    fig1 = px.bar(df, x = i,y = df.index,orientation='h', color = "Color",color_discrete_map={"yellow":"Yellow", "green":"green", "red":"red"})
    
    fig1.update_layout(xaxis_range=[0,100],yaxis_title=None, xaxis_title=None,width = 285,height = 500)
    fig1.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
    # # fig1['layout']['xaxis'].update(autorange = True)
    fig1.update_xaxes(tickfont=dict(size =10, family = "Arial Black"))
    fig1.update_yaxes(tickfont=dict(size =8,family = "Arial Black"))
    fig1.layout.showlegend = False
    # fig1.update_traces(textposition='outside')
    # c1.subheader(capital) 
    # a1.metric(label="Food System Resilience Score",value=df.loc[df["var_name"]=="Food System Resilience Score",i])
    if i not in all_factors1.keys():
        c1.metric(label=capital+" Capital",value=(np.round(df[i].mean(),1)))
    else:
        c1.subheader(capital)

    c1.plotly_chart(fig1)

def linePlotter(df,countrySelect,capital):
  print(df)
  if(len(countrySelect)!=0):
    for i in countrySelect:
        df1=df[df.index==i]
        print(df1)
        d1,d2 = st.columns([1,20])
        
        d1.image("Con_Flags/"+flags[i]+".png",width=50)
        d2.subheader(str.upper(i))
        dfm =df1.melt('Year',var_name="Indicators",value_name="Score")
        dfm = dfm.replace(all_factors1)
        fig = px.line(dfm,x="Year", y = "Score", color = "Indicators",markers=True,symbol ="Indicators")
        fig.update_xaxes(tickfont=dict(size =15, family = "Arial Black"))
        fig.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))
        fig.update_layout(width = 1000)
        fig.update_layout(
    # title="Plot Title",
    # xaxis_title="X Axis Title",
    # yaxis_title="Y Axis Title",
    # legend_title="Legend Title",
    font=dict(
        family="Arial Black",
        size=12,
    )
)
        st.plotly_chart(fig)




def linePlot1(df,countrySelect,capital):
    
    ltitle = []
    if capital=="Natural":
        ltitle = natural1
    elif capital=="Human":
        ltitle = human1
    elif capital=="Social":
        ltitle = social1
    elif capital=="Financial":
        ltitle = financial1
    else:
        ltitle = manufactured1
    
    # print(ltitle)

    if(len(countrySelect)!=0):
        for i in countrySelect:
            df1=df[df.index==i]
            print(df1)
            d1,d2 = st.columns([1,10])
            
            d1.image("Con_Flags/"+flags[i]+".png",width=50)
            d2.subheader(str.upper(i))
            # st.subheader(str.upper(i))
        


            fig2,axs = plt.subplots(figsize=(5,3))
            # fig2,axs = plt.subplots()
            
                    
            # plt.style.use(plt_style)

            dfm =df1.melt('Year',var_name="Capitals",value_name="Score")
            sns.lineplot(x="Year", y="Score", hue = "Capitals",style = "Capitals", markers=True, data = dfm)
            plt.ylabel(None)
            plt.ylim([-5,105])
            plt.legend(ltitle,loc='center left',bbox_to_anchor=(1.1, 0.5),prop={'size': 3})
            plt.show()
            st.pyplot(fig2)

def linePlot(df,countrySelect):
    df.index.name=None
    # c1.write(df)
    c1,c2 = st.columns(2)
    if(len(countrySelect)!=0):
        df =df[df.index.isin(countrySelect)]
        check = df.reset_index().set_index("Year")
        print(check)
        # c1.write(df)
        plt.style.use(plt_style)
        for i in range(int(len(df.columns)/2)):

            if(df.columns[2*i] in all_factors1.keys()):
        
                c1.subheader(str.upper(all_factors1[df.columns[2*i]]))


            fig,axs = plt.subplots(figsize=(6,4))

            df.reset_index().set_index("Year").groupby("index")[df.columns[2*i]].plot(legend = True,style='.-')

            plt.ylim([0,100])
            plt.legend(loc='lower left')
            # plt.show()
            c1.pyplot(fig)

            # c2.write(str.upper(df.columns[2*i+1]))
            c2.subheader(str.upper(all_factors1[df.columns[2*i+1]]))
            # c2.write(df[i].sort_values(ascending= True).head(10))
            fig1,axs1 = plt.subplots(figsize=(6,4))
            plt.style.use(plt_style)
            # c1.write(df[i].sort_values(ascending= False).head(10))
            df.reset_index().set_index("Year").groupby("index")[df.columns[2*i+1]].plot(legend = True,style='.-')
            plt.ylim([0,100])
            plt.legend(loc='lower left')
            # plt.show()
            c2.pyplot(fig1)

         
def visualizeComp(op,choiceDiff):
    global dataColl
    # global conPlots
    # conPlots.write("The default year is 2020")
    # print(type(yearChoice))
    yearChoice = []
    if choiceDiff=="1-year Analysis":
        yearChoice=[2020,2019]
    elif choiceDiff=="5-year Analysis":
        yearChoice=[2020,2015]
    elif choiceDiff == "YTD Analysis":
         yearChoice=[2020,2012]
    else:
        yearChoice=[i for i in range(2012,2021)]

    if op=="Country":
        countrySelect = st.sidebar.multiselect('Select Country(ies)',countries)
        # abc = abc.append(i for i in countrySelect)
        # df = dataColl[yearChoice[0]].subtract(dataColl[yearChoice[1]])[countrySelect]
        df = dataColl[yearChoice[0]].subtract(dataColl[yearChoice[1]])
        df = df[df.index.isin(countrySelect)].transpose()
        original = dataColl[yearChoice[0]][dataColl[yearChoice[0]].index.isin(countrySelect)].transpose()
        # df = org_data[countrySelect]
        print('*****')
        print(original.head())
        traffic(df,index = "indicator",present = original[original.index.isin(all_factors.keys())])
        # showPlot1(df,"Comp","indx",present = original)
    elif op =="Countryvs":
        countrySelect = st.sidebar.multiselect('Select Country(ies)',countries)
        indexes = ["Score","natural","human","social","financial","manufactured","Year"]
        tempData ={}
        df = pd.DataFrame()
        for i in yearChoice:
            abc = dataColl[i]
            abc["Year"]=i
            tempData[i]=abc
            df =pd.concat([df,tempData[i]])
        # print(df)
        df1= df[indexes]
        linePlot(df1,countrySelect)

    elif op =="Capitals":
        indexes=[]
        capital = st.sidebar.selectbox("Choose a capital", ["Natural", "Human","Social","Financial","Manufactured"])
        countrySelect = st.sidebar.multiselect('Select Country(ies)',countries)
        
        if capital=="Natural":
            indexes = natural
        elif capital=="Human":
            indexes = human
        elif capital=="Social":
            indexes = social
        elif capital=="Financial":
            indexes = financial
        else:
            indexes = manufactured
        if "Year" not in indexes:
            indexes.append("Year")
        # print(indexes)
        tempData ={}
        df = pd.DataFrame()
        # print(yearChoice)
        for i in yearChoice:
            abc = dataColl[i]
            # print(abc)
            abc = abc[abc.index.isin(countrySelect)]
            abc["Year"]=i
            tempData[i]=abc
            df =pd.concat([df,tempData[i]])
        # print(df)
        df1= df[indexes]
        # print(df1)
        # df1 = df1.reset_index()
        # print(df1.index)
        # linePlot1(df1,countrySelect,capital)
        linePlotter(df1,countrySelect,capital)

    else:
        # indSelect1 = st.sidebar.multiselect('Select indicator(s)',all_factors.keys())
        # indSelect = [all_factors[i] for i in indSelect1]
        # df1 = dataColl[yearChoice[0]].subtract(dataColl[yearChoice[1]])[indSelect]
        # print(df1)
        # showPlot(df1,index="country",visType="Comp")

        vistype = st.sidebar.selectbox("Visualization by:",["Income Category","Region"])
        capital = st.sidebar.selectbox('FSRS/Capital',capitals)
        indicator1=None
        if capital=="Natural":
            indicator1 = st.sidebar.selectbox("Indicator",natural1)
        elif capital=="Human":
            indicator1 = st.sidebar.selectbox("Indicator",human1)
        elif capital=="Social":
            indicator1 = st.sidebar.selectbox("Indicator",social1)
        elif capital=="Financial":
            indicator1 = st.sidebar.selectbox("Indicator",financial1)
        elif capital=="Manufactured":
            indicator1 = st.sidebar.selectbox("Indicator",manufactured1)
        else:
            indicator1 = "Food System Resilience Score"

        df = dataColl[yearChoice[0]].subtract(dataColl[yearChoice[1]])[[all_factors[indicator1]]]
        print(df)
        # df = df[df.index.isin(countrySelect)].transpose()
        # original = dataColl[yearChoice[0]][dataColl[yearChoice[0]].index.isin(countrySelect)].transpose()
        original = dataColl[yearChoice[0]][[all_factors[indicator1]]]
        # print(original)
        # indSelect1 = st.sidebar.multiselect('Select indicator(s)',all_factors.keys())
        # # trans_data=pd.read_csv(DATA_URL + "\\"+str(yearChoice)+'.csv',index_col= 'Country').transpose()
        # indSelect = [all_factors[i] for i in indSelect1]
        # print("choice of year = " + str(yearChoice))
        # trans_data=dataColl[yearChoice]
        # print(trans_data)
        # print(all_factors[indicator1])
        # df1 = trans_data.loc[:,[all_factors[indicator1]]]
        # print(yearChoice)
        # print("IF ELSE")
        # print(df1.head())

        showPlot1(df,index='country',visType=vistype,present = original)

def traffic(df,index = "country",visType="Time",check="nice",present=pd.DataFrame()):
    print("Entered Traffic")
    print(df)
    # df=df.transpose()
    # c1.write(df)
    # df.index.name=None
    # plt.style.use(plt_style)
    for i in df.columns:
        print(i)
        print(present)
        d1,d2 = st.columns([1,15])
        d1.image("Con_Flags/"+flags[i]+".png",width=50)
        d2.subheader(str.upper(i))
        
        st.metric("Food Systems Resilience Score", np.round(present[i].mean(),2),delta = np.round(float(df.loc[df.index=="Score",i]),1))

        c1,c2,c3,c4,c5 = st.columns(5)
        colored = df.sort_values(i,ascending=True).copy()
        
        colored["Color"] = "green"
        colored.loc[colored[i]<0,"Color"] = "red"
        # colored.loc[(colored[i]>=40) & (colored[i]<80),"Color"]= "yellow"
        colored.index = colored.index.map(all_factors1)

        print(colored)
               
        nat = colored[colored.index.isin(natural1)]
        hum =colored[colored.index.isin(human1)]
        soc = colored[colored.index.isin(social1)]
        fin = colored[colored.index.isin(financial1)]
        man = colored[colored.index.isin(manufactured1)]

        present_nat = present[present.index.isin(natural)]
        present_hum = present[present.index.isin(human)]
        present_soc = present[present.index.isin(social)]
        present_fin = present[present.index.isin(financial)]
        present_man = present[present.index.isin(manufactured)]
        print(nat)
        coloredPlot(nat,c1,"Natural",i,visType="Time",present = present_nat)
        coloredPlot(hum,c2,"Human",i,visType="Time",present = present_hum)
        coloredPlot(soc,c3,"Social",i,visType="Time",present = present_soc)
        coloredPlot(fin,c4,"Financial",i,visType="Time",present = present_fin)
        coloredPlot(man,c5,"Manufactured",i,visType="Time",present = present_man)

def coloredPlot(df,c1,capital,i,visType=None,present=pd.DataFrame()):
    fig1 = px.bar(df, x = i,y = df.index,orientation='h', color = "Color",color_discrete_map={"yellow":"Yellow", "green":"green", "red":"red"})
    
    fig1.update_layout(yaxis_title=None, xaxis_title=None,width = 285,height = 500)
    fig1.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
    # # fig1['layout']['xaxis'].update(autorange = True)
    fig1.update_xaxes(tickfont=dict(size =10, family = "Arial Black"))
    fig1.update_yaxes(tickfont=dict(size =8,family = "Arial Black"))
    fig1.layout.showlegend = False
    # fig1.update_traces(textposition='outside')
    # c1.subheader(capital) 
    # a1.metric(label="Food System Resilience Score",value=df.loc[df["var_name"]=="Food System Resilience Score",i])
    if i not in all_factors1.keys():
        if visType!="Time":
            c1.metric(label=capital+" Capital",value=(np.round(df[i].mean(),1)))
        else:
            c1.metric(label=capital+" Capital",value=np.round(present[i].mean(),2),delta = np.round(df[i].mean(),1))

    else:
        c1.subheader(capital)

    c1.plotly_chart(fig1)

def showPlot1(df,index = "country",visType="Des",check="nice",present=pd.DataFrame()):
    
    
    print("showplot1")
    print(df)
    # df.index = df["Country"]

    plt.style.use(plt_style)
    for i in df.columns:
        print(i)
        
        

        if i in all_factors1.keys():
            st.subheader(str.upper(all_factors1[i]))
            df["Color"] = "green"
            df.loc[df[i]<0,"Color"] = "red"
            # df.loc[(df[i]>=40) & (df[i]<80),"Color"]= "yellow"
        else:
            d1,d2 = st.columns([1,10])
            d1.image("Con_Flags/"+flags[i]+".png",width=50)
            d2.subheader(str.upper(i))
        # else:
        #     d1.subheader(str.upper(i))
        print(df.head())



        # if index!="country":
        #     df["var_name"] = [all_factors1[i] for i in df.index]
        # else:
        #      df["var_name"]  = df.index

        df1 =df.merge(incomeCat,left_on = df.index,right_on="Country",how="left")
        print(df1.head())

        print("Income = "+ str(len(df1["Income Group"].unique())))
        print("region = "+ str(len(df1["Region"].unique())))
        c = []
        


        

        if visType == "Income Category":
            c = st.columns(4)
            k=0
            for j in df1["Income Group"].unique():
            
                fd = df1[df1["Income Group"]==j].sort_values(i,ascending=True)
                fd.index = fd["Country"]
                print(c)
                coloredPlot(fd,c[k],j,i)
                k=k+1
        else:
            c = st.columns(5)
            k=0
            for j in df1["Region"].unique():
            
                fd = df1[df1["Region"]==j].sort_values(i,ascending=True)
                fd.index = fd["Country"]
                print(c)
                coloredPlot(fd,c[k],j,i)
                k=k+1

                if(k>4):
                    k=0


def showPlot(df,index = "country",visType="Des",check="nice",present=pd.DataFrame()):

    plt.style.use(plt_style)
    for i in df.columns:
        print(i)
        
        d1,d2 = st.columns([1,10])

        if i in all_factors1.keys():
            d2.subheader(str.upper(all_factors1[i]))
        else:
            d1.image("Con_Flags/"+flags[i]+".png",width=50)
            d2.subheader(str.upper(i))



        if index!="country":
            df["var_name"] = [all_factors1[i] for i in df.index]
        else:
             df["var_name"]  = df.index

        print(df.head())

        if(index!="country"):
            a1,a2,a3,a4,a5,a6 = st.columns(6)

            if(present.empty):    
                print("Present Empty")   

                a1.metric(label="Food System Resilience Score",value=df.loc[df["var_name"]=="Food System Resilience Score",i])
                a2.metric(label="Natural Capital",value=df.loc[df["var_name"]=="Natural Capital",i])
                a3.metric(label="Human Capital",value=df.loc[df["var_name"]=="Human Capital",i])
                a4.metric(label="Social Capital",value=df.loc[df["var_name"]=="Social Capital",i])
                a5.metric(label="Financial Capital",value=df.loc[df["var_name"]=="Financial Capital",i])
                a6.metric(label="Manufactured Capital",value=df.loc[df["var_name"]=="Manufactured Capital",i])
            else:
                print(present.head())
                print("OKOK")
                print(df.head())
                a1.metric(label="Food System Resilience Score",value=present.loc[present.index=="Score",i][0],delta=str(np.round(df.loc[df["var_name"]=="Food System Resilience Score",i][0],2)))
                a2.metric(label="Natural Capital",value=present.loc[present.index=="natural",i][0],delta=str(np.round(df.loc[df["var_name"]=="Natural Capital",i][0],2)))
                a3.metric(label="Human Capital",value=present.loc[present.index=="human",i][0],delta=str(np.round(df.loc[df["var_name"]=="Human Capital",i][0],2)))
                a4.metric(label="Social Capital",value=present.loc[present.index=="social",i][0],delta=str(np.round(df.loc[df["var_name"]=="Social Capital",i][0],2)))
                a5.metric(label="Financial Capital",value=present.loc[present.index=="financial",i][0],delta=str(np.round(df.loc[df["var_name"]=="Financial Capital",i][0],2)))
                a6.metric(label="Manufactured Capital",value=present.loc[present.index=="manufactured",i][0],delta=str(np.round(df.loc[df["var_name"]=="Manufactured Capital",i][0],2)))   
            
       
        best_10 = df.sort_values(i,ascending = False).head(10)
        best_10[i] = best_10[i].apply(np.round)
        best_10 = best_10.sort_values(i,ascending=True)

        print(best_10)

        c1,c2 = st.columns(2)


        fig1 = px.bar(best_10, x = i,y = "var_name",orientation='h',text=i)
        
        fig1.update_layout(xaxis_range=[0,100],yaxis_title=None, xaxis_title=None)
        fig1.update_xaxes(tickfont=dict(size =15, family = "Arial Black"))
        fig1.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))
        fig1.update_traces(textposition='outside')
    
        c1.plotly_chart(fig1)



        worst_10 = df.sort_values(i,ascending = True).head(10)
        worst_10[i] = worst_10[i].apply(np.round)
        worst_10 = worst_10.sort_values(i,ascending=False)
        print(worst_10)

        fig2 = px.bar(worst_10, x = i,y = "var_name",orientation='h',text=i)


        fig2.update_layout(xaxis_range=[0,100],yaxis_title=None, xaxis_title=None)
        fig2.update_xaxes(tickfont=dict(size =15, family = "Arial Black"))
        fig2.update_traces(textposition='outside')
        fig2.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))


        if(visType=="Des"):
            fig2.update_layout(xaxis_range=[0,100],yaxis_title=None, xaxis_title=None)
        else:
            fig2.update_layout(xaxis_range=[-100,5],yaxis_title=None, xaxis_title=None)
   
        c2.plotly_chart(fig2)

        del d1,d2,c1,c2

        if index!="country":
            del a1,a2,a3,a4,a5,a6


def app():
    choiceDiff =  st.sidebar.selectbox('Select a type',["1-year Analysis","5-Year Analysis", "YTD Analysis", "Country vs Country", "Capitals"])
    if choiceDiff in ["1-year Analysis","5-Year Analysis", "YTD Analysis"]:
        op =showOption()
    elif choiceDiff== "Country vs Country":
        op = "Countryvs"
    else:
        op = choiceDiff
    visualizeComp(op,choiceDiff)
