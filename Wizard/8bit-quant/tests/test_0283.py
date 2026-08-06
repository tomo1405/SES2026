python
import pytest
from src_0283 import task_func

def test_task_func():
    file_path = "test.jpg"
    def onpick(event):
        pass

    ax = task_func(file_path, onpick)

    assert isinstance(ax, Axes3D)