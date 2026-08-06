python
import pytest
from src_1097 import task_func

def test_task_func():
    text = "This is a sample text with $100 and $200 dollars."
    filename = "test.csv"
    result = task_func(text, filename)
    assert os.path.isfile(result)
    with open(result, 'r') as f:
        reader = csv.reader(f)
        rows = [row for row in reader]
        assert rows[0] == ['Word']
        assert rows[1] == ['$100']
        assert rows[2] == ['$200']