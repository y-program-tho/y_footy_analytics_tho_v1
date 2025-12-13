import streamlit as st
import pandas as pd

st.title("y_footy_analyitics_tho_v1")

data = pd.read_excel("epl_fbref_2425.xlsx", sheet_name="Sheet1")
st.write(data)