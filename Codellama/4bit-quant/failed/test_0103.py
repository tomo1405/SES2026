import pytest
from src_0103 import task_func

def test_task_func():
    fig, diabetes_df = task_func()
    assert isinstance(fig, matplotlib.figure.Figure)
    assert isinstance(diabetes_df, pandas.DataFrame)
    assert diabetes_df.shape == (442, 10)
    assert diabetes_df.columns.tolist() == ['age', 'bp', 'sg', 'alb', 'sugar', 'hemo', 'bmi', 'ped', 'creatinine', 'bun']
    assert diabetes_df.dtypes.tolist() == ['int64', 'int64', 'int64', 'int64', 'int64', 'int64', 'int64', 'int64', 'int64', 'int64']
    assert diabetes_df.describe().to_dict() == {'age': {'count': 442, 'mean': 41.6, 'std': 12.1, 'min': 21, '25%': 31.0, '50%': 41.0, '75%': 51.0, 'max': 71}, 'bp': {'count': 442, 'mean': 72.0, 'std': 14.0, 'min': 50, '25%': 60.0, '50%': 70.0, '75%': 80.0, 'max': 110}, 'sg': {'count': 442, 'mean': 0.571, 'std': 0.108, 'min': 0.0, '25%': 0.300, '50%': 0.500, '75%': 0.700, 'max': 1.0}, 'alb': {'count': 442, 'mean': 0.389, 'std': 0.071, 'min': 0.0, '25%': 0.200, '50%': 0.300, '75%': 0.400, 'max': 0.6}, 'sugar': {'count': 442, 'mean': 85.0, 'std': 41.0, 'min': 0, '25%': 30.0, '50%': 60.0, '75%': 90.0, 'max': 180}, 'hemo': {'count': 442, 'mean': 38.0, 'std': 14.0, 'min': 14.0, '25%': 26.0, '50%': 38.0, '75%': 50.0, 'max': 62.0}, 'bmi': {'count': 442, 'mean': 33.1, 'std': 8.2, 'min': 16.0, '25%': 23.0, '50%': 32.0, '75%': 42.0, 'max': 50.0}, 'ped': {'count': 442, 'mean': 0.627, 'std': 0.108, 'min': 0.0, '25%': 0.300, '50%': 0.500, '75%': 0.700, 'max': 1.0}, 'creatinine': {'count': 442, 'mean': 0.651, 'std': 0.108, 'min': 0.0, '25%': 0.300, '50%': 0.500, '75%': 0.700, 'max': 1.0}, 'bun': {'count': 442, 'mean': 11.0, 'std': 4.0, 'min': 7.0, '25%': 9.0, '50%': 11.0, '75%': 13.0, 'max': 20.0}}
    assert diabetes_df.isnull().sum().sum() == 0