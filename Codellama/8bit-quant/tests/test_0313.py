from src_0313 import task_func


def test_task_func():
    distribution, ax = task_func()
    assert len(distribution) == DISTRIBUTION_SIZE
    assert len(ax.get_xticks()) == bins
    assert len(ax.get_yticks()) == bins
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'
    assert ax.get_title() == 'Histogram of Gaussian Distribution'