import gspread
import pandas as pd
import streamlit as st
import altair as alt
import y_analytics_data_viz as ydz
from google.oauth2.service_account import Credentials

# Scopes are used to define the specific operations or accesses you want to have for certain files
# when using the Google API
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("fbref-football-data-sheets-creds.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "1Qy_gscrEgy4_msbws4-Mm5ztXuR1bEepxBVlJoq8Egw"
sheet = client.open_by_key(sheet_id)

# Load data from gspreadsheets
df = pd.DataFrame(sheet.get_worksheet(0).get_all_records()).set_index('Rk')
st.write(df)

# Space seperator
st.markdown('##') 

# EPL Points bar chart with desired sorting
ydz.league_points_bar_chart(df,"Squad","Pts")

# Space seperator
st.markdown('##') 

# Goal scoring perfomance
#st.pyplot() 
st.scatter_chart(df, x="GF", y="xG")

# Place input and display the output
x = st.text_input("Who is your favourite team?")
st.write(f"This fan supports: {x}!!!")