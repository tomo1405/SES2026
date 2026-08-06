import pytest
from src_1017 import task_func
from unittest.mock import patch, MagicMock
import matplotlib.pyplot as plt

@patch('requests.get')
@patch('PIL.Image.open')
@patch('numpy.array')
@patch('matplotlib.pyplot.subplots')
def test_task_func(mock_subplots, mock_np_array, mock_image_open, mock_requests_get):
    # Mock the response object
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.raw = MagicMock()
    
    # Mock the image object
    mock_image = MagicMock()
    mock_image.convert.return_value = mock_image
    
    # Mock the numpy array
    mock_np_array.return_value = np.zeros((100, 100))
    
    # Mock the subplots
    mock_ax = MagicMock()
    mock_fig, mock_ax = MagicMock(), mock_ax
    mock_subplots.return_value = (mock_fig, mock_ax)
    
    # Set up the mocks
    mock_requests_get.return_value = mock_response
    mock_image_open.return_value = mock_image
    
    # Call the function
    ax = task_func("http://example.com/image.jpg")
    
    # Assertions
    mock_requests_get.assert_called_once_with("http://example.com/image.jpg", stream=True, timeout=10)
    mock_image_open.assert_called_once_with(mock_response.raw)
    mock_image.convert.assert_called_once_with("L")
    mock_np_array.assert_called_once_with(mock_image)
    mock_ax.hist.assert_called_once_with(np.zeros((100, 100)).ravel(), bins=256, color="gray", alpha=0.7)
    mock_ax.set_title.assert_called_once_with("Grayscale Histogram")
    
    assert ax == mock_ax

def test_task_func_invalid_url():
    with pytest.raises(ValueError, match="Invalid URL provided."):
        task_func(None)

def test_task_func_request_exception():
    with patch('requests.get') as mock_requests_get:
        mock_requests_get.side_effect = requests.RequestException("Request failed")
        with pytest.raises(ValueError, match="Error downloading the image: Request failed"):
            task_func("http://example.com/image.jpg")

def test_task_func_io_error():
    with patch('requests.get') as mock_requests_get, patch('PIL.Image.open') as mock_image_open:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.raw = MagicMock()
        mock_requests_get.return_value = mock_response
        mock_image_open.side_effect = IOError("Image processing failed")
        with pytest.raises(IOError, match="Error processing the image: Image processing failed"):
            task_func("http://example.com/image.jpg")