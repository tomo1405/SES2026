python
import pytest
from src_0378 import task_func

def test_task_func():
    assert task_func() == '''
+----------+-------------+
| Item     | Value       |
+----------+-------------+
| CPU Usage(%)| 0.0         |
| Memory Usage(%)| 10.0        |
| Disk Usage(%)| 10.0        |
+----------+-------------+
'''