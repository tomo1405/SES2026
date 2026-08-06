python
import pytest
from src_0335 import task_func

def test_task_func():
    documents = ['This is a sample document.', 'This is another sample document.']
    expected_tfidf_df = pd.DataFrame(
        [[0.5760469, 0.5760469, 0.5760469, 0.5760469, 0.5760469],
         [0.5760469, 0.5760469, 0.5760469, 0.5760469, 0.5760469]],
        columns=['document', 'is', 'a', 'sample', 'document.1']
    )
    tfidf_df = task_func(documents)
    assert tfidf_df.equals(expected_tfidf_df)