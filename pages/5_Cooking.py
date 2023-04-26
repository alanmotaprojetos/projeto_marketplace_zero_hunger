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

st.set_page_config(page_title='Cooking', layout='wide')
##===================================================================================
## 2 - Importação do DataFrame
#df = pd.read_csv('/home/alan/Documents/repos/projeto_final/dataset/zomato.csv')
#df = pd.read_csv('/home/alan/Documents/repos/projeto_marketplace_zero_hunger/dataset/zomato.csv')
#df = pd.read_csv('../dataset/zomato.csv')
#df = pd.read_csv('/dataset/zomato.csv')
#df = pd.read_csv('/home/alan/Documents/repos/projeto_marketplace_zero_hunger/dataset/zomato.csv')
df = pd.read_csv('dataset/zomato.csv')
##===================================================================================
##===================================================================================
## Funções 
##===================================================================================
### 3 - Limpeza dos dados vazios
def clean_code( df ): 
    """ Função: Limpeza dos dados vazios 
        Tipo de limpeza:
        1 - Remoção dos dados vazios no DataFrame (Nan).
        
        Input: Dataframe
        Output: Dataframe
    """
    
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
    
    return df
##===================================================================================
def country_code( df ): 
    
    """ Função: Criando a coluna Country Code
        1 - Criando a coluna Country Code - Corresponde ao código de Cada País
        
        Input: Dataframe
        Output: Dataframe
    """

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
    return df

##===================================================================================
## Acionamento das Funções
##===================================================================================
df = clean_code( df )
df = country_code ( df )


##===================================================================================
##===================================================================================
## 4 - # Sidebar - Barra Lateral
st.header("Marketplace - Analytical Data")
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
##===================================================================================
# Footer
st.sidebar.markdown("""___""")
st.sidebar.markdown("##### Developed by: ")
st.sidebar.markdown("#### Alan Mota - Data Scientist ")
##===================================================================================
 
 
##===================================================================================
## 5 - Layout no Streamlit
tab1, tab2 = st.tabs(['Marketplace - Types of Cooking', '--'])

with tab1:
    with st.container():
        st.markdown("##### 5.1 - Italian cuisine restaurants with the highest average rating (Rating >= 4.8 ).")
        max_10_aggregate_rating_italian = df.loc[((df['Cuisines'] == 'Italian') & (df['Aggregate rating'] >= 4.8)), ['Restaurant Name','Aggregate rating']].groupby('Restaurant Name').max()
        max_10_aggregate_rating_italian.sort_values('Aggregate rating', ascending=False).head(10).reset_index()
        st.dataframe(data=max_10_aggregate_rating_italian, width=800, height=390, use_container_width=False) 
   
    st.markdown("""___""")        
    with st.container():
        st.markdown("##### 5.2 - Italian cuisine restaurants with the lowest average rating (Rating == 0.0 ).")
        min_10_aggregate_rating_italian = df.loc[((df['Cuisines'] == 'Italian') & (df['Aggregate rating'] == 0.0)), ['Restaurant Name','Aggregate rating']].groupby('Restaurant Name').max()
        min_10_aggregate_rating_italian.sort_values('Aggregate rating', ascending=False).head(10).reset_index()  
        st.dataframe(data=min_10_aggregate_rating_italian, width=800, height=210, use_container_width=True) 


    st.markdown("""___""")    
    with st.container():
        st.markdown(" ##### 5.3 - American cuisine restaurants with the highest average rating (Rating >= 4.8 ).")
        max_10_aggregate_rating_american =  df.loc[((df['Cuisines'] == 'American') & (df['Aggregate rating'] >= 4.8)), ['Restaurant Name','Aggregate rating']].groupby('Restaurant Name').max()
        max_10_aggregate_rating_american.sort_values('Aggregate rating', ascending=False).head(10).reset_index()  
        st.dataframe(data=max_10_aggregate_rating_american, width=800, height=390, use_container_width=False)
      
      
    st.markdown("""___""")        
    with st.container():
        st.markdown(" ##### 5.4 - American cuisine restaurants with the lowest average rating (Rating == 0.0 ).")
        min_10_aggregate_rating_american = df.loc[((df['Cuisines'] == 'American') & (df['Aggregate rating'] == 0.0)), ['Restaurant Name','Aggregate rating']].groupby('Restaurant Name').max()
        min_10_aggregate_rating_american.sort_values('Aggregate rating', ascending=True).head(10).reset_index()
        st.dataframe(data=min_10_aggregate_rating_american, width=800, height=210, use_container_width=True)
      
      
      
    st.markdown("""___""")        
    with st.container():
        st.markdown(" ##### 5.5 - Arabian cuisine restaurants with the highest average rating (Rating >= 4.0 ).")
        max_10_aggregate_rating_arabian =  df.loc[((df['Cuisines'] == 'Arabian') & (df['Aggregate rating'] >= 4.0)), ['Restaurant Name','Aggregate rating']].groupby('Restaurant Name').max()
        max_10_aggregate_rating_arabian.sort_values('Aggregate rating', ascending=False).head(10).reset_index()
        st.dataframe(data=max_10_aggregate_rating_arabian, width=800, height=210, use_container_width=True)

    st.markdown("""___""")        
    with st.container():
        st.markdown(" ##### 5.6 - Arabian cuisine restaurants with the lowest average rating (Rating == 0.0 ).")
        min_10_aggregate_rating_arabian =  df.loc[((df['Cuisines'] == 'Arabian') & (df['Aggregate rating'] == 0.0)), ['Restaurant Name','Aggregate rating']].groupby('Restaurant Name').max()
        min_10_aggregate_rating_arabian.sort_values('Aggregate rating', ascending=False).head(10).reset_index()
        st.dataframe(data=min_10_aggregate_rating_arabian, width=800, height=100, use_container_width=True)

      
    st.markdown("""___""")        
    with st.container():
        st.markdown(" ##### 5.7 - Japanese cuisine restaurants with the highest average rating (Rating >= 4.5 ).")
        max_10_aggregate_rating_japanese =  df.loc[((df['Cuisines'] == 'Japanese') & (df['Aggregate rating'] >= 4.5)), ['Restaurant Name','Aggregate rating']].groupby('Restaurant Name').max()
        max_10_aggregate_rating_japanese.sort_values('Aggregate rating', ascending=False).head(10).reset_index()
        st.dataframe(data=max_10_aggregate_rating_japanese, width=800, height=390, use_container_width=True)

      
    st.markdown("""___""")        
    with st.container():
        st.markdown(" ##### 5.8 - Japanese cuisine restaurants with the lowest average rating (Rating == 0.0 ).")
        min_10_aggregate_rating_japanese =  df.loc[((df['Cuisines'] == 'Japanese') & (df['Aggregate rating'] == 0.0)), ['Restaurant Name','Aggregate rating']].groupby('Restaurant Name').max()
        min_10_aggregate_rating_japanese.sort_values('Aggregate rating', ascending=True).head(10).reset_index()
        st.dataframe(data=min_10_aggregate_rating_japanese, width=800, height=100, use_container_width=True)

      
      
      
      
      
st.markdown("""___""")     
with st.container():
        st.markdown("")
        
        
        
with tab1:
    with st.container():
        st.markdown("")