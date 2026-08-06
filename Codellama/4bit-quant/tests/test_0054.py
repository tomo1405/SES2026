import pandas as pd
from src_0054 import task_func


def test_task_func():
    text = "Name: John Doe, Email: johndoe@example.com, Age: 25, Country: USA\nName: Jane Doe, Email: janedoe@example.com, Age: 30, Country: Canada\nName: Bob Smith, Email: bobsmith@example.com, Age: 35, Country: Australia"
    expected_data = [
        ["John Doe", "johndoe@example.com", 25, "USA"],
        ["Jane Doe", "janedoe@example.com", 30, "Canada"],
        ["Bob Smith", "bobsmith@example.com", 35, "Australia"]
    ]
    expected_df = pd.DataFrame(expected_data, columns=COLUMN_NAMES)
    expected_df["Age"] = expected_df["Age"].astype(int)
    expected_sns_plot = sns.histplot(data=expected_df, x="Age")
    expected_plt_show = plt.show()

    actual_df = task_func(text)
    actual_sns_plot = sns.histplot(data=actual_df, x="Age")
    actual_plt_show = plt.show()

    assert actual_df.equals(expected_df)
    assert actual_sns_plot == expected_sns_plot
    assert actual_plt_show == expected_plt_show