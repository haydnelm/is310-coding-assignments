All details for this assignment are included in the Jupyter Notebook. The dataframe is loaded using the following:

import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/melaniewalsh/responsible-datasets-in-context/main/datasets/top-500-novels/library_top_500.csv", sep=',', header=0, low_memory=False)

In order to gain inspiration for which columns or metadata values to use for this assignment, I just printed the dataframe using print(df) and I handpicked the columns that made sense to me. I decide that time was the most important variable included within the data, and I measured and viewed different variables across centuries to see any trends that might be visible. 