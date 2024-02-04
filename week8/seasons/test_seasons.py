from seasons import convert

def test_date():
    # Test case: Convert 10477 days to minutes and express in words
    assert convert(10477) == "Fifteen million, eighty-six thousand, eight hundred eighty minutes"

    # Test case: Convert 365 days to minutes and express in words
    assert convert(365) == "Five hundred twenty-five thousand, six hundred minutes"
