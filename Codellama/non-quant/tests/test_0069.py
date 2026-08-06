import pytest
from src_0069 import task_func

def test_task_func():
    # Test 1: Check if the function returns a tuple
    result = task_func()
    assert isinstance(result, tuple)

    # Test 2: Check if the first element of the tuple is a pandas DataFrame
    df, ax = result
    assert isinstance(df, pd.DataFrame)

    # Test 3: Check if the second element of the tuple is a seaborn Axes object
    assert isinstance(ax, sns.Axes)

    # Test 4: Check if the DataFrame has the correct columns
    expected_columns = ['Employee ID', 'Age']
    assert all(col in df.columns for col in expected_columns)

    # Test 5: Check if the DataFrame has the correct number of rows
    expected_num_rows = 10
    assert len(df) == expected_num_rows

    # Test 6: Check if the histogram is plotted correctly
    ax.set_xlabel('Age')
    ax.set_ylabel('Frequency')
    ax.set_title('Age Distribution')
    assert ax.get_xlabel() == 'Age'
    assert ax.get_ylabel() == 'Frequency'
    assert ax.get_title() == 'Age Distribution'