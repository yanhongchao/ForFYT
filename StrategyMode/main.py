"""
策略模式示例主程序
演示购物车和支付策略的使用
"""

from contexts.shopping_cart import ShoppingCart
from contexts.payment_context import PaymentContext
from strategies.discount_strategies import (
    NoDiscountStrategy,
    PercentageDiscountStrategy,
    FixedAmountDiscountStrategy,
    SeasonalDiscountStrategy
)
from strategies.payment_strategies import (
    AlipayStrategy,
    WeChatPayStrategy,
    CreditCardStrategy
)


def main():
    """主函数"""
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
    
    # 演示支付策略
    print("\n" + "=" * 50)
    print("=== 支付策略演示 ===")
    
    final_total = cart.calculate_total()
    
    # 使用支付宝支付
    payment_context = PaymentContext(AlipayStrategy())
    payment_context.execute_payment(final_total)
    
    # 切换到微信支付
    print("\n切换支付方式...")
    payment_context.set_strategy(WeChatPayStrategy())
    payment_context.execute_payment(final_total)
    
    # 切换到信用卡支付
    print("\n切换支付方式...")
    payment_context.set_strategy(CreditCardStrategy("1234567890123456"))
    payment_context.execute_payment(final_total)


if __name__ == "__main__":
    main()

