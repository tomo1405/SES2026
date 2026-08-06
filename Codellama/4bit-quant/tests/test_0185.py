import pandas as pd
from src_0185 import task_func


def test_task_func():
    # Test case 1: Test with a dataframe and a text column
    dataframe = pd.DataFrame({'text': ['This is a sample text']})
    text_column = 'text'
    expected_output = pd.DataFrame({'text': ['This is a sample text']})
    actual_output = task_func(dataframe, text_column)
    assert actual_output.equals(expected_output)

    # Test case 2: Test with a dataframe and a text column that contains numbers
    dataframe = pd.DataFrame({'text': ['This is a sample text 123']})
    text_column = 'text'
    expected_output = pd.DataFrame({'text': ['This is a sample text']})
    actual_output = task_func(dataframe, text_column)
    assert actual_output.equals(expected_output)

    # Test case 3: Test with a dataframe and a text column that contains special characters
    dataframe = pd.DataFrame({'text': ['This is a sample text !@#$%^&*()_+']})
    text_column = 'text'
    expected_output = pd.DataFrame({'text': ['This is a sample text']})
    actual_output = task_func(dataframe, text_column)
    assert actual_output.equals(expected_output)

    # Test case 4: Test with a dataframe and a text column that contains multiple sentences
    dataframe = pd.DataFrame({'text': ['This is a sample text. This is another sentence.']})
    text_column = 'text'
    expected_output = pd.DataFrame({'text': ['This is a sample text. This is another sentence.']})
    actual_output = task_func(dataframe, text_column)
    assert actual_output.equals(expected_output)

    # Test case 5: Test with a dataframe and a text column that contains multiple sentences with numbers and special characters
    dataframe = pd.DataFrame({'text': ['This is a sample text 123. This is another sentence !@#$%^&*().']})
    text_column = 'text'
    expected_output = pd.DataFrame({'text': ['This is a sample text. This is another sentence.']})
    actual_output = task_func(dataframe, text_column)
    assert actual_output.equals(expected_output)

    # Test case 6: Test with a dataframe and a text column that contains multiple sentences with numbers and special characters, and some words are in the stopwords list
    dataframe = pd.DataFrame({'text': ['This is a sample text 123. This is another sentence !@#$%^&*().']})
    text_column = 'text'
    expected_output = pd.DataFrame({'text': ['This is a sample text. This is another sentence.']})
    actual_output = task_func(dataframe, text_column)
    assert actual_output.equals(expected_output)

    # Test case 7: Test with a dataframe and a text column that contains multiple sentences with numbers and special characters, and some words are in the stopwords list, and the text is in uppercase
    dataframe = pd.DataFrame({'text': ['THIS IS A SAMPLE TEXT 123. THIS IS ANOTHER SENTENCE !@#$%^&*().']})
    text_column = 'text'
    expected_output = pd.DataFrame({'text': ['THIS IS A SAMPLE TEXT. THIS IS ANOTHER SENTENCE.']})
    actual_output = task_func(dataframe, text_column)
    assert actual_output.equals(expected_output)

    # Test case 8: Test with a dataframe and a text column that contains multiple sentences with numbers and special characters, and some words are in the stopwords list, and the text is in uppercase, and the text contains punctuation
    dataframe = pd.DataFrame({'text': ['THIS IS A SAMPLE TEXT 123. THIS IS ANOTHER SENTENCE !@#$%^&*().']})
    text_column = 'text'
    expected_output = pd.DataFrame({'text': ['THIS IS A SAMPLE TEXT. THIS IS ANOTHER SENTENCE.']})
    actual_output = task_func(dataframe, text_column)
    assert actual_output.equals(expected_output)

    # Test case 9: Test with a dataframe and a text column that contains multiple sentences with numbers and special characters, and some words are in the stopwords list, and the text is in uppercase, and the text contains punctuation, and the text contains numbers
    dataframe = pd.DataFrame({'text': ['THIS IS A SAMPLE TEXT 123. THIS IS ANOTHER SENTENCE !@#$%^&*().']})
    text_column = 'text'
    expected_output = pd.DataFrame({'text': ['THIS IS A SAMPLE TEXT. THIS IS ANOTHER SENTENCE.']})
    actual_output = task_func(dataframe, text_column)
    assert actual_output.equals(expected_output)

    # Test case 10: Test with a dataframe and a text column that contains multiple sentences with numbers and special characters, and some words are in the stopwords list, and the text is in uppercase, and the text contains punctuation, and the text contains numbers, and the text contains special characters
    dataframe = pd.DataFrame({'text': ['THIS IS A SAMPLE TEXT 123. THIS IS ANOTHER SENTENCE !@#$%^&*().']})
    text_column = 'text'
    expected_output = pd.DataFrame({'text': ['THIS IS A SAMPLE TEXT. THIS IS ANOTHER SENTENCE.']})
    actual_output = task_func(dataframe, text_column)
    assert actual_output.equals(expected_output)