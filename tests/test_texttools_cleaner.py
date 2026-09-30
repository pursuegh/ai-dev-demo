"""texttools.cleaner 的单元测试。"""

from texttools.cleaner import clean_text


def test_clean_text_merges_spaces():
    # 只合并空白，不删标点
    assert clean_text("Hello,   World!") == "Hello, World!"


def test_clean_text_strips_edges():
    assert clean_text("   hello world   ") == "hello world"
    assert clean_text("   ") == ""


def test_clean_text_handles_tabs_newlines():
    assert clean_text("a\tb\n\nc") == "a b c"
    assert clean_text("\t\t\n\n") == ""


def test_clean_text_empty():
    assert clean_text("") == ""
