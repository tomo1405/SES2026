import pandas as pd
import numpy as np
# Constants
COLUMNS = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']
def task_func(length):

    data = np.random.randint(0,100,size=(length, len(COLUMNS)))
    df = pd.DataFrame(data, columns=COLUMNS)

    return df