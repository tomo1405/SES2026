import pytest
from src_0106 import task_func

def test_task_func():
    # Test 1: Empty DataFrame
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df)

    # Test 2: DataFrame without required columns
    df = pd.DataFrame({'group': [1, 2, 3], 'date': [1, 2, 3], 'value': [1, 2, 3]})
    with pytest.raises(ValueError):
        task_func(df)

    # Test 3: 'date' column not in datetime format
    df = pd.DataFrame({'group': [1, 2, 3], 'date': [1, 2, 3], 'value': [1, 2, 3]})
    with pytest.raises(ValueError):
        task_func(df)

    # Test 4: Valid DataFrame
    df = pd.DataFrame({'group': [1, 2, 3], 'date': [1, 2, 3], 'value': [1, 2, 3]})
    heatmap_fig, pairplot_grid = task_func(df)
    assert isinstance(heatmap_fig, plt.Figure)
    assert isinstance(pairplot_grid, sns.PairGrid)

if __name__ == '__main__':
    pytest.main()