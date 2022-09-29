
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

# st.sidebar.title("Control Center")
years = range(2012,2021)
plt_style = 'bmh'
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

incomeCat=pd.read_csv("IncomeCat.csv")
print(incomeCat.head())


natural1 = [all_factors1[i] for i in ['natural','BDH.new', 'ECS', 'Sealevel', 'Forest', 'Land', 'energy', 'Water', 'GHP.new', 'WaterQuant', 'WaterQual']]
human1 = [all_factors1[i] for i in ['human','Demographics', 'literacy', 'HDI', 'labrate', 'agprod', 'agVol', 'obesity', 'foodsafe', 'drinking', 'Micro', 'Protein', 'Diversity']]
social1 = [all_factors1[i] for i in ['social','urbancap', 'safetynet', 'policyfood', 'nutritional', 'gender', 'political', 'corruption', 'conflict']]
financial1 = [all_factors1[i] for i in ['financial','perCapita', 'edu', 'tariff', 'agGDP', 'finance', 'priceVol', 'foodloss']]
manufactured1 = [all_factors1[i] for i in ['manufactured','kofgi', 'agadaptpolicy', 'climatesma', 'disman', 'Nindex', 'RND', 'mobile', 'transport', 'storage']]

natural = ['BDH.new', 'ECS', 'Sealevel', 'Forest', 'Land', 'energy', 'Water', 'GHP.new', 'WaterQuant', 'WaterQual']
human = ['Demographics', 'literacy', 'HDI', 'labrate', 'agprod', 'agVol', 'obesity', 'foodsafe', 'drinking', 'Micro', 'Protein', 'Diversity']
social = ['urbancap', 'safetynet', 'policyfood', 'nutritional', 'gender', 'political', 'corruption', 'conflict']
financial = ['perCapita', 'edu', 'tariff', 'agGDP', 'finance', 'priceVol', 'foodloss']
manufactured = ['kofgi', 'agadaptpolicy', 'climatesma', 'disman', 'Nindex', 'RND', 'mobile', 'transport', 'storage']

# capitals = ['Score','natural','human','social','financial','manufactured']

capitals = ['FSRS','Natural','Human','Social','Financial','Manufactured']

dataColl = {}
for i in years:
    abc = pd.read_csv(str(i)+'.csv',index_col= 'Country').transpose()
    # dataColl[i] = pd.read_csv(DATA_URL + "\\"+str(i)+'.csv',index_col= 'Country')
    dataColl[i] = abc
