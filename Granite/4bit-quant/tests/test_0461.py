import subprocess
import pandas as pd
import pytest

from src_0461 import task_func

def test_task_func():
    script_path = "path/to/script"
    output_file_path = "path/to/output_file"

    with pytest.raises(ValueError) as exc_info:
        task_func(script_path, output_file_path)

    assert "Error occurred while executing the script or script not found" in str(exc_info.value)

    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    df.to_csv(output_file_path, index=False)

    df, ax = task_func(script_path, output_file_path)

    assert len(df.columns) == 2
    assert df.columns[0] == "A"
    assert df.columns[1] == "B"

    assert ax.get_xlabel() == "A"