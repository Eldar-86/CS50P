from plates import is_valid

def test_is_valid1():
    assert is_valid("CS50") == True

def test_is_valid2():
    assert is_valid("ECTO88") == True

def test_is_valid3():
    assert is_valid("NRVOUS") == True

def test_is_valid4():
    assert is_valid("CS05") == False

def test_is_valid5():
    assert is_valid("50") == False

def test_is_valid6():
    assert is_valid("CS50P2") == False

def test_is_valid7():
    assert is_valid("PI3.14") == False

def test_is_valid8():
    assert is_valid("H") == False

def test_is_valid9():
    assert is_valid("OUTATIME") == False
