from src_0575 import task_func


def test_task_func():
    ax = task_func()
    assert ax is not None
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'
    assert ax.lines[0].get_label() == 'data'
    assert ax.lines[1].get_label() == 'fit: a=%5.3f, b=%5.3f' % tuple(popt)