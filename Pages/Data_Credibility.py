import streamlit as st
import pandas as pd


alldata1 = pd.read_csv("allIndicatorData1.csv")
notCountry = ['World','High income', 'Low income',
 'Lower middle income', 'Upper middle income', 'East Asia & Pacific',
 'Europe & Central Asia', 'Latin America & Caribbean',
 'Middle East & North Africa', 'North America', 'South Asia',
 'Sub-Saharan Africa']
countries = alldata1[~alldata1["Country"].isin(notCountry)]["Country"].unique()

capitals = ['Natural Capital','Human Capital','Social Capital','Financial Capital','Manufactured Capital']

capitals1 = ['Food Systems Resilience Score','Natural Capital','Human Capital','Social Capital','Financial Capital','Manufactured Capital']

dd = {}
dd['Natural Capital'] = ['Agricultural Water Quality','Agricultural Water Quantity','Biodiversity and Habitat','Ecosystem Services','Forest Change','Green House Emission Per Capita','Land Degradation','Natural Hazard Exposure','Soil Organic Content']
dd['Human Capital'] = ['Access to Agricultural Resources','Food Dietary Diversity','Food Loss','Food Safety','Food Supply Sufficiency','Labor Force Participation Rate','Literacy Rate','Micronutrient Availability','Population Growth Rate','Poverty Population','Protein Quality']
dd['Social Capital'] = ['Agricultural Women Empowerment','Armed Conflict','Community Organizations','Corruption','Dependency on Chronic Food Aid','Food Safety Net Programs','Food Security Policy Commitment','Gender Equality','Nutritional Standards','Political Stability Risk']
dd['Financial Capital'] = ['Access to Diversified Financial Services','Access to Financial Services','Agricultural GDP','Agricultural Production Volatility','Agricultural Trade','Food Price Volatility','Income Inequality','Per Capita GDP']
dd['Manufactured Capital'] = ['Agricultural R&D','Crop Storage Facilities','Disaster Risk Management','Early Warning Measures','Irrigation Infrastructure','KOFGI Globalization Index','Supply Chain Infrastructure','Sustainable Agriculture','Telecommunications']


