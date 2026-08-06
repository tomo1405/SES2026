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
    Score: 85, Category: Maths
    Score: 90, Category: Science
    Score: 75, Category: English
    """
    expected_df = pd.DataFrame({
        "Score": [85, 90, 75],
        "Category": ["Maths", "Science", "English"]
    })
    actual_df = task_func(text)
    assert actual_df.equals(expected_df)