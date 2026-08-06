import pytest
from src_0120 import task_func

def test_task_func(capsys):
    # Since the function uses plt.show(), we cannot directly capture the plot.
    # Instead, we can check if the function runs without errors.
    try:
        task_func()
    except Exception as e:
        pytest.fail(f"task_func raised an exception: {e}")

    # To further validate, we can mock plt.show() and check if it was called.
    from unittest.mock import patch

    with patch('matplotlib.pyplot.show') as mock_show:
        task_func()
        mock_show.assert_called_once()