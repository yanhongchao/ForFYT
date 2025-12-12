"""适配器模式示例。

源代码参考自菜鸟教程适配器模式示例：https://www.runoob.com/python-design-pattern/python-adapter.html
适配器模式用于在接口不兼容时建立“转换层”，让旧接口与新接口协同工作。

记住，适配器模式的核心思想是"转换"而不是"修改"，它帮助我们在不改变现有代码的情况下集成新的功能，是维护大型系统时的重要设计模式。
在实际开发中，合理使用适配器模式可以让你的代码更加灵活、可维护，并且易于扩展
"""

# 类适配器示例：通过多重继承将新接口适配到旧接口
class LegacyLogger:
    """被适配的旧日志类"""

    def write_log(self, message: str) -> None:
        print(f"[LEGACY] {message}")


class NewLoggerInterface:
    """目标接口"""

    def log(self, level: str, message: str) -> None:
        raise NotImplementedError


class LoggerAdapter(NewLoggerInterface, LegacyLogger):
    """类适配器 - 通过继承实现接口转换"""

    def log(self, level: str, message: str) -> None:
        formatted_message = f"{level}: {message}"
        self.write_log(formatted_message)


# 对象适配器示例：组合旧接口，并在适配器中做转换
class LegacyPayment:
    """被适配的旧支付系统"""

    def process_payment(self, amount_in_dollars: float) -> bool:
        print(f"处理支付: ${amount_in_dollars}")
        return True


class NewPaymentInterface:
    """新的支付接口"""

    def pay(self, amount: float, currency: str = "CNY") -> bool:
        raise NotImplementedError


class PaymentAdapter(NewPaymentInterface):
    """对象适配器 - 通过组合实现接口转换"""

    def __init__(self, legacy_payment: LegacyPayment):
        self.legacy_payment = legacy_payment

    def pay(self, amount: float, currency: str = "CNY") -> bool:
        # 简化的汇率转换示例
        amount_in_dollars = amount if currency == "USD" else amount / 7.0
        return self.legacy_payment.process_payment(amount_in_dollars)


def demo_class_adapter() -> None:
    print("=== 类适配器示例 ===")
    logger = LoggerAdapter()
    logger.log("INFO", "系统启动成功")
    logger.log("ERROR", "数据库连接失败")


def demo_object_adapter() -> None:
    print("\n=== 对象适配器示例 ===")
    legacy_payment = LegacyPayment()
    payment = PaymentAdapter(legacy_payment)
    payment.pay(700, "CNY")  # 支付 700 元人民币
    payment.pay(100, "USD")  # 支付 100 美元


def main() -> None:
    demo_class_adapter()
    demo_object_adapter()


if __name__ == "__main__":
    main()

