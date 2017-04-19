# -*- coding: utf-8 -*-
"""This module includes functions for reading data from different types of sources.

Attributes:
    None

Todo:
    Add support for SQL databases and multiple datatypes.
"""
import pandas as pd

def read_csv(path, *args, **kwargs):
    """ Reads a csv file"""
    dataframe = pd.read_csv(path, *args, **kwargs)
    return dataframe

def read_local_json(filepath):
    """ Reads a json file"""
    raise NotImplementedError

def read(filename):
    """ Reads any type of file, infers which pandas reader to use based on extension"""
    raise NotImplementedError
