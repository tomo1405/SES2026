import numpy as np
import pandas as pd
from src_0939 import task_func


def test_task_func():
    input_df = pd.DataFrame({'text': ['hello world', 'hello', 'world', np.nan]})
    expected_output = pd.DataFrame({'clean_text': ['helloworld', 'hello', 'world', ''],
                                   'text_length': [10, 5, 5, 0]})
    output = task_func(input_df)
    pd.testing.assert_frame_equal(output, expected_output)