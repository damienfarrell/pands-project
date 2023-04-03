# analysis.py
# Fisher’s Iris data set analysis.
# Author: Damien Farrell

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools

plt.style.use('ggplot')

file_name = 'iris.data'
column_headers = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Class']

df = pd.read_csv(file_name, 
                 header=None,
                 names=column_headers)

# Calculate summary statistics and save to a text file
summary_data = df.describe()
summary_data.to_csv('summary_data.txt')

# Generate histograms for each numeric variable and save as PNG files
for column in column_headers[:-1]: # Loop through all column headers except 'class'
    plt.figure() # Create a new figure for each histogram (Not needed for scatterplot)
    ax = df[column].plot(kind='hist', title=f'Histogram: {column}')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    plt.savefig(f'histogram_{column}.png')

# Generate scatterplots for all combinations of numeric variables
scatterplot_axes = list(itertools.combinations(column_headers[:-1], 2))

for x, y in scatterplot_axes: # Unpacks and loops the x and y variables from each tuple
    ax = df.plot(kind='scatter', x=x, y=y, title=f'Scatterplot: {x} vs {y}')
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    plt.savefig(f'scatterplot_{x}_vs_{y}.png')



# [A Gentle Introduction to Pandas Data Analysis](https://www.youtube.com/watch?v=_Eb0utIRdkw)
# [How To Add Header Row To A Pandas DataFrame](https://stackoverflow.com/questions/34091877/how-to-add-header-row-to-a-pandas-dataframe)
# [W3Schools Pandas Tutorial](https://www.w3schools.com/python/pandas/pandas_analyzing.asp)
# [How Do I Iterate Through Combinations Of A List](https://stackoverflow.com/questions/41680388/how-do-i-iterate-through-combinations-of-a-list)
# [Exploratory Data Analysis with Pandas Python 2023](https://www.youtube.com/watch?v=xi0vhXFPegw&t=2s)