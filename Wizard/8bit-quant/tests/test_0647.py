python
import os
import pandas as pd
from dateutil.parser import parse
import pytest
from src_0647 import task_func

OUTPUT_DIR = './output'

def test_task_func():
    # Test case 1: csv file exists and date_column is valid
    csv_path = os.path.join(OUTPUT_DIR, 'data.csv')
    date_column = 'date'
    df = pd.DataFrame({date_column: ['2021-01-01', '2021-02-01', '2021-03-01']})
    df.to_csv(csv_path, index=False)
    assert task_func(csv_path, date_column) == [2021, 2021, 2021]

    # Test case 2: csv file does not exist
    with pytest.raises(FileNotFoundError):
        task_func('non_existent_file.csv', date_column)

    # Test case 3: date_column is not valid
    with pytest.raises(KeyError):
        task_func(csv_path, 'non_existent_column')