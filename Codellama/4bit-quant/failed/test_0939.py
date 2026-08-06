import pytest
from src_0939 import task_func

def test_task_func():
    input_df = pd.DataFrame({'text': ['hello world', 'goodbye', np.nan]})
    expected_output = pd.DataFrame({'clean_text': ['hello world', 'goodbye', ''], 'text_length': [11, 7, 0]})
    output = task_func(input_df)
    assert output.equals(expected_output)