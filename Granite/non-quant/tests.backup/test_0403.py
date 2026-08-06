import pytest
from src_0403 import task_func

def test_task_func():
    pattern = r'example'
    result = task_func(pattern)
    assert result == os.path.abspath('matched_data.csv')
    assert os.path.exists('matched_data.csv')
    with open('matched_data.csv', 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
        assert rows == [re.findall(pattern, str(item)) for item in data['data']]