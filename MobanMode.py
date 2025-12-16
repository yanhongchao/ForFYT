"""
## 模板方法模式（Template Method Pattern）

模板方法模式是一种行为设计模式，它定义了一个算法的骨架，将某些步骤延迟到子类中实现。模板方法使得子类可以在不改变算法整体结构的情况下，重新定义算法的某些特定步骤。

### 模式结构

根据 UML 类图，模板方法模式包含以下组件：

1. **AbstractClass（抽象类）**：
   - `template_method()`: 模板方法，定义算法的骨架，通常包含多个步骤的调用
   - `step1()`: 抽象方法或钩子方法，由子类实现
   - `step2()`: 抽象方法或钩子方法，由子类实现
   - `hook()`: 钩子方法，可选实现，提供默认行为

2. **ConcreteClassA 和 ConcreteClassB（具体类）**：
   - 继承自 AbstractClass
   - 实现抽象方法 step1() 和 step2()
   - 可选择性地重写 hook() 方法

### 代码实现

### 模式优点

1. **代码复用**：将公共的算法逻辑放在抽象类中，避免代码重复
2. **控制流程**：父类控制算法的执行流程，子类只需实现具体步骤
3. **扩展性好**：添加新的具体类只需实现抽象方法，无需修改现有代码
4. **符合开闭原则**：对扩展开放，对修改关闭

### 使用场景

- 多个类有相似的算法流程，但某些步骤的实现不同
- 需要控制子类的扩展点，确保算法结构不变
- 框架设计：定义框架的骨架，让用户实现具体步骤

### 注意事项

- 模板方法应该是 final 的（在 Python 中通过约定实现），防止子类改变算法结构
- 钩子方法提供灵活性，但不要过度使用，以免增加复杂度
- 抽象方法的数量要适中，太多会导致子类实现负担过重

"""

from abc import ABC, abstractmethod

class BeverageMaker(ABC):
    """饮料制作模板"""
   
    def make_beverage(self):
        """制作饮料的模板方法"""
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
            self.add_condiments()
        self.serve()
   
    def boil_water(self):
        """烧水 - 具体方法"""
        print("烧开水")
   
    @abstractmethod
    def brew(self):
        """冲泡 - 抽象方法"""
        pass
   
    def pour_in_cup(self):
        """倒入杯子 - 具体方法"""
        print("倒入杯子中")
   
    @abstractmethod
    def add_condiments(self):
        """添加调料 - 抽象方法"""
        pass
   
    def customer_wants_condiments(self):
        """钩子方法 - 客户是否要调料"""
        return True
   
    def serve(self):
        """上饮料 - 具体方法"""
        print("饮料制作完成，请享用！")

class CoffeeMaker(BeverageMaker):
    """咖啡制作"""
   
    def brew(self):
        print("用沸水冲泡咖啡粉")
   
    def add_condiments(self):
        print("加入糖和牛奶")
   
    def customer_wants_condiments(self):
        answer = input("咖啡要加糖和牛奶吗？(y/n): ")
        return answer.lower() == 'y'

class TeaMaker(BeverageMaker):
    """茶制作"""
   
    def brew(self):
        print("用沸水浸泡茶叶")
   
    def add_condiments(self):
        print("加入柠檬")

# 使用示例
if __name__ == "__main__":
    print("制作咖啡:")
    coffee = CoffeeMaker()
    coffee.make_beverage()
   
    print("\n" + "="*30 + "\n")
   
    print("制作茶:")
    tea = TeaMaker()
    tea.make_beverage()