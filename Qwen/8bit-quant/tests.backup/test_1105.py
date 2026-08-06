import pytest
from src_1105 import task_func

def test_task_func_success(mocker):
    # Mock subprocess.call to simulate successful execution
    mocker.patch('subprocess.call', return_value=0)
    
    # Mock threading.Thread to simulate thread behavior
    thread_mock = mocker.Mock()
    mocker.patch('threading.Thread', return_value=thread_mock)
    thread_mock.is_alive.return_value = False
    
    result = task_func('test_script.py')
    assert result == 'Script executed successfully.'

def test_task_func_timeout(mocker):
    # Mock subprocess.call to simulate successful execution
    mocker.patch('subprocess.call', return_value=0)
    
    # Mock threading.Thread to simulate thread behavior
    thread_mock = mocker.Mock()
    mocker.patch('threading.Thread', return_value=thread_mock)
    thread_mock.is_alive.return_value = True
    
    # Mock os.system to simulate process termination
    mocker.patch('os.system')
    
    result = task_func('test_script.py', timeout=1)
    assert result == 'Terminating process due to timeout.'
    os.system.assert_called_once_with('pkill -f "test_script.py"')

def test_task_func_script_not_found(mocker):
    # Mock subprocess.call to simulate script not found error
    mocker.patch('subprocess.call', side_effect=subprocess.CalledProcessError(1, 'python'))
    
    # Mock threading.Thread to simulate thread behavior
    thread_mock = mocker.Mock()
    mocker.patch('threading.Thread', return_value=thread_mock)
    thread_mock.is_alive.return_value = False
    
    result = task_func('non_existent_script.py')
    assert result == 'Script executed successfully.'

def test_task_func_permission_error(mocker):
    # Mock subprocess.call to simulate permission error
    mocker.patch('subprocess.call', side_effect=PermissionError)
    
    # Mock threading.Thread to simulate thread behavior
    thread_mock = mocker.Mock()
    mocker.patch('threading.Thread', return_value=thread_mock)
    thread_mock.is_alive.return_value = False
    
    result = task_func('permission_denied_script.py')
    assert result == 'Script executed successfully.'