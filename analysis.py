# analysis.py
# Fisher’s Iris data set analysis.
# Author: Damien Farrell

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools

file_name = 'iris.data'
column_headers = ['sepal_length','sepal_width','petal_length','petal_width','class']

df = pd.read_csv(file_name, 
                 header=None,
                 names=column_headers)

# Statistics
summary_data = df.describe()

# Saves the statistics as txt.

summary_data.to_csv('summary_data.txt')

# Plots.
# Plots Formatting.

# Formatting: Text Size
title_fontsize = 15
axis_fontsize = 12

# Formatting: Labels etc.
plt.grid(True)
plt.xlabel('Value',fontsize=axis_fontsize)
plt.ylabel('Frequency',fontsize=axis_fontsize)

# Plotting: Histograms
# Saves a histogram of each variable to png files. Looped through the headers except 'class' to output the png.
column_number = 0
for histogram in range(len(column_headers)-1):
# Plot data per variable.
    plt.title(f'Histogram: {column_headers[column_number]}',fontsize=title_fontsize)
    df[column_headers[column_number]].plot(kind='hist', color='green')
 # Save Output.
    plt.savefig(f'histogram_{column_headers[column_number]}.png', dpi=300, bbox_inches='tight')
    column_number += 1

# Plotting: Scatterplots

A = [0, 1, 2, 3]
B = [0, 1, 2, 3]
scatterplot_axis = list(itertools.product(A, B))

print(scatterplot_axis)

tuple_num = 0
for scatterplot in range(len(scatterplot_axis)):
    xpoints, ypoints = scatterplot_axis[tuple_num]
    plt.title(f'Scatterplot: {xpoints} vs {ypoints}',fontsize=title_fontsize)
    df.plot(kind='scatter', x=xpoints, y=ypoints)
    tuple_num += 1
    plt.show()


plt.savefig(f'scatterplot_{xpoints} vs {ypoints}.png', dpi=300, bbox_inches='tight')







# [A Gentle Introduction to Pandas Data Analysis](https://www.youtube.com/watch?v=_Eb0utIRdkw)
# [How To Add Header Row To A Pandas DataFrame](https://stackoverflow.com/questions/34091877/how-to-add-header-row-to-a-pandas-dataframe)
# [W3Schools Pandas Tutorial](https://www.w3schools.com/python/pandas/pandas_analyzing.asp)
# [Feeding All Combinations Of 'X' And 'Y' Array Into A Function](https://stackoverflow.com/questions/40685659/feeding-all-combinations-of-x-and-y-array-into-function-fx-y)