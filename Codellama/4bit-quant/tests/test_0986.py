import os

import pandas as pd
import pytest
from src_0986 import task_func


def test_task_func_valid_json():
    json_data = '{"Countries": {"USA": 331.87, "China": 1.444, "India": 1.367}}'
    output_dir = "."
    file_name = "country_population_report.csv"
    expected_file_path = os.path.join(output_dir, file_name)
    expected_df = pd.DataFrame(
        [["USA", 331], ["China", 1], ["India", 1]], columns=["Country", "Population"]
    )

    file_path, df = task_func(json_data, output_dir, file_name)

    assert file_path == expected_file_path
    assert df.equals(expected_df)

def test_task_func_invalid_json():
    json_data = '{"Countries": {"USA": 331.87, "China": 1.444, "India": 1.367}'
    output_dir = "."
    file_name = "country_population_report.csv"

    with pytest.raises(ValueError):
        task_func(json_data, output_dir, file_name)

def test_task_func_invalid_country_name():
    json_data = '{"Countries": {"USA": 331.87, "China": 1.444, "India": 1.367}}'
    output_dir = "."
    file_name = "country_population_report.csv"

    with pytest.raises(ValueError):
        task_func(json_data, output_dir, file_name)

def test_task_func_invalid_population():
    json_data = '{"Countries": {"USA": 331.87, "China": 1.444, "India": 1.367}}'
    output_dir = "."
    file_name = "country_population_report.csv"

    with pytest.raises(ValueError):
        task_func(json_data, output_dir, file_name)

def test_task_func_negative_population():
    json_data = '{"Countries": {"USA": 331.87, "China": 1.444, "India": 1.367}}'
    output_dir = "."
    file_name = "country_population_report.csv"

    with pytest.raises(ValueError):
        task_func(json_data, output_dir, file_name)