python
import pytest
from src_1097 import task_func

def test_task_func():
    text = "This is a $100 test. $200 is the price."
    filename = "test.csv"
    result = task_func(text, filename)
    assert os.path.isfile(result)
    with open(result, 'r') as f:
        reader = csv.reader(f)
        rows = [row for row in reader]
        assert len(rows) == 2
        assert rows[0][0] == "Word"
        assert rows[1][0] == "$100"
        assert rows[1][1] == "$200"