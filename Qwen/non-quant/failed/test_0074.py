import pytest
from src_0074 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io

@pytest.fixture
def create_test_db(tmp_path):
    db_path = tmp_path / "test.db"
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE EmailData
                 (id INTEGER PRIMARY KEY, list TEXT)''')
    c.execute("INSERT INTO EmailData (list) VALUES ('[1, 2, 3]')")
    c.execute("INSERT INTO EmailData (list) VALUES ('[4, 5, 6]')")
    conn.commit()
    conn.close()
    return db_path

def test_task_func(create_test_db, monkeypatch):
    # Mock the plt.show() call to avoid opening a window
    def mock_show():
        pass
    monkeypatch.setattr(plt, 'show', mock_show)

    # Redirect stdout to capture print statements if any
    captured_output = io.StringIO()
    monkeypatch.setattr(sys, 'stdout', captured_output)

    # Call the function with the test database
    df, ax = task_func(str(create_test_db))

    # Check if the DataFrame is correctly created
    expected_df = pd.DataFrame({
        'id': [1, 2],
        'list': [[1, 2, 3], [4, 5, 6]],
        'sum': [6, 15],
        'mean': [2.0, 5.0],
        'var': [0.6666666666666666, 0.6666666666666666]
    })
    pd.testing.assert_frame_equal(df, expected_df)

    # Check if the plot is correctly created
    assert isinstance(ax, plt.Axes)

    # Check if there are no unexpected print statements
    assert captured_output.getvalue() == ''