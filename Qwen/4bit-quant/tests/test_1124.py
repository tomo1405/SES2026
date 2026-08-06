import ssl

from src_1124 import task_func


def test_task_func_no_urls():
    input_string = "No URLs here"
    assert task_func(input_string) == {}

def test_task_func_single_url():
    input_string = "Check out this website: https://example.com"
    # Note: This test assumes that 'https://example.com' is reachable and returns a valid SSL certificate.
    # In a real-world scenario, you might want to mock the SSL connection or use a known URL with a valid certificate.
    result = task_func(input_string)
    assert 'example.com' in result

def test_task_func_multiple_urls():
    input_string = "Visit https://example.com or https://test.com"
    # Similar to the single URL test, this assumes both URLs are reachable and return valid SSL certificates.
    result = task_func(input_string)
    assert 'example.com' in result
    assert 'test.com' in result

def test_task_func_invalid_ssl():
    input_string = "This URL has invalid SSL: https://invalid-ssl-url.com"
    # Mocking the SSL error to ensure the function handles it gracefully
    def mock_getpeercert(*args, **kwargs):
        raise ssl.SSLError("Mocked SSL Error")

    # Monkey patching the getpeercert method to simulate an SSL error
    original_getpeercert = ssl.SSLContext.getpeercert
    ssl.SSLContext.getpeercert = mock_getpeercert

    result = task_func(input_string)
    assert result == {}

    # Reverting the monkey patch
    ssl.SSLContext.getpeercert = original_getpeercert

def test_task_func_no_https():
    input_string = "This string contains no HTTPS URLs: http://example.com or ftp://example.com"
    assert task_func(input_string) == {}