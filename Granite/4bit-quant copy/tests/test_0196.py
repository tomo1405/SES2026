import subprocess
import platform
import time
import pytest

def task_func(url):
    if platform.system() == 'Darwin':
        cmd = 'open'
    elif platform.system() == 'Windows':
        cmd = 'start'
    else:
        cmd = 'xdg-open'

    # Open webpage in a background process
    process = subprocess.Popen([cmd, url], shell=True)

    # Wait for the process to complete
    while process.poll() is None:
        time.sleep(1)

    return process.returncode

def test_task_func():
    # Test case 1: Open a valid URL on macOS
    with patch('platform.system', return_value='Darwin'):
        with patch('subprocess.Popen') as mock_popen:
            result = task_func('https://www.example.com')
            mock_popen.assert_called_with(['open', 'https://www.example.com'], shell=True)
            assert result == 0

    # Test case 2: Open a valid URL on Windows
    with patch('platform.system', return_value='Windows'):
        with patch('subprocess.Popen') as mock_popen:
            result = task_func('https://www.example.com')
            mock_popen.assert_called_with(['start', 'https://www.example.com'], shell=True)
            assert result == 0

    # Test case 3: Open a valid URL on Linux
    with patch('platform.system', return_value='Linux'):
        with patch('subprocess.Popen') as mock_popen:
            result = task_func('https://www.example.com')
            mock_popen.assert_called_with(['xdg-open', 'https://www.example.com'], shell=True)
            assert result == 0