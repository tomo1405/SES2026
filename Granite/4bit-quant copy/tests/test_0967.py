import pandas as pd
import matplotlib.pyplot as plt
import pytest

def task_func(df: pd.DataFrame) -> pd.DataFrame:
    cumsum_df = df.cumsum()

    fig, ax = plt.subplots()
    cumsum_df.plot(kind="bar", ax=ax)
    ax.set_title("Cumulative Sum per Column")
    ax.set_xlabel("Index")
    ax.set_ylabel("Cumulative Sum")
    ax.legend()

    return cumsum_df, fig

def test_task_func():
    # Create a sample DataFrame for testing
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

    # Call the function and store the returned values
    cumsum_df, fig = task_func(df)

    # Assert the expected output
    assert isinstance(cumsum_df, pd.DataFrame)
    assert isinstance(fig, plt.Figure)

    # Assert the expected values in the DataFrame
    expected_cumsum_df = pd.DataFrame({'A': [1, 3, 6], 'B': [4, 9, 15]})
    assert cumsum_df.equals(expected_cumsum_df)

    # Assert the expected figure properties
    assert fig.axes[0].get_title() == "Cumulative Sum per Column"
    assert fig.axes[0].get_xlabel() == "Index"
    assert fig.axes[0].get_ylabel() == "Cumulative Sum"
    assert len(fig.axes[0].patches) == 2  # Assuming two columns in the DataFrame

if __name__ == "__main__":
    pytest.main()