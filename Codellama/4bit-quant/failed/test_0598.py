import pytest
from src_0598 import task_func

def test_task_func():
    data = [
        {'Name': 'Alice', 'Age': 21},
        {'Name': 'Bob', 'Age': 22},
        {'Name': 'Charlie', 'Age': 23},
        {'Name': 'David', 'Age': 24},
        {'Name': 'Eve', 'Age': 25},
        {'Name': 'Frank', 'Age': 26},
        {'Name': 'George', 'Age': 27},
        {'Name': 'Harry', 'Age': 28},
        {'Name': 'Ivy', 'Age': 29},
        {'Name': 'Jenny', 'Age': 30},
        {'Name': 'Kate', 'Age': 31},
        {'Name': 'Larry', 'Age': 32},
        {'Name': 'Mike', 'Age': 33},
        {'Name': 'Nick', 'Age': 34},
        {'Name': 'Olivia', 'Age': 35},
        {'Name': 'Pete', 'Age': 36},
        {'Name': 'Quincy', 'Age': 37},
        {'Name': 'Rose', 'Age': 38},
        {'Name': 'Sarah', 'Age': 39},
        {'Name': 'Ted', 'Age': 40},
        {'Name': 'Uma', 'Age': 41},
        {'Name': 'Victor', 'Age': 42},
        {'Name': 'Wendy', 'Age': 43},
        {'Name': 'Xavier', 'Age': 44},
        {'Name': 'Yvonne', 'Age': 45},
        {'Name': 'Zach', 'Age': 46},
    ]
    letter = 'a'
    expected_result = pd.DataFrame(
        [
            {'Name': 'Alice', 'Age': 21},
            {'Name': 'Bob', 'Age': 22},
            {'Name': 'Charlie', 'Age': 23},
            {'Name': 'David', 'Age': 24},
            {'Name': 'Eve', 'Age': 25},
            {'Name': 'Frank', 'Age': 26},
            {'Name': 'George', 'Age': 27},
            {'Name': 'Harry', 'Age': 28},
            {'Name': 'Ivy', 'Age': 29},
            {'Name': 'Jenny', 'Age': 30},
            {'Name': 'Kate', 'Age': 31},
            {'Name': 'Larry', 'Age': 32},
            {'Name': 'Mike', 'Age': 33},
            {'Name': 'Nick', 'Age': 34},
            {'Name': 'Olivia', 'Age': 35},
            {'Name': 'Pete', 'Age': 36},
            {'Name': 'Quincy', 'Age': 37},
            {'Name': 'Rose', 'Age': 38},
            {'Name': 'Sarah', 'Age': 39},
            {'Name': 'Ted', 'Age': 40},
            {'Name': 'Uma', 'Age': 41},
            {'Name': 'Victor', 'Age': 42},
            {'Name': 'Wendy', 'Age': 43},
            {'Name': 'Xavier', 'Age': 44},
            {'Name': 'Yvonne', 'Age': 45},
            {'Name': 'Zach', 'Age': 46},
        ]
    )
    result = task_func(data, letter)
    assert result.equals(expected_result)