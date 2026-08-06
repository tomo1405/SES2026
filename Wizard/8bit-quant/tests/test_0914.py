python
import pytest
from src_0914 import task_func

def test_task_func():
    # Test empty data
    assert task_func([], 1) == {'mode': np.array([], dtype='object'), 'count': np.array([], dtype=int), 'fft': np.array([])}

    # Test no repetitions
    assert task_func([1, 2, 3], 0) == {'mode': np.array([], dtype='object'), 'count': np.array([], dtype=int), 'fft': np.array([])}

    # Test single value
    assert task_func([1], 1) == {'mode': np.array([1]), 'count': np.array([1]), 'fft': np.array([1.0+0.j])}

    # Test multiple values
    assert task_func([1, 2, 3], 2) == {'mode': np.array([1, 2, 3]), 'count': np.array([1, 1, 1]), 'fft': np.array([1.0+0.j, 2.0+0.j, 3.0+0.j])}

    # Test mixed values
    assert task_func([1, 'a', 2, 'a', 3], 2) == {'mode': np.array([1, 'a']), 'count': np.array([1, 2]), 'fft': np.array([1.0+0.j, 2.0+0.j, 3.0+0.j])}

    # Test repeated values
    assert task_func([1, 2, 3], 3) == {'mode': np.array([1, 2, 3]), 'count': np.array([1, 1, 1]), 'fft': np.array([1.0+0.j, 2.0+0.j, 3.0+0.j])}

    # Test repeated values with different types
    assert task_func([1, 'a', 2, 'a', 3], 3) == {'mode': np.array([1, 'a']), 'count': np.array([1, 2]), 'fft': np.array([1.0+0.j, 2.0+0.j, 3.0+0.j])}