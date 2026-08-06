import pytest
from src_1015 import task_func

def test_task_func_valid_input():
    api_url = "https://api.example.com/data"
    df, plot = task_func(api_url)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(plot, plt.Figure)

def test_task_func_invalid_input():
    api_url = 123
    with pytest.raises(TypeError):
        task_func(api_url)

def test_task_func_empty_response():
    api_url = "https://api.example.com/data"
    with requests_mock.Mocker() as m:
        m.get(api_url, json={})
        df, plot = task_func(api_url)
        assert df.empty
        assert plot is None