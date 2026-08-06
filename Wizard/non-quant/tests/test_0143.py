python
import numpy as np
import matplotlib.pyplot as plt
import pytest

def task_func():
    x_values = np.linspace(0, 2 * np.pi, 400)
    fig, axs = plt.subplots(2)
    
    axs[0].plot(x_values, np.sin(x_values))
    axs[0].set_title('Sine function')
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('sin(x)')
    
    axs[1].plot(x_values, np.cos(x_values))
    axs[1].set_title('Cosine function')
    axs[1].set_xlabel('x')
    axs[1].set_ylabel('cos(x)')
    
    plt.tight_layout()
    
    return fig, axs

def test_task_func():
    fig, axs = task_func()
    assert isinstance(fig, plt.Figure)
    assert isinstance(axs, np.ndarray)
    assert len(axs) == 2
    assert isinstance(axs[0], plt.Axes)
    assert isinstance(axs[1], plt.Axes)
    assert axs[0].get_title() == 'Sine function'
    assert axs[1].get_title() == 'Cosine function'
    assert axs[0].get_xlabel() == 'x'
    assert axs[1].get_xlabel() == 'x'
    assert axs[0].get_ylabel() == 'sin(x)'
    assert axs[1].get_ylabel() == 'cos(x)'
    assert fig.get_size_inches() == (8.0, 6.0)