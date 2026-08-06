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
    assert fig.axes[2].get_xlabel() == 'sepal length (cm)'
    assert fig.axes[2].get_ylabel() == 'petal length (cm)'
    assert fig.axes[3].get_xlabel() == 'sepal length (cm)'
    assert fig.axes[3].get_ylabel() == 'petal width (cm)'
    assert fig.axes[4].get_xlabel() == 'sepal width (cm)'
    assert fig.axes[4].get_ylabel() == 'petal length (cm)'
    assert fig.axes[5].get_xlabel() == 'sepal width (cm)'
    assert fig.axes[5].get_ylabel() == 'petal width (cm)'