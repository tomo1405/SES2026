from io import StringIO

import pandas as pd
from src_0191 import task_func


def test_task_func_with_stringio():
    csv_input = StringIO('col1,col2,col3\n1,2,3\n4,5,6')
    dataframe = task_func(csv_input)
    assert isinstance(dataframe, pd.DataFrame)
    assert dataframe.shape == (2, 3)
    assert dataframe.columns.tolist() == ['col1', 'col2', 'col3']
    assert dataframe.iloc[0].tolist() == ['1', '2', '3']
    assert dataframe.iloc[1].tolist() == ['4', '5', '6']

def test_task_func_with_file_path():
    csv_input = 'test_data.csv'
    dataframe = task_func(csv_input)
    assert isinstance(dataframe, pd.DataFrame)
    assert dataframe.shape == (2, 3)
    assert dataframe.columns.tolist() == ['col1', 'col2', 'col3']
    assert dataframe.iloc[0].tolist() == ['1', '2', '3']
    assert dataframe.iloc[1].tolist() == ['4', '5', '6']