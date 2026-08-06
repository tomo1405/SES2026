import os

import pandas as pd
import pytest
from src_0986 import task_func


def test_task_func_valid_json(tmpdir):
    json_data = '{"Countries": {"USA": 331002651, "China": 1412600000}}'
    output_dir = str(tmpdir)
    file_path, df = task_func(json_data, output_dir)

    assert os.path.exists(file_path)
    assert df.equals(pd.DataFrame({"Country": ["USA", "China"], "Population": [331002651, 1412600000]}))

def test_task_func_invalid_json():
    json_data = '{"Countries": {"USA": "three hundred million"}}'
    with pytest.raises(ValueError, match="Population must be an integer. Invalid entry for USA: three hundred million"):
        task_func(json_data)

def test_task_func_missing_countries_key():
    json_data = '{"NotCountries": {"USA": 331002651}}'
    with pytest.raises(ValueError, match="No valid country population data found in JSON."):
        task_func(json_data)

def test_task_func_negative_population():
    json_data = '{"Countries": {"USA": -331002651}}'
    with pytest.raises(ValueError, match="Population cannot be negative."):
        task_func(json_data)

def test_task_func_float_population(tmpdir):
    json_data = '{"Countries": {"USA": 331002651.5}}'
    output_dir = str(tmpdir)
    file_path, df = task_func(json_data, output_dir)

    assert os.path.exists(file_path)
    assert df.equals(pd.DataFrame({"Country": ["USA"], "Population": [331002651]}))

def test_task_func_non_string_country(tmpdir):
    json_data = '{"Countries": {123: 331002651}}'
    with pytest.raises(ValueError, match="Country name must be a string. Invalid entry: 123"):
        task_func(json_data, output_dir=tmpdir)