import pytest
from src_0124 import task_func

def test_task_func():
    my_list = [1, 2, 3]
    file_dir = './data_files/'
    file_ext = '.csv'

    concatenated_df = task_func(my_list, file_dir, file_ext)

    assert isinstance(concatenated_df, pd.DataFrame)
    assert concatenated_df.shape[0] == sum(my_list)
    assert concatenated_df.shape[1] == 1

def test_task_func_invalid_input():
    my_list = [1, 2, 3]
    file_dir = './data_files/'
    file_ext = '.csv'

    with pytest.raises(TypeError):
        task_func(my_list, file_dir, file_ext, my_list)

    with pytest.raises(FileNotFoundError):
        task_func(my_list, file_dir, file_ext, [])