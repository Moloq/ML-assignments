"""Helper functions to describe the data in a pandas Dataframe.

Todo:
    Everything
"""
import pandas
import seaborn

def plot_correlation_heatmap(dataframe):
    correlations = dataframe.corr()
    sns.heatmap(corr)
