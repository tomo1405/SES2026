import pytest
from src_0986 import task_func

def test_task_func_valid_json():
    json_data = '{"Countries": {"USA": 331002651, "China": 1439323776, "Japan": 1264134374}}'
    output_dir = "."
    file_name = "country_population_report.csv"
    expected_file_path = os.path.join(output_dir, file_name)
    expected_df = pd.DataFrame({"Country": ["USA", "China", "Japan"], "Population": [331002651, 1439323776, 1264134374]})

    file_path, df = task_func(json_data, output_dir, file_name)

    assert file_path == expected_file_path
    assert df.equals(expected_df)

def test_task_func_invalid_json():
    json_data = '{"Countries": {"USA": 331002651, "China": 1439323776, "Japan": 1264134374'
    output_dir = "."
    file_name = "country_population_report.csv"

    with pytest.raises(ValueError):
        task_func(json_data, output_dir, file_name)

def test_task_func_invalid_country_name():
    json_data = '{"Countries": {"USA": 331002651, "China": 1439323776, "Japan": 1264134374}}'
    output_dir = "."
    file_name = "country_population_report.csv"

    with pytest.raises(ValueError):
        task_func(json_data, output_dir, file_name, country_name="USA")

def test_task_func_invalid_population():
    json_data = '{"Countries": {"USA": 331002651, "China": 1439323776, "Japan": 1264134374}}'
    output_dir = "."
    file_name = "country_population_report.csv"

    with pytest.raises(ValueError):
        task_func(json_data, output_dir, file_name, population=-1)

def test_task_func_invalid_output_dir():
    json_data = '{"Countries": {"USA": 331002651, "China": 1439323776, "Japan": 1264134374}}'
    output_dir = "invalid_dir"
    file_name = "country_population_report.csv"

    with pytest.raises(IOError):
        task_func(json_data, output_dir, file_name)