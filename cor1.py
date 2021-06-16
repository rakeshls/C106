import plotly.express as px
import pandas as pd
import csv
df = pd.read_csv('file1.csv')
fig = px.scatter(df,x='Temperature',y='Ice-cream Sales( ₹ )')
fig.show()