python
import pandas as pd
import pytest
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

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

# Test case 1: Valid input data
input_data = {"Salary_String": ["$100,000", "$150,000", "$200,000"], "Experience": [1, 2, 3]}
expected_output = plt.Axes
assert isinstance(task_func(input_data), expected_output)

# Test case 2: Invalid input data (missing keys)
input_data = {"Salary_String": ["$100,000", "$150,000", "$200,000"]}
with pytest.raises(ValueError):
    task_func(input_data)

# Test case 3: Invalid input data (empty DataFrame)
input_data = {"Salary_String": [], "Experience": []}
expected_output = plt.Axes
assert isinstance(task_func(input_data), expected_output)

# Test case 4: Invalid input data (invalid Salary_String)
input_data = {"Salary_String": ["$100,000", "$150,000", "$200,000"], "Experience": [1, 2, 3]}
input_data["Salary_String"][1] = "$150,000.50"
with pytest.raises(ValueError):
    task_func(input_data)