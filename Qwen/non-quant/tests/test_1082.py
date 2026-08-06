import pytest
import seaborn as sns
from src_1082 import task_func


def test_task_func_default_data():
    ax = task_func()
    assert isinstance(ax, sns.axisgrid.FacetGrid)
    df = ax.data
    assert "Weight_String" in df.columns
    assert "Height" in df.columns
    assert "Weight_Float" in df.columns
    assert df.shape == (5, 3)
    assert df["Weight_String"].dtype == object
    assert df["Weight_Float"].dtype == float
    assert df["Height"].dtype == int

def test_task_func_custom_data():
    custom_data = {
        "Weight_String": ["62.0", "67.5", "72.1"],
        "Height": [162, 167, 172],
    }
    ax = task_func(custom_data)
    assert isinstance(ax, sns.axisgrid.FacetGrid)
    df = ax.data
    assert "Weight_String" in df.columns
    assert "Height" in df.columns
    assert "Weight_Float" in df.columns
    assert df.shape == (3, 3)
    assert df["Weight_String"].dtype == object
    assert df["Weight_Float"].dtype == float
    assert df["Height"].dtype == int

def test_task_func_non_string_weights():
    custom_data = {
        "Weight_String": [62.0, 67.5, 72.1],
        "Height": [162, 167, 172],
    }
    with pytest.raises(ValueError, match="Weights must be provided as strings."):
        task_func(custom_data)