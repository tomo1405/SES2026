import subprocess
import platform
import time
import pytest
from src_0196 import task_func

def test_task_func():
    # Test with a valid URL
    url = 'https://www.example.com'
    result = task_func(url)
    assert result == 0  # Assuming a successful return code of 0

    # Test with an invalid URL
    url = 'not_a_valid_url'
    with pytest.raises(subprocess.CalledProcessError):
        task_func(url)