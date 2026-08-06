import pytest
from src_0114 import task_func

def test_task_func():
    # Test that the function raises an error if the keys parameter does not contain exactly 10 unique elements
    with pytest.raises(ValueError):
        task_func({}, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    # Test that the function updates the dictionary correctly
    my_dict = {}
    keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    task_func(my_dict, keys)
    assert my_dict == {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}

    # Test that the function creates a JSON file with the correct name and contents
    json_filename = "updated_dictionary.json"
    with open(json_filename, 'r') as json_file:
        assert json.load(json_file) == my_dict

    # Test that the function creates a text file with the correct name and contents
    txt_filename = "key_frequencies.txt"
    with open(txt_filename, 'r') as txt_file:
        assert txt_file.read() == "1: 1\n2: 2\n3: 3\n4: 4\n5: 5\n6: 6\n7: 7\n8: 8\n9: 9\n10: 10\n"