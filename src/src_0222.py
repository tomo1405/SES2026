import numpy as np
from scipy import stats
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