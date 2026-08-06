import pytest
from io import BytesIO
import matplotlib.pyplot as plt
from src_0988 import task_func

def test_task_func_valid_json():
    json_data = '{"a": {"b": [1, 2, 3, 4, 5]}}'
    data_key = "a.b"
    original, normalized, ax = task_func(json_data, data_key)
    
    assert isinstance(original, pd.Series)
    assert isinstance(normalized, pd.Series)
    assert isinstance(ax, plt.Axes)
    assert all(original == pd.Series([1, 2, 3, 4, 5], dtype='Float64'))
    assert all(normalized == pd.Series(MinMaxScaler().fit_transform([[1], [2], [3], [4], [5]]).flatten(), dtype='Float64'))

def test_task_func_invalid_key():
    json_data = '{"a": {"b": [1, 2, 3, 4, 5]}}'
    data_key = "a.c"
    
    with pytest.raises(KeyError) as excinfo:
        task_func(json_data, data_key)
    assert str(excinfo.value) == "Key path 'a.c' not found in the provided JSON data."

def test_task_func_empty_data():
    json_data = '{"a": {"b": []}}'
    data_key = "a.b"
    original, normalized, ax = task_func(json_data, data_key)
    
    assert original.empty
    assert normalized is None
    assert ax is None

def test_task_func_single_value():
    json_data = '{"a": {"b": [1]}}'
    data_key = "a.b"
    original, normalized, ax = task_func(json_data, data_key)
    
    assert isinstance(original, pd.Series)
    assert isinstance(normalized, pd.Series)
    assert isinstance(ax, plt.Axes)
    assert all(original == pd.Series([1], dtype='Float64'))
    assert all(normalized == pd.Series([0.0], dtype='Float64'))

def test_task_func_nested_keys():
    json_data = '{"a": {"b": {"c": [1, 2, 3]}}}'
    data_key = "a.b.c"
    original, normalized, ax = task_func(json_data, data_key)
    
    assert isinstance(original, pd.Series)
    assert isinstance(normalized, pd.Series)
    assert isinstance(ax, plt.Axes)
    assert all(original == pd.Series([1, 2, 3], dtype='Float64'))
    assert all(normalized == pd.Series(MinMaxScaler().fit_transform([[1], [2], [3]]).flatten(), dtype='Float64'))

def test_task_func_plot_output():
    json_data = '{"a": {"b": [1, 2, 3, 4, 5]}}'
    data_key = "a.b"
    original, normalized, ax = task_func(json_data, data_key)
    
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    
    assert buf.getvalue()  # Check that the buffer contains data