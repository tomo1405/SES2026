import pytest
from src_1103 import task_func

def test_task_func():
    # Mocking the subprocess.Popen behavior
    class MockPopen:
        def __init__(self, args, stdout, stderr):
            self.args = args
            self.stdout = stdout
            self.stderr = stderr

        def communicate(self):
            return self.stdout, self.stderr

    # Mocking the datetime.now behavior
    class MockDatetime:
        @staticmethod
        def now():
            return datetime(2023, 1, 1, 12, 0, 0)

    # Patching subprocess.Popen and datetime.now
    with pytest.mock.patch('subprocess.Popen', return_value=MockPopen([], b'stdout', b'stderr')) as mock_popen, \
         pytest.mock.patch('datetime.datetime', MockDatetime):
        
        # Calling the function
        result = task_func('/path/to/script.R')

        # Assertions
        assert result == {
            'Start Time': '2023-01-01 12:00:00',
            'End Time': '2023-01-01 12:00:00',
            'Stdout': 'stdout',
            'Stderr': 'stderr'
        }

        # Check if Popen was called with the correct arguments
        mock_popen.assert_called_once_with(
            ['/usr/bin/Rscript', '--vanilla', '/path/to/script.R'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )