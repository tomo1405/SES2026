import pytest
from src_0422 import task_func
import os
import tempfile
import requests

@pytest.fixture
def mock_requests_post(mocker):
    mock_post = mocker.patch('requests.post')
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_post.return_value = mock_response
    return mock_post

@pytest.fixture
def temp_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        yield temp_dir

@pytest.fixture
def sample_files(temp_directory):
    file_paths = []
    for i in range(3):
        file_path = os.path.join(temp_directory, f'sample_file_{i}.txt')
        with open(file_path, 'w') as f:
            f.write(f'This is sample file {i}')
        file_paths.append(file_path)
    return file_paths

def test_task_func(mock_requests_post, temp_directory, sample_files):
    url = 'http://example.com/upload'
    metadata = {'key': 'value'}
    
    status_codes = task_func(url, temp_directory, metadata)
    
    assert len(status_codes) == len(sample_files)
    assert all(code == 200 for code in status_codes)
    
    mock_requests_post.assert_called_with(
        url,
        files={'file': mocker.ANY},
        headers={'accept': 'text/json', 'Content-Type': 'application/json'},
        data=json.dumps(metadata)
    )
    assert mock_requests_post.call_count == len(sample_files)

def test_task_func_no_files(mock_requests_post, temp_directory):
    url = 'http://example.com/upload'
    metadata = {'key': 'value'}
    
    status_codes = task_func(url, temp_directory, metadata)
    
    assert status_codes == []
    mock_requests_post.assert_not_called()