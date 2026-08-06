import os
from unittest.mock import MagicMock, patch

import pandas as pd
from dateutil.parser import parse


def task_func(csv_path=os.path.join(OUTPUT_DIR, 'data.csv'), date_column='date'):
    if not os.path.isfile(csv_path):
        raise FileNotFoundError(f"{csv_path} does not exist")

    df = pd.read_csv(csv_path)
    df[date_column] = df[date_column].apply(lambda x: parse(x))

    return df[date_column].dt.year.hist()

def test_task_func():
    with patch('src_0647.os.path.isfile', MagicMock(return_value=True)):
        with patch('src_0647.pd.read_csv', MagicMock(return_value=pd.DataFrame())):
            with patch('src_0647.parse', MagicMock(return_value='parsed_date')):
                with patch('src_0647.pd.DataFrame.hist', MagicMock()) as mock_hist:
                    task_func()
                    mock_hist.assert_called_once()