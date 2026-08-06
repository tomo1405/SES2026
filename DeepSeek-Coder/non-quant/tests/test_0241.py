import pytest
from src_0241 import task_func

def test_task_func():
    result = task_func()
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert len(result) == 1000, "The DataFrame should contain 1000 rows"
    assert all(result.columns == ['Value']), "The DataFrame should have a column named 'Value'"
    assert all(0.0 <= value <= 10.0 for value in result['Value']), "All values should be between 0.0 and 10.0"