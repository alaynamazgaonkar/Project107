import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

pf=pd.read_csv("data.csv")
fig = px.scatter(pf, x="student_id", y="level",color="attempt")
fig.show()