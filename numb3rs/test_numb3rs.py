from numb3rs import validate

def test_validate1():
    assert validate("255.255.255.255") == True

def test_validate2():
    assert validate("512.512.512.512") == False

def test_validate3():
    assert validate("1.2.3.1000") == False

def test_validate4():
    assert validate("192.168.001.1") == False

def test_validate5():
    assert validate("cat") == False
