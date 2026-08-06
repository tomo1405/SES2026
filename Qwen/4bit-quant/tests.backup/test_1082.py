import pytest
from src_1082 import task_func

def test_task_func_default_data():
    ax = task_func()
    assert isinstance(ax, sns.axisgrid.FacetGrid)
    assert "Weight_Float" in ax.data.columns
    assert "Height" in ax.data.columns
    assert all(isinstance(weight, float) for weight in ax.data["Weight_Float"])

def test_task_func_custom_data():
    custom_data = {
        "Weight_String": ["55.3", "62.8", "68.4", "74.0", "79.2"],
        "Height": [155, 160, 165, 170, 175],
    }
    ax = task_func(custom_data)
    assert isinstance(ax, sns.axisgrid.FacetGrid)
    assert "Weight_Float" in ax.data.columns
    assert "Height" in ax.data.columns
    assert all(isinstance(weight, float) for weight in ax.data["Weight_Float"])

def test_task_func_invalid_weight_type():
    invalid_data = {
        "Weight_String": [60.5, 65.7, 70.2, 75.9, 80.1],
        "Height": [160, 165, 170, 175, 180],
    }
    with pytest.raises(ValueError, match="Weights must be provided as strings."):
        task_func(invalid_data)