import pytest
from src_0216 import task_func

def test_task_func():
    url = "https://api.example.com/data"
    parameters = {"param1": "value1", "param2": "value2"}

    try:
        df, ax = task_func(url, parameters)
        assert isinstance(df, pd.DataFrame)
        assert isinstance(ax, sns.heatmap)
    except Exception as e:
        pytest.fail(f"Exception raised: {e}")