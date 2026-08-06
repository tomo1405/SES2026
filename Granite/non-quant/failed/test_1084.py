import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from unittest.mock import patch

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
    data = {
        "Salary_String": ["100,000", "200,000", "300,000"],
        "Experience": [1, 2, 3]
    }
    ax = task_func(data)
    assert ax.get_title() == "Normalized Salary vs Experience"
    assert ax.get_xlabel() == "Experience"
    assert ax.get_ylabel() == "Normalized Salary"

def test_task_func_empty_data():
    data = {
        "Salary_String": [],
        "Experience": []
    }
    with patch("matplotlib.pyplot.subplots") as mock_subplots:
        ax = task_func(data)
        assert ax.get_title() == "Normalized Salary vs Experience"
        assert ax.get_xlabel() == "Experience"
        assert ax.get_ylabel() == "Normalized Salary"
        mock_subplots.assert_called_once_with()

def test_task_func_ salary_string_conversion_error():
    data = {
        "Salary_String": ["100,000", "200,000", "abc"],
        "Experience": [1, 2, 3]
    }
    with patch("ValueError", side_effect=ValueError("Error converting Salary_String to float.")):
        with patch("matplotlib.pyplot.subplots") as mock_subplots:
            try:
                task_func(data)
            except ValueError:
                pass
            mock_subplots.assert_not_called()