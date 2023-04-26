import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Home",
    page_icon="🧊",
    layout="wide",   
)

##===================================================================================
## 4 - # Sidebar - Barra Lateral
st.header("Marketplace - Zero Hunger")
st.sidebar.markdown("### Dashboard - Analytical Data")


image_path = '../projeto_marketplace_zero_hunger/logo.webp'
image = Image.open(image_path)
st.sidebar.image(image, width=120)
st.sidebar.markdown("""___""")

st.write("### Dashboard - Analytical Data")

st.markdown(
    """
Dashboard - Fome Zero aims to show an overview of restaurants spread over several countries, and their respective cuisines.

How to use the Dashboard - Zero Hunger?
    
Overview:
- Unique Restaurants Registered.
- Unique Countries Registered.
- Single Registered Cities.
- Total Evaluations Done.
- Total Types of Cuisine.
- Standard Deviation.
- Location of restaurants in countries and cities.
    
Country View:
- Number of Registered Cities per Country.
- Country with most registered restaurants.
- Top 15: Countries with Restaurants with a price level equal to 4.
- Country with the most evaluations done.
- Number of restaurants per Country that deliver.
- Country with the most restaurants that accept reservations.
- Average price of a dish for two per country.
    
    
City View:
- Larger City: Average cost for two.
- Top 10: Cities with most registered restaurants.
- Top 10: Cities with more restaurants with an average score above 4.
- Top 10: Cities with more restaurants with average score below 2.5.
- Top 10: City with the most restaurants that take reservations.
- Top 20: City with the most restaurants that accept online orders.

Restaurants View:
- Top 10: Restaurant with the most reviews.
- Brazilian cuisine that have a recorded average rating( Rating >= 4.5).
- Brazilian cuisine that have the lowest average ratings( Rating = 0 ).

Types of Cooking:
- Italian cuisine restaurants with the highest average rating (Rating >= 4.8 ).
- Italian cuisine restaurants with the lowest average rating (Rating == 0.0 ).
- American cuisine restaurants with the highest average rating (Rating >= 4.8 ).
- American cuisine restaurants with the lowest average rating (Rating == 0.0 ).
- Arabian cuisine restaurants with the highest average rating (Rating >= 4.0 ).
- Arabian cuisine restaurants with the lowest average rating (Rating == 0.0 ).
- Japanese cuisine restaurants with the highest average rating (Rating >= 4.5 ).


    ### Ask for Help
     - Please visit: https://alanmotaprojetos.github.io/portfolio_projetos/
    """
)


##===================================================================================
# Footer
st.sidebar.markdown("""___""")
st.sidebar.markdown("##### Developed by: ")
st.sidebar.markdown("#### Alan Mota - Data Scientist ")
##===================================================================================
