python
import pytest
from src_0239 import task_func

def test_task_func():
    df = {'Name': ['John', 'Mary', 'John', 'Peter', 'Mary'],
          'Age': [25, 30, 25, 40, 30],
          'Score': [85, 90, 75, 80, 85]}
    df = pd.DataFrame(df)

    df_clean, ax = task_func(df)

    assert df_clean.shape == (4, 3)
    assert ax.get_xlabel() == 'Age (standardized)'
    assert ax.get_ylabel() == 'Score (standardized)'
    assert ax.get_title() == 'Scatter Plot of Standardized Age and Score'