import pytest
from src_1060 import task_func

def test_task_func():
    # Test that the function returns a DataFrame with the correct shape
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (len(PLANETS), len(ELEMENTS))

    # Test that the DataFrame contains the correct column headers
    assert list(df.columns) == ELEMENTS

    # Test that the DataFrame contains the correct data
    for planet, element in itertools.product(PLANETS, ELEMENTS):
        assert df.loc[planet, element] == f"{planet}:{element}"