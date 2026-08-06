python
import pytest
from src_0592 import task_func

def test_task_func():
    # Test with default file path
    file_path, ax = task_func(10)
    assert isinstance(file_path, str)
    assert file_path == 'custom_data.csv'
    assert isinstance(ax, plt.Axes)

    # Test with custom file path
    file_path, ax = task_func(10, 'custom_file.csv')
    assert isinstance(file_path, str)
    assert file_path == 'custom_file.csv'
    assert isinstance(ax, plt.Axes)

    # Test with invalid input
    with pytest.raises(TypeError):
        task_func('10')

    # Test with invalid input
    with pytest.raises(ValueError):
        task_func(-10)