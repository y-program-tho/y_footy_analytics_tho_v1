import altair as alt
import matplotlib.pyplot as plt

def league_points_bar_chart(league_table, x_axis, y_axis):
    return alt.Chart(league_table).mark_bar().encode(x=alt.X(x_axis, sort=None), y=y_axis)

def league_scatter(df, x_axis, y_axis, xlabel, ylabel, teams):
    fig, ax = plt.subplots()
    ax.scatter(x=df[x_axis], y=df[y_axis])
    ax.set_facecolor("#FAE2B1")
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    for i, txt in enumerate(teams):
        ax.annotate(txt, (x_axis[i], y_axis[i]))
    return ax
