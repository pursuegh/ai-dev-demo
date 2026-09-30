"""texttools.stats 的单元测试。"""

from texttools.stats import char_frequency, count_lines, count_words


def test_count_words():
    assert count_words("hello world") == 2
    assert count_words("  a   b   c  ") == 3
    assert count_words("") == 0


def test_count_lines():
    assert count_lines("a\nb\nc") == 3
    assert count_lines("single line") == 1
    assert count_lines("") == 0


def test_char_frequency():
    freq = char_frequency("abca")
    assert freq == {"a": 2, "b": 1, "c": 1}


def test_char_frequency_empty():
    assert char_frequency("") == {}
