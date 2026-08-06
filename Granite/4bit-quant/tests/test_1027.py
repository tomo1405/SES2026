import pytest
import numpy as np
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

def task_func(kwargs):
    alpha = 0.05  # Define the significance level

    group1 = np.array(kwargs.get("group1", []))
    group2 = np.array(kwargs.get("group2", []))

    # Check for empty or all-NaN groups
    if (
        len(group1) == 0
        or len(group2) == 0
        or np.all(np.isnan(group1))
        or np.all(np.isnan(group2))
    ):
        raise ValueError("One or both groups are empty or contain only NaN values.")

    # Removing NaN values and ensuring sufficient data
    valid_group1 = group1[~np.isnan(group1)]
    valid_group2 = group2[~np.isnan(group2)]

    # Check for sufficient size and variance
    if len(valid_group1) < 2 or len(valid_group2) < 2:
        raise ValueError("Each group must have at least two non-NaN values.")

    if np.var(valid_group1) < 1e-8 or np.var(valid_group2) < 1e-8:
        raise ValueError("Variance in one or both groups is too low.")

    # Perform t-test
    _, p_val = ttest_ind(valid_group1, valid_group2, nan_policy="omit")

    significant = p_val < alpha

    # Calculate descriptive statistics
    group1_stats = {"mean": np.mean(valid_group1), "std": np.std(valid_group1)}
    group2_stats = {"mean": np.mean(valid_group2), "std": np.std(valid_group2)}

    # Plotting
    _, (ax_boxplot, ax_histogram) = plt.subplots(2, 1, figsize=(8, 12))

    # Boxplot
    ax_boxplot.boxplot([valid_group1, valid_group2], labels=["group1", "group2"])

    # Histogram
    ax_histogram.hist(valid_group1, alpha=0.5, label="group1")
    ax_histogram.hist(valid_group2, alpha=0.5, label="group2")
    ax_histogram.legend()

    return {
        "significant": significant,
        "group1_stats": group1_stats,
        "group2_stats": group2_stats,
        "ax_boxplot": ax_boxplot,
        "ax_histogram": ax_histogram,
    }

def test_task_func():
    # Test case 1: Both groups are empty
    kwargs = {"group1": [], "group2": []}
    with pytest.raises(ValueError, match="One or both groups are empty or contain only NaN values."):
        task_func(kwargs)

    # Test case 2: Group 1 is empty
    kwargs = {"group1": [], "group2": [1, 2, 3]}
    with pytest.raises(ValueError, match="One or both groups are empty or contain only NaN values."):
        task_func(kwargs)

    # Test case 3: Group 2 is empty
    kwargs = {"group1": [1, 2, 3], "group2": []}
    with pytest.raises(ValueError, match="One or both groups are empty or contain only NaN values."):
        task_func(kwargs)

    # Test case 4: Both groups contain only NaN values
    kwargs = {"group1": [np.nan, np.nan], "group2": [np.nan, np.nan]}
    with pytest.raises(ValueError, match="One or both groups are empty or contain only NaN values."):
        task_func(kwargs)

    # Test case 5: Group 1 contains only NaN values
    kwargs = {"group1": [np.nan, np.nan], "group2": [1, 2, 3]}
    with pytest.raises(ValueError, match="One or both groups are empty or contain only NaN values."):
        task_func(kwargs)

    # Test case 6: Group 2 contains only NaN values
    kwargs = {"group1": [1, 2, 3], "group2": [np.nan, np.nan]}
    with pytest.raises(ValueError, match="One or both groups are empty or contain only NaN values."):
        task_func(kwargs)

    # Test case 7: Both groups have sufficient size and variance
    kwargs = {"group1": [1, 2, 3], "group2": [4, 5, 6]}
    result = task_func(kwargs)
    assert result["significant"] == True
    assert result["group1_stats"]["mean"] == 2
    assert result["group1_stats"]["std"] == pytest.approx(1.0)
    assert result["group2_stats"]["mean"] == 5
    assert result["group2_stats"]["std"] == pytest.approx(1.0)
    assert isinstance(result["ax_boxplot"], plt.Axes)
    assert isinstance(result["ax_histogram"], plt.Axes)