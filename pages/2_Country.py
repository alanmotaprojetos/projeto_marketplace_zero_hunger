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

st.set_page_config(page_title='Country View', layout='wide')
##===================================================================================
## 2 - Importação do DataFrame
#df = pd.read_csv('/home/alan/Documents/repos/projeto_final/dataset/zomato.csv')
#df = pd.read_csv('/home/alan/Documents/repos/projeto_marketplace_zero_hunger/dataset/zomato.csv')
#df = pd.read_csv('../dataset/zomato.csv')
#df = pd.read_csv('/home/alan/Documents/repos/projeto_marketplace_zero_hunger/dataset/zomato.csv')

#df = pd.read_csv('/dataset/zomato.csv')
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
st.header("Marketplace - Country View")
st.sidebar.markdown("### Dashboard - Control")

image_path = '../projeto_marketplace_zero_hunger/logo.webp'#image_path = '../logo.webp'
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
tab1, tab2 = st.tabs(['Marketplace - Country View', '--'])

with tab1:           
    with st.container():
        st.markdown("#### 2.1 - Number of Registered Cities per Country.")
        pais_cidade = df[['Country Name', 'City']].groupby(['Country Name']).count().reset_index()
        pais_cidade.columns = ['Country Name', 'Total Cities']
        pais_cidade.sort_values('Total Cities', ascending=False).head(10)
        fig = px.bar(pais_cidade, y='Total Cities', x='Country Name', text_auto='.3s',title="2.1 - Chart: Country Name x Total Cities.")
        st.plotly_chart(fig, use_container_width=True)
        
       
    st.markdown("""___""")       
    with st.container():
        st.markdown("#### 2.2 - Country with most registered restaurants.")
        pais_rest_reg = df[['Country Name', 'Restaurant Name']].groupby(['Country Name']).count().reset_index()
        pais_rest_reg.columns = ['Country Name', 'Country Quantity']
        pais_rest_reg.sort_values('Country Quantity', ascending=False)
        fig = px.bar(pais_rest_reg, y='Country Quantity', x='Country Name', text_auto='.3s',title="2.2 - Chart: Country Quantity x Country Name.")
        st.plotly_chart(fig, use_container_width=True)
        
        
    st.markdown("""___""")       
    with st.container():
        st.markdown("#### 2.3 - Top 15: Countries with Restaurants with a price level equal to 4.")
        country_name_price = df.loc[(df['Price range'] == 4), ['Country Name', 'Price range']].groupby('Country Name').count().reset_index()
        country_name_price.columns = ['Country Name','Country Quantity']
        country_name_price.sort_values('Country Quantity', ascending=False)
        fig = px.bar(country_name_price, y='Country Name', x='Country Quantity', text_auto='.3s',title="2.3 - Chart: Country Quantity x Country Name.")
        st.plotly_chart(fig, use_container_width=True)
        
    st.markdown("""___""")       
    with st.container():
        st.markdown("#### 2.4 - Country with the most evaluations done.")
        pais_ava_efetuadas = df.loc[:, ['Country Name', 'Votes']].groupby('Country Name').nunique().reset_index()
        pais_ava_efetuadas.sort_values('Votes', ascending=False)
        fig = px.bar(pais_ava_efetuadas, y='Votes', x='Country Name', text_auto='.3s',title="2.4 - Country Name x Votes.")
        st.plotly_chart(fig, use_container_width=True)
        
        
        st.markdown("""___""")       
    with st.container():
        st.markdown("#### 2.5 - Number of restaurants per Country that deliver.")
        filtro_6 = (df['Is delivering now'] >= 1) 
        filtro_6_2 = df.loc[filtro_6, ['Country Name', 'Restaurant Name']].groupby('Country Name').count().reset_index()
        filtro_6_2.columns = ['Country Name', 'Quantity of Deliveries']
        filtro_6_2.sort_values('Quantity of Deliveries', ascending=False)
        fig = px.bar(filtro_6_2, y='Country Name', x='Quantity of Deliveries', text_auto='.3s',title="2.5 - Chart: Votes x Country Name.")
        st.plotly_chart(fig, use_container_width=True)
        st.table(data=filtro_6_2)
        
    st.markdown("""___""")       
    with st.container():
        st.markdown("#### 2.6 - Country with the most restaurants that accept reservations.")
        reservas_restaurante_pais = df.loc[(df['Has Table booking'] >= 1), ['Country Name', 'Has Table booking']].groupby(['Country Name']).count().reset_index()
        reservas_restaurante_pais.sort_values('Has Table booking', ascending=False)
        fig = px.bar(reservas_restaurante_pais, y='Has Table booking', x='Country Name', text_auto='.3s',title="2.6 - Chart: Has Table booking x Country Name.")
        st.plotly_chart(fig, use_container_width=True)
        
        
        
        st.markdown("""___""")       
    with st.container():
        st.markdown("#### 2.7 - Average price of a dish for two per country.")
        media_preco_p_dois = df.loc[(df['Average Cost for two'] != 0), ['Country Name', 'Price range']].groupby('Country Name').mean().reset_index()
        media_preco_p_dois.columns = ['Country Name','Mean Price']
        media_preco_p_dois.sort_values('Mean Price', ascending=False)
        fig = px.bar(media_preco_p_dois, y='Mean Price', x='Country Name', text_auto='.2s',title="2.7 - Chart: Mean Price x Country Name.")
        st.plotly_chart(fig, use_container_width=True)
        
        
with tab2:
    st.markdown("""___""")