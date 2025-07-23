from plates import is_valid


def test_min_two_chars_max_six():
    assert is_valid("S") is False
    assert is_valid("a") is False
    assert is_valid("yjahdiad") is False
    assert is_valid("ALDODUSa") is False


def test_no_numbers_in_middle():
    assert is_valid("jul88a") is False
    assert is_valid("t454hg") is False
    assert is_valid("tt54hg") is False
    assert is_valid("zz1hg") is False


def test_no_punctuation_space():
    assert is_valid("guy.12") is False
    assert is_valid("ter!11") is False
    assert is_valid("swet:1") is False
    assert is_valid("AL 87") is False


def test_no_numbers_at_start():
    assert is_valid("98guy") is False
    assert is_valid("2ride") is False
    assert is_valid("452re") is False

def test_no_number_start_zero():
    assert is_valid("GUY012") is False
    assert is_valid("CS0501") is False
    assert is_valid("GT09") is False

def test_letters_at_start():
    assert is_valid("") is False
    assert is_valid("1GJJH") is False

def test_no_numbers_before_letters():
    assert is_valid("AB1C") is False
    assert is_valid("ABC1D2") is False


