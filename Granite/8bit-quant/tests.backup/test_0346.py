import pandas as pd
import seaborn as sns
import pytest

def task_func(df, col1, col2):
    if not isinstance(df, pd.DataFrame) or df.empty or col1 not in df.columns or col2 not in df.columns:
        raise ValueError("The DataFrame is empty or the specified column does not exist.")
    
    ax = sns.regplot(x=col1, y=col2, data=df)

    return ax

class TestTaskFunc:
    def test_input_type(self):
        with pytest.raises(ValueError) as excinfo:
            task_func("not_a_dataframe", "col1", "col2")
        assert "The DataFrame is empty or the specified column does not exist." in str(excinfo.value)

    def test_empty_dataframe(self):
        df = pd.DataFrame()
        with pytest.raises(ValueError) as excinfo:
            task_func(df, "col1", "col2")
        assert "The DataFrame is empty or the specified column does not exist." in str(excinfo.value)

    def test_invalid_column(self):
        df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
        with pytest.raises(ValueError) as excinfo:
            task_func(df, "col3", "col2")
        assert "The DataFrame is empty or the specified column does not exist." in str(excinfo.value)

    def test_valid_input(self):
        df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
        ax = task_func(df, "col1", "col2")
        assert ax is not None