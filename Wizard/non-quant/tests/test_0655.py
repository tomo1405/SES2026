python
import pytest
from src_0655 import task_func

def test_task_func():
    array = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
    target_value = 3
    popt, ax = task_func(array, target_value)
    assert popt[0] == pytest.approx(1.0000000000000002)
    assert popt[1] == pytest.approx(0.09531017980432493)
    assert popt[2] == pytest.approx(2.9999999999999996)
    assert ax.get_title() == 'Fit'