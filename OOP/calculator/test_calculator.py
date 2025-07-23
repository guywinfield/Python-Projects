import pytest

from calculator import Calculator

cal = Calculator()


def test_addition():
    assert cal.add(2, 2) == 4
    assert cal.add(3467.67, 9872.92) == 13340.59
    assert cal.add(0, 100) == 100
    assert cal.add(100) == 200


def test_subtraction():
    assert cal.subtract(2, 7) == -5
    assert cal.subtract(538.98, -461.02) == 1000
    assert cal.subtract(99, -101) == 200
    assert cal.subtract(100) == 100


def test_multiply():
    assert cal.multiply(5, 5) == 25
    assert cal.multiply(20, 100) == 2000
    assert cal.multiply(-10) == -20000
    assert cal.multiply(10, -1) == -10


def test_divide():
    assert cal.divide(5, 5) == 1
    assert cal.divide(78.3, 13.5) == 5.8
    assert cal.divide(-10) == -0.58
    assert cal.divide(4) == -0.145


def test_square_root():
    assert cal.square_root(36) == 6
    assert cal.square_root(72) == 8.48528137423857
    assert cal.square_root(900) == 30
    assert cal.square_root() == 5.477225575051661


def test_reset_memory():
    assert cal.square_root(36) == 6
    assert cal.reset_memory() == 0
    assert cal.add(2, 2) == 4
    assert cal.reset_memory() == 0
