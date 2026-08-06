import numpy as np
import pandas as pd
def task_func(matrix1, matrix2):
    combined_matrix = np.concatenate((matrix1, matrix2), axis=1)
    df = pd.DataFrame(combined_matrix)
    return df.to_string(index=False, header=False)