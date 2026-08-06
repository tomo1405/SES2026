from src_0656 import task_func


def test_task_func():
    texts = ['This is a test text', 'Another test text', 'Yet another test text']
    num_topics = 2
    topics, _ = task_func(texts, num_topics)
    assert len(topics) == num_topics
    for topic in topics:
        assert len(topic) == num_topics

def test_task_func_no_texts():
    texts = []
    num_topics = 2
    topics, _ = task_func(texts, num_topics)
    assert topics == []

def test_task_func_all_stopwords():
    texts = ['This is a test text', 'Another test text', 'Yet another test text']
    num_topics = 2
    for text in texts:
        text = ' '.join(STOPWORDS)
    topics, _ = task_func(texts, num_topics)
    assert topics == []