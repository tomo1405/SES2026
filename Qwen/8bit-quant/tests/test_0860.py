import pytest
from src_0860 import task_func

def test_task_func_accuracy():
    accuracy, warning_msg = task_func()
    assert isinstance(accuracy, float)
    assert 0 <= accuracy <= 1

def test_task_func_warning():
    accuracy, warning_msg = task_func()
    if accuracy < 0.9:
        assert warning_msg == "The accuracy of the SVM classification is below 0.9."
    else:
        assert warning_msg is None