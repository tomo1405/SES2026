import pytest
from src_0793 import task_func

def test_task_func():
    df = pd.DataFrame({'feature': [1, 2, 3, 4, 5], 'target': [10, 20, 30, 40, 50]})
    feature = 'feature'
    target = 'target'
    n = 2

    largest_residual_indices, model = task_func(df, feature, target, n)

    assert len(largest_residual_indices) == n
    assert all(largest_residual_indices[i] in df.index for i in range(n))
    assert model.coef_[0] == pytest.approx(1)
    assert model.intercept_ == pytest.approx(0)