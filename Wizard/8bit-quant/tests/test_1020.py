python
import pytest
from src_1020 import task_func

def test_task_func():
    # Test case 1: OCR succeeds
    with open("tests/test_image.png", "rb") as f:
        image_bytes = f.read()
    with open("tests/test_image.txt", "r", encoding="utf8") as f:
        expected_text = f.read()
    assert task_func(image_bytes, "utf8", "utf8") == expected_text

    # Test case 2: OCR fails, fall back to comment
    with open("tests/test_image_no_ocr.png", "rb") as f:
        image_bytes = f.read()
    with open("tests/test_image_no_ocr.txt", "r", encoding="utf8") as f:
        expected_text = f.read()
    assert task_func(image_bytes, "utf8", "utf8") == expected_text

    # Test case 3: Incorrect encoding provided
    with open("tests/test_image.png", "rb") as f:
        image_bytes = f.read()
    with pytest.raises(ValueError):
        task_func(image_bytes, "invalid_encoding", "utf8")