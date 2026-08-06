import pandas as pd
import json
import os
import math
import pytest
from src_0986 import task_func

def test_task_func_valid_json_data():
    json_data = '{"Countries": {"USA": 328239523, "Canada": 37661811}}'
    file_path, df = task_func(json_data)
    assert os.path.isfile(file_path)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
    assert df.columns.tolist() == ["Country", "Population"]
    assert df.loc[0, "Country"] == "USA"
    assert df.loc[0, "Population"] == 328239523
    assert df.loc[1, "Country"] == "Canada"
    assert df.loc[1, "Population"] == 37661811

def test_task_func_invalid_json_data():
    json_data = '{"Invalid": "Data"}'
    with pytest.raises(ValueError) as exc_info:
        task_func(json_data)
    assert "Invalid JSON data provided." in str(exc_info.value)

def test_task_func_no_country_data():
    json_data = '{"Invalid": "Data"}'
    with pytest.raises(ValueError) as exc_info:
        task_func(json_data)
    assert "No valid country population data found in JSON." in str(exc_info.value)

def test_task_func_invalid_country_name():
    json_data = '{"Countries": {"USA": 328239523, 123: 37661811}}'
    with pytest.raises(ValueError) as exc_info:
        task_func(json_data)
    assert "Country name must be a string. Invalid entry: 123" in str(exc_info.value)

def test_task_func_invalid_population_type():
    json_data = '{"Countries": {"USA": 328239523, "Canada": "Invalid"}}'
    with pytest.raises(ValueError) as exc_info:
        task_func(json_data)
    assert "Population must be an integer. Invalid entry for Canada: Invalid" in str(exc_info.value)

def test_task_func_negative_population():
    json_data = '{"Countries": {"USA": 328239523, "Canada": -100}}'
    with pytest.raises(ValueError) as exc_info:
        task_func(json_data)
    assert "Population cannot be negative." in str(exc_info.value)

def test_task_func_invalid_output_dir():
    json_data = '{"Countries": {"USA": 328239523, "Canada": 37661811}}'
    with pytest.raises(IOError) as exc_info:
        task_func(json_data, output_dir="/invalid/path")
    assert "Failed to write the CSV file to /invalid/path: " in str(exc_info.value)