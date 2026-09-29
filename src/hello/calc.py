"""示例模块：基础计算。"""


def add(a: int, b: int) -> int:
    """加法。"""
    return a + b


def sub(a: int, b: int) -> int:
    """减法。"""
    return a - b


def mul(a: int, b: int) -> int:
    """乘法。"""
    return a * b


def div(a: int, b: int) -> int:
    """除法，除零抛 ValueError。"""
    if b == 0:
        raise ValueError("除数不能为 0")
    return a / b
