import streamlit as st
import pandas as pd
import altair as alt

st.title("y_footy_analyitics_tho_v1")

# View of league table
data = pd.read_excel("epl_fbref_2425.xlsx", sheet_name="league_table")
st.write(data)

# Spacing
st.write(" ")
st.write(" ")

# View of team points tall as bar chart
st.write(alt.Chart(data).mark_bar().encode(
    x=alt.X('Squad', sort=None),
    y='Pts'
))

# Spacing
st.write(" ")
st.write(" ")

# View of team goals scored compared to their xG as scatter chart
st.header("Goals For vs Expected Goals (EPL 2024/25)")
st.scatter_chart(data, x='xG', y='GF')

# Spacing
st.write(" ")
st.write(" ")

# View of teams GA compared to their xGA as scatter chart
st.header("Goals Against vs Expected Goals Against (EPL 2024/25)")
st.scatter_chart(data, x='xGA', y='GA')
