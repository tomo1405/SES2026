import numpy as np
import pandas as pd
from src_0939 import task_func


def test_task_func():
    input_df = pd.DataFrame({
        'text': ['Hello, world!', '12345', None]
    })
    expected_output = pd.DataFrame({
        'clean_text': ['HelloWorld', '12345', ''],
        'text_length': [11, 5, 0]
    })
    output_df = task_func(input_df)
    pd.testing.assert_frame_equal(output_df, expected_output)

def test_task_func_with_nan():
    input_df = pd.DataFrame({
        'text': [None, np.nan]
    })
    expected_output = pd.DataFrame({
        'clean_text': ['', ''],
        'text_length': [0, 0]
    })
    output_df = task_func(input_df)
    pd.testing.assert_frame_equal(output_df, expected_output)