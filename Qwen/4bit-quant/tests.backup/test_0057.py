import pytest
from src_0057 import task_func

def test_task_func_no_matches():
    text = "No scores or categories here."
    result = task_func(text)
    assert result.empty, "Expected an empty DataFrame when no matches are found."

def test_task_func_single_match():
    text = "Score: 100, Category: Math\n"
    expected_df = pd.DataFrame({"Score": [100], "Category": ["Math"]})
    result = task_func(text)
    pd.testing.assert_frame_equal(result, expected_df)

def test_task_func_multiple_matches():
    text = "Score: 90, Category: Science\nScore: 85, Category: History\n"
    expected_df = pd.DataFrame({"Score": [90, 85], "Category": ["Science", "History"]})
    result = task_func(text)
    pd.testing.assert_frame_equal(result, expected_df)

def test_task_func_trailing_newline():
    text = "Score: 70, Category: Art\n"
    expected_df = pd.DataFrame({"Score": [70], "Category": ["Art"]})
    result = task_func(text)
    pd.testing.assert_frame_equal(result, expected_df)

def test_task_func_no_category():
    text = "Score: 60, Category: \n"
    expected_df = pd.DataFrame({"Score": [60], "Category": [None]})
    result = task_func(text)
    pd.testing.assert_frame_equal(result, expected_df)

def test_task_func_non_numeric_score():
    text = "Score: abc, Category: Language\n"
    with pytest.raises(ValueError) as excinfo:
        task_func(text)
    assert "invalid literal for int() with base 10: 'abc'" in str(excinfo.value)

def test_task_func_empty_text():
    text = ""
    result = task_func(text)
    assert result.empty, "Expected an empty DataFrame when the input text is empty."