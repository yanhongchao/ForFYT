########################################################
# 工厂方法模式是一种设计模式,用于创建对象,但将对象的创建过程延迟到子类
# 在编程中，我们经常需要创建对象。如果直接在代码中使用 new 关键字或类的构造函数，会导致：
# 代码耦合度高：创建对象的代码与具体类紧密绑定
# 维护困难：当需要修改或添加新的对象类型时，需要修改多处代码
# 违反开闭原则：对扩展开放，对修改关闭的原则被破坏
# 工厂模式通过将对象的创建过程封装起来，解决了这些问题。
########################################################
# 不推荐：简单情况使用复杂工厂模式 
# 不推荐：一个工厂做太多事情



# 工厂方法模式  工厂方法模式通过让子类决定创建什么对象来解决简单工厂模式的问题
from abc import ABC, abstractmethod
import math
#抽象产品
class Graphics(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass
 
# 具体产品
class Circle(Graphics):
    def __init__(self, radius):
        print(f"Circle 初始化")
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Graphics):
    def __init__(self, width, height):
        print(f"Rectangle 初始化")
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Graphics):
    def __init__(self, a, b, c):
        print(f"Triangle 初始化")
        self.a = a
        self.b = b
        self.c = c

    def calculate_area(self):
        # 海伦公式
        p = (self.a + self.b + self.c) / 2
        area = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return area

    def calculate_perimeter(self):
        return self.a + self.b + self.c



# 创建者抽象类
class Dialog(ABC):
    def __init__(self):
        self.graphic = self.createGraphic()

    @abstractmethod
    def createGraphic(self) -> Graphics:
        pass
   
    def calculate(self):
        return self.graphic.calculate_area()

    def calculate_perimeter(self):
        return self.graphic.calculate_perimeter()

# 具体创建者
class CircleDialog(Dialog):
    def __init__(self, radius):
        self.radius = radius
        super().__init__()  # 调用父类初始化，创建 self.graphic

    def createGraphic(self) -> Graphics:
        return Circle(self.radius)

class TriangleDialog(Dialog):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        super().__init__()  # 调用父类初始化，创建 self.graphic
    def createGraphic(self) -> Graphics:
        return Triangle(self.a, self.b, self.c)

# 使用示例
def test_factory_method():
    # 根据配置选择具体的工厂
    config = "Circle"  # 可以从配置文件读取
   
    if config == "Circle":
        dialog = CircleDialog(radius=4)
    else:
        dialog = TriangleDialog(a=3, b=4, c=5)

    result = dialog.calculate()
    print(result)

if __name__ == "__main__":
    test_factory_method()

