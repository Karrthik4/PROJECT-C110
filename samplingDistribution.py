import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import random
import statistics
import pandas

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

population_mean = statistics.mean(data)
print("population mean:-", population_mean)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def plot_graph(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],["reading time"],show_hist=False)
    fig.add_trace(go.Scatter(x = [mean,mean], y = [0,1], mode = "lines", name = "Mean"))
    fig.show()

def setup():
    mean_list = []
    for i in range(0, 100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
    plot_graph(mean_list)
    mean = statistics.mean(mean_list)
    print("mean of sampling distribution:- ", mean)
setup()

def standard_deviation():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
        
    std_deviation = statistics.stdev(mean_list)
    print(std_deviation)
standard_deviation()