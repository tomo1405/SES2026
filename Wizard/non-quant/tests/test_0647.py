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
    with pytest.raises(FileNotFoundError):
        task_func(csv_path='./non_existent_file.csv')

    df = pd.DataFrame({'date': ['2021-01-01', '2022-02-02', '2023-03-03']})
    df.to_csv(os.path.join(OUTPUT_DIR, 'data.csv'), index=False)

    hist = task_func()
    assert hist.shape == (1,)
    assert hist.index[0] == 2021
    assert hist.values[0] == 1
    os.remove(os.path.join(OUTPUT_DIR, 'data.csv'))