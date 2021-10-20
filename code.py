import csv
import statistics
import plotly.express as px
import pandas as pd
import math 
import random
import plotly
import plotly.figure_factory as ff

df=pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
fig = ff.create_distplot([data], ["reading time"], show_hist=False)
fig.show()

population_mean =statistics.mean(data)
print("Mean = ", population_mean)
population_standerddevation = statistics.stdv(data)
print("standard Deviation = ", population_standerddevation)
