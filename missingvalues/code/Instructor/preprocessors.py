"""
Author      : Yi-Chieh Wu
Class       : HMC CS 121
Date        : 2018 Sep 25
Description : ML Preprocessors
"""

# python modules
from abc import ABC

# sklearn modules
from sklearn import preprocessing
from sklearn.impute import SimpleImputer

######################################################################
# classes
######################################################################

class Preprocessor(ABC):
    """Base class for preprocessor with hyper-parameter optimization.

    Attributes
    --------------------
        transformer_  -- transformer object
            This is assumed to implement the scikit-learn transformer interface.

        param_grid_ -- dict or list of dictionaries
            Dictionary with parameters names (string) as keys and lists of
            parameter settings to try as values, or a list of such
            dictionaries, in which case the grids spanned by each dictionary
            in the list are explored. This enables searching over any sequence
            of parameter settings.
    """
    def __init__(self):
        self.transformer_ = None
        self.param_grid_ = None

class Imputer(Preprocessor):
    """Preprocess to impute missing (NaN) entries."""

    def __init__(self):
        # impute missing (NaN) entries
        self.transformer_ = SimpleImputer(strategy='most_frequent')
        self.param_grid_ = {}


class Scaler(Preprocessor):
    """Preprocessor to scale features."""

    def __init__(self):
        self.transformer_ = preprocessing.StandardScaler()
        self.param_grid_ = {}


######################################################################
# globals
######################################################################

PREPROCESSORS = [c.__name__ for c in Preprocessor.__subclasses__()]