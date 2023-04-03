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

# Calculate summary statistics and save to a text file
summary_data = df.describe()
summary_data.to_csv('summary_data.txt')

# Set text size for plot titles and axes
title_fontsize = 15
axis_fontsize = 12

# Generate histograms for each numeric variable and save as PNG files
for column in column_headers[:-1]: # Loop through all column headers except 'class'
    plt.figure() # Create a new figure for each histogram
    plt.grid(True)
    plt.xlabel('Value', fontsize=axis_fontsize)
    plt.ylabel('Frequency', fontsize=axis_fontsize)
    plt.title(f'Histogram: {column}', fontsize=title_fontsize)
    df[column].plot(kind='hist', color='green')
    plt.savefig(f'histogram_{column}.png', dpi=300, bbox_inches='tight')

# Generate scatterplots for all combinations of numeric variables
scatterplot_axes = list(itertools.combinations(column_headers[:-1], 2))

for x, y in scatterplot_axes: # Unpack the x and y variables from each tuple
    plt.figure() # Create a new figure for each scatterplot
    plt.grid(True)
    plt.xlabel(x, fontsize=axis_fontsize)
    plt.ylabel(y, fontsize=axis_fontsize)
    plt.title(f'Scatterplot: {x} vs {y}', fontsize=title_fontsize)
    df.plot(kind='scatter', x=x, y=y)
    plt.savefig(f'scatterplot_{x}_vs_{y}.png', dpi=300, bbox_inches='tight')



# [A Gentle Introduction to Pandas Data Analysis](https://www.youtube.com/watch?v=_Eb0utIRdkw)
# [How To Add Header Row To A Pandas DataFrame](https://stackoverflow.com/questions/34091877/how-to-add-header-row-to-a-pandas-dataframe)
# [W3Schools Pandas Tutorial](https://www.w3schools.com/python/pandas/pandas_analyzing.asp)
# [How Do I Iterate Through Combinations Of A List](https://stackoverflow.com/questions/41680388/how-do-i-iterate-through-combinations-of-a-list)
# [Exploratory Data Analysis with Pandas Python 2023](https://www.youtube.com/watch?v=xi0vhXFPegw&t=2s)