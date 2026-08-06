import pytest
from src_0191 import task_func
from io import StringIO
import os

# Constants
DATABASE_NAME = 'test.db'
TABLE_NAME = 'test_table'

@pytest.fixture(scope='module', autouse=True)
def cleanup_db():
    yield
    if os.path.exists(DATABASE_NAME):
        os.remove(DATABASE_NAME)

def test_task_func_with_stringio():
    csv_data = """name,age,city
John Doe,30,New York
Jane Smith,25,Los Angeles"""
    csv_input = StringIO(csv_data)
    df = task_func(csv_input)
    
    assert not df.empty
    assert len(df) == 2
    assert set(df.columns) == {'name', 'age', 'city'}
    assert df.iloc[0]['name'] == 'John Doe'
    assert df.iloc[1]['age'] == 25

def test_task_func_with_file_path(tmpdir):
    csv_data = """name,age,city
Alice Johnson,35,Chicago
Bob Brown,40,Houston"""
    file_path = tmpdir.join("test.csv")
    with open(file_path, 'w') as f:
        f.write(csv_data)
    
    df = task_func(str(file_path))
    
    assert not df.empty
    assert len(df) == 2
    assert set(df.columns) == {'name', 'age', 'city'}
    assert df.iloc[0]['name'] == 'Alice Johnson'
    assert df.iloc[1]['age'] == 40

def test_task_func_empty_csv(tmpdir):
    csv_data = """name,age,city"""
    file_path = tmpdir.join("empty.csv")
    with open(file_path, 'w') as f:
        f.write(csv_data)
    
    df = task_func(str(file_path))
    
    assert df.empty
    assert len(df) == 0
    assert set(df.columns) == {'name', 'age', 'city'}

def test_task_func_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        task_func('nonexistent.csv')