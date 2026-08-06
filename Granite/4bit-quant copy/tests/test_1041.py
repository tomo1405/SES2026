import pytest
from src_1041 import task_func

def test_task_func():
    assert task_func() == "Server started on localhost:12345. Ran for 5 seconds."

def test_task_func_custom_server_address():
    assert task_func(server_address="127.0.0.1") == "Server started on 127.0.0.1:12345. Ran for 5 seconds."

def test_task_func_custom_server_port():
    assert task_func(server_port=54321) == "Server started on localhost:54321. Ran for 5 seconds."

def test_task_func_custom_buffer_size():
    assert task_func(buffer_size=4096) == "Server started on localhost:12345. Ran for 5 seconds."

def test_task_func_custom_run_duration():
    assert task_func(run_duration=10) == "Server started on localhost:12345. Ran for 10 seconds."