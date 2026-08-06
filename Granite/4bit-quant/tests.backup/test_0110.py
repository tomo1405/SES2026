import pandas as pd
import matplotlib.pyplot as plt
import pytest

def task_func(df, items=None, locations=None):
    if not isinstance(df, pd.DataFrame) or not all(col in df.columns for col in ['Item', 'Location']):
        raise ValueError("Invalid 'df': must be a DataFrame with 'Item' and 'Location' columns.")

    items = items or ['apple', 'banana', 'grape', 'orange', 'pineapple']
    locations = locations or ['store1', 'store2', 'store3', 'store4', 'store5']

    item_count_df = df.groupby(['Location', 'Item']).size().unstack().fillna(0)
    ax = item_count_df.plot(kind='bar', stacked=True)
    ax.set_title('Item Distribution by Location')
    ax.set_ylabel('Count')
    plt.show()
    return ax

def test_task_func():
    # Test case 1: Valid input
    df = pd.DataFrame({
        'Item': ['apple', 'banana', 'apple', 'orange', 'pineapple', 'banana'],
        'Location': ['store1', 'store2', 'store3', 'store1', 'store2', 'store4']
    })
    expected_output = task_func(df)
    assert expected_output is not None

    # Test case 2: Invalid input (not a DataFrame)
    with pytest.raises(ValueError) as excinfo:
        task_func('not a DataFrame')
    assert "Invalid 'df': must be a DataFrame with 'Item' and 'Location' columns." in str(excinfo.value)

    # Test case 3: Invalid input (missing 'Item' column)
    df = pd.DataFrame({
        'Location': ['store1', 'store2', 'store3', 'store1', 'store2', 'store4']
    })
    with pytest.raises(ValueError) as excinfo:
        task_func(df)
    assert "Invalid 'df': must be a DataFrame with 'Item' and 'Location' columns." in str(excinfo.value)

    # Test case 4: Invalid input (missing 'Location' column)
    df = pd.DataFrame({
        'Item': ['apple', 'banana', 'apple', 'orange', 'pineapple', 'banana']
    })
    with pytest.raises(ValueError) as excinfo:
        task_func(df)
    assert "Invalid 'df': must be a DataFrame with 'Item' and 'Location' columns." in str(excinfo.value)

if __name__ == '__main__':
    test_task_func()