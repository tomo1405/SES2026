import matplotlib.pyplot as plt
import pandas as pd
import random
from datetime import datetime
from unittest.mock import patch

def task_func(seed=42):
    try:
        plt.rc('font', family='Arial')

        random.seed(seed)
        dates = pd.date_range(end=datetime.now(), periods=30)
        values = [random.randint(0, 100) for _ in range(30)]
        
        fig, ax = plt.subplots()
        ax.plot(dates, values, label='Value over Time')
        ax.set_xlabel('Date')
        ax.set_ylabel('Value')
        ax.set_title('Random Time Series Data')
        ax.legend()

        return ax
    except Exception as e:
        raise ValueError(f"Error generating the plot: {e}")

def test_task_func():
    with patch('matplotlib.pyplot.show') as mock_show:
        ax = task_func()
        assert ax is not None
        mock_show.assert_called_once()

def test_task_func_seed():
    ax1 = task_func(seed=42)
    ax2 = task_func(seed=42)
    assert ax1.lines[0].get_ydata() == ax2.lines[0].get_ydata()

def test_task_func_seed_diff():
    ax1 = task_func(seed=42)
    ax2 = task_func(seed=43)
    assert ax1.lines[0].get_ydata() != ax2.lines[0].get_ydata()

def test_task_func_exception():
    with patch('matplotlib.pyplot.show') as mock_show:
        try:
            task_func(seed='abc')
        except ValueError:
            pass
        else:
            assert False, "Expected ValueError not raised"
        mock_show.assert_not_called()