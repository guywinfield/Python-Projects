from twttr import shorten

def test_contains_vowels():
    assert shorten("heart") == "hrt"
    assert shorten("haribo") == "hrb"
    assert shorten("bored") == "brd"
    assert shorten("you") == "y"

def test_contains_no_vowels():
    assert shorten("rhythm") == "rhythm"
    assert shorten("gypsy") == "gypsy"
    assert shorten("lynx") == "lynx"

def test_contains_uppercase():
    assert shorten("Table").islower()
    assert shorten("BANDAGE").islower()


