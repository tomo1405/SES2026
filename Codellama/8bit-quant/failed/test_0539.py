import pytest
from src_0539 import task_func

def test_task_func_valid_input():
    # Setup
    db_name = "test.db"
    table_name = "test_table"
    conn = sqlite3.connect(db_name)
    df = pd.DataFrame({"id": [1, 2, 3], "col1": [10, 20, 30], "col2": [100, 200, 300]})
    df.to_sql(table_name, conn, if_exists="replace", index=False)

    # Test
    ax = task_func(db_name, table_name)

    # Assert
    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.get_xlabel() == numerical_columns[0]
    assert ax.get_ylabel() == numerical_columns[1]
    assert len(ax.get_lines()) == 1

def test_task_func_invalid_input():
    # Setup
    db_name = "test.db"
    table_name = "test_table"
    conn = sqlite3.connect(db_name)
    df = pd.DataFrame({"id": [1, 2, 3], "col1": [10, 20, 30], "col2": [100, 200, 300]})
    df.to_sql(table_name, conn, if_exists="replace", index=False)

    # Test
    with pytest.raises(ValueError):
        task_func(db_name, "invalid_table")

    # Assert
    assert "The table must have at least two numerical columns to plot." in str(excinfo.value)