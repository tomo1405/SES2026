import pytest
from src_0221 import task_func

def test_task_func():
    colors = ['red', 'blue', 'green']
    task_func(colors)
    assert turtle.Screen().bgcolor() == 'white'
    assert turtle.Turtle().speed() == 1
    assert turtle.Turtle().color() in colors
    assert turtle.Turtle().forward(100) == 100
    assert turtle.Turtle().right(90) == 90
    assert time.sleep(1) == 1
    assert turtle.Screen().mainloop() == None