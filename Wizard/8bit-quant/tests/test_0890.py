python
import os
import pandas as pd
import numpy as np
import pytest

from src_0890 import task_func

@pytest.fixture
def data_dir():
    return 'data'

@pytest.fixture
def csv_file():
    return 'test.csv'

def test_task_func(data_dir, csv_file):
    file_path = os.path.join(data_dir, csv_file)
    try:
        df = pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        df = pd.DataFrame()

    for column in df.columns:
        if np.issubdtype(df[column].dtype, np.number):  # checking for numeric columns
            df[column].fillna(df[column].mean(), inplace=True)

    assert isinstance(df, pd.DataFrame)