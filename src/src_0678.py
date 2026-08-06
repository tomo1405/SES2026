import numpy as np
import pandas as pd
from scipy.stats import linregress
def task_func(df):
    
    regression = linregress(df['var1'], df['var2'])
    
    # Explicit use of np.array to demonstrate the np. prefix usage
    # This step is purely illustrative and may not be necessary for this specific logic
    predictions = np.array(regression.slope) * np.array(df['var1']) + np.array(regression.intercept)
    
    df['predicted'] = pd.Series(predictions, index=df.index)

    return df