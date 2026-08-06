from unittest.mock import Mock, call, patch

from src_0630 import task_func


def test_task_func():
    dataset = [df1, df2, df3]  # Replace df1, df2, and df3 with your actual DataFrame objects
    filename = 'output.csv'
    output_dir = '/path/to/output'  # Replace with your desired output directory

    # Mock the os and time modules to avoid actual file operations and timing
    mock_os = Mock()
    mock_time = Mock()
    modules = {'os': mock_os, 'time': mock_time}

    with patch.dict('sys.modules', modules):
        mock_os.path.exists.return_value = True
        mock_time.time.return_value = 100

        task_func(dataset, filename, output_dir)

        mock_os.makedirs.assert_not_called()
        mock_os.makedirs.assert_not_called()
        mock_os.path.join.assert_called_once_with(output_dir, filename)
        mock_open = mock_open()
        mock_open.return_value.__enter__.return_value = mock_file = Mock()
        mock_file.write.assert_has_calls([
            call('DataFrame 1 content\n'),
            call('------\n'),
            call('DataFrame 2 content\n'),
            call('\n'),
            call('DataFrame 3 content')
        ])
        mock_file.close.assert_called_once()
        mock_time.time.assert_has_calls([call(), call()])
        assert mock_time.time.call_count == 2