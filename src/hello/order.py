"""订单金额计算模块。"""

from decimal import Decimal, ROUND_HALF_UP


def calculate(amount: float, discount_rate: float = 1.0, tax_rate: float = 0.0) -> float:
    """计算最终应付金额：先应用折扣，再按税率先乘后四舍五入到分（保留两位小数）。

    使用 Decimal 避免浮点精度误差（如 0.1 + 0.2 != 0.3 类问题）。

    :param amount: 订单金额（必须 > 0 且最多两位小数）
    :param discount_rate: 折扣率，默认为 1.0（无折扣）
    :param tax_rate: 税率，默认为 0.0（无税）
    :return: 最终应付金额
    :raises ValueError: 金额非法时
    """
    if not validate(amount):
        raise ValueError("订单金额非法")

    final_amount = (
        Decimal(str(amount))
        * Decimal(str(discount_rate))
        * (1 + Decimal(str(tax_rate)))
    )
    return float(final_amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def validate(amount: float) -> bool:
    """校验订单金额合法：必须大于 0 且最多两位小数。

    用字符串判断小数位，避免浮点表示误差导致误判。

    :param amount: 订单金额
    :return: 是否合法
    """
    if amount <= 0:
        return False
    s = str(amount)
    if "." in s:
        return len(s.split(".")[1]) <= 2
    return True
