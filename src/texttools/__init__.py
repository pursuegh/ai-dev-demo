"""文本分析工具包。"""

from .stats import count_words, count_lines, char_frequency
from .cleaner import clean_text

__all__ = ["count_words", "count_lines", "char_frequency", "clean_text"]
