import re

def clean_text(text: str) -> str:
    """去除文本中的多余空白字符、合并连续空格。

    :param text: 输入文本
    :return: 清洁后的文本
    """
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text