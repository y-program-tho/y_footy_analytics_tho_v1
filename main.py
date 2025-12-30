import streamlit as st
import pandas as pd
import altair as alt
import y_footy_viz as yfv

st.title("y_footy_analyitics_tho_v1")

# Spacing
st.write(" ")
st.write(" ")

st.write("""
The aim of the app is to analyse provide insights into league, team and player performance 
         using data visualisations and statistics. \n
Hopefully this will be expanded in the future to include more leagues, teams and players. \n
Hope you enjoy my work :)
         """)

# Spacing
st.write(" ")
st.write(" ")

st.subheader("EPL 2024/25 League Analysis")

# View of league table
data = pd.read_excel("epl_fbref_2425.xlsx", sheet_name="league_table").set_index("Rk")
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

col1, col2, col3 = st.columns(3, gap="medium", vertical_alignment="center")
league_squad_list = data['Squad'].tolist()

with col1:
    st.write("Select a team:")
    selected_team = st.selectbox("Team", league_squad_list, key='a')

with col2:
    st.header(f"{selected_team}'s league rank is:")
    st.header(f"{int(data[data['Squad'] == selected_team].index[0])}")

with col3:
    st.header(f"Their points tally is:")
    st.header(f"{data[data['Squad'] == selected_team]['Pts'].values[0]}")

col4, col5, col6 = st.columns(3, gap="medium", vertical_alignment="center")

with col4:
    st.header(f"They've scored:")
    st.header(f"{data[data['Squad'] == selected_team]['GF'].values[0]} goals")

with col5:
    st.header(f"Their xG is:")
    st.header(f"{data[data['Squad'] == selected_team]['xG'].values[0]}")

with col6:
    st.header(f"They've conceded:")
    st.header(f"{data[data['Squad'] == selected_team]['GA'].values[0]} goals")

# Spacing
st.write(" ")
st.write(" ")

col7, col8 = st.columns(2, gap="medium", vertical_alignment="center")

with col7:
    st.header(f"Select a team")
    radar_team_1 = st.selectbox("Team", league_squad_list, key='b')

with col8:
    st.header(f"Now find a team to comapre them too")
    radar_team_2 = st.selectbox("Team", league_squad_list, key='c')

st.pyplot(yfv.league_teams_comp_radar(data, radar_team_1, radar_team_2))