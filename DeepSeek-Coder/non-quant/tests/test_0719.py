import pytest
from src_0719 import task_func

@pytest.fixture
def example_data():
    text1 = "This is a sample text for testing."
    text2 = "This text is for testing purposes."
    return text1, text2

@pytest.mark.parametrize("text1, text2, expected", [
    ("This is a sample text for testing.", "This text is for testing purposes.", (0.0, 1.0)),
    ("Another example text.", "Different text for comparison.", (0.0, 1.0)),
    ("No common words.", "Different words here.", (0.0, 1.0)),
])
def test_task_func(text1, text2, expected):
    result = task_func(text1, text2)
    assert pytest.approx(result, expected, abs=1e-6)