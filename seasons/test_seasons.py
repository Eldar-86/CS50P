from seasons import convert

#Test is created for date 2025-10-22 -- make sure to 

def test_convert1():
    assert convert("1986-01-06") == "Twenty million, nine hundred and twenty-eight thousand, nine hundred and sixty"

def test_convert2():
    assert convert("1982-12-08") == "Twenty-two million, five hundred and forty-eight thousand, nine hundred and sixty"

def test_convert3():
    assert convert("1962-03-13") == "Thirty-three million, four hundred and fifty-six thousand, nine hundred and sixty"

def test_convert4():
    assert convert("1956-04-16") == "Thirty-six million, five hundred and sixty-three thousand and forty"

def test_convert5():
    assert convert("1999-01-01") == "Five hundred twenty-five thousand, six hundred minutes"
