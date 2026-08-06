import pytest
from src_0378 import task_func
from unittest.mock import patch
from texttable import Texttable

def test_task_func_output_format():
    with patch('psutil.cpu_percent', return_value=50), \
         patch('psutil.virtual_memory', return_value=psutil._psutil_linux.svmem(total=1024, available=512, percent=50)), \
         patch('psutil.disk_usage', return_value=psutil._psutil_linux.sdiskusage(total=1024, used=512, free=512, percent=50)):
        result = task_func()
        expected_table = Texttable()
        expected_table.add_rows([
            ['Item', 'Value'],
            ['CPU Usage (%)', 50],
            ['Memory Usage (%)', 50],
            ['Disk Usage (%)', 50]
        ])
        assert result == expected_table.draw()

def test_task_func_cpu_usage():
    with patch('psutil.cpu_percent', return_value=75):
        result = task_func()
        assert 'CPU Usage (%)' in result and '75' in result

def test_task_func_memory_usage():
    with patch('psutil.virtual_memory', return_value=psutil._psutil_linux.svmem(total=1024, available=256, percent=75)):
        result = task_func()
        assert 'Memory Usage (%)' in result and '75' in result

def test_task_func_disk_usage():
    with patch('psutil.disk_usage', return_value=psutil._psutil_linux.sdiskusage(total=1024, used=768, free=256, percent=75)):
        result = task_func()
        assert 'Disk Usage (%)' in result and '75' in result