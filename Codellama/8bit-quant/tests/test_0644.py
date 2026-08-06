import pytest
from src_0644 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    dataframe = pd.DataFrame({'A': ['>1.23<', '>4.56<', '>7.89<'],
                            'B': ['>10.11<', '>12.13<', '>14.15<']})
    expected_output = pd.DataFrame({'A': [1.23, 4.56, 7.89],
                                  'B': [10.11, 12.13, 14.15]})
    output = task_func(dataframe)
    pd.testing.assert_frame_equal(output, expected_output)