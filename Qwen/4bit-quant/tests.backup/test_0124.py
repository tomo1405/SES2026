import pytest
from src_0124 import task_func

def test_task_func_with_valid_input():
    my_list = [1, 2, 3]
    file_dir = './data_files/'
    file_ext = '.csv'
    
    # Assuming there are at least 6 files (1+2+3) with .csv extension in the directory
    with pytest.raises(FileNotFoundError):
        task_func(my_list, file_dir, file_ext)

def test_task_func_with_non_list_input():
    my_list = "not_a_list"
    file_dir = './data_files/'
    file_ext = '.csv'
    
    with pytest.raises(TypeError):
        task_func(my_list, file_dir, file_ext)

def test_task_func_with_empty_list():
    my_list = []
    file_dir = './data_files/'
    file_ext = '.csv'
    
    # Assuming there is at least 1 file with .csv extension in the directory
    with pytest.raises(FileNotFoundError):
        task_func(my_list, file_dir, file_ext)

def test_task_func_with_insufficient_files():
    my_list = [5]
    file_dir = './data_files/'
    file_ext = '.csv'
    
    # Assuming there are less than 5 files with .csv extension in the directory
    with pytest.raises(FileNotFoundError):
        task_func(my_list, file_dir, file_ext)

# Note: The following test assumes that there are at least 6 files with .csv extension in the directory.
# If this condition is not met, the test will fail.
def test_task_func_with_sufficient_files():
    my_list = [1, 2, 3]
    file_dir = './data_files/'
    file_ext = '.csv'
    
    result_df = task_func(my_list, file_dir, file_ext)
    assert isinstance(result_df, pd.DataFrame)
    assert len(result_df) >= 6  # At least 6 rows if all files are read correctly