# org_data=pd.read_csv(DATA_URL + "\\"+str(2012)+'.csv',index_col= 'Country')
org_data=dataColl[2020]
print("original data")
print(org_data.head())
trans_data = org_data.transpose()
print(trans_data.head())
countries = org_data.index
print(list(countries))
flags = {
   'Afghanistan': 'af', 'Albania': 'al', 'Algeria': 'dz', 'American Samoa': 'as', 'Andorra': 'ad', 'Angola': 'ao', 'Anguilla': 'ai', 'Antarctica': 'aq', 'Antigua and Barbuda': 'ag', 'Argentina': 'ar', 'Armenia': 'am', 'Aruba': 'aw', 'Australia': 'au', 'Austria': 'at', 'Azerbaijan': 'az', 'Bahamas': 'bs', 'Bahrain': 'bh', 'Bangladesh': 'bd', 'Barbados': 'bb', 'Belarus': 'by', 'Belgium': 'be', 'Belize': 'bz', 'Benin': 'bj', 'Bermuda': 'bm', 'Bhutan': 'bt', 'Bolivia, Plurinational State of': 'bo', 'Bolivia': 'bo', 'Bosnia and Herzegovina': 'ba', 'Botswana': 'bw', 'Bouvet Island': 'bv', 'Brazil': 'br', 'British Indian Ocean Territory': 'io', 'Brunei Darussalam': 'bn', 'Brunei': 'bn', 'Bulgaria': 'bg', 'Burkina Faso': 'bf', 'Burundi': 'bi', 'Cambodia': 'kh', 'Cameroon': 'cm', 'Canada': 'ca', 'Cape Verde': 'cv', 'Cayman Islands': 'ky', 'Central African Republic': 'cf', 'Chad': 'td', 'Chile': 'cl', 'China': 'cn', 'Christmas Island': 'cx', 'Cocos (Keeling) Islands': 'cc', 'Colombia': 'co', 'Comoros': 'km', 'Congo': 'cg', 'Congo, the Democratic Republic of the': 'cd', 'Cook Islands': 'ck', 'Costa Rica': 'cr', "Côte d'Ivoire": 'ci', 'Ivory Coast': 'ci', 'Croatia': 'hr', 'Cuba': 'cu', 'Cyprus': 'cy', 'Czech Republic': 'cz', 'Denmark': 'dk', 'Djibouti': 'dj', 'Dominica': 'dm', 'Dominican Republic': 'do', 'Ecuador': 'ec', 'Egypt': 'eg', 'El Salvador': 'sv', 'Equatorial Guinea': 'gq', 'Eritrea': 'er', 'Estonia': 'ee', 'Ethiopia': 'et', 'Falkland Islands (Malvinas)': 'fk', 'Faroe Islands': 'fo', 'Fiji': 'fj', 'Finland': 'fi', 'France': 'fr', 'French Guiana': 'gf', 'French Polynesia': 'pf', 'French Southern Territories': 'tf', 'Gabon': 'ga', 'Gambia': 'gm', 'Georgia': 'ge', 'Germany': 'de', 'Ghana': 'gh', 'Gibraltar': 'gi', 'Greece': 'gr', 'Greenland': 'gl', 'Grenada': 'gd', 'Guadeloupe': 'gp', 'Guam': 'gu', 'Guatemala': 'gt', 'Guernsey': 'gg', 'Guinea': 'gn', 'Guinea-Bissau': 'gw', 'Guyana': 'gy', 'Haiti': 'ht', 'Heard Island and McDonald Islands': 'hm', 'Holy See (Vatican City State)': 'va', 'Honduras': 'hn', 'Hong Kong': 'hk', 'Hungary': 'hu', 'Iceland': 'is', 'India': 'in', 'Indonesia': 'id', 'Iran, Islamic Republic of': 'ir', 'Iraq': 'iq', 'Ireland': 'ie', 'Isle of Man': 'im', 'Israel': 'il', 'Italy': 'it', 'Jamaica': 'jm', 'Japan': 'jp', 'Jersey': 'je', 'Jordan': 'jo', 'Kazakhstan': 'kz', 'Kenya': 'ke', 'Kiribati': 'ki', "Korea, Democratic People's Republic of": 'kp', 'Korea, Republic of': 'kr', 'South Korea': 'kr', 'Kuwait': 'kw', 'Kyrgyzstan': 'kg', "Lao People's Democratic Republic": 'la', 'Latvia': 'lv', 'Lebanon': 'lb', 'Lesotho': 'ls', 'Liberia': 'lr', 'Libyan Arab Jamahiriya': 'ly', 'Libya': 'ly', 'Liechtenstein': 'li', 'Lithuania': 'lt', 'Luxembourg': 'lu', 'Macao': 'mo', 'Macedonia, the former Yugoslav Republic of': 'mk', 'Madagascar': 'mg', 'Malawi': 'mw', 'Malaysia': 'my', 'Maldives': 'mv', 'Mali': 'ml', 'Malta': 'mt', 'Marshall Islands': 'mh', 'Martinique': 'mq', 'Mauritania': 'mr', 'Mauritius': 'mu', 'Mayotte': 'yt', 'Mexico': 'mx', 'Micronesia, Federated States of': 'fm', 'Moldova, Republic of': 'md', 'Monaco': 'mc', 'Mongolia': 'mn', 'Montenegro': 'me', 'Montserrat': 'ms', 'Morocco': 'ma', 'Mozambique': 'mz', 'Myanmar': 'mm', 'Burma': 'mm', 'Namibia': 'na', 'Nauru': 'nr', 'Nepal': 'np', 'Netherlands': 'nl', 'Netherlands Antilles': 'an', 'New Caledonia': 'nc', 'New Zealand': 'nz', 'Nicaragua': 'ni', 'Niger': 'ne', 'Nigeria': 'ng', 'Niue': 'nu', 'Norfolk Island': 'nf', 'Northern Mariana Islands': 'mp', 'Norway': 'no', 'Oman': 'om', 'Pakistan': 'pk', 'Palau': 'pw', 'Palestinian Territory, Occupied': 'ps', 'Panama': 'pa', 'Papua New Guinea': 'pg', 'Paraguay': 'py', 'Peru': 'pe', 'Philippines': 'ph', 'Pitcairn': 'pn', 'Poland': 'pl', 'Portugal': 'pt', 'Puerto Rico': 'pr', 'Qatar': 'qa', 'Réunion': 're', 'Romania': 'ro', 'Russian Federation': 'ru', 'Russia': 'ru', 'Rwanda': 'rw', 'Saint Helena, Ascension and Tristan da Cunha': 'sh', 'Saint Kitts and Nevis': 'kn', 'Saint Lucia': 'lc', 'Saint Pierre and Miquelon': 'pm', 'Saint Vincent and the Grenadines': 'vc', 'Saint Vincent & the Grenadines': 'vc', 'St. Vincent and the Grenadines': 'vc', 'Samoa': 'ws', 'San Marino': 'sm', 'Sao Tome and Principe': 'st', 'Saudi Arabia': 'sa', 'Senegal': 'sn', 'Serbia': 'rs', 'Seychelles': 'sc', 'Sierra Leone': 'sl', 'Singapore': 'sg', 'Slovakia': 'sk', 'Slovenia': 'si', 'Solomon Islands': 'sb', 'Somalia': 'so', 'South Africa': 'za', 'South Georgia and the South Sandwich Islands': 'gs', 'South Sudan': 'ss', 'Spain': 'es', 'Sri Lanka': 'lk', 'Sudan': 'sd', 'Suriname': 'sr', 'Svalbard and Jan Mayen': 'sj', 'Swaziland': 'sz', 'Sweden': 'se', 'Switzerland': 'ch', 'Syrian Arab Republic': 'sy', 'Taiwan, Province of China': 'tw', 'Taiwan': 'tw', 'Tajikistan': 'tj', 'Tanzania': 'tz', 'Thailand': 'th', 'Timor-Leste': 'tl', 'Togo': 'tg', 'Tokelau': 'tk', 'Tonga': 'to', 'Trinidad and Tobago': 'tt', 'Tunisia': 'tn', 'Turkey': 'tr', 'Turkmenistan': 'tm', 'Turks and Caicos Islands': 'tc', 'Tuvalu': 'tv', 'Uganda': 'ug', 'Ukraine': 'ua', 'United Arab Emirates': 'ae', 'United Kingdom': 'gb', 'United States': 'us', 'United States Minor Outlying Islands': 'um', 'Uruguay': 'uy', 'Uzbekistan': 'uz', 'Vanuatu': 'vu', 'Venezuela, Bolivarian Republic of': 've', 'Venezuela': 've', 'Viet Nam': 'vn', 'Vietnam': 'vn', 'Virgin Islands, British': 'vg', 'Virgin Islands, U.S.': 'vi', 'Wallis and Futuna': 'wf', 'Western Sahara': 'eh', 'Yemen': 'ye', 'Zambia': 'zm', 'Zimbabwe': 'zw'
   }
