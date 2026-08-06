import pytest
from src_0937 import task_func

def test_task_func():
    # Test that the function raises a ValueError when the input word contains non-alphabetic characters
    with pytest.raises(ValueError):
        task_func('hello1')
    
    # Test that the function returns the correct alphabetical positions for a valid input word
    assert task_func('hello') == [8, 5, 12, 12, 12, 12]
    
    # Test that the function plots the correct bar chart
    fig, ax = plt.subplots()
    task_func('hello')
    assert ax.get_xlabel() == 'Letter Index'
    assert ax.get_ylabel() == 'Alphabetical Position'
    assert ax.get_title() == 'Alphabetical Position of Letters in Word'
    assert ax.get_xticks() == np.arange(len('hello'))
    assert ax.get_yticks() == np.array([8, 5, 12, 12, 12, 12])