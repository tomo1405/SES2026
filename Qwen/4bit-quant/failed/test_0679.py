import pytest
from src_0679 import task_func
import pandas as pd
import os
import shutil
import tempfile
import json

@pytest.fixture
def setup_test_files(tmpdir):
    test_data = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25}
    ]
    json_file1 = tmpdir.join("data1.json")
    json_file1.write(json.dumps(test_data))

    json_file2 = tmpdir.join("data2.json")
    json_file2.write(json.dumps({"name": "Charlie", "age": 35}))

    return str(tmpdir)

def test_task_func(setup_test_files):
    path = setup_test_files
    result_df = task_func(path)

    expected_data = {
        "name": ["Alice", "Bob", "Charlie"],
        "age": [30, 25, 35],
        "source": ["data1.json", "data1.json", "data2.json"]
    }
    expected_df = pd.DataFrame(expected_data)

    pd.testing.assert_frame_equal(result_df, expected_df)

    processed_path = os.path.join(path, 'processed')
    assert os.path.exists(processed_path)
    assert len(os.listdir(processed_path)) == 2
    assert "data1.json" in os.listdir(processed_path)
    assert "data2.json" in os.listdir(processed_path)