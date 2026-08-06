import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from collections import Counter
from src_0735 import task_func
import pytest

def test_task_func():
    content = "This is a sample sentence. Here is another sentence."
    expected_output = {'DT': 2, 'NN': 2, 'VBZ': 1, 'IN': 1, '.': 2}
    
    actual_output = task_func(content)
    
    assert actual_output == expected_output, "Output does not match expected output"

if __name__ == "__main__":
    pytest.main()