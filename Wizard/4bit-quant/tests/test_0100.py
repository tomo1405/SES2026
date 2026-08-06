python
import pytest
from src_0100 import task_func

def test_task_func():
    fig = task_func()
    assert isinstance(fig, plt.Figure)
    assert fig.axes[0].get_title() == 'Iris Dataset Pair Plot'
    assert fig.axes[0].get_xlabel() == 'sepal length (cm)'
    assert fig.axes[0].get_ylabel() == 'sepal width (cm)'
    assert fig.axes[1].get_xlabel() == 'petal length (cm)'
    assert fig.axes[1].get_ylabel() == 'petal width (cm)'
    assert len(fig.axes) == 2