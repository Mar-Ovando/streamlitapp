import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu


df = pd.read_csv("agriculture_dataset.csv")
with open('style.css') as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.markdown('<p class="h1">Agriculture dataset</p>', unsafe_allow_html = True)
st.markdown('<p class="h2">Usage of resources by soil type, crop type and more</p>', unsafe_allow_html = True)

#URL of the dataframe
gsheetid = "1ZDsyWu848abrjNg0zFugDeylcyptjlXLZxZ7Wc9JUCs"
sheetid = "275694"
url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetid}&format'
#st.write(url)

# Horizontal Menu
menu_selected = option_menu(None, ["Home", "Preview", "Usage of water", 'Usage of fertilizer'],
    icons=['house', 'cloud-upload', "water", 'plant'],
    menu_icon="cast", default_index=0, orientation="horizontal")

if menu_selected == "Preview":
    #show the dataframe table preview
    st.dataframe(df,use_container_width=True)

if menu_selected == "Usage of water":
    #show the graph of water vs soil type
      dfCategories = df.groupby('Soil_Type')['Water_Usage(cubic meters)'].sum().reset_index()
      fig1 = px.bar(dfCategories, x = 'Soil_Type', y = 'Water_Usage(cubic meters)', color = "Soil_Type", title = "Water usage by soil type")
      st.plotly_chart(fig1, use_container_width = True)

    #show the graph of water vs irrigation
      df = pd.read_csv(url)
      dfIrrigation = df.groupby('Irrigation_Type')['Water_Usage(cubic meters)'].sum().reset_index()
      fig3 = px.scatter(dfIrrigation, x = 'Irrigation_Type', y = 'Water_Usage(cubic meters)', color = 'Irrigation_Type', title = 'Irrigation Type and Water Usage')
      st.plotly_chart(fig3, use_container_width = True)

if menu_selected == "Usage of fertilizer":
    #show the graph of fertilizer vs Yield
      df = pd.read_csv(url)
      dfFertilizer = df.groupby('Fertilizer_Used(tons)')['Yield(tons)'].mean().reset_index()
      fig4 = px.box(dfFertilizer, x = 'Fertilizer_Used(tons)', y = 'Yield(tons)', title = 'Fertilizer Usage and Yield')
      st.plotly_chart(fig4, use_container_width = True)
