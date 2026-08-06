import pandas as pd
import pytest
from src_0633 import task_func

def test_task_func():
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']})
    filename = 'test_file.jsonl'
    result = task_func(df, filename)
    assert result == os.path.abspath(os.path.join(OUTPUT_DIR, filename))
    assert os.path.exists(os.path.join(OUTPUT_DIR, filename))