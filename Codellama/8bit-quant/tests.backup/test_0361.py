import pytest
from src_0361 import task_func

def test_task_func_file_not_found():
    with pytest.raises(FileNotFoundError):
        task_func('non_existent_file.xlsx', 'Sheet1')

def test_task_func_sheet_not_found():
    with pytest.raises(ValueError):
        task_func('test_data.xlsx', 'non_existent_sheet')

def test_task_func_valid_input():
    result, fig = task_func('test_data.xlsx', 'Sheet1')
    assert isinstance(result, dict)
    assert isinstance(fig, matplotlib.figure.Figure)
    assert len(result) == 3
    assert all(isinstance(key, str) for key in result.keys())
    assert all(isinstance(value, dict) for value in result.values())
    assert all(isinstance(mean, float) for mean in result.values())
    assert all(isinstance(std, float) for std in result.values())
    assert all(mean > 0 for mean in result.values())
    assert all(std > 0 for std in result.values())