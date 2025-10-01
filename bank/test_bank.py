from bank import value


def test_value1():
    assert value("Hello") == 0

def test_value2():
    assert value(" Hello") == 0

def test_value3():
    assert value("Hello, Newman") == 0

def test_value4():
    assert value("How you doing?") == 20

def test_value5():
    assert value("What's happening?") == 100

def test_value6():
    assert value("What's up?") == 100
    
