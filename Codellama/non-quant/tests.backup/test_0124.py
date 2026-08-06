import pytest
from src_0124 import task_func

def test_task_func_type_error():
    with pytest.raises(TypeError):
        task_func(123)

def test_task_func_file_not_found_error():
    with pytest.raises(FileNotFoundError):
        task_func([1, 2, 3], file_dir='./data_files/', file_ext='.txt')

def test_task_func_valid_input():
    my_list = [1, 2, 3]
    file_dir = './data_files/'
    file_ext = '.csv'
    expected_output = pd.concat([pd.read_csv(file) for file in glob.glob(os.path.join(file_dir, '*' + file_ext))], ignore_index=True)
    assert task_func(my_list, file_dir, file_ext).equals(expected_output)