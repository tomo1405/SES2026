import pytest
from src_0581 import task_func

def test_task_func():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert 'Random Numbers' in df.columns
    assert 'Moving Average' in df.columns
    assert len(df) == SIZE
    assert df['Random Numbers'].min() >= 0
    assert df['Random Numbers'].max() <= RANGE
    assert df['Moving Average'].notnull().all()
    assert df['Moving Average'].rolling(window=5).mean().notnull().all()

if __name__ == '__main__':
    pytest.main()