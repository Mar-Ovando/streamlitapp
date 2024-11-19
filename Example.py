
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import kagglehub
import streamlit as st

df = pd.read_csv("agriculture_dataset.csv")
df.describe()


st.title("Agriculture and Farming Dataset")
st.write("This is a dataset that helps visualize crops, land usage, sustainability and resource usage in farming and agriculture.")
st.write("Dataset summary")
st.write(df.describe())

st.write("Graph for the distribution of farm area in acres")
fig = px.histogram(df, x="Farm_Area(acres)")
st.plotly_chart(fig)

st.write("Scatterplot of pesticide and fertilizer usage")
fig = px.scatter(df, x="Pesticide_Used(kg)", y="Fertilizer_Used(tons)")
st.plotly_chart(fig)

st.caption("This project was created by Marcelo Ovando 👺")
