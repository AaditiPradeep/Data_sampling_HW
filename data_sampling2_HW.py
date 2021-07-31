import random
import plotly.express as px
import plotly.figure_factory as ff
import statistics
import pandas as pd

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

def random_setOfMean(counter):

    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    stdev = statistics.stdev(dataset)
    return mean

def show_figure(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["reading time"], show_hist = False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_setOfMean(30)
        mean_list.append(set_of_means)
    show_figure(mean_list)

setup()
