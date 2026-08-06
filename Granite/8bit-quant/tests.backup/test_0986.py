import pandas as pd
import json
import os
import math
import pytest
from src_0986 import task_func

def test_task_func_valid_json_data():
    json_data = '{"Countries": {"USA": 328239520, "Canada": 376618112}}'
    output_dir = "test_output"
    file_name = "test_country_population_report.csv"
    file_path, df = task_func(json_data, output_dir, file_name)
    assert os.path.exists(file_path)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
    assert df.columns.tolist() == ["Country", "Population"]
    assert df.loc[0, "Country"] == "USA"
    assert df.loc[0, "Population"] == 328239520
    assert df.loc[1, "Country"] == "Canada"
    assert df.loc[1, "Population"] == 376618112
    os.remove(file_path)
    os.rmdir(output_dir)

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
    json_data = '{"Countries": {"USA": 328239520, 123: 376618112}}'
    with pytest.raises(ValueError) as exc_info:
        task_func(json_data)
    assert "Country name must be a string. Invalid entry: 123" in str(exc_info.value)

def test_task_func_invalid_population():
    json_data = '{"Countries": {"USA": 328239520, "Canada": "Invalid"}}'
    with pytest.raises(ValueError) as exc_info:
        task_func(json_data)
    assert "Population must be an integer. Invalid entry for Canada: Invalid" in str(exc_info.value)

def test_task_func_negative_population():
    json_data = '{"Countries": {"USA": 328239520, "Canada": -100}}'
    with pytest.raises(ValueError) as exc_info:
        task_func(json_data)
    assert "Population cannot be negative." in str(exc_info.value)

def test_task_func_failed_csv_write():
    json_data = '{"Countries": {"USA": 328239520, "Canada": 376618112}}'
    output_dir = "/invalid_output_dir"
    file_name = "test_country_population_report.csv"
    with pytest.raises(IOError) as exc_info:
        task_func(json_data, output_dir, file_name)
    assert "Failed to write the CSV file to /invalid_output_dir" in str(exc_info.value)