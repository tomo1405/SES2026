import pandas as pd
import seaborn as sns
import pytest

from src_1082 import task_func

@pytest.fixture
def sample_data():
    return {
        "Weight_String": ["60.5", "65.7", "70.2", "75.9", "80.1"],
        "Height": [160, 165, 170, 175, 180],
    }

def test_task_func_with_no_data(sample_data):
    ax = task_func()
    df = pd.DataFrame(sample_data)
    assert ax.get_title() == "Weight vs Height"
    assert df["Weight_String"].dtype == "object"
    assert df["Weight_Float"].dtype == "float64"

def test_task_func_with_custom_data(sample_data):
    custom_data = {
        "Weight_String": ["65.0", "70.5", "75.2", "80.1", "85.5"],
        "Height": [165, 170, 175, 180, 185],
    }
    ax = task_func(custom_data)
    df = pd.DataFrame(custom_data)
    assert ax.get_title() == "Weight vs Height"
    assert df["Weight_String"].dtype == "object"
    assert df["Weight_Float"].dtype == "float64"

def test_task_func_with_invalid_data():
    invalid_data = {
        "Weight_String": ["60.5", "65.7", "70.2", "75.9", "80.1"],
        "Height": [160, 165, 170, 175, 180],
    }
    invalid_data["Weight_String"][0] = "abc"
    with pytest.raises(ValueError):
        task_func(invalid_data)