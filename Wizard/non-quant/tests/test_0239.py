python
import pytest
import matplotlib
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from src_0239 import task_func

def test_task_func():
    df = {'Name': ['John', 'John', 'Mary', 'Mary', 'Peter', 'Peter'],
          'Age': [25, 30, 20, 25, 35, 40],
          'Score': [85, 90, 70, 80, 95, 100]}
    df = pd.DataFrame(df)

    df, ax = task_func(df)

    assert df.shape == (5, 3)
    assert ax.get_xlabel() == 'Age (standardized)'
    assert ax.get_ylabel() == 'Score (standardized)'
    assert ax.get_title() == 'Scatter Plot of Standardized Age and Score'