import pytest
from src_1015 import task_func

def test_task_func():
    # Test with a valid API URL
    api_url = "https://api.example.com/data"
    df, plot = task_func(api_url)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(plot, plt.Figure)

    # Test with an invalid API URL
    api_url = 123
    with pytest.raises(TypeError):
        task_func(api_url)

    # Test with a valid API URL but no data
    api_url = "https://api.example.com/data"
    df, plot = task_func(api_url)
    assert isinstance(df, pd.DataFrame)
    assert plot is None