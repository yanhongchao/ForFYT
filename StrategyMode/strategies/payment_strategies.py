"""
支付策略模块
提供各种支付策略的实现
"""

from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    """支付策略接口"""
    
    @abstractmethod
    def pay(self, amount: float) -> bool:
        """执行支付
        
        Args:
            amount: 支付金额
            
        Returns:
            支付是否成功
        """
        pass


class AlipayStrategy(PaymentStrategy):
    """支付宝支付策略"""
    
    def pay(self, amount: float) -> bool:
        """使用支付宝支付
        
        Args:
            amount: 支付金额
            
        Returns:
            支付是否成功
        """
        print(f"使用支付宝支付 {amount} 元")
        # 模拟支付逻辑
        return True


class WeChatPayStrategy(PaymentStrategy):
    """微信支付策略"""
    
    def pay(self, amount: float) -> bool:
        """使用微信支付
        
        Args:
            amount: 支付金额
            
        Returns:
            支付是否成功
        """
        print(f"使用微信支付 {amount} 元")
        # 模拟支付逻辑
        return True


class CreditCardStrategy(PaymentStrategy):
    """信用卡支付策略"""
    
    def __init__(self, card_number: str = ""):
        """初始化信用卡支付策略
        
        Args:
            card_number: 信用卡号（可选）
        """
        self.card_number = card_number
    
    def pay(self, amount: float) -> bool:
        """使用信用卡支付
        
        Args:
            amount: 支付金额
            
        Returns:
            支付是否成功
        """
        if self.card_number:
            print(f"使用信用卡（尾号{self.card_number[-4:]}）支付 {amount} 元")
        else:
            print(f"使用信用卡支付 {amount} 元")
        # 模拟支付逻辑
        return True

