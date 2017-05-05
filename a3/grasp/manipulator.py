"""Helper function submodule with functions to generate features from existing dataframe

"""
import pandas

def continuous_to_bins(dataframe, num_bins, column_list, new_columns_list=None, \
    by_quantile=True, inplace=True):
    """For each specified column, create new columns that place values into specified number of
    bins, by value range or by quantile.
    """
    if inplace is False:
        dataframe = dataframe.copy()
    if new_columns_list is None:
        new_columns_list = [col + '_bin' for col in column_list]
    for col, new_col in zip(column_list, new_columns_list):
        if by_quantile:
            dataframe[new_col] = pandas.qcut(dataframe[col], num_bins)
        else:
            dataframe[new_col] = pandas.cut(dataframe[col], num_bins)
    return dataframe

def category_to_dummies(dataframe, column_list, inplace=True):
    """For each column in column_list, create new dummy variable columns for each of the categories
    """
    return pandas.get_dummies(dataframe, columns=column_list)

