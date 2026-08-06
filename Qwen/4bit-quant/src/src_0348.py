import pandas as pd
import re
import numpy as np
# Constants
PATTERN = r"([a-fA-F\d]{32})"
def task_func(df, column):

    matches = df[column].apply(lambda x: re.findall(PATTERN, x))
    flattened_matches = np.concatenate(matches.values)
    counts = pd.Series(flattened_matches).value_counts()
    
    return counts