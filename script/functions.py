import pandas as pd
import numpy as np


def get_catecorials(data, drop_features=None):
    """Get categorical data from a dataset

	Parameters
	----------

    data : DataFrame
        The dataset.

    drop_features : string, optional (default=None)
        If some features have to be avoided.

    Returns
    -------
    categorial_features : list of strings
        The features names than are considered categorical.

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


def get_dummies(data, dummy_na=True, sparse=False):
    """Convert categorials to dummies

    Parameters
    ----------
    data : DataFrame
        The categorical data. 

    dummy_na : bool, optional (default=True)
        Should we add a column for the NaN values.

    sparse : bool, optional (default=False)
        Whether the dummy columns should be sparse or not.

    Returns
    -------
    df_dummies : pd.Dataframe, shape = [n_samples, n_dummies]
        Return the data sample.
    """
    
    df_dummies = pd.DataFrame()
    for feat in data.columns.tolist():
        df = pd.get_dummies(data[feat], dummy_na=dummy_na, prefix=feat, sparse=sparse)
        df_dummies = pd.concat([df_dummies, df], axis=1)
        
    return df_dummies