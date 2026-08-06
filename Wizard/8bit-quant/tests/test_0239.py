python
import pytest
from src_0239 import task_func

def test_task_func():
    df = pd.DataFrame({'Name': ['John', 'John', 'Mary', 'Peter', 'Peter'],
                       'Age': [25, 30, 20, 35, 40],
                       'Score': [85, 90, 70, 80, 95]})

    df, ax = task_func(df)

    assert df.shape == (4, 3)
    assert ax.get_xlabel() == 'Age (standardized)'
    assert ax.get_ylabel() == 'Score (standardized)'
    assert ax.get_title() == 'Scatter Plot of Standardized Age and Score'