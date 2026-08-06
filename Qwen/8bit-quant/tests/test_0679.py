import pytest
from src_0679 import task_func
import pandas as pd
import os
import shutil
import tempfile
import json

@pytest.fixture
def setup_test_directory():
    test_dir = tempfile.mkdtemp()
    processed_dir = os.path.join(test_dir, 'processed')
    os.makedirs(processed_dir)

    # Create some test JSON files
    data1 = {'key1': 'value1'}
    data2 = [{'key2': 'value2'}, {'key3': 'value3'}]
    with open(os.path.join(test_dir, 'file1.json'), 'w') as f:
        json.dump(data1, f)
    with open(os.path.join(test_dir, 'file2.json'), 'w') as f:
        json.dump(data2, f)
    with open(os.path.join(test_dir, 'file3.txt'), 'w') as f:
        f.write('This is a text file.')

    yield test_dir

    # Clean up
    shutil.rmtree(test_dir)

def test_task_func(setup_test_directory):
    test_dir = setup_test_directory
    result_df = task_func(test_dir)

    # Check if the processed directory exists
    processed_dir = os.path.join(test_dir, 'processed')
    assert os.path.exists(processed_dir)

    # Check if the original JSON files have been moved to the processed directory
    assert not os.path.exists(os.path.join(test_dir, 'file1.json'))
    assert not os.path.exists(os.path.join(test_dir, 'file2.json'))
    assert os.path.exists(os.path.join(processed_dir, 'file1.json'))
    assert os.path.exists(os.path.join(processed_dir, 'file2.json'))

    # Check the contents of the resulting DataFrame
    expected_data = [
        {'key1': 'value1', 'source': 'file1.json'},
        {'key2': 'value2', 'source': 'file2.json'},
        {'key3': 'value3', 'source': 'file2.json'}
    ]
    expected_df = pd.DataFrame(expected_data)
    pd.testing.assert_frame_equal(result_df.reset_index(drop=True), expected_df)

def test_task_func_no_json_files(setup_test_directory):
    test_dir = setup_test_directory
    # Remove all JSON files
    for filename in os.listdir(test_dir):
        if filename.endswith('.json'):
            os.remove(os.path.join(test_dir, filename))

    result_df = task_func(test_dir)

    # Check if the processed directory exists
    processed_dir = os.path.join(test_dir, 'processed')
    assert os.path.exists(processed_dir)

    # Check if the DataFrame is empty
    assert result_df.empty

def test_task_func_empty_directory(setup_test_directory):
    test_dir = setup_test_directory
    # Remove all files
    for filename in os.listdir(test_dir):
        os.remove(os.path.join(test_dir, filename))

    result_df = task_func(test_dir)

    # Check if the processed directory exists
    processed_dir = os.path.join(test_dir, 'processed')
    assert os.path.exists(processed_dir)

    # Check if the DataFrame is empty
    assert result_df.empty