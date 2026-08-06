python
import pytest
from src_0074 import task_func

def test_task_func():
    db_file = "test.db"
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute("CREATE TABLE EmailData (id INTEGER PRIMARY KEY, list TEXT)")
    c.execute("INSERT INTO EmailData (list) VALUES (?)", (str([1, 2, 3, 4, 5]),))
    c.execute("INSERT INTO EmailData (list) VALUES (?)", (str([6, 7, 8, 9, 10]),))
    conn.commit()
    conn.close()

    df, ax = task_func(db_file)

    assert df.shape == (2, 4)
    assert df['sum'][0] == 21
    assert df['mean'][0] == 6.5
    assert df['var'][0] == 8.25
    assert df['sum'][1] == 35
    assert df['mean'][1] == 8.5
    assert df['var'][1] == 9.25
    assert ax.get_xlabel() == 'Index'
    assert ax.get_ylabel() == 'Value'
    assert ax.get_title() == 'Bar Chart'