import pytest
from src_1010 import task_func

def test_task_func_valid_xml():
    xml_content = "<root><child>value</child></root>"
    output_csv_path = "output.csv"
    task_func(xml_content, output_csv_path)
    with open(output_csv_path, "r") as f:
        reader = csv.reader(f)
        data = list(reader)
    assert data == [["root", ""], ["child", "value"]]

def test_task_func_invalid_xml():
    xml_content = "<root><child>value</child></root>"
    output_csv_path = "output.csv"
    with pytest.raises(ET.ParseError):
        task_func(xml_content, output_csv_path)

def test_task_func_invalid_csv_path():
    xml_content = "<root><child>value</child></root>"
    output_csv_path = "invalid_path.csv"
    with pytest.raises(IOError):
        task_func(xml_content, output_csv_path)