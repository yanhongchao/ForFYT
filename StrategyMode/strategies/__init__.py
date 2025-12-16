"""
策略模式 - 策略模块
提供各种策略接口和实现
"""

from .base_strategy import BaseStrategy
from .discount_strategies import (
    DiscountStrategy,
    NoDiscountStrategy,
    PercentageDiscountStrategy,
    FixedAmountDiscountStrategy,
    SeasonalDiscountStrategy
)
from .payment_strategies import (
    PaymentStrategy,
    AlipayStrategy,
    WeChatPayStrategy,
    CreditCardStrategy
)

__all__ = [
    'BaseStrategy',
    'DiscountStrategy',
    'NoDiscountStrategy',
    'PercentageDiscountStrategy',
    'FixedAmountDiscountStrategy',
    'SeasonalDiscountStrategy',
    'PaymentStrategy',
    'AlipayStrategy',
    'WeChatPayStrategy',
    'CreditCardStrategy',
]

