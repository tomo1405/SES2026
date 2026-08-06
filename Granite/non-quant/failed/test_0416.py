import pandas as pd
import codecs
from src_0416 import task_func
import pytest

@pytest.mark.parametrize("input_df, expected_output_df", [
    (pd.DataFrame({'UnicodeString': ['\u0041\u0042\u0043']}), pd.DataFrame({'UnicodeString': ['ABC']})),
    (pd.DataFrame({'UnicodeString': ['\u00E9\u00E8\u00E7']}), pd.DataFrame({'UnicodeString': ['éèç']})),
    (pd.DataFrame({'UnicodeString': ['\u00FF']}), pd.DataFrame({'UnicodeString': ['ÿ']}))
])
def test_task_func(input_df, expected_output_df):
    output_df = task_func(input_df)
    assert output_df.equals(expected_output_df)