# analysis.py
# Fisher’s Iris data set analysis.
# Author: Damien Farrell

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

plt.style.use('ggplot') # Uses style template

folder_path = 'plot-image-files/'
url_name = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
column_headers = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Class'] # Column headers to add

df = pd.read_csv(url_name, 
                 header=None,
                 names=column_headers) # Inserts column headers

# Convert the class labels to numerical format
df['Class_Int'] = df['Class'].copy() # Make a copy of the class coolumn to later encode
le = LabelEncoder()
df['Class_Int'] = le.fit_transform(df['Class'])
df = df[['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Class_Int','Class']] # Rearrange columns.

# Calculate summary statistics and save to a text file
summary_data = df.describe()
summary_data.to_csv('summary_data.txt')

df_stats = df.groupby(['Class']).agg(['mean', 'max', 'min'])
print(df_stats)

# Generate histograms for each numeric variable and save as PNG files
for column in df.columns[:-2]: # Loop through all column headers except 'Class' and 'Class_Int'
    plt.figure() # Create a new figure for each histogram
    ax = df[column].plot(kind='hist', title=f'Histogram: {column}')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    plt.savefig(f'{folder_path}Histogram_{column}.png', dpi=150) # Saves file.

# Generate scatterplots for all combinations of numeric variables
scatterplot_axes = list(itertools.combinations(df.columns[:-1], 2))

for x, y in scatterplot_axes: # Unpacks and loops the x and y variables from each tuple
    plt.figure() # Create a new figure for each histogram
    sns.scatterplot(x=x, # Plotting
                y=y,
                hue='Class',
                data=df,)
    plt.title(f'Scatterplot: {x} vs {y}')
    plt.savefig(f'{folder_path}Scatterplot_{x}_vs_{y}.png', dpi=150) # Saves file.

sns.pairplot(df, 
             vars=df.columns[:-1],
             hue='Class')
plt.savefig(f'{folder_path}Pairplot.png', dpi=150) # Saves file.

plt.figure() # Creates new figure for correlation heatmap
df_corr = df[['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Class_Int']].corr()
sns.heatmap(df_corr, annot=True)
plt.title('Heatmap: Correlation')
plt.tight_layout() # Adjust the layout of the figure
plt.savefig(f'{folder_path}Heatmap_Correlation.png', dpi=150)

# Model:
# Separate features and labels
x = df[['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width']]
y = df['Class_Int']

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Create and train the logistic regression model
model = LogisticRegression(max_iter=200)
model.fit(x_train, y_train)

# Evaluate the model
y_pred = model.predict(x_test)
print(classification_report(y_test, y_pred))