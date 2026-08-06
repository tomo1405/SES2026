import pytest
from src_1057 import task_func

def test_task_func():
    # Test with default value
    bars = task_func()
    assert len(bars) == 26
    assert all(isinstance(bar, matplotlib.patches.Rectangle) for bar in bars)
    assert all(bar.get_label() == f"{letter}:{number}" for bar, letter, number in zip(bars, LETTERS, NUMBERS))

    # Test with custom value
    bars = task_func(n_pairs=10)
    assert len(bars) == 10
    assert all(isinstance(bar, matplotlib.patches.Rectangle) for bar in bars)
    assert all(bar.get_label() == f"{letter}:{number}" for bar, letter, number in zip(bars, LETTERS[:10], NUMBERS[:10]))

    # Test with invalid value
    with pytest.raises(ValueError):
        task_func(n_pairs=0)