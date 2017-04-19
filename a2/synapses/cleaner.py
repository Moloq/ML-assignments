"""Functions to deal with basic data pre-processing and cleaning on a pandas Dataframe.

Todo:
    Convince the python community to move towards overloading and polymorphism

"""
import pandas

def fill_in_column_using_mean(dataframe, column_list, inplace=True, *args):
    """ Fills in a column in a Pandas dataframe using the mean of the existing values"""
    if not inplace:
        dataframe = dataframe.copy()
    for column in column_list:
        dataframe[column].fillna(dataframe[column].mean(), inplace=True, *args)

def cap_values(dataframe, column, value):
    dataframe[column] = dataframe[column].where(dataframe[column] <= value, value)

def drop_all_na(dataframe, *args):
    raise NotImplementedError
