import pytest
from src_0644 import task_func
import pandas as pd
import re

# Sample data for testing
data = {
    'col1': ['>5.5<', '>6.6<', '>7.7<'],
    'col2': ['>8.8<', '>9.9<', '>10.10<']
}
df = pd.DataFrame(data)

def test_task_func():
    result = task_func(df)
    expected_result = pd.DataFrame({
        'col1': [5.5, 6.6, 7.7],
        'col2': [8.8, 9.9, 10.1]
    })
    pd.testing.assert_frame_equal(result, expected_result)