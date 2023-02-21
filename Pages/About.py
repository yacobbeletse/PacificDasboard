import streamlit as st



def app():
    about = st.sidebar.selectbox("More about...", ["Abstract","Using the Tool", "Adapted Five-Capitals Framework"])
    
    showText(about)
    



def showText(option):
    abstract = """**Food Systems Resilience Diagnostics Tool**

**Abstract**

The food system is a complex web of actors/agents and interactions that spans production to the consumption of food. The global food system has been severely disrupted by the COVID-19 pandemic putting millions of people at risk of hunger and malnutrition. In a post-COVID-19 era, a stock-take will be required to see how our food system changed in response to current drivers/pressures and what lessons we learnt regarding the actions required to improve its resilience. The ability to understand, interpret, evaluate, and monitor key aspects of the food system is pivotal in building resilient food systems, as it is through this collection and analysis of information that we can improve resource allocation and effective decision-making. Thus, we present a diagnostic tool that can identify and monitor food stress using a food system resilience score. This score is derived from several indicators that describe natural, human, social, financial, and manufactured dimensions of the food system. The tool incorporates three major functionalities - situational awareness, scenario analysis, and intervention analysis. The situational awareness component helps derive a clear understanding of the strengths and weaknesses of food systems, while the scenario analysis component enables the anticipation of how various aspects within food systems may change when exposed to food shocks. The intervention analysis component points out the most effective and realistic interventions against anticipated food shocks. We have constructed the tool so that it can be deployed at various levels to enable better-informed decision-making toward building resilient food systems in the long term."""

    tool ="""
    **A. Using the tool**

**1. About**

This page displays the basic information about the tools with its components. The components of the tool offer different functionalities for food system resilience diagnostics.

**2. Components/Functionalities**


**2.1 World Map**

This component generates color-coded world map based on the value of the indicator chosen in the Control Center. You can also customize the world map for year.


**2.2 Diagnostics**

This component summarizes the strengths and weaknesses of a national food system when the analysis is chosen by “Country”. When the analysis is chosen by “Indicator”, the component lists the best performing and the worst performing countries for the chosen indicator(s). The visualizations can also be customized for analysis years and multiple selections of countries and indicators.

**2.3 Time-Series Analysis**

This component facilitates comparisons of performance of national food systems at a temporal scale. The visualizations in this component can be chosen by either “Country” or “Indicator”. The visualizations also allow for multiple selections of countries and indicators. Five different types of analyses are available in the component.

**Year-on-Year Analysis:** It draws a picture of the current strengths and weaknesses of a national food system when the analysis is chosen by “Country” and the current best performing and worst performing countries when the analysis is chosen by “Indicator” for the chosen year range.

**Country vs Country:** It directly compares a country against other and shows how the scores of the countries in five capitals including overall food system resilience have changed at a temporal scale.
Capitals: It displays the performance of chosen countries for all indicators within the selected capital at a temporal scale.

**Capitals**: It shows the trend of the performance of a selected country for the indicators in the chosen capital.


**2.4 Disaster Vulnerability**

This component represents the vulnerability of countries to several forms of hazards. When the chosen scale is "Global", the component generates a color-coded world map based on the standardized values of either total deaths, total affected, or total economic damages. For the country scale, the component generates a chart that shows the standardized mean impact of several hazards for the chosen country.

**2.5 Compare**
This component allows the comparison of the ranks of the chosen countries for food systems resilience score and five capitals score against the rank of the countries in terms of HDI, the proprotion of undernourished population, and the proportion of food insecure population.
"""
    framework = """
**3. Five Capitals based framework for food system resilience assessment**

**The five capitals approach provides a holistic way to measure value.**

**Table 1: Categorization of the variables under five capitals**

**A positive influence of an indicator signifies higher the indicator more resilient the national food system is and vice-versa.*

|**Indicator**	                    |**Source**	     |**Influence** |
|-------------------|----------------------|----------------------|
|**Natural Capital**  |       |           |           |
|Agricultural Water Quality|	GFSI  	 |Positive   |
|Agricultural Water Quantity|	GFS	|	Positive|
|Biodiversity and Habitat|	EPI	|Positive|
|Ecosystem Services|	EPI		|Positive|
|Forest Change|	GFSI, World Bank	|	Negative|
|Green House Emission Per Capita|	EPI	|	Negative|
|Land Degradation|	GFSI, UN		|Negative|
|Natural Hazard Exposures|	GFSI, ND-GAIN	|	Negative|
|Soil Organic Content|	GFSI, FAO	|	Positive|
|-------------------|----------------------|----------------------|
|**Human Capital** | | | |
|Access to Agricultural Resources|	GFSI, UN|	Positive|
|Food Dietary Diversity	|GFSI	|Positive|
|Food Loss|	GFSI, FAO|	Negative|
|Food Safety|	GFSI|	Positive|
|Food Supply Sufficiency|	GFSI, FAO|	Positive|
|Labor Force Participation Rate|	World Bank|	Positive|
|Literacy Rate|	World Bank|	Positive|
|Micronutrient Availability|	GFSI, Global Nutrient Database|	Positive|
|Protein Quality | GFSI| Postive |
|-------------------|----------------------|----------------------|
|**Social Capital** ||||
|Agricultural Women Empowerment|	GFSI|	Positive|
|Armed Conflict|	GFSI|	Negative|
|Community Organizations|	GFSI|	Positive|
|Corruption|	GFSI|	Negative|
|Dependency on Chronic Food Aid|	GFSI, OECD|	Negative|
|Food Safety Net Programs|	GFSI|	Positive|
|Food Security Policy Commitment|	GFSI|	Positive|
|Gender Equality|	GFSI, UNDP|	Positive|
|Nutritional Standards|	GFSI|	Positive|
|Political Stability Risks|	GFSI|	Negative|
|-------------------|----------------------|----------------------|
|**Financial Capital**|
|Access to Diversified Financial Services|	GFSI|	Positive|
|Access to Financial Services|	GFSI|	Positive|
|Agricultural GDP|	FAO|	Negative|
|Agricultural Production Volatility|	GFSI|	Negative|
|Agricultural Trade|	GFSI|	Positive|
|Food Price Volatility|	GFSI, FAO|	Negative|
|Income Inequality|	GFSI,UNDP|	Negative|
|-------------------|----------------------|----------------------|
|**Manufactured Capital**||||
|Adaptation of Innovative Technologies|	GFSI|	Positive|
|Agricultural R&D Expenses|	GFSI|	Positive|
|Crop Storage Facilities|	GFSI|	Positive|
|Disaster Risk Management|	GFSI|	Positive|
|Irrigation Infrastructure|	GFSI, FAO|	Positive|
|KOFGI Globalization Index|	KOFGI|	Positive|
|Supply Chain Infrastructure|	GFSI, World Bank|	Positive|
|Sustainable Agriculture|	GFSI|	Positive|
|Telecommunications|	GFSI, ITU|	Positive|
|Early Warning Measures|	GFSI, CCAFS|	Positive|   
"""    
    if option=="Abstract":
        st.markdown(abstract)
    elif option =="Using the Tool":
        st.markdown(tool)
    else:
        st.markdown(framework)
    

    # st.subheader('Abstract')
    # st.write('The food system is a complex web of actors/agents and interactions that spans production to the consumption of food. The global food system has been severely disrupted by the COVID-19 pandemic putting millions of people at risk of hunger and malnutrition. In a post-COVID-19 era, a stock-take will be required to see how our food system changed in response to current drivers/pressures and what lessons we learnt regarding the actions required to improve its resilience. The ability to understand, interpret, evaluate, and monitor key aspects of the food system is pivotal in building resilient food systems, as it is through this collection and analysis of information that we can improve resource allocation and effective decision-making. Thus, we present a diagnostic tool that can identify and monitor food stress using a food system resilience score. This score is derived from several indicators that describe natural, human, social, financial, and manufactured dimensions of the food system. The tool incorporates three major functionalities - situational awareness, scenario analysis, and intervention analysis. The situational awareness component helps derive a clear understanding of the strengths and weaknesses of food systems, while the scenario analysis component enables the anticipation of how various aspects within food systems may change when exposed to food shocks. The intervention analysis component points out the most effective and realistic interventions against anticipated food shocks. We have constructed the tool so that it can be deployed at various levels to enable better-informed decision-making toward building resilient food systems in the long term.')