natural = ['Agricultural Water Quality','Agricultural Water Quantity','Biodiversity and Habitat','Ecosystem Services','Forest Change','Green House Emission Per Capita','Land Degradation','Natural Hazard Exposure','Soil Organic Content']
human = ['Access to Agricultural Resources','Food Dietary Diversity','Food Loss','Food Safety','Food Supply Sufficiency','Labor Force Participation Rate','Literacy Rate','Micronutrient Availability','Population Growth Rate','Poverty Population','Protein Quality']
social = ['Agricultural Women Empowerment','Armed Conflict','Community Organizations','Corruption','Dependency on Chronic Food Aid','Food Safety Net Programs','Food Security Policy Commitment','Gender Equality','Nutritional Standards','Political Stability Risk']
financial = ['Access to Diversified Financial Services','Access to Financial Services','Agricultural GDP','Agricultural Production Volatility','Agricultural Trade','Food Price Volatility','Income Inequality','Per Capita GDP']
manufactured = ['Agricultural R&D','Crop Storage Facilities','Disaster Risk Management','Early Warning Measures','Irrigation Infrastructure','KOFGI Globalization Index','Supply Chain Infrastructure','Sustainable Agriculture','Telecommunications']
flags = {
   'Afghanistan': 'af', 'Albania': 'al', 'Algeria': 'dz', 'American Samoa': 'as', 'Andorra': 'ad', 'Angola': 'ao', 'Anguilla': 'ai', 'Antarctica': 'aq', 'Antigua and Barbuda': 'ag', 'Argentina': 'ar', 'Armenia': 'am', 'Aruba': 'aw', 'Australia': 'au', 'Austria': 'at', 'Azerbaijan': 'az', 'Bahamas': 'bs', 'Bahrain': 'bh', 'Bangladesh': 'bd', 'Barbados': 'bb', 'Belarus': 'by', 'Belgium': 'be', 'Belize': 'bz', 'Benin': 'bj', 'Bermuda': 'bm', 'Bhutan': 'bt', 'Bolivia, Plurinational State of': 'bo', 'Bolivia': 'bo', 'Bosnia and Herzegovina': 'ba', 'Botswana': 'bw', 'Bouvet Island': 'bv', 'Brazil': 'br', 'British Indian Ocean Territory': 'io', 'Brunei Darussalam': 'bn', 'Brunei': 'bn', 'Bulgaria': 'bg', 'Burkina Faso': 'bf', 'Burundi': 'bi', 'Cambodia': 'kh', 'Cameroon': 'cm', 'Canada': 'ca', 'Cape Verde': 'cv', 'Cayman Islands': 'ky', 'Central African Republic': 'cf', 'Chad': 'td', 'Chile': 'cl', 'China': 'cn', 'Christmas Island': 'cx', 'Cocos (Keeling) Islands': 'cc', 'Colombia': 'co', 'Comoros': 'km', 'Congo': 'cg', 'DR Congo':'cd','Congo, the Democratic Republic of the': 'cd', 'Cook Islands': 'ck', 'Costa Rica': 'cr', "Côte d'Ivoire": 'ci', 'Ivory Coast': 'ci', 'Croatia': 'hr', 'Cuba': 'cu', 'Cyprus': 'cy', 'Czech Republic': 'cz', 'Denmark': 'dk', 'Djibouti': 'dj', 'Dominica': 'dm', 'Dominican Republic': 'do', 'Ecuador': 'ec', 'Egypt': 'eg', 'El Salvador': 'sv', 'Equatorial Guinea': 'gq', 'Eritrea': 'er', 'Estonia': 'ee', 'Ethiopia': 'et', 'Falkland Islands (Malvinas)': 'fk', 'Faroe Islands': 'fo', 'Fiji': 'fj', 'Finland': 'fi', 'France': 'fr', 'French Guiana': 'gf', 'French Polynesia': 'pf', 'French Southern Territories': 'tf', 'Gabon': 'ga', 'Gambia': 'gm', 'Georgia': 'ge', 'Germany': 'de', 'Ghana': 'gh', 'Gibraltar': 'gi', 'Greece': 'gr', 'Greenland': 'gl', 'Grenada': 'gd', 'Guadeloupe': 'gp', 'Guam': 'gu', 'Guatemala': 'gt', 'Guernsey': 'gg', 'Guinea': 'gn', 'Guinea-Bissau': 'gw', 'Guyana': 'gy', 'Haiti': 'ht', 'Heard Island and McDonald Islands': 'hm', 'Holy See (Vatican City State)': 'va', 'Honduras': 'hn', 'Hong Kong': 'hk', 'Hungary': 'hu', 'Iceland': 'is', 'India': 'in', 'Indonesia': 'id', 'Iran, Islamic Republic of': 'ir', 'Iraq': 'iq', 'Ireland': 'ie', 'Isle of Man': 'im', 'Israel': 'il', 'Italy': 'it', 'Jamaica': 'jm', 'Japan': 'jp', 'Jersey': 'je', 'Jordan': 'jo', 'Kazakhstan': 'kz', 'Kenya': 'ke', 'Kiribati': 'ki', "Korea, Democratic People's Republic of": 'kp', 'Korea, Republic of': 'kr', 'South Korea': 'kr', 'Kuwait': 'kw', 'Kyrgyzstan': 'kg', "Lao People's Democratic Republic": 'la', 'Latvia': 'lv', 'Lebanon': 'lb', 'Lesotho': 'ls', 'Liberia': 'lr', 'Libyan Arab Jamahiriya': 'ly', 'Libya': 'ly', 'Liechtenstein': 'li', 'Lithuania': 'lt', 'Luxembourg': 'lu', 'Macao': 'mo', 'Macedonia, the former Yugoslav Republic of': 'mk', 'Madagascar': 'mg', 'Malawi': 'mw', 'Malaysia': 'my', 'Maldives': 'mv', 'Mali': 'ml', 'Malta': 'mt', 'Marshall Islands': 'mh', 'Martinique': 'mq', 'Mauritania': 'mr', 'Mauritius': 'mu', 'Mayotte': 'yt', 'Mexico': 'mx', 'Micronesia, Federated States of': 'fm', 'Moldova, Republic of': 'md', 'Monaco': 'mc', 'Mongolia': 'mn', 'Montenegro': 'me', 'Montserrat': 'ms', 'Morocco': 'ma', 'Mozambique': 'mz', 'Myanmar': 'mm', 'Burma': 'mm', 'Namibia': 'na', 'Nauru': 'nr', 'Nepal': 'np', 'Netherlands': 'nl', 'Netherlands Antilles': 'an', 'New Caledonia': 'nc', 'New Zealand': 'nz', 'Nicaragua': 'ni', 'Niger': 'ne', 'Nigeria': 'ng', 'Niue': 'nu', 'Norfolk Island': 'nf', 'Northern Mariana Islands': 'mp', 'Norway': 'no', 'Oman': 'om', 'Pakistan': 'pk', 'Palau': 'pw', 'Palestinian Territory, Occupied': 'ps', 'Panama': 'pa', 'Papua New Guinea': 'pg', 'Paraguay': 'py', 'Peru': 'pe', 'Philippines': 'ph', 'Pitcairn': 'pn', 'Poland': 'pl', 'Portugal': 'pt', 'Puerto Rico': 'pr', 'Qatar': 'qa', 'Réunion': 're', 'Romania': 'ro', 'Russian Federation': 'ru', 'Russia': 'ru', 'Rwanda': 'rw', 'Saint Helena, Ascension and Tristan da Cunha': 'sh', 'Saint Kitts and Nevis': 'kn', 'Saint Lucia': 'lc', 'Saint Pierre and Miquelon': 'pm', 'Saint Vincent and the Grenadines': 'vc', 'Saint Vincent & the Grenadines': 'vc', 'St. Vincent and the Grenadines': 'vc', 'Samoa': 'ws', 'San Marino': 'sm', 'Sao Tome and Principe': 'st', 'Saudi Arabia': 'sa', 'Senegal': 'sn', 'Serbia': 'rs', 'Seychelles': 'sc', 'Sierra Leone': 'sl', 'Singapore': 'sg', 'Slovakia': 'sk', 'Slovenia': 'si', 'Solomon Islands': 'sb', 'Somalia': 'so', 'South Africa': 'za', 'South Georgia and the South Sandwich Islands': 'gs', 'South Sudan': 'ss', 'Spain': 'es', 'Sri Lanka': 'lk', 'Sudan': 'sd', 'Suriname': 'sr', 'Svalbard and Jan Mayen': 'sj', 'Swaziland': 'sz', 'Sweden': 'se', 'Switzerland': 'ch', 'Syrian Arab Republic': 'sy', 'Taiwan, Province of China': 'tw', 'Taiwan': 'tw', 'Tajikistan': 'tj', 'Tanzania': 'tz', 'Thailand': 'th', 'Timor-Leste': 'tl', 'Togo': 'tg', 'Tokelau': 'tk', 'Tonga': 'to', 'Trinidad and Tobago': 'tt', 'Tunisia': 'tn', 'Turkey': 'tr', 'Turkmenistan': 'tm', 'Turks and Caicos Islands': 'tc', 'Tuvalu': 'tv', 'Uganda': 'ug', 'Ukraine': 'ua', 'United Arab Emirates': 'ae', 'United Kingdom': 'gb', 'United States': 'us', 'United States of America':'us','United States Minor Outlying Islands': 'um', 'Uruguay': 'uy', 'Uzbekistan': 'uz', 'Vanuatu': 'vu', 'Venezuela, Bolivarian Republic of': 've', 'Venezuela': 've', 'Viet Nam': 'vn', 'Vietnam': 'vn', 'Virgin Islands, British': 'vg', 'Virgin Islands, U.S.': 'vi', 'Wallis and Futuna': 'wf', 'Western Sahara': 'eh', 'Yemen': 'ye', 'Zambia': 'zm', 'Zimbabwe': 'zw'
   }


