import numpy as np
import pandas as pd
from src_0939 import task_func


def test_task_func():
    input_df = pd.DataFrame({'text': ['Hello, world!', '12345', np.nan]})
    expected_output = pd.DataFrame({
        'clean_text': ['Helloworld', '12345', ''],
        'text_length': [11, 5, 0]
    })
    actual_output = task_func(input_df)
    pd.testing.assert_frame_equal(actual_output, expected_output)