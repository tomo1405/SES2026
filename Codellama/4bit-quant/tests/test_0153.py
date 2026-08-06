from src_0153 import task_func


def test_task_func():
    grades_df = task_func()
    assert grades_df.shape == (len(STUDENTS), len(COURSES) + 2)
    assert grades_df.columns.tolist() == ['Name'] + COURSES + ['Average Grade']
    assert grades_df['Name'].tolist() == STUDENTS
    assert grades_df['Average Grade'].tolist() == [np.mean(grades) for grades in grades_df[COURSES].values]