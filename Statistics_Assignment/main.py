import pandas as pd
import statistics as stats


df = pd.read_excel("data.xlsx")


mean_x = df['x'].mean()
mean_y = df['y'].mean()

mode_x = stats.mode(df['x'])

std_dev_y = df['y'].std()

range_x = df['x'].max() - df['x'].min()
range_y = df['y'].max() - df['y'].min()


print("Mean of x:", mean_x)
print("Mean of y:", mean_y)
print("Mode of x:", mode_x)
print("Standard Deviation of y:", std_dev_y)
print("Range of x:", range_x)
print("Range of y:", range_y)
