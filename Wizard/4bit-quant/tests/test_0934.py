python
import string
import wordninja
import pytest

def task_func(word):
    ALPHABET = list(string.ascii_lowercase)
    # Map each letter in the word to its corresponding alphabetical number
    word_numbers = [ALPHABET.index(letter) + 1 for letter in word]
    
    # Combine each letter with its alphabetical number in a tuple
    return [(word[i], word_numbers[i]) for i in range(len(word))],  wordninja.split(word)

def test_task_func():
    # Test case 1
    word = "hello"
    expected_result = [("h", 1), ("e", 2), ("l", 3), ("l", 4), ("o", 5)], ['he', 'll', 'o']
    assert task_func(word) == expected_result
    
    # Test case 2
    word = "python"
    expected_result = [("p", 1), ("y", 2), ("t", 3), ("h", 4), ("o", 5), ("n", 6)], ['py', 'th', 'on']
    assert task_func(word) == expected_result
    
    # Test case 3
    word = "programming"
    expected_result = [("p", 1), ("r", 2), ("o", 3), ("g", 4), ("r", 5), ("a", 6), ("m", 7), ("i", 8), ("n", 9)], ['prog', 'ram', 'ming']
    assert task_func(word) == expected_result
    
    # Test case 4
    word = "testing"
    expected_result = [("t", 1), ("e", 2), ("s", 3), ("t", 4), ("i", 5), ("n", 6), ("g", 7)], ['test', 'ing']
    assert task_func(word) == expected_result
    
    # Test case 5
    word = "pythonprogramming"
    expected_result = [("p", 1), ("y", 2), ("t", 3), ("h", 4), ("o", 5), ("n", 6), ("p", 7), ("r", 8), ("o", 9), ("g", 10), ("r", 11), ("a", 12), ("m", 13), ("i", 14), ("n", 15)], ['py', 'th', 'on', 'prog', 'ram', 'ming']
    assert task_func(word) == expected_result