import pandas as pd
import plotly_express as px

df=pd.read_csv("./csv files/line_chart.csv")
fig=px.bar(df,x="Year",y="Per capita income",title="Per capita income")
fig.show()
