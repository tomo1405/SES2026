import pandas as pd
import numpy as np
import itertools
from src_0871 import task_func

def test_task_func():
    data_list = [('a', 1, 2.1), ('b', 2, 3.2), ('c', 3, 4.3), ('d', 4, 5.4), ('e', 5, 6.5)]
    unzipped_data = list(itertools.zip_longest(*data_list, fillvalue=np.nan))
    mean_values = []
    for column in unzipped_data[:]:
        numeric_values = [val for val in column if isinstance(val, (int, float))]
        if numeric_values:
            mean_values.append(np.nanmean(numeric_values))
        else:
            mean_values.append(np.nan)
    expected_df = pd.DataFrame(mean_values, columns=['Mean Value'], 
                               index=['Position {}'.format(i) for i in range(len(mean_values))])
    actual_df = task_func(data_list)
    pd.testing.assert_frame_equal(actual_df, expected_df)