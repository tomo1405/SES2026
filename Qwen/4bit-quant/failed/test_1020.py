import pytest
from src_1020 import task_func

# Mocking dependencies
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_image_open(monkeypatch):
    mock_image = MagicMock(spec=Image.Image)
    mock_image.info = {"comment": "Sample comment"}
    mock_image_to_string = MagicMock(return_value="Extracted text")
    monkeypatch.setattr(pytesseract, 'image_to_string', mock_image_to_string)
    monkeypatch.setattr(Image, 'open', lambda x: mock_image)
    return mock_image

def test_task_func_with_ocr_success(mock_image_open):
    result = task_func()
    assert result == "Extracted text"

def test_task_func_with_comment_success(mock_image_open):
    mock_image_open.info["comment"] = b"Sample comment in cp1251".decode("cp1251")
    result = task_func()
    assert result == "Sample comment in cp1251"

def test_task_func_with_incorrect_encoding(mock_image_open):
    with pytest.raises(ValueError, match="Incorrect encoding provided."):
        task_func(from_encoding="invalid_encoding")

def test_task_func_with_no_text_or_comment(mock_image_open):
    mock_image_open.info["comment"] = None
    mock_image_to_string.return_value = ""
    result = task_func()
    assert result == ""

@patch('src_1020.Image.open')
def test_task_func_with_file_not_found(mock_image_open):
    mock_image_open.side_effect = FileNotFoundError
    with pytest.raises(FileNotFoundError):
        task_func(filename="non_existent_image.png")