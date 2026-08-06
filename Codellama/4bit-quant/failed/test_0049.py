import pytest
from src_0049 import task_func

def test_task_func():
    # Test that the function returns a list of timestamps
    timestamps = task_func(10)
    assert isinstance(timestamps, list)
    assert len(timestamps) == 10

    # Test that the function generates a histogram with the correct number of bins
    timestamps = task_func(10, output_path="test.png")
    assert plt.hist([datetime.strptime(t, DATE_FORMAT) for t in timestamps])

    # Test that the function saves the histogram to the correct file path
    timestamps = task_func(10, output_path="test.png")
    assert os.path.exists("test.png")

    # Test that the function raises a ValueError if the output_path is not a string
    with pytest.raises(ValueError):
        task_func(10, output_path=123)