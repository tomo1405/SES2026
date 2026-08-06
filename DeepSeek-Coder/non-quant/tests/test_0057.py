import pytest
from src_0057 import task_func

@pytest.fixture
def sample_data():
    return "Score: 85, Category: Math\nScore: 90, Category: Science\nScore: 78, Category: History"

def test_task_func(sample_data):
    result = task_func(sample_data)
    expected_df = pd.DataFrame({
        "Score": [85, 90, 78],
        "Category": ["Math", "Science", "History"]
    })
    pd.testing.assert_frame_equal(result, expected_df)