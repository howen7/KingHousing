import pandas as pd
import numpy as np
import json

import matplotlib.pyplot as plt
import seaborn as sns

import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.diagnostic import linear_rainbow, het_breuschpagan
from statsmodels.stats.outliers_influence import variance_inflation_factor

from sklearn.preprocessing import LabelEncoder



def correlation_info(dataframe, target, minimum_correlation):
    ''' 
    Creates a list of top correlated features and a heat map from a given dataframe
    Parameters
    ----------
    dataframe: a pandas dataframe
    
    target: The column from the dataframe we want to predict.(Example target = 'price')
        
    minimum_correlation: the minimum amount of correlation we want to see between our target variable and its features. (Example: .2)
    
    Returns
    -------
    A list of features with correlation over the minimum_correlation and a heat map of the correlation between all the dataframe columns. 
    '''

    correlation_index = dataframe.corr()[target].sort_values(ascending=False).index
    correlation = dataframe.corr()[target].sort_values(ascending=False)
    top_correlation =[]
    for i,j in correlation.items():
        if j > minimum_correlation:
            top_correlation.append(i)
    top_corr = top_correlation[1:]
    
    corr = dataframe[top_correlation].corr();
    mask = np.triu(np.ones_like(corr, dtype=np.bool));

    fig1, ax1 = plt.subplots(figsize=(16, 12));
    graph = sns.heatmap(corr, mask=mask, ax=ax1, cmap="viridis");
    
    return top_corr, graph


def model_summary(dataframe, target, list_of_features):
    '''
    dataframe: a pandas dataframe
    
    target: The column from the dataframe we want to predict.(Example target = 'price')
        
    list of features we want to use to predict our target: (Example  ['first', 'second', 'thrid'])
    
    Returns
    -------
    a summary of the model. 
    
    
    '''
    #features_scaled = (dataframe[list_of_features] - np.mean(dataframe[list_of_features])) / np.std(dataframe[list_of_features])
    #predictors = sm.add_constant(features_scaled)
    global test_model
    test_model = sm.OLS(dataframe[target], dataframe[list_of_features]).fit()
    return test_model.summary(), test_model