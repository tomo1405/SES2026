python
import pandas as pd
import random
import pytest

def task_func(num_rows=100, categories=["a", "b", "c", "d", "e"], random_seed=42):
    if num_rows <= 0:
        raise ValueError("num_rows must not be negative")

    random.seed(random_seed)

    df = pd.DataFrame(
        {
            "Category": [
                categories[random.randint(0, len(categories) - 1)]
                for _ in range(num_rows)
            ],
            "Value": [random.randint(1, 100) for _ in range(num_rows)],
        }
    )

    ax = (
        df["Category"]
        .value_counts()
        .plot(kind="bar", title="Category Counts", figsize=(10, 6))
    )

    return df, ax

def test_task_func():
    # Test case 1: num_rows is negative
    with pytest.raises(ValueError):
        task_func(num_rows=-10)

    # Test case 2: num_rows is zero
    with pytest.raises(ValueError):
        task_func(num_rows=0)

    # Test case 3: num_rows is positive
    df, ax = task_func(num_rows=10)
    assert df.shape == (10, 2)
    assert ax.get_title() == "Category Counts"
    assert ax.get_xlabel() == "Category"
    assert ax.get_ylabel() == "Count"
    assert ax.get_ylim() == (0, 10)
    assert ax.get_xticks() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert ax.get_xticklabels() == ["a", "b", "c", "d", "e"]
    assert ax.get_yticks() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert ax.get_yticklabels() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert ax.get_figure().get_size_inches() == (10.0, 6.0)

    # Test case 4: categories is empty
    with pytest.raises(ValueError):
        task_func(categories=[])

    # Test case 5: categories has duplicates
    with pytest.raises(ValueError):
        task_func(categories=["a", "b", "c", "d", "e", "a"])

    # Test case 6: random_seed is negative
    with pytest.raises(ValueError):
        task_func(random_seed=-10)

    # Test case 7: random_seed is zero
    with pytest.raises(ValueError):
        task_func(random_seed=0)

    # Test case 8: random_seed is positive
    df, ax = task_func(random_seed=42)
    assert df.shape == (100, 2)
    assert ax.get_title() == "Category Counts"
    assert ax.get_xlabel() == "Category"
    assert ax.get_ylabel() == "Count"
    assert ax.get_ylim() == (0, 50)
    assert ax.get_xticks() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert ax.get_xticklabels() == ["a", "b", "c", "d", "e"]
    assert ax.get_yticks() == [0, 10, 20, 30, 40, 50]
    assert ax.get_yticklabels() == [0, 10, 20, 30, 40, 50]
    assert ax.get_figure().get_size_inches() == (10.0, 6.0)