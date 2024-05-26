import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

# Load the data
@st.cache
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
    st.write(f"For the 9 nights and 10 days, your countries are: {n19}")
    selection = st.sidebar.selectbox("From these countries enter one which you would like to eliminate", selection19)
    if selection:
        m = [country for country in n19 if country not in selection]
        m.append('FRANCE')
        m.append('DENMARK')
        st.write(f"Your selected countries are: {m}")
        map_ = printmap(m, df2)
        folium_static(map_)

elif selected_days == '29N/30D':
    st.write(f"For the 29 nights and 30 days, your countries are: {n29}")
    selection = st.sidebar.selectbox("From these countries enter one which you would like to eliminate", selection29)
    if selection:
        m = [country for country in n29 if country not in selection]
        m.append('FRANCE')
        m.append('DENMARK')
        st.write(f"Your selected countries are: {m}")
        map_ = printmap(m, df2)
        folium_static(map_)

elif selected_days == '39N/40D':
    st.write(f"For the 39 nights and 40 days, your countries are: {n39}")
    st.write(f"Your selected countries are: {n39}")
    map_ = printmap(n39, df2)
    folium_static(map_)

else:
    st.write("Invalid input")
    