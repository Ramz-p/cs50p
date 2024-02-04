from twttr import shorten

def test_difference():
    # Test with mixed case and spaces
    assert shorten("hello world") == "hll wrld"

    # Test with all uppercase letters
    assert shorten("HELLO WORLD") == "HLL WRLD"

    # Test with alphanumeric characters
    assert shorten("h3ll0 w0rld") == "h3ll0 w0rld"

    # Test with special characters
    assert shorten("h@llo w*rld!!!") == "h@ll w*rld!!!"
