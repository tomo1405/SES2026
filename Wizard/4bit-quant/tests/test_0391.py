python
import pytest
from src_0391 import task_func

def test_task_func_valid_input():
    csv_url_dict = {"URL": "https://example.com/data.csv"}
    sorted_df = task_func(csv_url_dict)
    assert isinstance(sorted_df, pd.DataFrame)
    assert sorted_df.shape[0] > 0
    assert sorted_df.shape[1] > 0

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func({})