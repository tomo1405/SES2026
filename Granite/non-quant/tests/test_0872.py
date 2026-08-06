from unittest.mock import call, patch

from src_0872 import task_func


def test_task_func():
    data_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]
    file_name = 'mean_values.txt'
    
    # Mocking the open function to avoid file operations during testing
    with patch('src_0872.open', mock_open()) as mock_file:
        mean_values = task_func(data_list, file_name)
    
    # Asserting the returned mean values
    assert mean_values == [5.5, 7.5, 9.5]
    
    # Asserting that the file was opened with the correct mode and the correct data was written
    mock_file.assert_called_once_with(file_name, 'w')
    mock_file.return_value.write.assert_has_calls([
        call('Position 1: 5.5\n'),
        call('Position 2: 7.5\n'),
        call('Position 3: 9.5\n')
    ])