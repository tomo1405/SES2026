import pytest
from src_0986 import task_func
import pandas as pd
import os
import json

def test_task_func_valid_json(tmpdir):
    json_data = '{"Countries": {"USA": 331002651, "China": 1412600000}}'
    output_dir = str(tmpdir)
    file_path, df = task_func(json_data, output_dir)

    assert os.path.exists(file_path)
    expected_df = pd.DataFrame({
        "Country": ["USA", "China"],
        "Population": [331002651, 1412600000]
    })
    pd.testing.assert_frame_equal(df, expected_df)

def test_task_func_invalid_json():
    json_data = '{"Countries": {"USA": 331002651, "China": "invalid"}}'
    with pytest.raises(ValueError) as excinfo:
        task_func(json_data)
    assert "Population must be an integer" in str(excinfo.value)

def test_task_func_missing_countries_key():
    json_data = '{"NotCountries": {"USA": 331002651}}'
    with pytest.raises(ValueError) as excinfo:
        task_func(json_data)
    assert "No valid country population data found in JSON" in str(excinfo.value)

def test_task_func_non_string_country():
    json_data = '{"Countries": {123: 331002651}}'
    with pytest.raises(ValueError) as excinfo:
        task_func(json_data)
    assert "Country name must be a string" in str(excinfo.value)

def test_task_func_negative_population():
    json_data = '{"Countries": {"USA": -331002651}}'
    with pytest.raises(ValueError) as excinfo:
        task_func(json_data)
    assert "Population cannot be negative" in str(excinfo.value)

def test_task_func_float_population(tmpdir):
    json_data = '{"Countries": {"USA": 331002651.5}}'
    output_dir = str(tmpdir)
    file_path, df = task_func(json_data, output_dir)

    assert os.path.exists(file_path)
    expected_df = pd.DataFrame({
        "Country": ["USA"],
        "Population": [331002651]
    })
    pd.testing.assert_frame_equal(df, expected_df)

def test_task_func_io_error(tmpdir):
    json_data = '{"Countries": {"USA": 331002651}}'
    output_dir = os.path.join(str(tmpdir), "non_writable")
    os.chmod(output_dir, 0o000)  # Make directory non-writable
    with pytest.raises(IOError) as excinfo:
        task_func(json_data, output_dir)
    assert "Failed to write the CSV file to" in str(excinfo.value)
    os.chmod(output_dir, 0o777)  # Reset permissions for cleanup