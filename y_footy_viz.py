import pandas as pd 
import matplotlib.pyplot as plt
from soccerplots.radar_chart import Radar

def league_teams_comp_radar(league_table_df, team_one, team_two):

    team_comp_df = league_table_df[(league_table_df['Squad']==team_one)|(league_table_df['Squad']==team_two)].reset_index()

    team_comp_df = team_comp_df.drop(['Rk', 'MP', 'W', 'D', 'L', 'Pts', 
                                    'xGD', 'xGD/90', 'Attendance', 'Top Team Scorer', 
                                    'Goalkeeper', 'Notes'], axis=1)

    team_params = list(team_comp_df.columns)
    team_params = team_params[1:]

    team_ranges = []
    team_one_values = []
    team_two_values = []

    for col in team_params:
        a = min(team_comp_df[team_params][col])
        a = a - (a*0.25)

        b = max(team_comp_df[team_params][col])
        b = b + (b*0.25)

        team_ranges.append((a, b))

    for i in range(len(team_comp_df['Squad'])):
        if team_comp_df['Squad'][i]==team_one:
            team_one_values = team_comp_df.iloc[i].values.tolist()
        if team_comp_df['Squad'][i]==team_two:
            team_two_values = team_comp_df.iloc[i].values.tolist()

    team_one_values = team_one_values[1:]
    team_two_values = team_two_values[1:]
    team_values = [team_one_values, team_two_values]

    team_titles = dict(
        title_name = team_one,
        title_color = '#c30b4e',
        title_name_2 = team_two,
        title_color_2 = '#262fe2',
        title_fontsize = 18,
        subtitle_fontsize = 18
    )

    endnote = '@y_programming_tho \n data via Fbref/Statsbomb'

    radar = Radar()

    fig, ax = radar.plot_radar(ranges=team_ranges, 
                            params=team_params,
                            values=team_values,
                            radar_color=[team_titles['title_color'], team_titles['title_color_2']],
                            alphas=[0.75, 0.6],
                            title=team_titles,
                            endnote=endnote,
                            compare=True
                            )
    fig.set_size_inches(10, 10)
    return fig
