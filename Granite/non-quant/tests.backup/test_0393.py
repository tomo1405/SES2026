import pytest
from src_0393 import task_func

def test_task_func():
    # Mock DataFrame
    df = pd.DataFrame({
        'group_col': ['A', 'B', 'A', 'C', 'B'],
        'value_col': [10, 20, 30, 40, 50]
    })

    # Test case 1: group_name exists in group_col
    ax = task_func(df, 'group_col', 'value_col', 'A')
    assert ax.get_title() == 'Bar chart of value_col for A'

    # Test case 2: group_name does not exist in group_col
    with pytest.raises(ValueError):
        task_func(df, 'group_col', 'value_col', 'D')

    # Test case 3: empty DataFrame
    df_empty = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df_empty, 'group_col', 'value_col', 'A')