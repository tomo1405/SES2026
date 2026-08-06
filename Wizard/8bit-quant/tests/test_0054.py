python
import pandas as pd
import regex as re
import seaborn as sns
import matplotlib.pyplot as plt

COLUMN_NAMES = ["Name", "Email", "Age", "Country"]

def task_func(text):
    pattern = r"Name: (.*?), Email: (.*?), Age: (.*?), Country: (.*?)($|\n)"
    matches = re.findall(pattern, text)
    data = []
    for match in matches:
        data.append(match[:-1])
    df = pd.DataFrame(data, columns=COLUMN_NAMES)
    df["Age"] = df["Age"].astype(int)
    sns.histplot(data=df, x="Age")
    plt.show()
    return df

def test_task_func():
    text = """Name: John Doe, Email: johndoe@example.com, Age: 30, Country: USA\nName: Jane Doe, Email: janedoe@example.com, Age: 25, Country: Canada"""
    df = task_func(text)
    assert df.shape == (2, 4)
    assert df.iloc[0]["Name"] == "John Doe"
    assert df.iloc[0]["Email"] == "johndoe@example.com"
    assert df.iloc[0]["Age"] == 30
    assert df.iloc[0]["Country"] == "USA"
    assert df.iloc[1]["Name"] == "Jane Doe"
    assert df.iloc[1]["Email"] == "janedoe@example.com"
    assert df.iloc[1]["Age"] == 25
    assert df.iloc[1]["Country"] == "Canada"