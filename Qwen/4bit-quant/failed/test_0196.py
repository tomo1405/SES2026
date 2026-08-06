import pytest
from src_0196 import task_func

def test_task_func_success():
    # Mock the platform.system to simulate a Darwin system
    platform.system = lambda: 'Darwin'
    
    # Mock subprocess.Popen to simulate a successful process
    class MockPopen:
        def __init__(self, args, shell):
            self.args = args
            self.shell = shell
        
        def poll(self):
            return 0  # Simulate successful completion
    
    subprocess.Popen = MockPopen
    
    # Test with a valid URL
    result = task_func('http://example.com')
    assert result == 0

def test_task_func_failure():
    # Mock the platform.system to simulate a Darwin system
    platform.system = lambda: 'Darwin'
    
    # Mock subprocess.Popen to simulate a failed process
    class MockPopen:
        def __init__(self, args, shell):
            self.args = args
            self.shell = shell
        
        def poll(self):
            return 1  # Simulate failure
    
    subprocess.Popen = MockPopen
    
    # Test with a valid URL
    result = task_func('http://example.com')
    assert result == 1

def test_task_func_windows():
    # Mock the platform.system to simulate a Windows system
    platform.system = lambda: 'Windows'
    
    # Mock subprocess.Popen to simulate a successful process
    class MockPopen:
        def __init__(self, args, shell):
            self.args = args
            self.shell = shell
        
        def poll(self):
            return 0  # Simulate successful completion
    
    subprocess.Popen = MockPopen
    
    # Test with a valid URL
    result = task_func('http://example.com')
    assert result == 0

def test_task_func_other():
    # Mock the platform.system to simulate another OS (e.g., Linux)
    platform.system = lambda: 'Linux'
    
    # Mock subprocess.Popen to simulate a successful process
    class MockPopen:
        def __init__(self, args, shell):
            self.args = args
            self.shell = shell
        
        def poll(self):
            return 0  # Simulate successful completion
    
    subprocess.Popen = MockPopen
    
    # Test with a valid URL
    result = task_func('http://example.com')
    assert result == 0