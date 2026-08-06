import pytest
from src_0410 import task_func

def test_task_func():
    # Test case 1: File not found
    with pytest.raises(FileNotFoundError):
        task_func('path/to/file', 'file_name', 'column_name')

    # Test case 2: Column not found
    with pytest.raises(ValueError):
        task_func('path/to/file', 'file_name', 'column_name')

    # Test case 3: Valid file and column
    df = pd.DataFrame({'column_name': [1, 2, 3, 4, 5]})
    mean = np.mean(df['column_name'])
    median = np.median(df['column_name'])
    std_dev = np.std(df['column_name'])
    expected_result = {'mean': mean, 'median': median, 'std_dev': std_dev}
    assert task_func('path/to/file', 'file_name', 'column_name') == expected_result