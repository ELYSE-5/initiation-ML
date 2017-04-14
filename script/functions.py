import pandas as pd
import numpy as np


def get_catecorials(data, drop_features=None):
    """Get categorical data from a dataset

	Input
	=====
    """
    features = np.setdiff1d(data.columns.tolist(), drop_features).tolist()

    # Which one are objects types
    data_objects = data[features].loc[:, data.dtypes == object]
    categorial_features = []

    for feat in data_objects.columns.tolist():
        values = pd.unique(data_objects[feat])
        values = values[pd.notnull(values)]
        
        # Don't need to use the Bool with missing values
        tmp = np.setdiff1d(values, [True, False])

        # There is no need to keep the features with only one unique value
        if len(tmp) > 0:
        	categorial_features.append(feat)
            
    return categorial_features


def get_dummies(data_categorial):    
    """Convert categorials to dummies
    """ 
    df_dummies = pd.DataFrame()
    for feat in data_categorial.columns.tolist():
        df = pd.get_dummies(data_categorial[feat], dummy_na=True, prefix=feat)
        df_dummies = pd.concat([df_dummies, df], axis=1)
        
    return df_dummies