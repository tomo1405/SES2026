import pytest
from src_0252 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_input_not_df():
    data = "not a DataFrame"
    with pytest.raises(ValueError):
        task_func(data)

def test_task_func_input_df():
    data = pd.DataFrame({"Job": ["A", "B", "C", "A", "B", "C"]})
    result = task_func(data)
    assert isinstance(result, plt.Figure)
    assert result.axes[0].pie.called
    assert result.axes[0].axis.called
    assert result.axes[0].set_equal.called