import pytest
from src_0325 import task_func

def test_task_func():
    # Assuming the function is supposed to execute files and return exit codes
    # We need to mock subprocess and threading for testing
    
    # Mocking subprocess and threading for testing
    class MockProcess:
        def __init__(self):
            self.poll_result = None
        
        def poll(self):
            return self.poll_result
        
        def set_poll_result(self, result):
            self.poll_result = result
    
    class MockThread:
        def __init__(self, target, args=()):
            self.target = target
            self.args = args
        
        def start(self):
            self.target(*self.args)
        
        def join(self):
            pass
    
    # Mocking the imports
    import subprocess
    import threading
    
    # Mocking the subprocess.Popen
    subprocess.Popen = MockProcess
    threading.Thread = MockThread
    
    # Test data
    file_list = ["file1", "file2"]
    
    # Call the function
    result = task_func(file_list)
    
    # Assert the result (assuming we expect some specific exit codes)
    assert result == [None, None]  # Adjust based on expected exit codes