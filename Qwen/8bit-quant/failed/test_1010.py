import pytest
from src_1010 import task_func
import xml.etree.ElementTree as ET
import os

def test_task_func_valid_xml(tmp_path):
    xml_content = """<root><child1>text1</child1><child2>text2</child2></root>"""
    output_csv_path = tmp_path / "output.csv"
    task_func(xml_content, output_csv_path)
    
    assert output_csv_path.exists()
    
    with open(output_csv_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    expected_rows = [['root', None], ['child1', 'text1'], ['child2', 'text2']]
    assert rows == expected_rows

def test_task_func_invalid_xml(tmp_path):
    xml_content = """<root><child1>text1</child1><child2>text2</child2"""
    output_csv_path = tmp_path / "output.csv"
    
    with pytest.raises(ET.ParseError) as excinfo:
        task_func(xml_content, output_csv_path)
    
    assert "Error parsing XML" in str(excinfo.value)

def test_task_func_io_error(tmp_path):
    xml_content = """<root><child1>text1</child1><child2>text2</child2></root>"""
    output_csv_path = "/invalid/path/output.csv"
    
    with pytest.raises(IOError) as excinfo:
        task_func(xml_content, output_csv_path)
    
    assert "Error writing CSV file" in str(excinfo.value)