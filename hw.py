import streamlit as st
import altair as alt
import numpy as np
import pandas as pd

data=pd.read_csv('C:\\Users\\sucha\\Downloads\\va\\HR_Data.csv')
st.write(data)


st.sidebar.header("Pick two variables for your Bar Graph")

x_variable = st.sidebar.selectbox("Pick your 2nd x-axis",data.columns.tolist())
y_variable = st.sidebar.selectbox("Pick your 2nd y-axis",data.columns.tolist())

bars = alt.Chart(data, title=f"Bar Graph between {x_variable} and {y_variable}").mark_bar().encode(alt.X(x_variable,title=f'{x_variable}'), alt.Y(y_variable,title=f'{y_variable}'), tooltip=[x_variable, y_variable]).configure(background='#D9E9F0')
st.altair_chart(bars, use_container_width=True)