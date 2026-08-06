import subprocess

import pytest
from src_0196 import task_func


def test_task_func_darwin():
    url = 'https://www.example.com'
    expected_cmd = 'open'
    expected_returncode = 0

    with pytest.raises(subprocess.CalledProcessError) as e:
        task_func(url)

    assert e.returncode == expected_returncode
    assert e.cmd == expected_cmd

def test_task_func_windows():
    url = 'https://www.example.com'
    expected_cmd = 'start'
    expected_returncode = 0

    with pytest.raises(subprocess.CalledProcessError) as e:
        task_func(url)

    assert e.returncode == expected_returncode
    assert e.cmd == expected_cmd

def test_task_func_linux():
    url = 'https://www.example.com'
    expected_cmd = 'xdg-open'
    expected_returncode = 0

    with pytest.raises(subprocess.CalledProcessError) as e:
        task_func(url)

    assert e.returncode == expected_returncode
    assert e.cmd == expected_cmd