"""
折扣策略模块
提供各种折扣策略的实现
"""

from abc import ABC, abstractmethod
from typing import Dict, Any


# 策略接口
class DiscountStrategy(ABC):
    """折扣策略接口"""
    
    @abstractmethod
    def calculate_discount(self, original_price: float) -> float:
        """计算折扣后的价格
        
        Args:
            original_price: 原始价格
            
        Returns:
            折扣后的价格
        """
        pass


# 具体策略实现
class NoDiscountStrategy(DiscountStrategy):
    """无折扣策略"""
    
    def calculate_discount(self, original_price: float) -> float:
        """计算折扣后的价格（无折扣）
        
        Args:
            original_price: 原始价格
            
        Returns:
            原始价格（无折扣）
        """
        return original_price


class PercentageDiscountStrategy(DiscountStrategy):
    """百分比折扣策略"""
    
    def __init__(self, percentage: float):
        """初始化百分比折扣策略
        
        Args:
            percentage: 折扣百分比（0-100）
            
        Raises:
            ValueError: 当折扣百分比不在 0-100 之间时
        """
        if not 0 <= percentage <= 100:
            raise ValueError("折扣百分比必须在 0-100 之间")
        self.percentage = percentage
    
    def calculate_discount(self, original_price: float) -> float:
        """计算折扣后的价格（百分比折扣）
        
        Args:
            original_price: 原始价格
            
        Returns:
            折扣后的价格
        """
        discount_amount = original_price * (self.percentage / 100)
        return original_price - discount_amount


class FixedAmountDiscountStrategy(DiscountStrategy):
    """固定金额折扣策略"""
    
    def __init__(self, discount_amount: float):
        """初始化固定金额折扣策略
        
        Args:
            discount_amount: 折扣金额
            
        Raises:
            ValueError: 当折扣金额为负数时
        """
        if discount_amount < 0:
            raise ValueError("折扣金额不能为负数")
        self.discount_amount = discount_amount
    
    def calculate_discount(self, original_price: float) -> float:
        """计算折扣后的价格（固定金额折扣）
        
        Args:
            original_price: 原始价格
            
        Returns:
            折扣后的价格（最低为0）
        """
        return max(0, original_price - self.discount_amount)


class SeasonalDiscountStrategy(DiscountStrategy):
    """季节性折扣策略"""
    
    def __init__(self, base_discount: float, seasonal_multiplier: float):
        """初始化季节性折扣策略
        
        Args:
            base_discount: 基础折扣金额
            seasonal_multiplier: 季节性系数
        """
        self.base_discount = base_discount
        self.seasonal_multiplier = seasonal_multiplier
    
    def calculate_discount(self, original_price: float) -> float:
        """计算折扣后的价格（季节性折扣）
        
        Args:
            original_price: 原始价格
            
        Returns:
            折扣后的价格（最低为0）
        """
        total_discount = self.base_discount * self.seasonal_multiplier
        return max(0, original_price - total_discount)

