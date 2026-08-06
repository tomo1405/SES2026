import pytest
from src_0986 import task_func
import pandas as pd
import json
import os
import tempfile

def test_task_func_valid_json():
    json_data = '{"Countries": {"USA": 331002651, "Canada": 37742154}}'
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path, df = task_func(json_data, output_dir=temp_dir)
        assert os.path.exists(file_path)
        expected_df = pd.DataFrame({
            "Country": ["USA", "Canada"],
            "Population": [331002651, 37742154]
        })
        pd.testing.assert_frame_equal(df, expected_df)

def test_task_func_invalid_json():
    json_data = '{"Countries": {"USA": 331002651, "Canada": "37742154"}}'
    with pytest.raises(ValueError) as excinfo:
        task_func(json_data)
    assert "Population must be an integer" in str(excinfo.value)

def test_task_func_missing_countries_key():
    json_data = '{"NotCountries": {"USA": 331002651, "Canada": 37742154}}'
    with pytest.raises(ValueError) as excinfo:
        task_func(json_data)
    assert "No valid country population data found in JSON" in str(excinfo.value)

def test_task_func_non_string_country_name():
    json_data = '{"Countries": {123: 331002651, "Canada": 37742154}}'
    with pytest.raises(ValueError) as excinfo:
        task_func(json_data)
    assert "Country name must be a string" in str(excinfo.value)

def test_task_func_negative_population():
    json_data = '{"Countries": {"USA": -331002651, "Canada": 37742154}}'
    with pytest.raises(ValueError) as excinfo:
        task_func(json_data)
    assert "Population cannot be negative" in str(excinfo.value)

def test_task_func_float_population():
    json_data = '{"Countries": {"USA": 331002651.123, "Canada": 37742154}}'
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path, df = task_func(json_data, output_dir=temp_dir)
        assert os.path.exists(file_path)
        expected_df = pd.DataFrame({
            "Country": ["USA", "Canada"],
            "Population": [331002651, 37742154]
        })
        pd.testing.assert_frame_equal(df, expected_df)

def test_task_func_invalid_output_dir():
    json_data = '{"Countries": {"USA": 331002651, "Canada": 37742154}}'
    invalid_dir = "/invalid/path"
    with pytest.raises(IOError) as excinfo:
        task_func(json_data, output_dir=invalid_dir)
    assert f"Failed to write the CSV file to {invalid_dir}" in str(excinfo.value)