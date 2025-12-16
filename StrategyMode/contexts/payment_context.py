"""
支付上下文类
用于管理和执行支付策略
"""

from typing import Optional
from strategies.payment_strategies import PaymentStrategy


class PaymentContext:
    """支付上下文类"""
    
    def __init__(self, strategy: Optional[PaymentStrategy] = None):
        """初始化支付上下文
        
        Args:
            strategy: 支付策略（可选）
        """
        self._strategy = strategy
    
    def set_strategy(self, strategy: PaymentStrategy):
        """设置支付策略
        
        Args:
            strategy: 支付策略实例
        """
        self._strategy = strategy
    
    def execute_payment(self, amount: float) -> bool:
        """执行支付
        
        Args:
            amount: 支付金额
            
        Returns:
            支付是否成功
            
        Raises:
            ValueError: 当未设置支付策略时
        """
        if not self._strategy:
            raise ValueError("未设置支付策略")
        
        return self._strategy.pay(amount)

