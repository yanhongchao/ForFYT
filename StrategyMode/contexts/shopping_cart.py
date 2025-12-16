"""
购物车类
使用折扣策略计算商品总价
"""

from typing import List, Dict
from strategies.discount_strategies import DiscountStrategy, NoDiscountStrategy


class ShoppingCart:
    """购物车类"""
    
    def __init__(self):
        """初始化购物车"""
        self.items: List[Dict[str, any]] = []
        self._discount_strategy: DiscountStrategy = NoDiscountStrategy()
    
    def add_item(self, item: str, price: float):
        """添加商品
        
        Args:
            item: 商品名称
            price: 商品价格
        """
        self.items.append({"item": item, "price": price})
    
    def set_discount_strategy(self, strategy: DiscountStrategy):
        """设置折扣策略
        
        Args:
            strategy: 折扣策略实例
        """
        self._discount_strategy = strategy
    
    def calculate_total(self) -> float:
        """计算总价（应用折扣后）
        
        Returns:
            折扣后的总价
        """
        total = sum(item["price"] for item in self.items)
        return self._discount_strategy.calculate_discount(total)
    
    def display_cart(self):
        """显示购物车内容"""
        print("购物车内容:")
        for item in self.items:
            print(f"  - {item['item']}: {item['price']}元")
        
        original_total = sum(item["price"] for item in self.items)
        final_total = self.calculate_total()
        
        print(f"原价: {original_total}元")
        print(f"折后价: {final_total}元")
        
        if original_total != final_total:
            discount = original_total - final_total
            print(f"节省: {discount}元")

