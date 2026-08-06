import pytest
from src_0846 import task_func

@pytest.fixture
def example_input():
    return "example input text", "example input text"

def test_task_func(example_input):
    text1, text2 = example_input
    result = task_func(text1, text2)
    assert isinstance(result, tuple), "The result should be a tuple"
    assert len(result) == 2, "The result should contain two elements"
    cosine_similarity, levenshtein_ratio = result
    assert isinstance(cosine_similarity, (int, float)), "Cosine similarity should be a number"
    assert isinstance(levenshtein_ratio, (int, float)), "Levenshtein ratio should be a number"