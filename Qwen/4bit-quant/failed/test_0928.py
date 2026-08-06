import pytest
from src_0928 import task_func
import pandas as pd

@pytest.fixture
def sample_data():
    data = {
        'text_column': ['apple\nbanana', 'cherry', 'date\nfig', 'grape']
    }
    df = pd.DataFrame(data)
    return df

@pytest.fixture
def temp_csv_file(tmpdir, sample_data):
    temp_file = tmpdir.join("temp.csv")
    sample_data.to_csv(temp_file, index=False)
    return str(temp_file)

def test_task_func_replaces_newlines(temp_csv_file):
    result_df = task_func(temp_csv_file, 'text_column')
    assert result_df['text_column'].eq('apple<br>banana').any(), "Newlines should be replaced with <br>"
    assert result_df['text_column'].eq('date<br>fig').any(), "Newlines should be replaced with <br>"

def test_task_func_label_encoding(temp_csv_file):
    result_df = task_func(temp_csv_file, 'text_column')
    unique_values = result_df['text_column'].unique()
    assert len(unique_values) == 4, "All unique values should be encoded"
    assert all(isinstance(value, int) for value in unique_values), "All encoded values should be integers"

def test_task_func_input_validation(temp_csv_file):
    with pytest.raises(KeyError):
        task_func(temp_csv_file, 'non_existent_column')

def test_task_func_file_not_found():
    with pytest.raises(FileNotFoundError):
        task_func('non_existent_file.csv', 'text_column')