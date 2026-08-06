import pytest
from src_1005 import task_func

def test_task_func():
    url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    word_freq, ax = task_func(url)
    assert isinstance(word_freq, dict)
    assert len(word_freq) > 10
    assert isinstance(ax, object)

if __name__ == "__main__":
    pytest.main()