# y_foot_analytics_v1

A football analytics website that provides insighte in to players, teasm and leagies through teh use of data visualization and and statistics.

The v1 will use the folowing technolgies:
- Python
- Clickhouse
- MinIO
- Streamlit
- PySpark

Directory structure:
y_footy_analytics_v1/
├── app.py
├── dags
├── etl
├── spark_jobs
├── tests
├── README.md
└── requirements.txt

The source of data that will be used for v1 will be the [Football-Data API](https://www.football-data.org/). The API provides data on football leagues, teams, and players for leagues all around the world. The intial version will do the English Premiere League, and will extend to the top 5 leagues in Europe.