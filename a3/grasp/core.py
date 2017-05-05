""" Core definitions and imports
"""
import pandas as pd
from os import path
from sklearn import preprocessing, cross_validation, svm, metrics, tree, decomposition, svm
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.linear_model import LogisticRegression, Perceptron, SGDClassifier, OrthogonalMatchingPursuit, RandomizedLogisticRegression
from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import train_test_split
from sklearn.grid_search import ParameterGrid
from sklearn.metrics import *
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV

class Grasp(object):
    """A ML project complete with data, options, etc.

    Attributes:
        data: The data read
        train_set: The set for training
        test_set: the set for testing

    """
    def __init__(self, data):
        self.data = data
        self.scores = ['accuracy']
        pass

    available_classifiers = {
        'RF': RandomForestClassifier(n_estimators=50, n_jobs=-1),
        'ET': ExtraTreesClassifier(n_estimators=10, n_jobs=-1, criterion='entropy'),
        'AB': AdaBoostClassifier(DecisionTreeClassifier(max_depth=1), algorithm="SAMME", n_estimators=200),
        'LR': LogisticRegression(penalty='l1', C=1e5),
        'SVM': svm.SVC(kernel='linear', probability=True, random_state=0),
        'GB': GradientBoostingClassifier(learning_rate=0.05, subsample=0.5, max_depth=6, n_estimators=10),
        'NB': GaussianNB(),
        'DT': DecisionTreeClassifier(),
        'SGD': SGDClassifier(loss="hinge", penalty="l2"),
        'KNN': KNeighborsClassifier(n_neighbors=3)
        }

    def split_test_train(self, test_fraction, target):
        self.X = self.data.drop(target, axis=1)
        self.y = self.data[target]
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, \
            test_size=test_fraction)

    def gridsearch(self, params_dict, scores=['accuracy']):
        models = [(x, Grasp.available_classifiers[x], params_dict[x]) for x in list(params_dict.keys())]
        for score in scores:
            for model_abbr, model, params in models:
                clf = GridSearchCV(model, params, scoring=score, n_jobs=4)
                clf.fit(self.X_train, self.y_train)
                print(clf.best_params_)
    