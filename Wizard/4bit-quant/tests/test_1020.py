python
import pytest
from src_1020 import task_func

def test_task_func():
    # Test case 1: Test OCR with valid image
    with open("tests/test_image.png", "rb") as f:
        image_bytes = f.read()
    with open("tests/test_image.txt", "r", encoding="utf8") as f:
        expected_text = f.read()
    assert task_func(image_bytes, "cp1251", "utf8") == expected_text

    # Test case 2: Test OCR with invalid image
    with open("tests/test_image_invalid.png", "rb") as f:
        image_bytes = f.read()
    with pytest.raises(ValueError):
        task_func(image_bytes, "cp1251", "utf8")

    # Test case 3: Test fallback to image comment
    with open("tests/test_image_comment.png", "rb") as f:
        image_bytes = f.read()
    with open("tests/test_image_comment.txt", "r", encoding="utf8") as f:
        expected_text = f.read()
    assert task_func(image_bytes, "cp1251", "utf8") == expected_text

    # Test case 4: Test fallback to invalid image comment
    with open("tests/test_image_comment_invalid.png", "rb") as f:
        image_bytes = f.read()
    with pytest.raises(ValueError):
        task_func(image_bytes, "cp1251", "utf8")

    # Test case 5: Test fallback to empty image comment
    with open("tests/test_image_comment_empty.png", "rb") as f:
        image_bytes = f.read()
    assert task_func(image_bytes, "cp1251", "utf8") == ""