import json
import math
import os
import pandas as pd
import pytest

from src_0986 import task_func

def test_task_func_valid_json_data():
    json_data = '{"Countries": {"China": 1403500365, "India": 1354417754}}'
    output_dir = "test_output"
    file_name = "test_country_population_report.csv"
    expected_file_path = os.path.join(output_dir, file_name)
    expected_df = pd.DataFrame(
        data=[["China", 1403500365], ["India", 1354417754]],
        columns=["Country", "Population"],
    )

    file_path, df = task_func(json_data, output_dir, file_name)

    assert file_path == expected_file_path
    assert df.equals(expected_df)

def test_task_func_invalid_json_data():
    json_data = '{"Invalid": "JSON"}'
    output_dir = "test_output"
    file_name = "test_country_population_report.csv"

    with pytest.raises(ValueError, match="Invalid JSON data provided."):
        task_func(json_data, output_dir, file_name)

def test_task_func_no_country_data():
    json_data = '{"Invalid": "JSON"}'
    output_dir = "test_output"
    file_name = "test_country_population_report.csv"

    with pytest.raises(ValueError, match="No valid country population data found in JSON."):
        task_func(json_data, output_dir, file_name)

def test_task_func_invalid_country_name():
    json_data = '{"Countries": {"123": 123}}'
    output_dir = "test_output"
    file_name = "test_country_population_report.csv"

    with pytest.raises(ValueError, match="Country name must be a string. Invalid entry: 123"):
        task_func(json_data, output_dir, file_name)

def test_task_func_invalid_population_type():
    json_data = '{"Countries": {"China": "123"}}'
    output_dir = "test_output"
    file_name = "test_country_population_report.csv"

    with pytest.raises(ValueError, match="Population must be an integer. Invalid entry for China: 123"):
        task_func(json_data, output_dir, file_name)

def test_task_func_invalid_population_value():
    json_data = '{"Countries": {"China": -123}}'
    output_dir = "test_output"
    file_name = "test_country_population_report.csv"

    with pytest.raises(ValueError, match="Population cannot be negative."):
        task_func(json_data, output_dir, file_name)

def test_task_func_failed_csv_write():
    json_data = '{"Countries": {"China": 123}}'
    output_dir = "invalid_output"
    file_name = "test_country_population_report.csv"

    with pytest.raises(IOError, match="Failed to write the CSV file to invalid_output"):
        task_func(json_data, output_dir, file_name)