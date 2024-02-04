from plates import is_valid


#max 6 characters
def test_length():
    assert is_valid("HICS50") == True
    assert is_valid("CS") == True
    assert is_valid("HELLOCS50") == False


#no special char like spaces or !
def test_punctuation():
    assert is_valid("CS50!") == False


#At least two letters
def test_twoletters():
    assert is_valid("CS") == True
    assert is_valid("50") == False
    assert is_valid("C0") == False
    assert is_valid("0") == False


#no num in middle
def test_number():
    assert is_valid("CSS550") == True
    assert is_valid("CSS50S") == False
    assert is_valid("CSS050") == False



