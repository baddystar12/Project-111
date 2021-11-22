import plotly.figure_factory as ff
import statistics
import csv
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('data.csv')
data = df['id'].to_list
mean = statistics.mean(data)
stdev = statistics.stdev(data)

print('mean of the data is: '.format(mean))
print('standard deviation of the data is: '.format(stdev))

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)

stdev = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)

first_stdev_start, first_stdev_end = mean - stdev, mean + stdev
second_stdev_start, second_stdev_end = mean - (2*stdev), mean + (2*stdev)
third_stdev_start, third_stdev_end = mean - (3*stdev), mean + (3*stdev)

df = pd.read_csv('data.csv')
data = df['id'].to_list
mean_of_sample = statistics.mean(data)
print('mean of sampling distribution', mean_of_sample)

fig = ff.create_distplot([mean_list], ['population mean'], show_hist = False, colors = ['#ff0066'])
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0,17], mode = 'lines', name = 'mean'))
fig.add_trace(go.Scatter(x = [mean_of_sample,mean_of_sample], y = [0,0,17], mode = 'lines', name = 'mean of sample'))
fig.add_trace(go.Scatter(x = [first_stdev_end,first_stdev_end], y = [0,0,17], mode = 'lines', name = 'standard deviation 1 end'))

z_score = (mean_of_sample - mean)/stdev
print('z score is: ', z_score)

