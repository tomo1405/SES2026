from src_1060 import task_func


def test_task_func_output_shape():
    df = task_func()
    assert df.shape == (len(PLANETS), len(ELEMENTS)), "DataFrame shape is incorrect"

def test_task_func_column_headers():
    df = task_func()
    assert all(df.columns == ELEMENTS), "Column headers do not match the expected elements"

def test_task_func_row_labels():
    df = task_func()
    assert all(df.index == range(len(PLANETS))), "Row labels should be a range starting from 0"

def test_task_func_randomness():
    df1 = task_func()
    df2 = task_func()
    assert not df1.equals(df2), "The two DataFrames should not be identical due to shuffling"

def test_task_func_pair_format():
    df = task_func()
    for planet in PLANETS:
        for element in ELEMENTS:
            assert f"{planet}:{element}" in df.values, f"Missing pair: {planet}:{element}"

def test_task_func_unique_pairs():
    df = task_func()
    unique_pairs = set(df.values.flatten())
    assert len(unique_pairs) == len(PLANETS) * len(ELEMENTS), "Not all pairs are unique"