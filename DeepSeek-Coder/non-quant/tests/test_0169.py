import pytest
from src_0169 import task_func

def test_task_func():
    # Call the function and capture the output
    fig, data, plot_filename = task_func()

    # Add assertions to verify the output
    assert isinstance(fig, plt.Figure)
    assert isinstance(data, pd.DataFrame)
    assert isinstance(plot_filename, str)
    assert plot_filename.endswith('.png')

    # Additional assertions to verify the plot
    assert os.path.exists(plot_filename), "The plot file does not exist"

    # Clean up by removing the plot file if the test passes
    if os.path.exists(plot_filename):
        os.remove(plot_filename)