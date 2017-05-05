# -*- coding: utf-8 -*-
"""This module includes functions for reading data from different types of sources.

Attributes:
    None

Todo:
    Add support for SQL databases and multiple datatypes.
"""
import pandas as pd
from os import path

def read_csv(path, *args, **kwargs):
    """ Reads a csv file"""
    dataframe = pd.read_csv(path, *args, **kwargs)
    return dataframe

def read_local_json(filepath):
    """ Reads a json file"""
    raise NotImplementedError

def read(filepath, *args, **kwargs):
    """ Reads any type of file, infers which pandas reader to use based on extension"""
    extension = path.splitext(filepath)[1].lower()
    if extension == '.csv':
        data = pd.read_csv(filepath, *args, **kwargs)
    elif extension == '.json':
        data = pd.read_json(filepath, *args, **kwargs)
    return data

