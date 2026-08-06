import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from unittest.mock import patch

from src_0470 import task_func

def test_task_func_with_empty_student_grades():
    with patch("src_0470.plt.show") as mock_show:
        with pytest.raises(ValueError) as exc_info:
            task_func([])
        assert "student_grades cannot be empty" in str(exc_info.value)
        mock_show.assert_not_called()

def test_task_func_with_valid_input():
    student_grades = ["A", "B", "C", "D", "F", "A", "B", "C", "D", "F"]
    expected_report_data = {"A": 2, "B": 2, "C": 2, "D": 2, "F": 2}
    expected_report_df = pd.DataFrame.from_dict(expected_report_data, orient="index", columns=["Count"])
    expected_report_df.index.name = "Grade"

    with patch("src_0470.plt.show") as mock_show:
        report_df, ax = task_func(student_grades)
        assert report_df.equals(expected_report_df)
        assert ax.get_ylabel() == "Number of Students"
        assert ax.get_xlabel() == "Grade"
        mock_show.assert_called_once()