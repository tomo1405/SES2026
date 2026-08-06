import pytest
from src_0071 import task_func
import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_json_file(tmp_path):
    data = [
        {"email": "test1@example.com", "list": [1, 2, 3]},
        {"email": "test2@example.com", "list": [4, 5, 6]}
    ]
    json_file = tmp_path / "sample.json"
    with open(json_file, 'w') as f:
        json.dump(data, f)
    return json_file

def test_task_func_with_data(sample_json_file):
    df, ax = task_func(str(sample_json_file))
    
    # Check DataFrame content
    expected_df = pd.DataFrame({
        'email': ['test1@example.com', 'test2@example.com'],
        'list': [[1, 2, 3], [4, 5, 6]],
        'sum': [6, 15],
        'mean': [2.0, 5.0]
    })
    pd.testing.assert_frame_equal(df, expected_df)
    
    # Check plot type
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == ''
    assert ax.get_xlabel() == ''
    assert ax.get_ylabel() == ''

def test_task_func_empty_json_file(tmp_path):
    json_file = tmp_path / "empty.json"
    json_file.touch()
    
    df, ax = task_func(str(json_file))
    
    # Check empty DataFrame
    expected_df = pd.DataFrame(columns=['email', 'list', 'sum', 'mean'])
    pd.testing.assert_frame_equal(df, expected_df)
    
    # Check that no plot is returned
    assert ax is None

def test_task_func_nonexistent_file(tmp_path):
    json_file = tmp_path / "nonexistent.json"
    
    with pytest.raises(FileNotFoundError):
        task_func(str(json_file))