import pytest
from src_1017 import task_func

@pytest.mark.parametrize("url, expected_exception", [
    ("", ValueError),
    (123, ValueError),
    ("https://example.com", None),
    ("https://invalid-url", ValueError),
])
def test_task_func(url, expected_exception):
    if expected_exception is None:
        ax = task_func(url)
        assert isinstance(ax, plt.Axes)
    else:
        with pytest.raises(expected_exception):
            task_func(url)