import pandas as pd
import numpy as np
DEFAULT_COLUMNS = ['Element', 'Count']
def task_func(elements, include_index=False):
    elements_series = pd.Series(elements)
    count_series = elements_series.apply(lambda x: len(x))
    data_dict = {'Element': elements_series, 'Count': count_series}
    if include_index:
        data_dict['Index'] = np.arange(len(elements))
    count_df = pd.DataFrame(data_dict)
    if include_index:
        count_df = count_df[['Index', 'Element', 'Count']]  # Reordering columns to put 'Index' first
    return count_df