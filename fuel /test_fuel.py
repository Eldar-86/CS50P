import pytest
from fuel import convert
from fuel import gauge


def test_convert():
    assert convert("2/3") == 67

def test_non_digits():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("-1/4")

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("0/0")

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(45) == "45%"
