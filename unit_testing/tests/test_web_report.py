import pytest
import os
from patterns.web_report import create_content, create_file
from patterns.csv_utils import Ride, parse_file
from datetime import datetime

def test_create_content():
    
    content = create_content(parse_file("test_rides.csv"))
    assert "<h1>Taxi Report</h1>" in content
    assert "<td>17083</td>" in content
    assert "<td>2018-01-01T00:18:50</td>" in content
    assert "<td>2018-01-01T00:24:39</td>" in content
    assert "<td>5</td>" in content
    assert "<td>0.7</td>" in content
    assert "<td>7.3</td>" in content

def test_create_file():
    test_content = "<h1>Test Content</h1>"
    test_file_path = "financial-report.html"
    
    if os.path.exists(test_file_path):
        os.remove(test_file_path)
    
    create_file(test_content)
    
    assert os.path.exists(test_file_path)
    with open(test_file_path, "r") as file:
        assert file.read() == test_content
    
    os.remove(test_file_path)
