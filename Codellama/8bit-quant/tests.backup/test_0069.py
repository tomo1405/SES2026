import pytest
from src_0069 import task_func

def test_task_func():
    # Test 1: Check that the function returns a tuple with two elements
    result = task_func()
    assert isinstance(result, tuple)
    assert len(result) == 2

    # Test 2: Check that the first element of the tuple is a pandas DataFrame
    df, ax = result
    assert isinstance(df, pd.DataFrame)

    # Test 3: Check that the second element of the tuple is a seaborn Axes object
    assert isinstance(ax, sns.Axes)

    # Test 4: Check that the DataFrame returned by the function has the correct shape
    assert df.shape == (10, 3)

    # Test 5: Check that the Axes object returned by the function has the correct shape
    assert ax.shape == (10, 3)

    # Test 6: Check that the DataFrame returned by the function has the correct column names
    assert df.columns.tolist() == ['Employee ID', 'Age', 'Salary']

    # Test 7: Check that the Axes object returned by the function has the correct x-axis label
    assert ax.get_xlabel() == 'Age'

    # Test 8: Check that the Axes object returned by the function has the correct y-axis label
    assert ax.get_ylabel() == 'Salary'

    # Test 9: Check that the DataFrame returned by the function has the correct data
    assert df.equals(pd.DataFrame({'Employee ID': ['EMP1', 'EMP2', 'EMP3', 'EMP4', 'EMP5', 'EMP6', 'EMP7', 'EMP8', 'EMP9', 'EMP10'],
                                 'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
                                 'Salary': [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000]}))

    # Test 10: Check that the Axes object returned by the function has the correct data
    assert ax.get_data() == (np.array([25, 30, 35, 40, 45, 50, 55, 60, 65, 70]), np.array([50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000]))