python
import psutil
from texttable import Texttable
import os

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
+----------+-------+
| Item     | Value |
+----------+-------+
| CPU Usage (%) | 1.0 |
| Memory Usage (%) | 1.0 |
| Disk Usage (%) | 1.0 |
+----------+-------+
'''