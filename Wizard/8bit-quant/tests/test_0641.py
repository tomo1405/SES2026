python
import pytest
from src_0641 import task_func

def test_task_func():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (12, 5)
    assert df.index.tolist() == ['Month' + str(i) for i in range(1, 13)]
    assert df.columns.tolist() == ['Product' + str(i) for i in range(1, 6)]
    assert df.sum().sum() == 7800
    assert df.isnull().sum().sum() == 0
    assert df.dtypes.tolist() == [np.int64] * 5