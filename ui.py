import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

import warnings 
warnings.filterwarnings('ignore')

# Load the data

def load_data():
    df = pd.read_excel('./country_coordinates.xlsx')
    return df

# Function to create map
def create_map(df):
    var = folium.Map(location=[df.LONGTITUDE.mean(), df.LATITUDE.mean()], zoom_start=3, control_scale=True)
    for i, row in df.iterrows():
        iframe = folium.IFrame('Country: ' + str(row["COUNTRY"]))
        popup = folium.Popup(iframe, min_width=300, max_width=300)
        folium.Marker(location=[row['LONGTITUDE'], row['LATITUDE']], popup=popup).add_to(var)
    return var

# Function to filter countries and create map
def printmap(selected_countries, df):
    df_filtered = df[df['COUNTRY'].isin(selected_countries)]
    var = folium.Map(location=[df_filtered.LONGTITUDE.mean(), df_filtered.LATITUDE.mean()], zoom_start=3, control_scale=True)
    for i, row in df_filtered.iterrows():
        iframe = folium.IFrame('Country: ' + str(row["COUNTRY"]))
        popup = folium.Popup(iframe, min_width=300, max_width=300)
        folium.Marker(location=[row['LONGTITUDE'], row['LATITUDE']], popup=popup).add_to(var)
    return var

# Streamlit app
st.title("Europe Tour Dashboard")

df2 = load_data()

days_options = {'19N/20D': 'a', '29N/30D': 'b', '39N/40D': 'c'}
days = list(days_options.keys())

n19 = ['FRANCE', 'BELGIUM', 'NETHERLANDS', 'GERMANY', 'SWITZERLAND', 'CZECHIA', 'DENMARK']
n29 = ['FRANCE', 'BELGIUM', 'NETHERLANDS', 'GERMANY', 'SWITZERLAND', 'CZECHIA', 'ITALY', 'AUSTRIA', 'DENMARK']
n39 = df2['COUNTRY'].unique().tolist()

selection19 = ['BELGIUM', 'NETHERLANDS', 'GERMANY', 'SWITZERLAND', 'CZECHIA', 'AUSTRIA']
selection29 = ['BELGIUM', 'LUXEMBOURG', 'NETHERLANDS', 'GERMANY', 'HUNGARY', 'SWITZERLAND', 'CZECHIA', 'ITALY', 'AUSTRIA']

st.sidebar.header("Plan Your Trip")
selected_days = st.sidebar.selectbox("Select Trip Duration", days)

st.write(f"### Selected Trip Duration: {selected_days}")

if selected_days == '19N/20D':
    st.write(f"For the 19 nights and 20 days: ")
    st.sidebar.write("Your Entry and Exit Points are Switzerland and Denmark select any 5 more countries you wish to visit:")
    selection = [country for country in selection19 if st.sidebar.checkbox(country, value=False)]
    
    if selection:

        m = [country for country in n19 if country in selection]
        m.append('FRANCE')
        m.append('DENMARK')
        st.write(f"Your selected countries are: ")
        map_ = printmap(m, df2)
        folium_static(map_)
        

elif selected_days == '29N/30D':
    st.write(f"For the 29 nights and 30 days: ")
    st.sidebar.write("Your Entry and Exit Points are Switzerland and Denmark select any 8 more countries you wish to visit:")
    selection = [country for country in selection29 if st.sidebar.checkbox(country, value=False)]

    if selection:

        m = [country for country in n29 if country in selection]
        m.append('FRANCE')
        m.append('DENMARK')
        st.write(f"Your selected countries are: ")
        map_ = printmap(m, df2)
        folium_static(map_)

elif selected_days == '39N/40D':
    st.write(f"For the 39 nights and 40 days")
    st.write(f"Your selected countries are: ")
    st.caption("FRANCE, BELGIUM, LUXEMBOURG, NETHERLANDS, DENMARK, GERMANY, CZECHIA, AUSTRIA, HUNGARY, SWITZERLAND, ITALY and SPAIN")
    map_ = printmap(n39, df2)
    folium_static(map_)

else:
    st.write("Invalid input")
