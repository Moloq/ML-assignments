"""Functions to deal with basic data pre-processing and cleaning on a pandas Dataframe.

Todo:
    Convince the python community to move towards overloading and polymorphism

"""
import pandas

def fill_in_column_using_mean(dataframe, column_list, inplace=True, **kwargs):
    """ Fills in a column in a Pandas dataframe using the mean of the existing values"""
    if not inplace:
        dataframe = dataframe.copy()
    for column in column_list:
        fill_in_column_using_value(dataframe, column, dataframe[column].mean(), kwargs)
        #dataframe[column].fillna(dataframe[column].mean(), inplace=True, *args)
    return dataframe

def fill_in_column_using_median(dataframe, column_list, inplace=True, **kwargs):
    """ Fills in a column in a Pandas dataframe using the mean of the existing values"""
    if not inplace:
        dataframe = dataframe.copy()
    for column in column_list:
        fill_in_column_using_value(dataframe, column, dataframe[column].median(), kwargs)
        #dataframe[column].fillna(dataframe[column].mean(), inplace=True, *args)
    return dataframe

def fill_in_column_using_value(dataframe, column, value, **kwargs)
    dataframe[column].fillna(value, inplace=True, *kwargs)

def cap_values(dataframe, column, value):
    dataframe[column] = dataframe[column].where(dataframe[column] <= value, value)

def drop_all_na(dataframe, *args):
    raise NotImplementedError

def create_dummy_for_missing_data(dataframe, column_list=None, prefix='missing_'):
    """bla
    """
    if column_list is None:
        column_list = dataframe.columns.values.tolist()
    for col in column_list:
#        if dataframe[col].count() < len(dataframe)
        if dataframe[col].isnull().any():
            missing_col_name = prefix + col
            dataframe[missing_col_name] = dataframe[col].isnull()


