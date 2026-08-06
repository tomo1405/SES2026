import pytest
from src_0221 import task_func

def test_task_func():
    # Test that the function runs without error
    task_func(['red', 'blue', 'green'])

    # Test that the function changes the background color
    window = turtle.Screen()
    window.bgcolor('white')
    task_func(['red', 'blue', 'green'])
    assert window.bgcolor() == 'red'

    # Test that the function changes the turtle color
    t = turtle.Turtle()
    t.color('black')
    task_func(['red', 'blue', 'green'])
    assert t.color() == 'red'

    # Test that the function moves the turtle forward and right
    t.forward(100)
    t.right(90)
    task_func(['red', 'blue', 'green'])
    assert t.xcor() == 100
    assert t.ycor() == 0

    # Test that the function sleeps for 1 second
    start_time = time.time()
    task_func(['red', 'blue', 'green'])
    end_time = time.time()
    assert end_time - start_time >= 1