# st.image("Con_Flags/"+flags['Afghanistan']+".png",width=50)
# flags = pd.read_csv('Flag.csv',index_col="Country").T.to_dict("index")
# print(flags)



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

def traffic(df,index = "country",visType="Des",check="nice",present=pd.DataFrame()):
    print(df)
    # df=df.transpose()
    # c1.write(df)
    # df.index.name=None
    # plt.style.use(plt_style)
    for i in df.columns:
        print(i)
        d1,d2 = st.columns([1,15])
        d1.image("Con_Flags/"+flags[i]+".png",width=50)
        d2.subheader(str.upper(i))
        
        st.metric("Food Systems Resilience Score", np.round(df[i].mean(),2))

        c1,c2,c3,c4,c5 = st.columns(5)

        colored = df.sort_values(i,ascending=True).copy()[[i]]
        print(colored.head())
        
        colored["Color"] = "green"
        colored.loc[colored[i]<40,"Color"] = "red"
        colored.loc[(colored[i]>=40) & (colored[i]<80),"Color"]= "yellow"
        # colored.index = colored.index.map(all_factors1)

        print(colored)
               
        nat = colored[colored.index.isin(natural1)]
        hum =colored[colored.index.isin(human1)]
        soc = colored[colored.index.isin(social1)]
        fin = colored[colored.index.isin(financial1)]
        man = colored[colored.index.isin(manufactured1)]
        print(nat)
        coloredPlot(nat,c1,"Natural",i)
        coloredPlot(hum,c2,"Human",i)
        coloredPlot(soc,c3,"Social",i)
        coloredPlot(fin,c4,"Financial",i)
        coloredPlot(man,c5,"Manufactured",i)


