import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv
import plotly.graph_objects as go 

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

population_mean = statistics.mean(data)
print("The population mean is", population_mean)

population_stdev = statistics.stdev(data)
print("The population stv is", population_stdev)

fig = ff.create_distplot([data], ["reading time"], show_hist = False)
fig.add_trace(go.Scatter(x = [population_mean], y = [0 , 1], mode = "lines", name = "MEAN"))
fig.show()
