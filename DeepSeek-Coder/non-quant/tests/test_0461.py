import pytest
from src_0461 import task_func
import subprocess
import pandas as pd
import io

# Mock subprocess.run to simulate the behavior of running a script
def mock_subprocess_run(*args, **kwargs):
    class MockCompletedProcess:
        def __init__(self, returncode, stdout=b'', stderr=b''):
            self.returncode = returncode
            self.stdout = stdout
            self.stderr = stderr

    return MockCompletedProcess(returncode=0)

subprocess.run = mock_subprocess_run

# Mock pandas DataFrame
def test_task_func():
    # Mock DataFrame
    data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
    df = pd.DataFrame(data)
    output = io.StringIO()
    df.to_csv(output, index=False)

    # Call the function
    result = task_func('script_path', 'output.csv')

    # Assertions
    assert result == (df, ax)