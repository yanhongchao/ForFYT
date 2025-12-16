"""支付系统桥接模式示例。

支付方式（实现层）：支付宝、微信支付、银行卡
支付类型（抽象层）：普通支付、分期支付、组合支付

桥接模式将“支付类型”和“支付方式”解耦，二者可独立扩展。
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Tuple


# ========== 实现层：支付方式 ==========
class PaymentMethod(ABC):
    """支付方式接口"""

    @abstractmethod
    def pay(self, amount: float) -> None:
        raise NotImplementedError

    def name(self) -> str:
        return self.__class__.__name__


class Alipay(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"[{self.name()}] 支付 {amount:.2f} 元")


class WeChatPay(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"[{self.name()}] 支付 {amount:.2f} 元")


class BankCardPay(PaymentMethod):
    def __init__(self, card_no: str):
        self.card_no = card_no

    def pay(self, amount: float) -> None:
        masked = self.card_no[:-4].replace(self.card_no[:-4], "*" * len(self.card_no[:-4])) + self.card_no[-4:]
        print(f"[{self.name()} {masked}] 支付 {amount:.2f} 元")


# ========== 抽象层：支付类型 ==========
class PaymentType(ABC):
    """支付类型抽象层，桥接到支付方式"""

    def __init__(self, method: PaymentMethod):
        self.method = method

    def set_method(self, method: PaymentMethod) -> None:
        """切换支付方式"""
        self.method = method

    @abstractmethod
    def pay(self, amount: float, **kwargs) -> None:
        raise NotImplementedError


class NormalPayment(PaymentType):
    """普通支付"""

    def pay(self, amount: float, **kwargs) -> None:
        self.method.pay(amount)


class InstallmentPayment(PaymentType):
    """分期支付"""

    def pay(self, amount: float, months: int = 3, **kwargs) -> None:
        if months <= 0:
            raise ValueError("分期月数必须大于 0")
        monthly = amount / months
        print(f"分期支付：共 {months} 期，每期 {monthly:.2f} 元")
        for i in range(1, months + 1):
            print(f"第 {i} 期：", end="")
            self.method.pay(monthly)


class CompositePayment(PaymentType):
    """组合支付：按比例拆分到多个支付方式"""

    def __init__(self, method_shares: List[Tuple[PaymentMethod, float]]):
        if not method_shares:
            raise ValueError("组合支付需要至少一个支付方式")
        total_ratio = sum(ratio for _, ratio in method_shares)
        if total_ratio <= 0:
            raise ValueError("组合支付比例和必须大于 0")
        # 归一化比例，避免输入比例和不为 1
        self.method_shares = [(m, ratio / total_ratio) for m, ratio in method_shares]

    def pay(self, amount: float, **kwargs) -> None:
        print("组合支付开始：")
        for method, ratio in self.method_shares:
            portion = amount * ratio
            print(f"- 分配 {portion:.2f} 元到 {method.name()}（占比 {ratio:.2%}）")
            method.pay(portion)


# ========== 演示用例 ==========
def main() -> None:
    print("=== 普通支付（支付宝） ===")
    normal = NormalPayment(Alipay())
    normal.pay(120)

    print("\n=== 分期支付（微信，6 期） ===")
    installment = InstallmentPayment(WeChatPay())
    installment.pay(1200, months=6)

    print("\n=== 组合支付（支付宝 + 银行卡） ===")
    composite = CompositePayment([
        (Alipay(), 0.4),
        (BankCardPay("6222334455667788"), 0.6),
    ])
    composite.pay(500)

    print("\n=== 切换支付方式后再次普通支付（银行卡） ===")
    normal.set_method(BankCardPay("4111222233334444"))
    normal.pay(300)


if __name__ == "__main__":
    main()



