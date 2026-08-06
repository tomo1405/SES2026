import pytest
from src_0872 import task_func

def test_task_func():
    data_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    file_name = 'mean_values.txt'
    expected_mean_values = [2, 5, 8]
    
    # Mocking the open function to avoid file operations during testing
    def mock_open(file, mode):
        mock_file = MagicMock(spec=file)
        return mock_file
    
    with patch('src_0872.open', mock_open) as mock_file:
        mean_values = task_func(data_list, file_name)
        mock_file.assert_called_once_with(file_name, 'w')
        
        # Asserting that the written mean values match the expected values
        for i, line in enumerate(mock_file.return_value.__enter__.return_value.write.call_args_list):
            position, mean_value = line[0][0].split(': ')
            assert int(position) == i + 1
            assert float(mean_value) == expected_mean_values[i]
        
        # Asserting that the returned mean values match the expected values
        assert mean_values == expected_mean_values