import pytest
from src_0344 import task_func

def test_task_func():
    # Test that the function raises a ValueError when the DataFrame is empty
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df, 'col')

    # Test that the function raises a ValueError when the specified column does not exist
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
    with pytest.raises(ValueError):
        task_func(df, 'col3')

    # Test that the function returns a valid plot when the DataFrame is not empty and the specified column exists
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
    ax = task_func(df, 'col1')
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Pie Chart'

    # Test that the function returns a valid plot with a custom title when the DataFrame is not empty and the specified column exists
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
    ax = task_func(df, 'col1', 'Custom Title')
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Custom Title'