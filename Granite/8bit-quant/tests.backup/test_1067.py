import pytest
from src_1067 import task_func

def test_task_func():
    data, outliers_detected, ax = task_func()
    assert isinstance(data, np.ndarray)
    assert isinstance(outliers_detected, np.ndarray)
    assert isinstance(ax, plt.Axes)
    assert len(data) == NUM_SAMPLES + NUM_OUTLIERS
    if NUM_SAMPLES > 0:
        assert len(outliers_detected) == NUM_OUTLIERS
    else:
        assert len(outliers_detected) == NUM_SAMPLES + NUM_OUTLIERS
    assert ax.get_xlabel() == 'Value'
    assert ax.get_ylabel() == 'Frequency'
    assert ax.get_title() == 'Histogram of Data'