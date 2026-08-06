python
import pytest
from texttable import Texttable
import os
import psutil

def task_func():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_usage = psutil.disk_usage(os.sep)

    table = Texttable()
    table.add_rows([
        ['Item', 'Value'],
        ['CPU Usage (%)', cpu_usage],
        ['Memory Usage (%)', memory_info.percent],
        ['Disk Usage (%)', disk_usage.percent]
    ])
    return table.draw()

def test_task_func():
    assert task_func() == '''
+----------+-------------+
| Item     | Value       |
+----------+-------------+
| CPU Usage(%) | 10.0        |
| Memory Usage(%) | 10.0        |
| Disk Usage(%) | 10.0        |
+----------+-------------+
'''