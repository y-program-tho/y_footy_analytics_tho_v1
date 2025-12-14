import streamlit as st
import pandas as pd

st.title("y_footy_analyitics_tho_v1")

data = pd.read_excel("epl_fbref_2425.xlsx", sheet_name="Sheet1")
st.write(data)

# View of league table

# View of team points tall as bar chart

# View of team goals scored compared to their xG as scatter chart

# View of teams GA compared to their xGA as scatter chart
