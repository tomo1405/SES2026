import matplotlib.pyplot as plt
import numpy as np
from src_0281 import task_func


def test_task_func():
    signal = np.array([1, 2, 3, 4, 5])
    precision = 2
    seed = 777
    expected_transformed_signal = np.array([1, 2, 3, 4, 5])
    expected_ax = plt.subplots(2, 1)
    expected_ax[0].plot(signal)
    expected_ax[0].set_title('Original Signal')
    expected_ax[1].plot(expected_transformed_signal)
    expected_ax[1].set_title('Transformed Signal')
    plt.tight_layout()

    transformed_signal, ax = task_func(signal, precision, seed)

    assert np.array_equal(transformed_signal, expected_transformed_signal)
    assert np.array_equal(ax, expected_ax)