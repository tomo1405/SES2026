import pytest
from src_0589 import task_func

def test_task_func():
    # Test that the function returns a DataFrame
    assert isinstance(task_func(), pd.DataFrame)

    # Test that the DataFrame has the correct shape
    assert task_func().shape == (SIZE, 2)

    # Test that the DataFrame contains only integers within the specified range
    assert np.all(task_func()['X'] >= 0)
    assert np.all(task_func()['X'] < RANGE)
    assert np.all(task_func()['Y'] >= 0)
    assert np.all(task_func()['Y'] < RANGE)

    # Test that the function draws a scatter plot using Seaborn
    assert sns.scatterplot.called
    assert plt.show.called