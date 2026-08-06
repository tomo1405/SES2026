python
import pandas as pd
import regex as re
import seaborn as sns
import matplotlib.pyplot as plt

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
    text = """
    Name: John Doe, Email: johndoe@example.com, Age: 30, Country: USA
    Name: Jane Doe, Email: janedoe@example.com, Age: 25, Country: Canada
    Name: Bob Smith, Email: bobsmith@example.com, Age: 40, Country: UK
    """
    df = task_func(text)
    assert df.shape == (3, 4)
    assert df.columns.tolist() == COLUMN_NAMES
    assert df["Age"].dtype == int
    assert df["Age"].min() == 25
    assert df["Age"].max() == 40
    assert df["Country"].nunique() == 3