# analysis.py
# Fisher’s Iris data set analysis.
# Author: Damien Farrell

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools
import seaborn as sns

plt.style.use('ggplot') # Uses style template

file_name = 'iris.data'
column_headers = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Class']

df = pd.read_csv(file_name, 
                 header=None,
                 names=column_headers) # Inserts column headers

# Calculate summary statistics and save to a text file
summary_data = df.describe()
summary_data.to_csv('summary_data.txt')

# Generate histograms for each numeric variable and save as PNG files
for column in column_headers[:-1]: # Loop through all column headers except 'class'
    plt.figure() # Create a new figure for each histogram
    ax = df[column].plot(kind='hist', title=f'Histogram: {column}')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    plt.savefig(f'Histogram_{column}.png', dpi=300) # Saves file.

# Generate scatterplots for all combinations of numeric variables
scatterplot_axes = list(itertools.combinations(column_headers[:-1], 2))

for x, y in scatterplot_axes: # Unpacks and loops the x and y variables from each tuple
    plt.figure() # Create a new figure for each histogram
    sns.scatterplot(x=x, # Plotting
                y=y,
                hue='Class',
                data=df,)
    plt.title(f'Scatterplot: {x} vs {y}')
    plt.savefig(f'Scatterplot_{x}_vs_{y}.png', dpi=300) # Saves file.

sns.pairplot(df, 
             vars=['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width'],
             hue='Class')
plt.savefig(f'Pairplot.png', dpi=300)

plt.figure() # Creates new figure for correlation heatmap
df_corr = df[['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width']].corr()
sns.heatmap(df_corr, annot=True)
plt.title('Heatmap: Correlation')
plt.savefig(f'Heatmap_Correlation', dpi=300)