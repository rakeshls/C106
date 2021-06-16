import plotly.express as px
import pandas as pd
import csv
df = pd.read_csv('file4.csv')
fig = px.scatter(df,x='Coffee in ml',y='sleep in hours')
fig.show()