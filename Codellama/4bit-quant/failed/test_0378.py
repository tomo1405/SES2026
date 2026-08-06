import pytest
from src_0378 import task_func

def test_task_func():
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
    expected_output = table.draw()

    assert task_func() == expected_output