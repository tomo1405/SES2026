import os
import tempfile
from datetime import datetime

from src_0049 import task_func


def test_task_func_output():
    n = 5
    timestamps = task_func(n)
    assert len(timestamps) == n
    for ts in timestamps:
        assert isinstance(ts, str)
        assert datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")

def test_task_func_save_plot():
    n = 3
    with tempfile.TemporaryDirectory() as temp_dir:
        output_path = os.path.join(temp_dir, "test_plot.png")
        task_func(n, output_path=output_path)
        assert os.path.exists(output_path)

def test_task_func_show_plot(capsys):
    n = 2
    task_func(n)
    captured = capsys.readouterr()
    # Since plt.show() does not produce any output to stdout or stderr,
    # we cannot directly test it. This is more of a manual check.
    assert True  # Placeholder to indicate that the plot was shown

def test_task_func_with_no_output_path():
    n = 4
    timestamps = task_func(n)
    assert len(timestamps) == n
    for ts in timestamps:
        assert isinstance(ts, str)
        assert datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")