![Banner Image](./markdown-image-files/PANDS_PROJECT.png)
---
---
![GitHub last commit](https://img.shields.io/github/last-commit/damienfarrell/pands-project)
![GitHub contributors](https://img.shields.io/github/contributors/damienfarrell/pands-project)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/damienfarrell/pands-project)

In this code, we analyse the Iris dataset, which contains measurements of sepal and petal lengths and widths for three different species of iris flowers. The script is organised as follows:

1. Import necessary libraries: We begin by importing the required libraries - pandas, numpy, matplotlib, itertools, and seaborn.<sup>[1,](#ref1)</sup><sup>[3](#ref3)</sup>
2. Set plot style: The ggplot style is applied to the plots for better visualization.<sup>[5](#ref5)</sup>
3. Load dataset: The Iris dataset is loaded into a DataFrame with custom column headers using pandas.<sup>[1](#ref1)</sup><sup>[2](#ref2)</sup>
4. Generate summary statistics: We calculate summary statistics for each column and save the resulting DataFrame to a text file.<sup>[1](#ref1)</sup><sup>[3](#ref3)</sup>
5. Create histograms: For each numeric variable, a histogram is generated, displaying the distribution of values. Each histogram is saved as a PNG file.<sup>[3](#ref3)</sup>
6. Create scatterplots: Scatterplots are created for all combinations of numeric variables, with different colors representing the different iris species. Each scatterplot is saved as a PNG file.<sup>[3](#ref3)</sup><sup>[4](#ref4)</sup><sup>[5](#ref5)</sup>
7. Create pairplot: A pairplot is generated using seaborn, which provides a compact visualization of all possible scatterplots between numeric variables, as well as histograms for each variable. The pairplot is saved as a PNG file.<sup>[3](#ref3)</sup><sup>[4](#ref4)</sup><sup>[5](#ref5)</sup>
8. Create correlation heatmap: A correlation heatmap is created to visualize the correlation between the numeric variables. The heatmap is saved as a PNG file.

10. Completed a README.md of the process.<sup>[6](#ref6)</sup><sup>[7](#ref7)</sup>

## References
<a name="ref1">1</a>: [A Gentle Introduction to Pandas Data Analysis](https://www.youtube.com/watch?v=_Eb0utIRdkw)
<a name="ref2">2</a>: [How To Add Header Row To A Pandas DataFrame](https://stackoverflow.com/questions/34091877/how-to-add-header-row-to-a-pandas-dataframe)
<a name="ref3">3</a>: [W3Schools Pandas Tutorial](https://www.w3schools.com/python/pandas/pandas_analyzing.asp)
<a name="ref4">4</a>: [How Do I Iterate Through Combinations Of A List](https://stackoverflow.com/questions/41680388/how-do-i-iterate-through-combinations-of-a-list)
<a name="ref5">5</a>: [Exploratory Data Analysis with Pandas Python 2023](https://www.youtube.com/watch?v=xi0vhXFPegw&t=2s)
<a name="ref6">6</a>: [Footnotes in Markdown](https://www.javatpoint.com/footnotes-in-markdown)
<a name="ref7">7</a>: [How to add footnotes to GitHub-flavoured Markdown?](https://stackoverflow.com/questions/25579868 how-to-add-footnotes-to-github-flavoured-markdown)