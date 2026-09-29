import pytest

from hello.order import calculate, validate


def test_calculate():
    assert calculate(100, 0.9, 0.1) == 99.0


def test_calculate_no_discount_no_tax():
    assert calculate(100) == 100.0


def test_calculate_no_tax():
    assert calculate(100, 0.9) == 90.0


def test_calculate_no_discount():
    assert calculate(100, tax_rate=0.1) == 110.0


def test_validate_valid_amount():
    assert validate(100.0) is True


def test_validate_negative_amount():
    assert validate(-100.0) is False


def test_validate_more_than_two_decimal_places():
    assert validate(100.111) is False
