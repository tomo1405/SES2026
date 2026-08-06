import csv
import xml.etree.ElementTree as ET

import pytest
from src_1010 import task_func


def test_task_func_valid_xml(tmpdir):
    xml_content = "<root><child1>text1</child1><child2>text2</child2></root>"
    output_csv_path = str(tmpdir / "output.csv")
    
    task_func(xml_content, output_csv_path)
    
    with open(output_csv_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    expected_rows = [['root', None], ['child1', 'text1'], ['child2', 'text2']]
    assert rows == expected_rows

def test_task_func_invalid_xml(tmpdir):
    xml_content = "<root><child1>text1</child1><child2>text2"
    output_csv_path = str(tmpdir / "output.csv")
    
    with pytest.raises(ET.ParseError) as excinfo:
        task_func(xml_content, output_csv_path)
    
    assert "Error parsing XML" in str(excinfo.value)

def test_task_func_io_error(tmpdir):
    xml_content = "<root><child1>text1</child1><child2>text2</child2></root>"
    output_csv_path = "/nonexistent/path/output.csv"
    
    with pytest.raises(IOError) as excinfo:
        task_func(xml_content, output_csv_path)
    
    assert "Error writing CSV file" in str(excinfo.value)

def test_task_func_empty_xml(tmpdir):
    xml_content = ""
    output_csv_path = str(tmpdir / "output.csv")
    
    task_func(xml_content, output_csv_path)
    
    with open(output_csv_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    expected_rows = [['', None]]
    assert rows == expected_rows