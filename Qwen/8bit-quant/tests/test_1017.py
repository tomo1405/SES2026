import io

import pytest
import requests
from PIL import Image
from src_1017 import task_func


def test_task_func_invalid_url():
    with pytest.raises(ValueError, match="Invalid URL provided."):
        task_func(None)
    with pytest.raises(ValueError, match="Invalid URL provided."):
        task_func("")
    with pytest.raises(ValueError, match="Invalid URL provided."):
        task_func(123)

def test_task_func_image_not_found():
    invalid_url = "http://example.com/nonexistentimage.jpg"
    with pytest.raises(ValueError, match="Error downloading the image:"):
        task_func(invalid_url)

def test_task_func_invalid_image_format():
    invalid_image_data = b"GIF89a\x01\x00\x01\x00\x80\x00\x00\xff\xff\xff\x00\x00\x00!\xf9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;"
    response = io.BytesIO(invalid_image_data)
    response.name = "invalid.gif"
    with pytest.raises(IOError, match="Error processing the image:"):
        task_func(response)

def test_task_func_valid_image():
    # Create a simple test image
    image = Image.new('RGB', (100, 100), color = 'red')
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='JPEG')
    img_byte_arr.seek(0)
    
    # Use a mock to simulate the response
    class MockResponse:
        def __init__(self, content):
            self.content = content
        def raw(self):
            return self.content
        def close(self):
            pass
    
    response = MockResponse(img_byte_arr)
    
    # Use a context manager to replace requests.get with our mock
    with pytest.MonkeyPatch().context() as mp:
        mp.setattr(requests, 'get', lambda *args, **kwargs: response)
        
        ax = task_func("http://example.com/testimage.jpg")
        assert isinstance(ax, plt.Axes)
        assert len(ax.lines) == 1  # There should be one line in the histogram
        assert ax.title.get_text() == "Grayscale Histogram"