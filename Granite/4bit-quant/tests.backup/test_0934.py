import string
import wordninja
from src_0934 import task_func

def test_task_func():
    word = "hello"
    expected_output = [("h", 8), ("e", 5), ("l", 12), ("l", 12), ("o", 15)]
    expected_wordninja_output = ["hello"]
    actual_output = task_func(word)
    assert actual_output[0] == expected_output
    assert actual_output[1] == expected_wordninja_output

def test_task_func_with_special_characters():
    word = "h҆!"
    expected_output = [("h", 8), ("a", 1), ("p", 16), ("p", 16), ("l", 12), ("e", 5), ("!", 27)]
    expected_wordninja_output = [" halp", "e!"]
    actual_output = task_func(word)
    assert actual_output[0] == expected_output
    assert actual_output[1] == expected_wordninja_output