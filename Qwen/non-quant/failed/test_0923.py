import pytest
from src_0923 import task_func

# Sample data for testing
data = [
    {"text": "This is a test sentence with some stopwords."},
    {"text": "Another example, without any stopwords."},
    {"text": "Punctuation should be removed, as well as stopwords."}
]

def test_task_func():
    # Expected output after removing stopwords
    expected_output = [
        {"text": "test sentence with some"},
        {"text": "Another example without any stopwords"},
        {"text": "Punctuation should be removed as well as stopwords"}
    ]
    
    # Convert expected output to DataFrame for comparison
    expected_df = pd.DataFrame(expected_output)
    
    # Call the function with sample data and the column name
    result_df = task_func(data, "text")
    
    # Check if the result matches the expected output
    assert result_df.equals(expected_df), "The function did not return the expected output."

def test_task_func_empty_data():
    # Test with empty data
    data = []
    expected_output = pd.DataFrame(columns=["text"])
    
    result_df = task_func(data, "text")
    
    assert result_df.equals(expected_output), "The function did not handle empty data correctly."

def test_task_func_no_stopwords():
    # Test with text that has no stopwords
    data = [{"text": "Unique words only"}]
    expected_output = pd.DataFrame({"text": ["Unique words only"]})
    
    result_df = task_func(data, "text")
    
    assert result_df.equals(expected_output), "The function did not handle text with no stopwords correctly."

def test_task_func_all_stopwords():
    # Test with text that contains only stopwords
    data = [{"text": "is a the of and"}]
    expected_output = pd.DataFrame({"text": [" "]})
    
    result_df = task_func(data, "text")
    
    assert result_df.equals(expected_output), "The function did not handle text with only stopwords correctly."