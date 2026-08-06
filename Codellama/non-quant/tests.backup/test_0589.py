import pytest
from src_0589 import task_func

def test_task_func():
    # Test that the function returns a DataFrame
    assert isinstance(task_func(), pd.DataFrame)

    # Test that the DataFrame has the correct shape
    assert task_func().shape == (SIZE, 2)

    # Test that the DataFrame has the correct column names
    assert task_func().columns.tolist() == ['X', 'Y']

    # Test that the DataFrame has the correct data types
    assert task_func().dtypes.tolist() == [np.int64, np.int64]

    # Test that the DataFrame has the correct range of values
    assert (task_func()['X'] >= 0).all() and (task_func()['X'] < RANGE).all()
    assert (task_func()['Y'] >= 0).all() and (task_func()['Y'] < RANGE).all()

    # Test that the function plots a scatter plot using Seaborn
    assert plt.gcf().get_axes()[0].get_xlabel() == 'X'
    assert plt.gcf().get_axes()[0].get_ylabel() == 'Y'
    assert plt.gcf().get_axes()[0].get_title() == 'Scatter Plot'
    assert plt.gcf().get_axes()[0].get_xlim() == (0, RANGE)
    assert plt.gcf().get_axes()[0].get_ylim() == (0, RANGE)
    assert plt.gcf().get_axes()[0].get_xticks() == np.arange(0, RANGE+1)
    assert plt.gcf().get_axes()[0].get_yticks() == np.arange(0, RANGE+1)