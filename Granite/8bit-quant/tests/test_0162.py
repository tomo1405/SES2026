import pytest
from src_0162 import task_func

def test_task_func_valid_log_file():
    log_file = "valid_log_file.log"
    with open(log_file, "w") as file:
        file.write("ERROR: [2022-01-01 12:00:00] - Error message 1n")
        file.write("INFO: [2022-01-01 12:00:01] - Info message 1n")
        file.write("ERROR: [2022-01-01 12:00:02] - Error message 2n")
    output_csv_path = task_func(log_file)
    assert output_csv_path == "log_data.csv"
    with open("log_data.csv", "r") as file:
        contents = file.read()
        assert contents == "Type,Timestamp,MessagenERROR,2022-01-01 12:00:00,Error message 1nINFO,2022-01-01 12:00:01,Info message 1nERROR,2022-01-01 12:00:02,Error message 2n"

def test_task_func_invalid_log_file():
    log_file = "invalid_log_file.log"
    with open(log_file, "w") as file:
        file.write("Invalid log entry 1n")
        file.write("Invalid log entry 2n")
    with pytest.raises(ValueError) as excinfo:
        task_func(log_file)
    assert "No valid log entries found." in str(excinfo.value)

def test_task_func_invalid_timestamp_format():
    log_file = "invalid_timestamp_format.log"
    with open(log_file, "w") as file:
        file.write("ERROR: [2022-01-01 12:00:00] - Error message 1n")
        file.write("INFO: [2022-01-01 12:00:01] - Info message 1n")
        file.write("ERROR: [2022-01-01 12:00:02] - Error message 2n")
        file.write("ERROR: [2022-01-01 12:00:03] - Error message 3n")
    with pytest.raises(ValueError) as excinfo:
        task_func(log_file)
    assert "Invalid timestamp format: 2022-01-01 12:00:03" in str(excinfo.value)