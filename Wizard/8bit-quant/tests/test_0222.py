python
import numpy as np
import scipy.stats as stats
import pandas as pd

# Constants
FEATURES = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']

def task_func(df, dct):
    # Replace values using dictionary mapping
    df = df.replace(dct)
    
    statistics = {}
    try:
        for feature in FEATURES:
            # Calculate statistics
            mean = np.mean(df[feature])
            median = np.median(df[feature])
            mode = stats.mode(df[feature])[0][0]
            variance = np.var(df[feature])
            
            # Store statistics in dictionary
            statistics[feature] = {'mean': mean, 'median': median, 'mode': mode, 'variance': variance}
    except Exception as e:
        return "Invalid input"        
    return statistics

# Test the function
df = pd.DataFrame({'feature1': [1, 2, 3, 4, 5],
                   'feature2': [2, 3, 4, 5, 6],
                   'feature3': [3, 4, 5, 6, 7],
                   'feature4': [4, 5, 6, 7, 8],
                   'feature5': [5, 6, 7, 8, 9]})

dct = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e'}

assert task_func(df, dct) == {'feature1': {'mean': 3.0, 'median': 3.0, 'mode': 3, 'variance': 2.0},
                              'feature2': {'mean': 3.5, 'median': 3.5, 'mode': 3, 'variance': 2.25},
                              'feature3': {'mean': 4.0, 'median': 4.0, 'mode': 4, 'variance': 2.5},
                              'feature4': {'mean': 4.5, 'median': 4.5, 'mode': 4, 'variance': 2.75},
                              'feature5': {'mean': 5.0, 'median': 5.0, 'mode': 5, 'variance': 3.0}}

# Test with invalid input
df = pd.DataFrame({'feature1': [1, 2, 3, 4, 5],
                   'feature2': [2, 3, 4, 5, 6],
                   'feature3': [3, 4, 5, 6, 7],
                   'feature4': [4, 5, 6, 7, 8],
                   'feature5': [5, 6, 7, 8, 9]})

dct = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f'}

assert task_func(df, dct) == "Invalid input"