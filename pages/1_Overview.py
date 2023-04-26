##===================================================================================
## Projeto Final
## 1 - Importação das bibliotecas necessárias
import pandas as pd
import io
import re
import numpy as np
from datetime import date, datetime
import plotly.express as px
import plotly.graph_objects as go
import folium
from haversine import haversine
import streamlit as st
from PIL import Image
from streamlit_folium import folium_static

st.set_page_config(page_title='Overview', layout='wide')
##===================================================================================
## 2 - Importação do DataFrame
#df = pd.read_csv('/home/alan/Documents/repos/projeto_final/dataset/zomato.csv')
#df = pd.read_csv('/home/alan/Documents/repos/projeto_marketplace_zero_hunger/dataset/zomato.csv')
#df = pd.read_csv('../dataset/zomato.csv')
#df = pd.read_csv('/dataset/zomato.csv')
df = pd.read_csv('dataset/zomato.csv')
#df = pd.read_csv('/home/alan/Documents/repos/projeto_marketplace_zero_hunger/dataset/zomato.csv')

##===================================================================================
### 3 - Limpeza dos dados vazios
linhas_vazias = (df['Restaurant Name'] != 'NaN')
df = df.loc[linhas_vazias, :].copy()

linhas_vazias = (df['Country Code'] != 'NaN')
df = df.loc[linhas_vazias, :].copy()

linhas_vazias = (df['City'] != 'NaN')
df = df.loc[linhas_vazias, :].copy()

linhas_vazias = (df['Address'] != 'NaN')
df = df.loc[linhas_vazias, :].copy()

linhas_vazias = (df['Locality'] != 'NaN')
df = df.loc[linhas_vazias, :].copy()

linhas_vazias = (df['Locality Verbose'] != 'NaN')
df = df.loc[linhas_vazias, :].copy()

linhas_vazias = (df['Cuisines'] != 'NaN')
df = df.loc[linhas_vazias, :].copy()

linhas_vazias = (df['Average Cost for two'] != 'NaN')
df = df.loc[linhas_vazias, :].copy()

linhas_vazias = (df['Currency'] != 'NaN')
df = df.loc[linhas_vazias, :].copy()

linhas_vazias = (df['Has Table booking'] != 'NaN')
df = df.loc[linhas_vazias, :].copy()

linhas_vazias = (df['Has Online delivery'] != 'NaN')
df = df.loc[linhas_vazias, :].copy()

linhas_vazias = (df['Switch to order menu'] != 'NaN')
df = df.loc[linhas_vazias, :].copy()

linhas_vazias = (df['Price range'] != 'NaN')
df = df.loc[linhas_vazias, :].copy()

linhas_vazias = (df['Aggregate rating'] != 'NaN')
df = df.loc[linhas_vazias, :].copy()

linhas_vazias = (df['Rating color'] != 'NaN')
df = df.loc[linhas_vazias, :].copy()

linhas_vazias = (df['Rating text'] != 'NaN')
df = df.loc[linhas_vazias, :].copy()

linhas_vazias = (df['Votes'] != 'NaN')
df = df.loc[linhas_vazias, :].copy()

##===================================================================================
# 3 - Criando a coluna Country Code - Corresponde ao código de Cada País
# Criando a coluna Country Code - Corresponde ao código de Cada País
COUNTRIES = {
1: "India",
14: "Australia",
30: "Brazil",
37: "Canada",
94: "Indonesia",
148: "New Zeland",
162: "Philippines",
166: "Qatar",
184: "Singapure",
189: "South Africa",
191: "Sri Lanka",
208: "Turkey",
214: "United Arab Emirates",
215: "England",
216: "United States of America",
}

df['Country Name'] = df['Country Code'].map(COUNTRIES)

COLORS = {
"3F7E00": "darkgreen",
"5BA829": "green",
"9ACD32": "lightgreen",
"CDD614": "orange",
"FFBA00": "red",
"CBCBC8": "darkred",
"FF7800": "darkred",
}

df['Color'] = df['Rating color'].map(COLORS)

##===================================================================================
## 4 - # Sidebar - Barra Lateral
st.header("Marketplace - Overview")
st.sidebar.markdown("### Dashboard - Control")


image_path = '../projeto_marketplace_zero_hunger/logo.webp'
image = Image.open(image_path)
st.sidebar.image(image, width=120)
st.sidebar.markdown("""___""")

##===================================================================================
# Filter  - options_country  
options_country = st.sidebar.multiselect(
    'Select Country:',
    ['India', 'Australia', 'Brazil', 'Canada', 'Indonesia', 'New Zeland', 'Philippines', 'Qatar', 'Singapure', 'South Africa', 'Sri Lanka', 'Turkey', 'United Arab Emirates', 'England', 'United States of America'],
    default= ['India', 'Australia', 'Brazil', 'Canada', 'Indonesia', 'New Zeland', 'Philippines', 'Qatar', 'Singapure', 'South Africa', 'Sri Lanka', 'Turkey', 'United Arab Emirates', 'England', 'United States of America'])

country_filter = df['Country Name'].isin( options_country)
df = df.loc[country_filter, :]




##===================================================================================
# Footer
st.sidebar.markdown("""___""")
st.sidebar.markdown("##### Developed by: ")
st.sidebar.markdown("#### Alan Mota - Data Scientist ")
##===================================================================================
##===================================================================================
##===================================================================================
 
##===================================================================================
## 5 - Layout no Streamlit
tab1, tab2 = st.tabs(['Marketplace - Overview', '--'])

with tab1:
    with st.container():
        col1, col2, col3  = st.columns(3)
        
        with col1:
            st.markdown("###### Unique Restaurants Registered")
            quant_rest = (len(df.loc[:, ['Restaurant ID', 'Restaurant Name']].groupby('Restaurant ID').nunique()))
            st.metric("", quant_rest)
            
            
        with col2:
            st.markdown("###### Unique Countries Registered")
            countries_rest = (len(df.loc[:, ['Country Code', 'Country Name']].groupby('Country Code').nunique()))
            st.metric("", countries_rest)
            
        with col3:
            st.markdown("###### Single Registered Cities")
            quant_cities = (len(df.loc[:,['City']].groupby(['City']).nunique()))
            st.metric("", quant_cities)
      
    st.markdown("""___""")            
    with st.container():
        col1, col2, col3  = st.columns(3) 
        
        with col1:
            st.markdown("###### Total Evaluations Done")
            total_done = (df['Votes'].sum())
            st.metric("", total_done)
            
            
        with col2:
            st.markdown("###### Total Types of Cuisine")
            total_types_cuisine = (len(df.loc[:,['Cuisines']].groupby(['Cuisines']).nunique()))
            st.metric("", total_types_cuisine)
            
        with col3:
            st.markdown("###### Standard Deviation")
            standard_deviation = np.round(df['Aggregate rating'].std(),2)
            st.metric("", standard_deviation)
            
                        
    st.markdown("""___""")            
    with st.container():
        st.markdown("### 1.1 - Location of restaurants in countries and cities")
        df_aux = df.loc[:, ['City', 'Latitude', 'Longitude']].groupby(['City']).median().reset_index()

        map_ = folium.Map()

        for i in range( len( df_aux ) ):
            folium.Marker( [df_aux.loc[i, 'Latitude'], df_aux.loc[i, 'Longitude']]).add_to(map_)
        
        folium_static(map_, width=1024 , height=720)
    
        