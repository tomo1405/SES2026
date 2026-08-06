import pytest
from src_1018 import task_func
import pandas as pd

# Mocking dependencies
class MockDataFrame:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, key):
        return self.data[key]

    def drop(self, columns, axis=1):
        return MockDataFrame({col: self.data[col] for col in self.data if col not in columns})

    def to_csv(self, path_or_buf=None, index=False):
        pass

@pytest.fixture
def mock_csv_file(tmpdir):
    data = {
        'feature1': [0, 1, 0, 1],
        'feature2': [1, 0, 1, 0],
        'target': [0, 1, 0, 1]
    }
    df = pd.DataFrame(data)
    csv_file_path = tmpdir.join("test_data.csv")
    df.to_csv(csv_file_path, index=False)
    return str(csv_file_path)

def test_task_func(mock_csv_file):
    result = task_func(mock_csv_file)
    assert "precision" in result
    assert "recall" in result
    assert "f1-score" in result
    assert "support" in result

def test_task_func_missing_target_column(mock_csv_file):
    with pytest.raises(ValueError, match="'missing_target' column not found in the CSV file."):
        task_func(mock_csv_file, target_column="missing_target")

def test_task_func_with_custom_parameters(mock_csv_file):
    result = task_func(mock_csv_file, test_size=0.5, n_estimators=50)
    assert "precision" in result
    assert "recall" in result
    assert "f1-score" in result
    assert "support" in result