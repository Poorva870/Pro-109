import pandas as pd
import statistics
import csv
import plotly.figure_factory as ff

df = pd.read_csv("StdPerformance.csv")
data = df['reading score'].tolist()

mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
std_deviation = statistics.stdev(data)

fig = ff.create_distplot([data], ['reading score'], show_hist=False)
fig.show()

first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

list_of_data_within_1_std_deviation = [result for result in data if result >first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in data if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in data if result > third_std_deviation_start and result < third_std_deviation_end]

print("Mean of data is {}".format(mean))
print("Mode Deviation of data is {}".format(mode))
print("Median of data is {}".format(median))
print("Standard Deviation of data is {}".format(std_deviation))
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(data)))
print("{}% of data lies within 2 standard deviations".format(len(list_of_data_within_2_std_deviation)*100.0/len(data)))
print("{}% of data lies within 3 standard deviations".format(len(list_of_data_within_3_std_deviation)*100.0/len(data)))