dataInfo = pd.read_csv('DataSource.csv')
print(dataInfo.head())

def app():
    choice = st.sidebar.selectbox("Data Check by: ", ["Country","Indicator"])
    if choice=="Country":
        country = st.sidebar.selectbox("Country: ", countries)
        df = alldata1[alldata1['Country']==country].drop_duplicates(["Country","Indicator"],keep='last').drop(columns = ["value","Income Group","Region"])
        try:
            st.image("Con_Flags/"+flags[country]+".png",width=100)
            st.subheader(str.upper(country))
        except:
            st.subheader(str.upper(country))
        # print(df["Indicator"].unique())
        st.subheader("Available Indicators: "+ str(len(df[~df["Indicator"].isin(capitals1)])))

        for i in capitals:
            st.subheader(i)
            temp = df[df["Indicator"].isin(dd[i])]
            for k in temp["Indicator"].unique():
                st.write(k+', '+str(temp[temp["Indicator"]==k]["Year"].iloc[0]))
        
    else:
        capital = st.sidebar.selectbox('Capital',['Natural Capital','Human Capital','Social Capital','Financial Capital','Manufactured Capital'])
        indicator1=None
        if capital=="Natural Capital":
            indicator1 = st.sidebar.selectbox("Indicator",natural)
        elif capital=="Human Capital":
            indicator1 = st.sidebar.selectbox("Indicator",human)
        elif capital=="Social Capital":
            indicator1 = st.sidebar.selectbox("Indicator",social)
        elif capital=="Financial Capital":
            indicator1 = st.sidebar.selectbox("Indicator",financial)
        elif capital=="Manufactured Capital":
            indicator1 = st.sidebar.selectbox("Indicator",manufactured)
        else:
            indicator1 = "Food Systems Resilience Score"
        df = alldata1.dropna(subset=['value'])[(alldata1['Indicator']==indicator1)].drop_duplicates(["Country","Indicator"],keep = 'last').drop(columns = ["value","Income Group","Region"])
        df =df[~df['Country'].isin(notCountry)]
        st.subheader(indicator1)
        print(indicator1)
        print(dataInfo[dataInfo["Indicator"]==indicator1])
        st.subheader("Countries Covered: " + str(dataInfo[datuaInfo["Indicator"]==indicator1]["#Countries"].iloc[0]))
        text_html = "<h3> Source: <a href = '{}'> {}</a> </h3>".format(dataInfo[dataInfo["Indicator"]==indicator1]["Link"].iloc[0],dataInfo[dataInfo["Indicator"]==indicator1]["Source"].iloc[0])
        print(text_html)
        st.markdown(text_html,unsafe_allow_html=True)
        print(df["Country"].unique())


    



