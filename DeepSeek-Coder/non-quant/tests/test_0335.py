import pytest
from src_0335 import task_func

@pytest.fixture
def sample_data():
    documents = [
        "This is a sample document.",
        "Here is another document.",
        "And here is a third one."
    ]
    return documents

def test_task_func(sample_data):
    result = task_func(sample_data)
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert not result.empty, "The DataFrame should not be empty"
    assert set(result.columns) == set(word_tokenize(" ".join(sample_data))), "The columns should match the tokenized words"