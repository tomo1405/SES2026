import pytest
from src_0281 import task_func

def test_task_func():
    signal = np.array([1, 2, 3, 4, 5])
    precision = 2
    seed = 777

    transformed_signal, ax = task_func(signal, precision, seed)

    assert np.allclose(transformed_signal, np.array([1, 2, 3, 4, 5]))
    assert ax[0].get_title() == 'Original Signal'
    assert ax[1].get_title() == 'Transformed Signal'
    assert ax[0].get_xlabel() == 'Time'
    assert ax[0].get_ylabel() == 'Amplitude'
    assert ax[1].get_xlabel() == 'Frequency'
    assert ax[1].get_ylabel() == 'Amplitude'
    assert ax[0].get_xlim() == (0, 5)
    assert ax[0].get_ylim() == (0, 5)
    assert ax[1].get_xlim() == (0, 5)
    assert ax[1].get_ylim() == (0, 5)