from datetime import datetime
from unittest.mock import MagicMock, patch

import pytest
from src_1048 import task_func


@pytest.mark.parametrize("date_str", ["2023-10-05", "2023-02-14", "2021-12-31"])
def test_task_func(date_str):
    # Patching plt.subplots to avoid actual plotting
    with patch('matplotlib.pyplot.subplots') as mock_subplots:
        mock_ax = MagicMock()
        mock_subplots.return_value = (None, mock_ax)

        ax = task_func(date_str)

        # Check if subplots was called correctly
        mock_subplots.assert_called_once()

        # Check if plot was called on the ax object
        mock_ax.plot.assert_called_once()

        # Check if the number of values generated is correct
        date = datetime.strptime(date_str, "%Y-%m-%d")
        num_of_values = date.day
        assert len(mock_ax.plot.call_args[0][0]) == num_of_values

        # Check if the returned object is the ax object
        assert ax == mock_ax