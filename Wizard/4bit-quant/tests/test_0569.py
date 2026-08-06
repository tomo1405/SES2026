python
import inspect
import matplotlib.pyplot as plt
import pandas as pd
import pytest

def task_func(f_list):
    func_info = []
    for f in f_list:
        if f.__name__ == "<lambda>":
            raise ValueError("The function should not be a lambda function.")
        spec = inspect.getfullargspec(f)
        func_info.append([f.__name__, len(spec.args)])

    df = pd.DataFrame(func_info, columns=['Function Name', 'Number of Arguments'])
    df.set_index('Function Name', inplace=True)
    df.plot(kind='bar')  # Uncomment to visualize the bar chart
    plt.show()  # Uncomment to display the plot
    return df

def test_task_func():
    def func1(a, b, c):
        pass

    def func2(d, e, f):
        pass

    def func3(g, h, i):
        pass

    f_list = [func1, func2, func3]

    with pytest.raises(ValueError):
        task_func([lambda x: x+1, func1, func2])

    with pytest.raises(ValueError):
        task_func([func1, func2, lambda x: x+1])

    df = task_func(f_list)
    assert df.shape == (3, 2)
    assert df.loc['func1', 'Number of Arguments'] == 3
    assert df.loc['func2', 'Number of Arguments'] == 3
    assert df.loc['func3', 'Number of Arguments'] == 3