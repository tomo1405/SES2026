python
import pytest
from src_0074 import task_func

def test_task_func():
    db_file = "test.db"
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('''CREATE TABLE EmailData
                 (id INTEGER PRIMARY KEY,
                 email TEXT,
                 list TEXT)''')
    c.execute("INSERT INTO EmailData (email, list) VALUES (?, ?)",
              ('email1', '[1, 2, 3]'))
    c.execute("INSERT INTO EmailData (email, list) VALUES (?, ?)",
              ('email2', '[4, 5, 6]'))
    conn.commit()
    conn.close()

    df, ax = task_func(db_file)

    assert df.shape == (2, 4)
    assert df['sum'][0] == 6
    assert df['mean'][0] == 3
    assert df['var'][0] == 2.6666666666666665
    assert ax is not None

    import os
    os.remove(db_file)