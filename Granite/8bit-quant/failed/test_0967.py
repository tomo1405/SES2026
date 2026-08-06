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
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
    })

    # Call the function and store the returned values
    cumsum_df, fig = task_func(df)

    # Assert that the returned values are of the expected type
    assert isinstance(cumsum_df, pd.DataFrame)
    assert isinstance(fig, plt.Figure)

    # Assert that the plot has the expected title, x-label, and y-label
    assert fig.axes[0].get_title() == "Cumulative Sum per Column"
    assert fig.axes[0].get_xlabel() == "Index"
    assert fig.axes[0].get_ylabel() == "Cumulative Sum"

    # Assert that the legend is displayed
    assert len(fig.axes[0].legend().get_lines()) == 3

if __name__ == "__main__":
    pytest.main()