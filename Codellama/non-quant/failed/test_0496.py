import pytest
from src_0496 import task_func

def test_task_func():
    days = 10
    random_seed = 0
    expected_output = pd.DataFrame({
        "date": pd.date_range(start="2023-01-01", periods=days, freq="D"),
        "Groceries": np.random.randint(0, 100, size=(days)),
        "Entertainment": np.random.randint(0, 100, size=(days)),
        "Rent": np.random.randint(0, 100, size=(days)),
        "Utilities": np.random.randint(0, 100, size=(days)),
        "Miscellaneous": np.random.randint(0, 100, size=(days))
    })
    expected_output.set_index("date", inplace=True)

    output = task_func(days, random_seed)

    assert output.equals(expected_output)