import pytest
from src_0783 import task_func

def test_task_func():
    # Test with default parameters
    df = task_func(5)
    assert len(df) == 5
    assert all(df['title'].str.startswith("Article "))
    assert all(df['title_url'].str.endswith("/Article_"))
    assert all(df['id'] == df.index)
    assert all(df['category'].isin(['Sports', 'Technology', 'Health', 'Science', 'Business']))
    assert all(df['views'] >= 0)

    # Test with custom domain and categories
    df_custom = task_func(3, domain="example.com", categories=['Lifestyle', 'Entertainment'])
    assert all(df_custom['title_url'].str.startswith("http://example.com/Article_"))
    assert all(df_custom['category'].isin(['Lifestyle', 'Entertainment']))

    # Test with random seed for reproducibility
    df_seeded_1 = task_func(2, random_seed=42)
    df_seeded_2 = task_func(2, random_seed=42)
    pd.testing.assert_frame_equal(df_seeded_1, df_seeded_2)

    # Test with zero articles
    df_zero = task_func(0)
    assert df_zero.empty

    # Test with one article
    df_one = task_func(1)
    assert len(df_one) == 1