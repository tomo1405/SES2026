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
    test_data = [
        ("Score: 10, Category: A", pd.DataFrame({"Score": [10], "Category": ["A"]})),
        ("Score: 20, Category: B\nScore: 30, Category: C", pd.DataFrame({"Score": [20, 30], "Category": ["B", "C"]})),
    ]
    for text, expected_output in test_data:
        actual_output = task_func(text)
        assert actual_output.equals(expected_output)

if __name__ == "__main__":
    pytest.main()