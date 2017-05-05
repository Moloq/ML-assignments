from grasp import core
from grasp import reader
import pandas as pd 
import sklearn

df = reader.read("data/credit-data.csv")
obj = core.Grasp(df)

obj.data = df
obj.target_var = 'SeriousDlqin2yrs'
obj.data = obj.data[['NumberOfTimes90DaysLate','age','NumberOfOpenCreditLinesAndLoans', 'SeriousDlqin2yrs']]
test_grid = { 
    'RF':{'n_estimators': [1], 'max_depth': [1], 'max_features': ['sqrt'],'min_samples_split': [10]},
    'LR': { 'penalty': ['l1'], 'C': [0.01]},
    'SGD': { 'loss': ['perceptron'], 'penalty': ['l2']},
    'ET': { 'n_estimators': [1], 'criterion' : ['gini'] ,'max_depth': [1], 'max_features': ['sqrt'],'min_samples_split': [10]},
    'AB': { 'algorithm': ['SAMME'], 'n_estimators': [1]},
    'GB': {'n_estimators': [1], 'learning_rate' : [0.1],'subsample' : [0.5], 'max_depth': [1]},
    'NB' : {},
    'DT': {'criterion': ['gini'], 'max_depth': [1], 'max_features': ['sqrt'],'min_samples_split': [10]},
    'SVM' :{'C' :[0.01],'kernel':['linear']},
    'KNN' :{'n_neighbors': [5],'weights': ['uniform'],'algorithm': ['auto']}
           }

obj.split_test_train(0.8, 'SeriousDlqin2yrs')
obj.gridsearch(test_grid)
