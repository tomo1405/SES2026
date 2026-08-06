import pytest
from src_0860 import task_func

def test_task_func():
    accuracy, warning_msg = task_func()
    assert accuracy >= 0.9, "The accuracy of the SVM classification is below 0.9."
    assert warning_msg is None, "A warning message was raised, but it should not have been."

def test_task_func_warning():
    accuracy, warning_msg = task_func()
    assert accuracy < 0.9, "The accuracy of the SVM classification is not below 0.9."
    assert warning_msg is not None, "No warning message was raised, but one should have been."