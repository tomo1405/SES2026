python
import pytest
from src_1020 import task_func

def test_task_func():
    # Test case 1: Test OCR with valid image
    with open("tests/test_image.png", "rb") as f:
        image_bytes = f.read()
    extracted_text = "This is a test image for OCR."
    pytesseract.pytesseract.tesseract_cmd = "tests/tesseract.exe"
    with mock.patch("pytesseract.image_to_string", return_value=extracted_text):
        result = task_func(filename=image_bytes)
        assert result == extracted_text

    # Test case 2: Test OCR with invalid image
    with open("tests/test_image_invalid.png", "rb") as f:
        image_bytes = f.read()
    with pytest.raises(ValueError):
        task_func(filename=image_bytes)

    # Test case 3: Test fallback to image comment with valid image
    with open("tests/test_image.png", "rb") as f:
        image_bytes = f.read()
    comment = "This is a test image comment."
    with mock.patch.object(Image.Image, "info", {"comment": comment.encode("utf8")}):
        result = task_func(filename=image_bytes)
        assert result == comment

    # Test case 4: Test fallback to image comment with invalid image
    with open("tests/test_image_invalid.png", "rb") as f:
        image_bytes = f.read()
    with pytest.raises(ValueError):
        task_func(filename=image_bytes)

    # Test case 5: Test fallback to image comment with invalid encoding
    with open("tests/test_image.png", "rb") as f:
        image_bytes = f.read()
    with pytest.raises(ValueError):
        task_func(filename=image_bytes, from_encoding="invalid_encoding", to_encoding="utf8")