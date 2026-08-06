import os
import re
import json
import glob
from unittest.mock import patch, mock_open, MagicMock

def task_func(directory_path: str) -> list:
    # Check if directory exists
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"Directory {directory_path} not found.")
    
    json_files = glob.glob(directory_path + '/*.json')
    processed_files = []
    
    for json_file in json_files:
        with open(json_file, 'r') as file:
            data = json.load(file)
        
        escaped_data = json.dumps(data, ensure_ascii=False)
        escaped_data = re.sub(r'(?<!\\)"', r'\\\"', escaped_data)
        
        with open(json_file, 'w') as file:
            file.write(escaped_data)
        
        processed_files.append(json_file)
    
    return processed_files

def test_task_func():
    # Test if directory exists
    with patch('os.path.exists') as mock_exists:
        mock_exists.return_value = False
        with pytest.raises(FileNotFoundError) as exc_info:
            task_func('/path/to/directory')
        assert 'Directory /path/to/directory not found.' in str(exc_info.value)
    
    # Test if JSON files are processed correctly
    with patch('glob.glob') as mock_glob:
        mock_glob.return_value = ['/path/to/directory/file1.json', '/path/to/directory/file2.json']
        with patch('json.load') as mock_json_load:
            mock_json_load.return_value = {'key': 'value'}
            with patch('json.dumps') as mock_json_dumps:
                mock_json_dumps.return_value = '{"key": "value"}'
                with patch('re.sub') as mock_re_sub:
                    mock_re_sub.return_value = '{"key": "value"}'
                    with patch('json.dump') as mock_json_dump:
                        mock_json_dump.return_value = None
                        processed_files = task_func('/path/to/directory')
                        assert processed_files == ['/path/to/directory/file1.json', '/path/to/directory/file2.json']