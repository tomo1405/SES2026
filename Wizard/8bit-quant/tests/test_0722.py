python
import os
import csv
from collections import Counter
import pytest

def task_func(file_path):
    if not os.path.isfile(file_path):
        return None

    word_counter = Counter()

    with open(file_path, 'r') as f:
        csv_reader = csv.reader(f, delimiter=',', skipinitialspace=True)
        for row in csv_reader:
            for word in row:
                word_counter[word.strip()] += 1

    if not word_counter:
        return None

    most_common_word, frequency = word_counter.most_common(1)[0]
    return most_common_word, frequency

def test_task_func():
    # Test case 1: file does not exist
    assert task_func('non_existent_file.csv') is None

    # Test case 2: file is empty
    with open('empty_file.csv', 'w') as f:
        f.write('')
    assert task_func('empty_file.csv') is None

    # Test case 3: file has one row with one word
    with open('one_word_file.csv', 'w') as f:
        f.write('word')
    assert task_func('one_word_file.csv') == ('word', 1)

    # Test case 4: file has one row with multiple words
    with open('multiple_words_file.csv', 'w') as f:
        f.write('word1, word2, word3')
    assert task_func('multiple_words_file.csv') == ('word1', 1)

    # Test case 5: file has multiple rows with multiple words
    with open('multiple_rows_file.csv', 'w') as f:
        f.write('word1, word2, word3\n')
        f.write('word1, word2, word3\n')
        f.write('word1, word2, word3\n')
    assert task_func('multiple_rows_file.csv') == ('word1', 3)

    # Test case 6: file has multiple rows with multiple words, some with the same frequency
    with open('multiple_rows_file_2.csv', 'w') as f:
        f.write('word1, word2, word3\n')
        f.write('word1, word2, word3\n')
        f.write('word1, word2, word3\n')
        f.write('word4, word5, word6\n')
        f.write('word4, word5, word6\n')
        f.write('word4, word5, word6\n')
    assert task_func('multiple_rows_file_2.csv') == ('word4', 3)

    # Test case 7: file has multiple rows with multiple words, some with the same frequency, some with the same word
    with open('multiple_rows_file_3.csv', 'w') as f:
        f.write('word1, word2, word3\n')
        f.write('word1, word2, word3\n')
        f.write('word1, word2, word3\n')
        f.write('word4, word5, word6\n')
        f.write('word4, word5, word6\n')
        f.write('word4, word5, word6\n')
        f.write('word1, word2, word3\n')
        f.write('word1, word2, word3\n')
        f.write('word1, word2, word3\n')
    assert task_func('multiple_rows_file_3.csv') == ('word1', 3)

    # Test case 8: file has multiple rows with multiple words, some with the same frequency, some with the same word, some with the same frequency and word
    with open('multiple_rows_file_4.csv', 'w') as f:
        f.write('word1, word2, word3\n')
        f.write('word1, word2, word3\n')
        f.write('word1, word2, word3\n')
        f.write('word4, word5, word6\n')
        f.write('word4, word5, word6\n')
        f.write('word4, word5, word6\n')
        f.write('word1, word2, word3\n')
        f.write('word1, word2, word3\n')
        f.write('word1, word2, word3\n')
        f.write('word4, word5, word6\n')
        f.write('word4, word5, word6\n')
        f.write('word4, word5, word6\n')
    assert task_func('multiple_rows_file_4.csv') == ('word1', 3)