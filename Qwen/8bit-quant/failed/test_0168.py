import pytest
from src_0168 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from unittest.mock import patch

@pytest.fixture
def mock_randint(mocker):
    return mocker.patch('random.randint', side_effect=[10, 20, 30, 40, 50])

def test_task_func(mock_randint):
    num_types = 5
    integer_range = (0, 100)
    fig, ax = task_func(num_types, integer_range)

    # Check that the correct number of labels are created
    expected_labels = [f'Type{i + 1}' for i in range(num_types)]
    assert list(ax.get_xticklabels()) == expected_labels

    # Check that the data is correctly plotted
    expected_data = pd.DataFrame({
        'Type1': [10],
        'Type2': [20],
        'Type3': [30],
        'Type4': [40],
        'Type5': [50]
    })
    plotted_data = pd.DataFrame(ax.containers[0].datavalues).T
    plotted_data.columns = expected_labels
    pd.testing.assert_frame_equal(plotted_data, expected_data)

    # Check that the plot is horizontal and stacked
    assert ax.get_xlabel() == 'value'
    assert ax.get_ylabel() == 'Type'
    assert ax.get_legend().get_texts()[0].get_text() == 'Type1'

    # Check that the figure and axis are returned
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)

    # Check that randint is called with the correct arguments
    mock_randint.assert_has_calls([pytest.call(*integer_range) for _ in range(num_types)])