def showPlot(df,index = "country",visType="Des",check="nice",present=pd.DataFrame()):
    
    

    print(df)
    # df.index = df["Country"]

    # plt.style.use(plt_style)
    for i in df.columns:
        print(i)
        
        

        if i in all_factors1.keys():
            st.subheader(str.upper(all_factors1[i]))
            df["Color"] = "green"
            df.loc[df[i]<40,"Color"] = "red"
            df.loc[(df[i]>=40) & (df[i]<80),"Color"]= "yellow"
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
        c = st.columns(4)


        

        if visType == "Income Category":
            k=0
            for j in df1["Income Group"].unique():
            
                fd = df1[df1["Income Group"]==j].sort_values(i,ascending=True)
                fd.index = fd["Country"]
                # print(c)
                coloredPlot(fd,c[k],j,i)
                k=k+1
        else:
            k=0
            for j in df1["Region"].unique():
            
                fd = df1[df1["Region"]==j].sort_values(i,ascending=True)
                fd.index = fd["Country"]
                # print(c)
                coloredPlot(fd,c[k],j,i)
                k=k+1

                if(k>3):
                    k=0






def showOption():
    opts = ['Country','Indicator']
    op = st.sidebar.selectbox('Analysis by:',opts)
    return op

def visualizeOp(op,yearChoice=2020):
    global dataColl
    if(isinstance(yearChoice,list)):
        if(len(yearChoice)==1):
            yearChoice = yearChoice[0]
        else:
            yearChoice=2020
    # trans_data=dataColl[yearChoice]
    if op=="Country":
        countrySelect = st.sidebar.multiselect('Select Country(ies)',countries)
        print("choice of year = " + str(yearChoice))
        # abc = abc.append(i for i in countrySelect)
        # org_data=pd.read_csv(DATA_URL + "\\"+str(yearChoice)+'.csv',index_col= 'Country')
        org_data=dataColl[yearChoice]
        # df = org_data[countrySelect]
        df = org_data[org_data.index.isin(countrySelect)].transpose()
        print(df)
        traffic(df,index = "indicator")
        # showPlot(df,index='indicator')

     
    else:
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
        # indSelect1 = st.sidebar.multiselect('Select indicator(s)',all_factors.keys())
        # # trans_data=pd.read_csv(DATA_URL + "\\"+str(yearChoice)+'.csv',index_col= 'Country').transpose()
        # indSelect = [all_factors[i] for i in indSelect1]
        # print("choice of year = " + str(yearChoice))
        
        # print(trans_data)
        # print(all_factors[indicator1])
        print(trans_data)
        df1 = trans_data.loc[:,[all_factors[indicator1]]]
        print(df1)

        showPlot(df1,index='country',visType=vistype)



def app():
    yearChoice =  st.sidebar.selectbox('Select Year(s)',sorted(list(years),reverse=True))
    op =showOption()
    visualizeOp(op,yearChoice)