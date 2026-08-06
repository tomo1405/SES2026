python
import pandas as pd
import regex as re
import pytest

def task_func(text):
    pattern = r"Score: (.*?), Category: (.*?)(\n|$)"
    matches = re.findall(pattern, text)
    data = [
        match[:2] for match in matches
    ]  # Extracting only the score and category from each match
    df = pd.DataFrame(data, columns=["Score", "Category"])
    df["Score"] = df["Score"].astype(int)
    return df

def test_task_func():
    text = """
    Score: 85, Category: Math
    Score: 90, Category: Science
    Score: 75, Category: English
    """
    expected_df = pd.DataFrame(
        data=[
            [85, "Math"],
            [90, "Science"],
            [75, "English"],
        ],
        columns=["Score", "Category"],
    )
    expected_df["Score"] = expected_df["Score"].astype(int)
    assert task_func(text).equals(expected_df)