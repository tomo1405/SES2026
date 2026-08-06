python
import pytest
from src_0124 import task_func

def test_task_func():
    # Test case 1: my_list is not a list
    with pytest.raises(TypeError):
        task_func("not a list")

    # Test case 2: file_dir does not exist
    with pytest.raises(FileNotFoundError):
        task_func([1, 2, 3], file_dir='./non_existent_dir/')

    # Test case 3: file_ext does not exist
    with pytest.raises(FileNotFoundError):
        task_func([1, 2, 3], file_ext='.txt')

    # Test case 4: valid input
    concatenated_df = task_func([1, 2, 3])
    assert isinstance(concatenated_df, pd.DataFrame)