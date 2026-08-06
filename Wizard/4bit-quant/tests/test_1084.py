python
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import pytest

def task_func(data):
    # Validate input data
    if not all(key in data for key in ["Salary_String", "Experience"]):
        raise ValueError(
            "Input data must contain 'Salary_String' and 'Experience' keys."
        )

    # Convert data to DataFrame
    df = pd.DataFrame(data)

    # Check if the data is empty
    if df.empty:
        # Handle empty data case (e.g., return a default Axes instance or raise an error)
        _, ax = plt.subplots()
        ax.set_title("Normalized Salary vs Experience")
        ax.set_xlabel("Experience")
        ax.set_ylabel("Normalized Salary")
        return ax

    # Convert Salary_String to float and handle potential conversion errors
    try:
        df["Salary_Float"] = df["Salary_String"].str.replace(",", "").astype(float)
    except ValueError:
        raise ValueError("Error converting Salary_String to float.")

    # Normalize the Salary_Float values
    scaler = MinMaxScaler()
    df["Normalized_Salary"] = scaler.fit_transform(df[["Salary_Float"]])

    # Plot the data
    _, ax = plt.subplots()
    ax.scatter(df["Experience"], df["Normalized_Salary"])
    ax.set_title("Normalized Salary vs Experience")
    ax.set_xlabel("Experience")
    ax.set_ylabel("Normalized Salary")

    return ax

def test_task_func():
    # Test case 1: Valid input data
    data = {
        "Salary_String": ["$100,000", "$150,000", "$200,000"],
        "Experience": [1, 2, 3],
    }
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Normalized Salary vs Experience"
    assert ax.get_xlabel() == "Experience"
    assert ax.get_ylabel() == "Normalized Salary"
    assert len(ax.collections) == 1
    assert len(ax.collections[0].get_offsets()) == 3
    assert ax.collections[0].get_offsets()[0] == (1, 0.0)
    assert ax.collections[0].get_offsets()[1] == (2, 0.5)
    assert ax.collections[0].get_offsets()[2] == (3, 1.0)

    # Test case 2: Invalid input data (missing keys)
    data = {"Salary_String": ["$100,000", "$150,000", "$200,000"]}
    with pytest.raises(ValueError):
        task_func(data)

    # Test case 3: Invalid input data (invalid Salary_String)
    data = {
        "Salary_String": ["$100,000", "$150,000", "$200,000"],
        "Experience": [1, 2, 3],
    }
    df = pd.DataFrame(data)
    df.loc[2, "Salary_String"] = "$100,000.5"
    with pytest.raises(ValueError):
        task_func(df)

    # Test case 4: Empty input data
    data = {}
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Normalized Salary vs Experience"
    assert ax.get_xlabel() == "Experience"
    assert ax.get_ylabel() == "Normalized Salary"
    assert len(ax.collections) == 0