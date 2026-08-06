import os

from src_1051 import task_func


def test_task_func():
    input_string = "Hello\nWorld\nPython\n"
    expected_output = [
        os.path.join(DIRECTORY, "48e6433e9499027135026546d1d349129b8f597e.txt"),
        os.path.join(DIRECTORY, "7509e5bda0c762d2bac7f90d758b5b2263fa01cc.txt"),
        os.path.join(DIRECTORY, "11b4e497554961425f859875212eb19004a9f7e2.txt"),
    ]
    output = task_func(input_string)
    assert output == expected_output