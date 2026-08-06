import pytest
from src_0221 import task_func
from unittest.mock import patch, MagicMock

def test_task_func():
    with patch('src_0221.turtle.Screen') as MockScreen, \
         patch('src_0221.turtle.Turtle') as MockTurtle, \
         patch('src_0221.time.sleep') as MockSleep, \
         patch('src_0221.choice', return_value='red') as MockChoice:

        # Create mock objects
        mock_screen = MockScreen.return_value
        mock_turtle = MockTurtle.return_value

        # Call the function
        task_func(['red', 'blue', 'green'])

        # Assert that Screen and Turtle were called
        MockScreen.assert_called_once()
        MockTurtle.assert_called_once()

        # Assert that bgcolor was set to white
        mock_screen.bgcolor.assert_called_once_with('white')

        # Assert that speed was set to 1
        mock_turtle.speed.assert_called_once_with(1)

        # Assert that color was set 5 times
        assert mock_turtle.color.call_count == 5
        mock_turtle.color.assert_called_with('red')

        # Assert that forward and right were called correctly
        expected_calls = [((100,),), ((90,),), ((100,),), ((90,),), ((100,),), ((90,),), ((100,),), ((90,),)] * 5
        assert mock_turtle.forward.call_args_list == expected_calls[:8]
        assert mock_turtle.right.call_args_list == expected_calls[1::2]

        # Assert that sleep was called 5 times
        MockSleep.assert_called_with(1)
        assert MockSleep.call_count == 5

        # Assert that choice was called 5 times
        MockChoice.assert_called_with(['red', 'blue', 'green'])
        assert MockChoice.call_count == 5