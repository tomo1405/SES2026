import pytest
from src_0209 import task_func

def test_task_func_positive_integer():
    elements = 10
    seed = 0
    descriptive_stats, ax = task_func(elements, seed)
    assert isinstance(descriptive_stats, dict)
    assert isinstance(ax, matplotlib.axes.Axes)

def test_task_func_negative_integer():
    elements = -10
    seed = 0
    with pytest.raises(ValueError):
        task_func(elements, seed)

def test_task_func_non_integer():
    elements = 10.5
    seed = 0
    with pytest.raises(ValueError):
        task_func(elements, seed)

def test_task_func_zero_integer():
    elements = 0
    seed = 0
    with pytest.raises(ValueError):
        task_func(elements, seed)

def test_task_func_positive_seed():
    elements = 10
    seed = 1
    descriptive_stats, ax = task_func(elements, seed)
    assert isinstance(descriptive_stats, dict)
    assert isinstance(ax, matplotlib.axes.Axes)

def test_task_func_negative_seed():
    elements = 10
    seed = -1
    descriptive_stats, ax = task_func(elements, seed)
    assert isinstance(descriptive_stats, dict)
    assert isinstance(ax, matplotlib.axes.Axes)

def test_task_func_zero_seed():
    elements = 10
    seed = 0
    descriptive_stats, ax = task_func(elements, seed)
    assert isinstance(descriptive_stats, dict)
    assert isinstance(ax, matplotlib.axes.Axes)

def test_task_func_positive_percentiles():
    elements = 10
    seed = 0
    descriptive_stats, ax = task_func(elements, seed, percentiles=[.05, .25, .5, .75, .95])
    assert isinstance(descriptive_stats, dict)
    assert isinstance(ax, matplotlib.axes.Axes)

def test_task_func_negative_percentiles():
    elements = 10
    seed = 0
    with pytest.raises(ValueError):
        task_func(elements, seed, percentiles=[-0.05, -0.25, -0.5, -0.75, -0.95])

def test_task_func_zero_percentiles():
    elements = 10
    seed = 0
    with pytest.raises(ValueError):
        task_func(elements, seed, percentiles=[0, 0, 0, 0, 0])

def test_task_func_non_numeric_percentiles():
    elements = 10
    seed = 0
    with pytest.raises(ValueError):
        task_func(elements, seed, percentiles=['0.05', '0.25', '0.5', '0.75', '0.95'])

def test_task_func_non_list_percentiles():
    elements = 10
    seed = 0
    with pytest.raises(ValueError):
        task_func(elements, seed, percentiles=0.05)

def test_task_func_non_numeric_seed():
    elements = 10
    seed = '0'
    with pytest.raises(ValueError):
        task_func(elements, seed)

def test_task_func_non_integer_seed():
    elements = 10
    seed = 0.5
    with pytest.raises(ValueError):
        task_func(elements, seed)

def test_task_func_non_numeric_elements():
    elements = '10'
    seed = 0
    with pytest.raises(ValueError):
        task_func(elements, seed)

def test_task_func_non_integer_elements():
    elements = 10.5
    seed = 0
    with pytest.raises(ValueError):
        task_func(elements, seed)

def test_task_func_non_numeric_percentiles():
    elements = 10
    seed = 0
    with pytest.raises(ValueError):
        task_func(elements, seed, percentiles='0.05, 0.25, 0.5, 0.75, 0.95')

def test_task_func_non_list_percentiles():
    elements = 10
    seed = 0
    with pytest.raises(ValueError):
        task_func(elements, seed, percentiles=0.05)