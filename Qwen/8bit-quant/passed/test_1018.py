import pytest
from src_1018 import task_func
import pandas as pd
from io import StringIO

def test_task_func_with_valid_data():
    data = StringIO("""
    feature1,feature2,target
    0,0,0
    0,1,1
    1,0,1
    1,1,0
    """)
    csv_file_path = "data.csv"
    with open(csv_file_path, 'w') as file:
        file.write(data.getvalue())

    result = task_func(csv_file_path)
    assert isinstance(result, str)
    assert "precision" in result
    assert "recall" in result
    assert "f1-score" in result
    assert "support" in result

def test_task_func_with_missing_target_column():
    data = StringIO("""
    feature1,feature2
    0,0
    0,1
    1,0
    1,1
    """)
    csv_file_path = "data.csv"
    with open(csv_file_path, 'w') as file:
        file.write(data.getvalue())

    with pytest.raises(ValueError) as excinfo:
        task_func(csv_file_path, target_column="target")
    assert str(excinfo.value) == "'target' column not found in the CSV file."

def test_task_func_with_custom_test_size():
    data = StringIO("""
    feature1,feature2,target
    0,0,0
    0,1,1
    1,0,1
    1,1,0
    """)
    csv_file_path = "data.csv"
    with open(csv_file_path, 'w') as file:
        file.write(data.getvalue())

    result = task_func(csv_file_path, test_size=0.5)
    assert isinstance(result, str)
    assert "precision" in result
    assert "recall" in result
    assert "f1-score" in result
    assert "support" in result

def test_task_func_with_custom_n_estimators():
    data = StringIO("""
    feature1,feature2,target
    0,0,0
    0,1,1
    1,0,1
    1,1,0
    """)
    csv_file_path = "data.csv"
    with open(csv_file_path, 'w') as file:
        file.write(data.getvalue())

    result = task_func(csv_file_path, n_estimators=50)
    assert isinstance(result, str)
    assert "precision" in result
    assert "recall" in result
    assert "f1-score" in result
    assert "support" in result