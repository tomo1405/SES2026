import matplotlib.pyplot as plt
import pandas as pd
from src_0103 import task_func


def test_task_func():
    fig, diabetes_df = task_func()
    assert isinstance(fig, plt.Figure)
    assert isinstance(diabetes_df, pd.DataFrame)
    assert diabetes_df.shape == (442, 10)
    assert diabetes_df.columns.tolist() == ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']
    assert diabetes_df.dtypes.tolist() == ['int64', 'int64', 'float64', 'float64', 'float64', 'float64', 'float64', 'float64', 'float64', 'float64']
    assert diabetes_df.isnull().sum().sum() == 0