python
import pytest
from src_0779 import task_func

def test_task_func():
    # Test case 1: Valid input
    news_articles = [
        {'category': 'Technology', 'id': 1, 'title': 'Python is awesome', 'title_url': 'https://www.python.org/'},
        {'category': 'Entertainment', 'id': 2, 'title': 'The Lion King', 'title_url': 'https://www.youtube.com/watch?v=4sj1MT05lAA'},
        {'category': 'Technology', 'id': 3, 'title': 'Java is the best', 'title_url': 'https://www.java.com/'},
        {'category': 'Entertainment', 'id': 4, 'title': 'Inception', 'title_url': 'https://www.youtube.com/watch?v=YoHD9XEInc0'}
    ]
    expected_output = {
        'Technology': [{'category': 'Technology', 'id': 1, 'title': 'Python is awesome', 'title_url': 'https://www.python.org/'},
                       {'category': 'Technology', 'id': 3, 'title': 'Java is the best', 'title_url': 'https://www.java.com/'}],
        'Entertainment': [{'category': 'Entertainment', 'id': 2, 'title': 'The Lion King', 'title_url': 'https://www.youtube.com/watch?v=4sj1MT05lAA'},
                          {'category': 'Entertainment', 'id': 4, 'title': 'Inception', 'title_url': 'https://www.youtube.com/watch?v=YoHD9XEInc0'}]
    }
    assert task_func(news_articles) == expected_output

    # Test case 2: Invalid input
    news_articles = [
        {'category': 'Technology', 'id': 1, 'title': 'Python is awesome', 'title_url': 'https://www.python.org/'},
        {'category': 'Entertainment', 'id': 2, 'title': 'The Lion King', 'title_url': 'https://www.youtube.com/watch?v=4sj1MT05lAA'},
        {'category': 'Technology', 'id': 3, 'title': 'Java is the best', 'title_url': 'https://www.java.com/'},
        {'category': 'Entertainment', 'id': 4, 'title': 'Inception', 'title_url': 'https://www.youtube.com/watch?v=YoHD9XEInc0'},
        {'category': 'Sports', 'id': 5, 'title': 'The Great American', 'title_url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'}
    ]
    with pytest.raises(ValueError):
        task_func(news_articles)