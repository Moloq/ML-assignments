""" 
"""
from sklearn.linear_model import LogisticRegression 

def get_trained_model(dataframe, features, target, method='logistic'):
    """ Returns a sklearn model object from the selected dataframe, features and target column
    that uses the specified method.
    Currently only supports logistic regression, the default.
    """
    if method == 'logistic':
        model = LogisticRegression()
        model.fit(dataframe[features], dataframe[target])
        return model
    else:
        raise NotImplementedError

def predict(model, dataframe, features, target_name='score', inplace=True):
    """ Adds a column 'score' (or target_name) with the predicted value for each row
    according tot he prediction made by the model.
    """
    if inplace is False:
        dataframe = dataframe.copy()
    dataframe[target_name] = model.predict(dataframe[features])
    return dataframe

def get_accuracy(dataframe, actual, predicted):
    """ """
    raise NotImplementedError