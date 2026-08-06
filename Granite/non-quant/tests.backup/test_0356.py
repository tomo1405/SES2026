import pytest
from src_0356 import task_func

@pytest.mark.parametrize("amplitude, frequency, time", [
    (1.0, 1.0, np.linspace(0, 1, 100)),  # Test case 1
    (2.0, 2.0, np.linspace(0, 2, 200)),  # Test case 2
    (3.0, 3.0, np.linspace(0, 3, 300)),  # Test case 3
])
def test_task_func(amplitude, frequency, time):
    wave, fig, ax = task_func(amplitude, frequency, time)
    assert isinstance(wave, np.ndarray)  # Check if wave is a numpy array
    assert fig.get_size_inches() == (10, 4)  # Check if figure size is correct
    assert ax.get_xlabel() == "Time"  # Check if x label is correct
    assert ax.get_ylabel() == "Amplitude"  # Check if y label is correct
    assert ax.get_legend().get_texts()[0].get_text() == "Real Part"  # Check if legend text is correct