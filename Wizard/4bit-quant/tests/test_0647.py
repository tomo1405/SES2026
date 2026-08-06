python
import os
import pandas as pd
from dateutil.parser import parse
import pytest

OUTPUT_DIR = './output'

def task_func(csv_path=os.path.join(OUTPUT_DIR, 'data.csv'), date_column='date'):

    if not os.path.isfile(csv_path):
        raise FileNotFoundError(f"{csv_path} does not exist")

    df = pd.read_csv(csv_path)
    df[date_column] = df[date_column].apply(lambda x: parse(x))

    return df[date_column].dt.year.hist()

def test_task_func():
    # Test case 1: Test if the function raises a FileNotFoundError if the csv file does not exist
    with pytest.raises(FileNotFoundError):
        task_func(csv_path='./data.csv')

    # Test case 2: Test if the function returns a histogram of the years in the date column
    df = pd.DataFrame({'date': ['2021-01-01', '2022-02-02', '2023-03-03', '2024-04-04']})
    df['date'] = df['date'].apply(lambda x: parse(x))
    hist = task_func(df=df)
    assert hist.shape == (4,)
    assert hist.sum() == 4