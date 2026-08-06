python
import pytest
from src_0287 import task_func

def test_task_func():
    # Test case 1
    test_directory = './test_files/'
    output_file = './output.csv'
    expected_total_words = 10
    expected_word_counts = [('the', 3), ('quick', 1), ('brown', 1), ('fox', 1), ('jumps', 1), ('over', 1), ('lazy', 1), ('dog', 1), ('foxes', 1), ('are', 1)]
    try:
        task_func(output_file, test_directory)
        with open(output_file, 'r') as file:
            reader = csv.reader(file)
            rows = [row for row in reader]
            assert rows[0] == ['Word', 'Count']
            assert rows[1:] == expected_word_counts
        with open(output_file, 'r') as file:
            total_words = sum(int(row[1]) for row in csv.reader(file)[1:])
        assert total_words == expected_total_words
    except Exception as e:
        print(e)
        assert False

    # Test case 2
    test_directory = './test_files/'
    output_file = './output.csv'
    expected_total_words = 10
    expected_word_counts = [('the', 3), ('quick', 1), ('brown', 1), ('fox', 1), ('jumps', 1), ('over', 1), ('lazy', 1), ('dog', 1), ('foxes', 1), ('are', 1)]
    try:
        task_func(output_file, test_directory)
        with open(output_file, 'r') as file:
            reader = csv.reader(file)
            rows = [row for row in reader]
            assert rows[0] == ['Word', 'Count']
            assert rows[1:] == expected_word_counts
        with open(output_file, 'r') as file:
            total_words = sum(int(row[1]) for row in csv.reader(file)[1:])
        assert total_words == expected_total_words
    except Exception as e:
        print(e)
        assert False