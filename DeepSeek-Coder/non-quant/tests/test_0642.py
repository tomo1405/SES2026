import pytest
from src_0642 import task_func
import os
import pandas as pd

@pytest.fixture
def setup():
    # Create a temporary directory and files for testing
    test_dir = 'test_dir'
    os.makedirs(test_dir, exist_ok=True)
    with open(os.path.join(test_dir, 'test_file1.txt'), 'w') as f:
        f.write('test content')
    yield test_dir
    # Clean up
    os.system(f'rm -rf {test_dir}')

def test_task_func(setup):
    pattern = 'test'
    directory = setup
    output_csv = 'output.csv'
    result = task_func(pattern, directory, output_csv)
    assert os.path.exists(output_csv)
    df = pd.read_csv(output_csv)
    assert not df.empty
    os.remove(output_csv)