import pytest
from src_1060 import task_func

def test_task_func():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ["Hydrogen", "Helium", "Oxygen", "Carbon", "Nitrogen", "Magnesium", "Silicon", "Iron", "Nickel"]
    assert df.shape == (9, 9)

def test_task_func_randomness():
    df1 = task_func()
    df2 = task_func()
    assert not df1.equals(df2)

def test_task_func_ planet_element_pairs():
    df = task_func()
    planet_element_pairs = [f"{planet}:{element}" for planet, element in itertools.product(PLANETS, ELEMENTS)]
    assert df.values.flatten().tolist() == planet_element_pairs