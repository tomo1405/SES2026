import pytest
from src_0882 import task_func

# Mocking pandas read_csv to avoid reading actual files
def mock_read_csv(file_path):
    if file_path == 'test_data.csv':
        data = {'data': ['1x', '2y', '3x', '4z', '5x']}
        return pd.DataFrame(data)
    else:
        raise FileNotFoundError(f"No such file: '{file_path}'")

# Patching pandas read_csv with the mock function
@pytest.fixture(autouse=True)
def patch_pandas_read_csv(monkeypatch):
    monkeypatch.setattr(pd, 'read_csv', mock_read_csv)

def test_task_func_default_sample_size():
    result = task_func('test_data.csv')
    assert result.equals(pd.DataFrame({'data': ['1x', '3x', '5x']}))

def test_task_func_custom_sample_size():
    result = task_func('test_data.csv', sample_size=2)
    assert len(result) == 2
    assert all(result['data'].isin(['1x', '3x', '5x']))

def test_task_func_no_matches():
    result = task_func('test_data.csv', pattern='[a-zA-Z]+')
    assert result.empty

def test_task_func_invalid_file_path():
    with pytest.raises(FileNotFoundError):
        task_func('non_existent.csv')

def test_task_func_nonexistent_column():
    with pytest.raises(KeyError):
        task_func('test_data.csv', column_name='non_existent_column')

def test_task_func_zero_sample_size():
    result = task_func('test_data.csv', sample_size=0)
    assert result.empty

def test_task_func_larger_sample_size_than_matches():
    result = task_func('test_data.csv', sample_size=10)
    assert result.equals(pd.DataFrame({'data': ['1x', '3x', '5x']}))