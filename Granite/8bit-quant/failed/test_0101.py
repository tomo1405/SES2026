import matplotlib.pyplot as plt
import pandas as pd
import random
from datetime import datetime
from unittest.mock import patch

import pytest

from src_0101 import task_func

@pytest.fixture
def seed():
    return 42

@pytest.fixture
def dates():
    return pd.date_range(end=datetime.now(), periods=30)

@pytest.fixture
def values():
    return [random.randint(0, 100) for _ in range(30)]

@pytest.fixture
def ax():
    fig, ax = plt.subplots()
    return ax

def test_task_func(seed, dates, values, ax):
    with patch('random.seed', return_value=None) as mock_seed, \
         patch('random.randint', side_effect=values) as mock_randint, \
         patch('matplotlib.pyplot.subplots', return_value=(None, ax)) as mock_subplots, \
         patch('datetime.datetime') as mock_datetime:
         
        mock_datetime.now.return_value = datetime(2023, 1, 1)

        result = task_func(seed=seed)

        mock_seed.assert_called_once_with(seed)
        mock_randint.assert_has_calls([call(0, 100) for _ in range(30)])
        mock_datetime.now.assert_called_once()
        mock_subplots.assert_called_once_with()
        assert result == ax
        ax.plot.assert_called_once_with(dates, values, label='Value over Time')
        ax.set_xlabel.assert_called_once_with('Date')
        ax.set_ylabel.assert_called_once_with('Value')
        ax.set_title.assert_called_once_with('Random Time Series Data')
        ax.legend.assert_called_once_with()

def test_task_func_exception(seed):
    with patch('random.seed', return_value=None) as mock_seed, \
         patch('matplotlib.pyplot.subplots', side_effect=Exception('Mock Exception')) as mock_subplots:
         
        with pytest.raises(ValueError) as excinfo:
            task_func(seed=seed)

        mock_seed.assert_called_once_with(seed)
        mock_subplots.assert_called_once_with()
        assert str(excinfo.value) == "Error generating the plot: Mock Exception"