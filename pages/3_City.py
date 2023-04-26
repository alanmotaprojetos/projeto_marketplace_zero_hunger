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

st.set_page_config(page_title='City View', layout='wide')
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
#options_cities = st.sidebar.multiselect(
#    'Select City:',
#    ['Surat', 'Birmingham', 'Abu Dhabi', 'Doha', 'Gangtok', 'Goa', 'Cape Town', 'Patna', 'Rio de Janeiro'],
#    default= ['Surat', 'Birmingham', 'Abu Dhabi', 'Doha', 'Gangtok', 'Goa', 'Cape Town', 'Patna', 'Rio de Janeiro'])

#city_filter = df['City'].isin( options_cities )
#df = df.loc[city_filter, :]


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
tab1, tab2 = st.tabs(['Marketplace - City View', '--'])

st.markdown("""___""")
with tab1:
    
    with st.container():
        st.markdown("#### 3.1 - Larger City: Average cost for two")
        v_medio_prato_p_dois = df.loc[:, ['City', 'Average Cost for two']].groupby('City').mean()
        v_medio_prato_p_dois.sort_values('Average Cost for two', ascending=False)
        df_aux_3_4 = v_medio_prato_p_dois.idxmax()
        st.dataframe(data=df_aux_3_4, width=300, height=100, use_container_width=False)
    
    
    
    
    st.markdown("""___""")  
    with st.container():
        st.markdown("#### 3.1 - Top 10: Cities with most registered restaurants.")
        df2 = df.loc[:, ['City', 'Restaurant Name']].groupby('City').count().reset_index()
        df2.columns = ['City', 'Quantity']
        df3 = df2.sort_values('Quantity', ascending=False).head(10)
        fig_3_1 = px.pie(df3, names='City', values='Quantity', title='Fig. 3.1 Chart: Top 10 : City x Quantity .')    
        st.plotly_chart(fig_3_1, use_container_width=True)     
            
    
    st.markdown("""___""")    
    with st.container():
        st.markdown("#### 3.2 - Top 10: Cities with more restaurants with an average score above 4.0")
        media_rest = df.loc[(df['Aggregate rating'] >= 4), ['City', 'Aggregate rating']].groupby('City').count().reset_index()
        media_rest.columns = ['City', 'Quantity: Average score above 4']
        df_aux_3_2 = media_rest.sort_values('Quantity: Average score above 4', ascending=False).head(10)
        fig_3_2 = px.bar(df_aux_3_2, x='City', y='Quantity: Average score above 4', text_auto='.2s', title='Fig. 3.2 - Chart: Top 10 - Quantity: Average score above 4 x City.')
        st.plotly_chart(fig_3_2, use_container_width=True)
        
      
    st.markdown("""___""") 
    with st.container():
        st.markdown("#### 3.3 - Top 10: Cities with more restaurants with average score below 2.5.")
        media_rest_menor_2_5 = df.loc[(df['Aggregate rating'] < 2.5), ['City', 'Aggregate rating']].groupby('City').count().reset_index()
        media_rest_menor_2_5.columns = ['City', 'Quantity']
        df_aux_3_3 = media_rest_menor_2_5.head(10)
        df_aux_3_3.sort_values('Quantity', ascending=False)
        df_aux_3_3_fig = px.bar(df_aux_3_3, y='Quantity', x='City', text_auto='.2s',title="Fig. 3.3 - Chart: Top 10 - : Quantity x City")
        st.plotly_chart(df_aux_3_3_fig, use_container_width=True)
    

    st.markdown("""___""") 
    with st.container():
        st.markdown("#### 3.4 -Top 10:  City with the most restaurants that take reservations.")
        city_reserva = df.loc[:, ['City', 'Has Table booking']].groupby('City').count().reset_index()
        city_reserva.sort_values('Has Table booking', ascending=False)
        df_aux_3_6 = city_reserva.head(10)
        fig = go.Figure([go.Bar(x=df_aux_3_6['City'], y=df_aux_3_6['Has Table booking'])])
        st.plotly_chart(fig, use_container_width=True)
        
       

    st.markdown("""___""") 
    with st.container():
        st.markdown("#### 3.5 - Top 20: City with the most restaurants that accept online orders.")
        city_pedidos_online = df.loc[:, ['Country Name', 'City', 'Has Online delivery']].groupby(['Country Name', 'City']).count().reset_index()
        city_pedidos_online.columns = ['Country Name', 'City','Has Online delivery']
        city_pedidos_online.sort_values('Has Online delivery', ascending=False)
        df_aux_3_8 = city_pedidos_online.head(20)
        fig = px.sunburst(df_aux_3_8, path=['Country Name', 'City'], values='Has Online delivery')
        st.plotly_chart(fig, use_container_width=True)
       
with tab2: 
     with st.container():
        st.markdown("")
        
         
    
        
        