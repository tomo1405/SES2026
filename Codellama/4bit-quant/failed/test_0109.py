import pytest
from src_0109 import task_func

def test_task_func():
    # Test 1: Valid input
    df = pd.DataFrame({'group': ['A', 'B', 'C'], 'date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'value': [10, 20, 30]})
    result, ax = task_func(df, freq='D', decomposition_model='multiplicative')
    assert isinstance(result, pd.DataFrame)
    assert isinstance(ax, plt.Axes)

    # Test 2: Invalid input
    df = pd.DataFrame({'group': ['A', 'B', 'C'], 'date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'value': [10, 20, 30]})
    with pytest.raises(ValueError):
        task_func(df, freq='D', decomposition_model='invalid')

    # Test 3: Missing or non-numeric values in 'value' column
    df = pd.DataFrame({'group': ['A', 'B', 'C'], 'date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'value': [10, 20, 30]})
    df['value'][0] = 'invalid'
    with pytest.raises(ValueError):
        task_func(df, freq='D', decomposition_model='multiplicative')

    # Test 4: Invalid 'freq' parameter
    df = pd.DataFrame({'group': ['A', 'B', 'C'], 'date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'value': [10, 20, 30]})
    with pytest.raises(ValueError):
        task_func(df, freq=10, decomposition_model='multiplicative')

    # Test 5: Invalid 'decomposition_model' parameter
    df = pd.DataFrame({'group': ['A', 'B', 'C'], 'date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'value': [10, 20, 30]})
    with pytest.raises(ValueError):
        task_func(df, freq='D', decomposition_model='invalid')