import pandas as pd
import numpy as np
def task_func(file_path, num_rows, data_dimensions=5, random_seed=None):
    np.random.seed(random_seed)
    df = pd.DataFrame(np.random.rand(num_rows, data_dimensions),
                      columns=[f'Feature_{i + 1}' for i in range(data_dimensions)])

    df.to_csv(file_path, index=False)

    return file_path