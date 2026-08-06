import numpy as np
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt
from src_1027 import task_func
import pytest

def test_task_func():
    # Test case 1: Both groups are empty
    with pytest.raises(ValueError) as excinfo:
        task_func({"group1": [], "group2": []})
    assert "One or both groups are empty or contain only NaN values." in str(excinfo.value)

    # Test case 2: Group 1 is empty
    with pytest.raises(ValueError) as excinfo:
        task_func({"group1": [], "group2": [1, 2, 3]})
    assert "One or both groups are empty or contain only NaN values." in str(excinfo.value)

    # Test case 3: Group 2 is empty
    with pytest.raises(ValueError) as excinfo:
        task_func({"group1": [1, 2, 3], "group2": []})
    assert "One or both groups are empty or contain only NaN values." in str(excinfo.value)

    # Test case 4: Both groups contain only NaN values
    with pytest.raises(ValueError) as excinfo:
        task_func({"group1": [np.nan, np.nan], "group2": [np.nan, np.nan]})
    assert "One or both groups are empty or contain only NaN values." in str(excinfo.value)

    # Test case 5: Group 1 contains only NaN values
    with pytest.raises(ValueError) as excinfo:
        task_func({"group1": [np.nan, np.nan], "group2": [1, 2, 3]})
    assert "One or both groups are empty or contain only NaN values." in str(excinfo.value)

    # Test case 6: Group 2 contains only NaN values
    with pytest.raises(ValueError) as excinfo:
        task_func({"group1": [1, 2, 3], "group2": [np.nan, np.nan]})
    assert "One or both groups are empty or contain only NaN values." in str(excinfo.value)

    # Test case 7: Both groups have sufficient size and variance
    group1 = np.random.normal(size=100)
    group2 = np.random.normal(size=100)
    result = task_func({"group1": group1, "group2": group2})
    assert result["significant"] == True
    assert result["group1_stats"]["mean"] == pytest.approx(np.mean(group1))
    assert result["group1_stats"]["std"] == pytest.approx(np.std(group1))
    assert result["group2_stats"]["mean"] == pytest.approx(np.mean(group2))
    assert result["group2_stats"]["std"] == pytest.approx(np.std(group2))
    assert isinstance(result["ax_boxplot"], plt.Axes)
    assert isinstance(result["ax_histogram"], plt.Axes)