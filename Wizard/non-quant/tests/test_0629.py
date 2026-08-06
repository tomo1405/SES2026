python
import math
import random
import matplotlib.pyplot as plt
import pytest

from src_0629 import task_func

def test_task_func():
    x = [i/100 for i in range(1000)]
    frequency = random.randint(1, 5)
    amplitude = random.randint(1, 5)
    phase_shift = random.randint(0, 360)

    y = [amplitude * math.sin(2 * math.pi * frequency * (xi + phase_shift)) for xi in x]

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title('Random Sine Wave')
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.grid(True)

    assert task_func() == ax