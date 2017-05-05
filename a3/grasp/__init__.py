"""Module with different submodules for different parts of a basic Machine Learning pipeline.
Mostly a wrapper around Pandas, sklearn and plotting modules. 

Dependencies:
    Pandas 0.19+
    SKLearn

"""
from grasp.core import Grasp
__all__ = ['reader', 'cleaner', 'core']
