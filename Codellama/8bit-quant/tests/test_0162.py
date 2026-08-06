import pytest
from src_0162 import task_func

def test_task_func_valid_log_file():
    log_file = 'valid_log_file.log'
    output_csv_path = task_func(log_file)
    assert output_csv_path == 'log_data.csv'
    df = pd.read_csv(output_csv_path)
    assert df.shape == (3, 3)
    assert df['Type'].tolist() == ['ERROR', 'INFO', 'ERROR']
    assert df['Timestamp'].tolist() == ['2022-01-01 12:00:00', '2022-01-01 12:00:01', '2022-01-01 12:00:02']
    assert df['Message'].tolist() == ['Error message 1', 'Info message 1', 'Error message 2']

def test_task_func_invalid_log_file():
    log_file = 'invalid_log_file.log'
    with pytest.raises(ValueError):
        task_func(log_file)

def test_task_func_empty_log_file():
    log_file = 'empty_log_file.log'
    with pytest.raises(ValueError):
        task_func(log_file)