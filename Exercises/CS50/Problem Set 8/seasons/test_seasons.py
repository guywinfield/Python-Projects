from datetime import date
import pytest

from seasons import Time

def test_date():
    a = Time("1993-07-09")
    assert a.birth == date(1993, 7, 9)

    with pytest.raises(ValueError):
        Time("07/09/1993")

def test_words():
    a = Time("1993-07-09")
    # monkey-patch minutes() to return known values
    a.minutes = lambda: 16833600
    assert a.get_minutes_in_words() == "Sixteen million, eight hundred thirty-three thousand, six hundred"
