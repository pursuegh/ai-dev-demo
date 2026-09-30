def count_words(text: str) -> int:
    """统计文本的字数。

    :param text: 输入文本
    :return: 字数
    """
    return len(text.split())

def count_lines(text: str) -> int:
    """统计文本的行数（空文本返回 0）。"""
    return len(text.splitlines())

def char_frequency(text: str) -> dict:
    """统计字符出现频率。

    :param text: 输入文本
    :return: 字符频率字典
    """
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency