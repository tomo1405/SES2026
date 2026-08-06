import pytest
from src_0636 import task_func

def test_task_func():
    # Test case 1: Check if the function returns an empty DataFrame and an axes object when the input text is empty after removing stopwords
    matrix_df, ax = task_func("")
    assert matrix_df.empty
    assert isinstance(ax, plt.Axes)

    # Test case 2: Check if the function returns a non-empty DataFrame and an axes object when the input text is not empty after removing stopwords
    matrix_df, ax = task_func("This is a sample text with some words.")
    assert not matrix_df.empty
    assert isinstance(ax, plt.Axes)

    # Test case 3: Check if the function returns a DataFrame with the correct number of rows and columns when the input text has multiple words
    matrix_df, ax = task_func("This is a sample text with multiple words.")
    assert matrix_df.shape == (len(matrix_df.index), len(matrix_df.columns))

    # Test case 4: Check if the function returns a DataFrame with the correct number of n-grams when the input text has multiple words and the value of n is greater than 1
    matrix_df, ax = task_func("This is a sample text with multiple words.", n=3)
    assert matrix_df.shape == (len(matrix_df.index), len(matrix_df.columns))

if __name__ == "__main__":
    pytest.main()