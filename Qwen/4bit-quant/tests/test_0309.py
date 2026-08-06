from src_0309 import task_func


def test_task_func_no_additional_fields():
    df = task_func()
    assert all(field in df.columns for field in FIELDS)
    assert 'Average Grade' in df.columns
    assert 'Average' in df.index
    assert len(df) == len(STUDENTS) + 1  # 100 students + 1 average row

def test_task_func_with_additional_fields():
    additional_fields = ['Art', 'Music']
    df = task_func(additional_fields)
    assert all(field in df.columns for field in FIELDS + additional_fields)
    assert 'Average Grade' in df.columns
    assert 'Average' in df.index
    assert len(df) == len(STUDENTS) + 1  # 100 students + 1 average row

def test_task_func_average_grade_calculation():
    df = task_func()
    for student in STUDENTS:
        student_row = df.loc[student]
        calculated_average = mean(student_row[:-1])  # Exclude 'Average Grade'
        assert student_row['Average Grade'] == calculated_average

def test_task_func_subject_average_calculation():
    df = task_func()
    for field in FIELDS:
        calculated_average = mean(df[field])
        assert df.loc['Average', field] == calculated_average

def test_task_func_random_grades():
    df = task_func()
    for student in STUDENTS:
        for field in FIELDS:
            assert 0 <= df.loc[student, field] <= 100

def test_task_func_additional_fields_random_grades():
    additional_fields = ['Art', 'Music']
    df = task_func(additional_fields)
    for student in STUDENTS:
        for field in additional_fields:
            assert 0 <= df.loc[student, field] <= 100