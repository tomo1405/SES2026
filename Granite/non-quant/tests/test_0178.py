import pytest
from src_0178 import task_func

def test_task_func():
    import pandas as pd
    df = pd.DataFrame({
        "Title": ["This is an interesting article"],
        "Content": ["This article is about AI and it's fascinating!"]
    })
    expected_result = {"ai": 1, "fascinating": 1}
    result = task_func(df)
    assert result == expected_result

def test_task_func_with_empty_df():
    import pandas as pd
    df = pd.DataFrame({
        "Title": [],
        "Content": []
    })
    expected_result = {}
    result = task_func(df)
    assert result == expected_result

def test_task_func_with_missing_columns():
    import pandas as pd
    df = pd.DataFrame({
        "Title": ["This is an interesting article"],
        "Other Column": ["This article is about AI and it's fascinating!"]
    })
    with pytest.raises(ValueError) as excinfo:
        task_func(df)
    assert "DataFrame must include 'Title' and 'Content' columns." in str(excinfo.value)