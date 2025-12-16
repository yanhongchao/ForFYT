project/
├── strategies/
│   ├── __init__.py
│   ├── base_strategy.py      # 基础策略接口
│   ├── discount_strategies.py # 折扣相关策略
│   └── payment_strategies.py # 支付相关策略
├── contexts/
│   ├── __init__.py
│   ├── payment_context.py    # 支付上下文类
│   └── shopping_cart.py      # 上下文类

└── main.py

在项目中，我们定义了三个策略：
1. 基础策略接口：BaseStrategy
代码如下：
```python
from abc import ABC, abstractmethod

class BaseStrategy(ABC):
    """基础策略接口"""
   
    @abstractmethod
    def execute(self) -> bool:
        """执行策略"""
        pass
```

2. 折扣相关策略：DiscountStrategy
```python
from abc import ABC, abstractmethod
from typing import Dict, Any

# 策略接口
class DiscountStrategy(ABC):
    """折扣策略接口"""
   
    @abstractmethod
    def calculate_discount(self, original_price: float) -> float:
        """计算折扣后的价格"""
        pass

# 具体策略实现
class NoDiscountStrategy(DiscountStrategy):
    """无折扣策略"""
   
    def calculate_discount(self, original_price: float) -> float:
        return original_price

class PercentageDiscountStrategy(DiscountStrategy):
    """百分比折扣策略"""
   
    def __init__(self, percentage: float):
        if not 0 <= percentage <= 100:
            raise ValueError("折扣百分比必须在 0-100 之间")
        self.percentage = percentage
   
    def calculate_discount(self, original_price: float) -> float:
        discount_amount = original_price * (self.percentage / 100)
        return original_price - discount_amount

class FixedAmountDiscountStrategy(DiscountStrategy):
    """固定金额折扣策略"""
   
    def __init__(self, discount_amount: float):
        if discount_amount < 0:
            raise ValueError("折扣金额不能为负数")
        self.discount_amount = discount_amount
   
    def calculate_discount(self, original_price: float) -> float:
        return max(0, original_price - self.discount_amount)

class SeasonalDiscountStrategy(DiscountStrategy):
    """季节性折扣策略"""
   
    def __init__(self, base_discount: float, seasonal_multiplier: float):
        self.base_discount = base_discount
        self.seasonal_multiplier = seasonal_multiplier
   
    def calculate_discount(self, original_price: float) -> float:
        total_discount = self.base_discount * self.seasonal_multiplier
        return max(0, original_price - total_discount)

```
3. 支付相关策略：PaymentStrategy
```python
class PaymentContext:
    """支付上下文类"""
   
    def __init__(self, strategy: PaymentStrategy = None):
        self._strategy = strategy
   
    def set_strategy(self, strategy: PaymentStrategy):
        """设置支付策略"""
        self._strategy = strategy
   
    def execute_payment(self, amount: float) -> bool:
        """执行支付"""
        if not self._strategy:
            raise ValueError("未设置支付策略")
       
        return self._strategy.pay(amount)

```
4 购物车：ShoppingCart
```python
class ShoppingCart:
    """购物车类"""
   
    def __init__(self):
        self.items = []
        self._discount_strategy = NoDiscountStrategy()
   
    def add_item(self, item: str, price: float):
        """添加商品"""
        self.items.append({"item": item, "price": price})
   
    def set_discount_strategy(self, strategy: DiscountStrategy):
        """设置折扣策略"""
        self._discount_strategy = strategy
   
    def calculate_total(self) -> float:
        """计算总价"""
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
```

5. 主函数：main.py
```python
def main():
    # 创建购物车
    cart = ShoppingCart()
   
    # 添加商品
    cart.add_item("Python编程书", 89.0)
    cart.add_item("无线鼠标", 129.0)
    cart.add_item("机械键盘", 399.0)
   
    print("=== 无折扣 ===")
    cart.set_discount_strategy(NoDiscountStrategy())
    cart.display_cart()
   
    print("\n=== 8折优惠 ===")
    cart.set_discount_strategy(PercentageDiscountStrategy(20))  # 8折
    cart.display_cart()
   
    print("\n=== 满减优惠（减50元）===")
    cart.set_discount_strategy(FixedAmountDiscountStrategy(50))
    cart.display_cart()
   
    print("\n=== 季节性优惠 ===")
    cart.set_discount_strategy(SeasonalDiscountStrategy(30, 1.5))  # 基础折扣30，季节性系数1.5
    cart.display_cart()

if __name__ == "__main__":
    main()
```

