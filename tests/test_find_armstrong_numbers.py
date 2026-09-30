"""findArmstrongNumbers 的单元测试。"""

import pytest

from hello.find_armstrong_numbers import findArmstrongNumbers


def test_find_armstrong_numbers_normal_path():
    # 100~200 区间内只有 153 是阿姆斯特朗数
    assert findArmstrongNumbers(100, 200) == [153]


def test_find_armstrong_numbers_boundary_path():
    assert findArmstrongNumbers(1, 9) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # 900~999 区间没有阿姆斯特朗数（999 不是：9^3*3 = 729）
    assert findArmstrongNumbers(900, 999) == []


def test_find_armstrong_numbers_empty_range():
    assert findArmstrongNumbers(100, 99) == []


def test_find_armstrong_numbers_negative_range():
    # 负数没有阿姆斯特朗数，函数正常返回空列表（不抛异常）
    assert findArmstrongNumbers(-100, -1) == []


def test_find_armstrong_numbers_non_integer_range():
    with pytest.raises(TypeError):
        findArmstrongNumbers(100.5, 200.5)


def test_find_armstrong_numbers_single_digit():
    assert findArmstrongNumbers(0, 9) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_find_armstrong_numbers_large_range():
    assert findArmstrongNumbers(1, 1000) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]
