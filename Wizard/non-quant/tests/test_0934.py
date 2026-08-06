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
    assert task_func("hello") == ([('h', 1), ('e', 2), ('l', 3), ('l', 4), ('o', 5)], ['he', 'll', 'o'])
    
    # Test case 2
    assert task_func("python") == ([('p', 1), ('y', 2), ('t', 3), ('h', 4), ('o', 5), ('n', 6)], ['py', 'th', 'on'])
    
    # Test case 3
    assert task_func("programming") == ([('p', 1), ('r', 2), ('o', 3), ('g', 4), ('r', 5), ('a', 6), ('m', 7), ('i', 8), ('n', 9), ('g', 10)], ['pro', 'gram', 'min', 'g'])
    
    # Test case 4
    assert task_func("hello world") == ([('h', 1), ('e', 2), ('l', 3), ('l', 4), ('o', 5), (' ', 6), ('w', 7), ('o', 8), ('r', 9), ('l', 10), ('d', 11)], ['he', 'll', 'o', ' ', 'wo', 'rl', 'd'])
    
    # Test case 5
    assert task_func("programming is fun") == ([('p', 1), ('r', 2), ('o', 3), ('g', 4), ('r', 5), ('a', 6), ('m', 7), ('i', 8), ('n', 9), ('g', 10), (' ', 11), ('i', 12), ('s', 13), (' ', 14), ('f', 15), ('u', 16), ('n', 17)], ['pro', 'gram', 'min', 'g', ' ', 'is', ' ', 'fu', 'n'])