import os
from datetime import datetime

import matplotlib
import pandas as pd
import pytest
from dateutil.parser import parse

OUTPUT_DIR = './output'
def task_func(csv_path=os.path.join(OUTPUT_DIR, 'data.csv'), date_column='date'):
    if not os.path.isfile(csv_path):
        raise FileNotFoundError(f"{csv_path} does not exist")
    df = pd.read_csv(csv_path)
    df[date_column] = df[date_column].apply(lambda x: parse(x))
    return df[date_column].dt.year.hist()
def test_task_func():
    # Test if the function raises a FileNotFoundError when the csv file does not exist
    with pytest.raises(FileNotFoundError):
        task_func(csv_path='invalid_path.csv')
    # Test if the function returns a histogram of years when the csv file exists
    csv_path = os.path.join(OUTPUT_DIR, 'data.csv')
    df = pd.DataFrame({
        'date': [datetime(2020, 1, 1), datetime(2021, 1, 1), datetime(2022, 1, 1)]
    })
    df.to_csv(csv_path, index=False)
    result = task_func(csv_path=csv_path)
    assert isinstance(result, matplotlib.axes.Axes)
    assert len(result.patches) == 3