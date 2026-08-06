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

    # Perform assertions to test the function's behavior
    assert isinstance(cumsum_df, pd.DataFrame)
    assert isinstance(fig, plt.Figure)
    assert list(cumsum_df.columns) == ['A', 'B', 'C']
    assert fig.axes[0].get_title() == "Cumulative Sum per Column"
    assert fig.axes[0].get_xlabel() == "Index"
    assert fig.axes[0].get_ylabel() == "Cumulative Sum"
    assert fig.axes[0].get_legend_handles_labels() == ([<matplotlib.lines.Line2D object at 0x7f875d419b00>], ['A', 'B', 'C'])

if __name__ == "__main__":
    pytest.main()