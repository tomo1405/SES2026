import pytest
from src_0097 import task_func
from collections import Counter

def test_task_func_with_simple_csv():
    # Create a temporary CSV file
    csv_content = "apple,banana\napple,orange\nbanana,apple"
    with open('temp.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for line in csv_content.split('\n'):
            writer.writerow(line.split(','))

    # Expected result
    expected_result = [('apple', 3), ('banana', 2), ('orange', 1)]

    # Run the function
    result = task_func('temp.csv', ',')

    # Assert the result
    assert result == expected_result

def test_task_func_with_different_delimiter():
    # Create a temporary CSV file with a different delimiter
    csv_content = "apple;banana\napple;orange\nbanana;apple"
    with open('temp.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        for line in csv_content.split('\n'):
            writer.writerow(line.split(';'))

    # Expected result
    expected_result = [('apple', 3), ('banana', 2), ('orange', 1)]

    # Run the function
    result = task_func('temp.csv', ';')

    # Assert the result
    assert result == expected_result

def test_task_func_with_single_word():
    # Create a temporary CSV file with a single word
    csv_content = "apple"
    with open('temp.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([csv_content])

    # Expected result
    expected_result = [('apple', 1)]

    # Run the function
    result = task_func('temp.csv', ',')

    # Assert the result
    assert result == expected_result

def test_task_func_with_empty_file():
    # Create an empty temporary CSV file
    with open('temp.csv', 'w', newline='') as f:
        pass

    # Expected result
    expected_result = []

    # Run the function
    result = task_func('temp.csv', ',')

    # Assert the result
    assert result == expected_result

def test_task_func_with_no_file():
    # Expected to raise FileNotFoundError
    with pytest.raises(FileNotFoundError):
        task_func('non_existent_file.csv', ',')

# Clean up temporary files after tests
import os
@pytest.fixture(autouse=True)
def cleanup():
    yield
    for filename in ['temp.csv']:
        if os.path.exists(filename):
            os.remove(filename)