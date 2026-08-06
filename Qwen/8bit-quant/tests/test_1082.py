import pandas as pd
import pytest
import seaborn as sns
from src_1082 import task_func


def test_task_func_default_data():
    ax = task_func()
    assert isinstance(ax, sns.axisgrid.FacetGrid)
    df = ax.data
    assert df.equals(pd.DataFrame({
        "Weight_String": ["60.5", "65.7", "70.2", "75.9", "80.1"],
        "Height": [160, 165, 170, 175, 180],
        "Weight_Float": [60.5, 65.7, 70.2, 75.9, 80.1]
    }))

def test_task_func_custom_data():
    custom_data = {
        "Weight_String": ["55.3", "62.8", "68.4"],
        "Height": [155, 162, 168],
    }
    ax = task_func(custom_data)
    assert isinstance(ax, sns.axisgrid.FacetGrid)
    df = ax.data
    assert df.equals(pd.DataFrame({
        "Weight_String": ["55.3", "62.8", "68.4"],
        "Height": [155, 162, 168],
        "Weight_Float": [55.3, 62.8, 68.4]
    }))

def test_task_func_non_string_weights():
    custom_data = {
        "Weight_String": [60.5, 65.7, 70.2],
        "Height": [160, 165, 170],
    }
    with pytest.raises(ValueError, match="Weights must be provided as strings."):
        task_func(custom_data)