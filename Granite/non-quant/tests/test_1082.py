import pandas as pd
import seaborn as sns
import pytest

def task_func(data=None):
    if data is None:
        data = {
            "Weight_String": ["60.5", "65.7", "70.2", "75.9", "80.1"],
            "Height": [160, 165, 170, 175, 180],
        }

    df = pd.DataFrame(data)

    # Validate weight values are strings
    if not all(isinstance(weight, str) for weight in df["Weight_String"]):
        raise ValueError("Weights must be provided as strings.")

    # Convert string weights to floats
    df["Weight_Float"] = df["Weight_String"].astype(float)

    # Plotting the scatter plot
    ax = sns.scatterplot(data=df, x="Weight_Float", y="Height")
    ax.set_title("Weight vs Height")
    return ax

def test_task_func():
    # Test case 1: Validate weight values are strings
    with pytest.raises(ValueError) as excinfo:
        task_func(data={"Weight_String": [60.5, 65.7, 70.2, 75.9, 80.1], "Height": [160, 165, 170, 175, 180]})
    assert "Weights must be provided as strings." in str(excinfo.value)

    # Test case 2: Validate weight values are strings
    with pytest.raises(ValueError) as excinfo:
        task_func(data={"Weight_String": ["60.5", "65.7", "70.2", "75.9", "80.1"], "Height": [160, 165, 170, 175, 180, "invalid"]})
    assert "Weights must be provided as strings." in str(excinfo.value)

    # Test case 3: Validate weight values are strings
    ax = task_func(data={"Weight_String": ["60.5", "65.7", "70.2", "75.9", "80.1"], "Height": [160, 165, 170, 175, 180]})
    assert ax.get_title() == "Weight vs Height"