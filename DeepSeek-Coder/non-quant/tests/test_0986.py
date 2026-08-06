import pytest
from src_0986 import task_func
import os
import json
import pandas as pd
import math

def test_task_func_valid_data():
    json_data = '''{
        "Countries": {
            "USA": 331002651,
            "India": 1380004385,
            "Russia": 145912025
        }
    }'''
    output_dir = "test_output"
    file_name = "test_report.csv"
    os.makedirs(output_dir, exist_ok=True)
    file_path, df = task_func(json_data, output_dir)
    assert os.path.exists(file_path)
    df = pd.read_csv(file_path)
    assert df.shape == (3, 2)
    os.remove(file_path)
    os.rmdir(output_dir)

def test_task_func_invalid_json():
    json_data = "invalid_json"
    output_dir = "test_output"
    with pytest.raises(ValueError):
        task_func(json_data, output_dir)

def test_task_func_invalid_population():
    json_data = '''{
        "Countries": {
            "USA": 331002651,
            "India": "invalid_population",
            "Russia": -100
        }
    }'''
    output_dir = "test_output"
    with pytest.raises(ValueError):
        task_func(json_data, output_dir)

def test_task_func_invalid_country_name():
    json_data = '''{
        "Countries": {
            "USA": 331002651,
            "India": 1380004385,
            "Russia": "invalid_country_name"
        }
    }'''
    output_dir = "test_output"
    with pytest.raises(ValueError):
        task_func(json_data, output_dir)

def test_task_func_invalid_population_value():
    json_data = '''{
        "Countries": {
            "USA": 331002651,
            "India": 1380004385,
            "Russia": 145912025
        }
    }'''
    output_dir = "test_output"
    with pytest.raises(ValueError):
        task_func(json_data, output_dir)

def test_task_func_invalid_json_decode():
    json_data = "invalid_json"
    output_dir = "test_output"
    with pytest.raises(ValueError):
        task_func(json_data, output_dir)