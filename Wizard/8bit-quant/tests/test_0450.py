python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import pytest

def task_func(data: pd.DataFrame) -> (pd.DataFrame, list):
    FEATURES = ["Feature1", "Feature2", "Feature3", "Feature4", "Feature5"]

    scaler = StandardScaler()
    data_standardized = pd.DataFrame(
        scaler.fit_transform(data[FEATURES]), columns=FEATURES
    )

    axes_list = []
    for feature in FEATURES:
        fig, ax = plt.subplots()
        ax.hist(data_standardized[feature], bins=20, alpha=0.5)
        ax.set_title("Histogram of {}".format(feature))
        axes_list.append(ax)

    return data_standardized, axes_list

def test_task_func():
    # Test case 1: Test with valid input data
    data = pd.DataFrame(
        {
            "Feature1": [1, 2, 3, 4, 5],
            "Feature2": [2, 3, 4, 5, 6],
            "Feature3": [3, 4, 5, 6, 7],
            "Feature4": [4, 5, 6, 7, 8],
            "Feature5": [5, 6, 7, 8, 9],
        }
    )
    expected_data_standardized = pd.DataFrame(
        {
            "Feature1": [-1.3416407864998738, -0.4472136, 0.4472136, 1.3416407864998738, 2.23606797749979],
            "Feature2": [-1.0, -0.8944271909999159, -0.4472136, 0.4472136, 1.3416407864998738],
            "Feature3": [-0.8944271909999159, -0.4472136, 0.4472136, 1.3416407864998738, 2.23606797749979],
            "Feature4": [-0.4472136, 0.4472136, 1.3416407864998738, 2.23606797749979, 3.1622776601683795],
            "Feature5": [0.4472136, 1.3416407864998738, 2.23606797749979, 3.1622776601683795, 4.123105625617661],
        },
        columns=["Feature1", "Feature2", "Feature3", "Feature4", "Feature5"],
    )
    expected_axes_list = [
        plt.Axes(0.125, 0.3333333333333333, 0.8, 0.6666666666666666),
        plt.Axes(0.125, 0.1111111111111111, 0.8, 0.6666666666666666),
        plt.Axes(0.125, 0.6666666666666666, 0.8, 0.6666666666666666),
        plt.Axes(0.125, 0.8888888888888888, 0.8, 0.6666666666666666),
        plt.Axes(0.125, 0.4444444444444444, 0.8, 0.6666666666666666),
    ]
    for i, feature in enumerate(FEATURES):
        expected_axes_list[i].set_title("Histogram of {}".format(feature))
        expected_axes_list[i].hist(expected_data_standardized[feature], bins=20, alpha=0.5)

    result_data_standardized, result_axes_list = task_func(data)

    assert result_data_standardized.equals(expected_data_standardized)
    assert len(result_axes_list) == len(expected_axes_list)
    for i in range(len(result_axes_list)):
        assert result_axes_list[i].get_title() == expected_axes_list[i].get_title()
        assert result_axes_list[i].get_xlim() == expected_axes_list[i].get_xlim()
        assert result_axes_list[i].get_ylim() == expected_axes_list[i].get_ylim()
        assert result_axes_list[i].get_xticks() == expected_axes_list[i].get_xticks()
        assert result_axes_list[i].get_yticks() == expected_axes_list[i].get_yticks()
        assert result_axes_list[i].get_lines() == expected_axes_list[i].get_lines()

    # Test case 2: Test with invalid input data (not a DataFrame)
    with pytest.raises(TypeError):
        task_func("not a DataFrame")

    # Test case 3: Test with invalid input data (empty DataFrame)
    with pytest.raises(ValueError):
        task_func(pd.DataFrame())