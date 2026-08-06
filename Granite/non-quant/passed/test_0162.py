import re
import pandas as pd
from datetime import datetime
from src_0162 import task_func
import pytest

def test_task_func():
    log_file = 'sample_log_file.txt'
    with open(log_file, 'w') as file:
        file.write("ERROR: [2023-01-01 12:00:00] - Error message 1n")
        file.write("INFO: [2023-01-01 12:00:01] - Info message 1n")
        file.write("ERROR: [2023-01-01 12:00:02] - Error message 2n")
        file.write("Invalid timestamp format: [2023-01-01 12:00:03] - Invalid timestampn")
        file.write("INFO: [2023-01-01 12:00:04] - Info message 2n")
    output_csv_path = task_func(log_file)
    assert output_csv_path == 'log_data.csv'
    df = pd.read_csv(output_csv_path)
    assert df.shape == (3, 3)
    assert df['Type'].tolist() == ['ERROR', 'INFO', 'ERROR']
    assert df['Timestamp'].tolist() == ['2023-01-01 12:00:00', '2023-01-01 12:00:01', '2023-01-01 12:00:02']
    assert df['Message'].tolist() == ['Error message 1', 'Info message 1', 'Error message 2']
    with pytest.raises(ValueError):
        task_func('invalid_log_file.txt')