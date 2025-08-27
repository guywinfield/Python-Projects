import pytest

from working import convert

def test_excess_number():
    with pytest.raises(ValueError):
        convert("9:111 AM to 156:00 PM")

    with pytest.raises(ValueError):
        convert("109:11 AM to 6:00 PM")

    with pytest.raises(ValueError):
        convert("9:003 AM to 5:007 PM")

def test_midnight_midday():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"


def test_over_60():
    with pytest.raises(ValueError):
        convert("12:65 AM to 12 PM")

    with pytest.raises(ValueError):
        convert("12 PM to 12:87 AM")

def test_morning_afternoon():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"


def test_afternoon_morning():
    assert convert("5 PM to 9 AM") == "17:00 to 09:00"
    assert convert("5:00 PM to 9:00 AM") == "17:00 to 09:00"
    assert convert("8:50 PM to 10 AM") == "20:50 to 10:00"

def test_omit_to():
    with pytest.raises(ValueError):
        convert("9:00 AM  5:00 PM")
