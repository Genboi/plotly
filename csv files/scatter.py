import pandas as pd
import plotly_express as px

df=pd.read_csv("./csv files/data.csv")
fig=px.scatter(df,x="Population",y="Per capita",color="Country",size_max=80,size="Percentage")
fig.show()
