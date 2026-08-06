import pytest
from src_0063 import task_func
import random
import matplotlib.pyplot as plt
import seaborn as sns
from unittest.mock import patch, MagicMock

def test_task_func():
    # Mocking random.choice to control the color selection
    with patch('random.choice', return_value='b'):
        # Mocking plt.figure and sns.histplot to avoid actual plotting
        with patch('matplotlib.pyplot.figure') as mock_figure, \
             patch('seaborn.histplot') as mock_histplot, \
             patch('matplotlib.pyplot.show') as mock_show:
            # Sample input data
            result = [
                {'from_user': 10},
                {'from_user': 20},
                {'from_user': 30}
            ]
            
            # Call the function
            task_func(result)
            
            # Assertions
            mock_figure.assert_called_once()
            mock_histplot.assert_called_once_with([10, 20, 30], color='b')
            mock_show.assert_called_once()

def test_task_func_no_from_user():
    # Mocking random.choice to control the color selection
    with patch('random.choice', return_value='g'):
        # Mocking plt.figure and sns.histplot to avoid actual plotting
        with patch('matplotlib.pyplot.figure') as mock_figure, \
             patch('seaborn.histplot') as mock_histplot, \
             patch('matplotlib.pyplot.show') as mock_show:
            # Sample input data without 'from_user' key
            result = [
                {'other_key': 10},
                {'other_key': 20},
                {'other_key': 30}
            ]
            
            # Call the function
            task_func(result)
            
            # Assertions
            mock_figure.assert_called_once()
            mock_histplot.assert_not_called()
            mock_show.assert_called_once()

def test_task_func_empty_result():
    # Mocking random.choice to control the color selection
    with patch('random.choice', return_value='r'):
        # Mocking plt.figure and sns.histplot to avoid actual plotting
        with patch('matplotlib.pyplot.figure') as mock_figure, \
             patch('seaborn.histplot') as mock_histplot, \
             patch('matplotlib.pyplot.show') as mock_show:
            # Empty input data
            result = []
            
            # Call the function
            task_func(result)
            
            # Assertions
            mock_figure.assert_called_once()
            mock_histplot.assert_not_called()
            mock_show.assert_called_once()