import pytest

from um import um_count

def test_um_counts():
    assert um_count("Um um um um um") == 5
    assert um_count("Um um hmmmm hum mumum um") == 3
    assert um_count("Ummmmmmm") == 0

def test_um_punctuation():
    assert um_count("umm! um! um!!! u?!? ") == 2
    assert um_count("......um.....umm! /um") == 2
    assert um_count("um.um.um!um!um") == 5

def test_um_sentences():
    assert um_count("Girl you got that yummy yum that yummy yum ummmmm um um") == 2
    assert um_count("ummm what would you um say to um going to um, ") == 3

