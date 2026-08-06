import pandas as pd
from src_0054 import task_func


def test_task_func():
    text = """
    Name: John, Email: john@example.com, Age: 25, Country: US
    Name: Jane, Email: jane@example.com, Age: 30, Country: UK
    """
    expected_df = pd.DataFrame({
        "Name": ["John", "Jane"],
        "Email": ["john@example.com", "jane@example.com"],
        "Age": [25, 30],
        "Country": ["US", "UK"]
    })
    df = task_func(text)
    assert df.equals(expected_df)