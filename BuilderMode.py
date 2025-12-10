########################################################
# 建造者模式是一种设计模式,用于创建一个复杂的对象,但将对象的创建过程分解为多个步骤
########################################################
# 1. Product（产品） 要创建的复杂对象
# 2. Builder（抽象建造者）定义创建产品各个部分的抽象接口
# 3. ConcreteBuilder（具体建造者） 实现 Builder 接口，构造和装配各个部件
# 4. Director（指挥者） 构建一个使用 Builder 接口的对象


from abc import ABC, abstractmethod

class Computer:
    """电脑产品类"""
    def __init__(self):
        self.cpu = None
        self.memory = None
        self.storage = None
        self.graphics_card = None
        self.monitor = None
        self.opticalDrive = None
        self.cpu_price = 0
        self.memory_price = 0
        self.storage_price = 0
        self.graphics_card_price = 0
        self.monitor_price = 0
        self.opticalDrive_price = 0
   
    def __str__(self):
        specs = []
        if self.cpu:
            specs.append(f"CPU: {self.cpu}")
        if self.memory:
            specs.append(f"内存: {self.memory}GB")
        if self.storage:
            specs.append(f"存储: {self.storage}GB")
        if self.graphics_card:
            specs.append(f"显卡: {self.graphics_card}")
        if self.monitor:
            specs.append(f"显示器: {self.monitor}")
        if self.opticalDrive:
            specs.append(f"光驱: {self.opticalDrive}")
        
        if self.memory and self.memory >4:
            specs.append(f"内存检查正常")
        else:
            specs.append(f"内存检查不正常")

        specs.append(f"总价: {self.price()}")
       
        return "电脑配置:\n" + "\n".join(f"  - {spec}" for spec in specs)
    
    def price(self):
        """计算电脑总价"""
        total = 0
        total += self.cpu_price if self.cpu_price else 0
        total += self.memory_price if self.memory_price else 0
        total += self.storage_price if self.storage_price else 0
        total += self.graphics_card_price if self.graphics_card_price else 0
        total += self.monitor_price if self.monitor_price else 0
        total += self.opticalDrive_price if self.opticalDrive_price else 0
        return total

class ComputerBuilder(ABC):
    """电脑建造者抽象类"""
   
    def __init__(self):
        self.computer = Computer()
   
    @abstractmethod
    def build_cpu(self):
        pass
   
    @abstractmethod
    def build_memory(self):
        pass
   
    @abstractmethod
    def build_storage(self):
        pass
   
    @abstractmethod
    def build_graphics_card(self):
        pass
   
    @abstractmethod
    def build_monitor(self):
        pass
   
    # @abstractmethod
    # def build_optical_drive(self):
    #     pass
   
    def get_computer(self):
        return self.computer


class GamingComputerBuilder(ComputerBuilder):
    """游戏电脑建造者"""
   
    def build_cpu(self):
        self.computer.cpu = "Intel i9-13900K"
        self.computer.cpu_price = 5000
   
    def build_memory(self):
        self.computer.memory = 1
        self.computer.memory_price = 1000
   
    def build_storage(self):
        self.computer.storage = 2000  # 2TB
        self.computer.storage_price = 1000
   
    def build_graphics_card(self):
        self.computer.graphics_card = "NVIDIA RTX 4090"
        self.computer.graphics_card_price = 1000
   
    def build_monitor(self):
        self.computer.monitor = "32寸 4K 144Hz"
        self.computer.monitor_price = 1000

    def build_optical_drive(self):
        self.computer.opticalDrive = "DVD光驱"
        self.computer.opticalDrive_price = 1000
class OfficeComputerBuilder(ComputerBuilder):
    """办公电脑建造者"""
   
    def build_cpu(self):
        self.computer.cpu = "Intel i5-13400"
        self.computer.cpu_price = 3000
   
    def build_memory(self):
        self.computer.memory = 16
        self.computer.memory_price = 500
   
    def build_storage(self):
        self.computer.storage = 512
        self.computer.storage_price = 1000
   
    def build_graphics_card(self):
        self.computer.graphics_card = "集成显卡"
        self.computer.graphics_card_price = 1000
   
    def build_monitor(self):
        self.computer.monitor = "24寸 1080P"
        self.computer.monitor_price = 1000

    # def build_optical_drive(self):
    #     self.computer.opticalDrive = "DVD光驱"
    #     self.computer.opticalDrive_price = 1000

class ComputerDirector:
    """电脑建造指挥者"""
   
    def __init__(self, builder):
        self.builder = builder
   
    def construct_computer(self):
        """构建电脑的完整过程"""
        self.builder.build_cpu()
        self.builder.build_memory()
        self.builder.build_storage()
        self.builder.build_graphics_card()
        self.builder.build_monitor()
        # 如果建造者实现了 build_optical_drive 方法，则调用它
        if hasattr(self.builder, 'build_optical_drive'):
            self.builder.build_optical_drive()
   
    def get_computer(self):
        return self.builder.get_computer()

def main():
    print("=== 建造者模式演示 ===\n")
   
    # 创建游戏电脑
    print("1. 构建游戏电脑:")
    gaming_builder = GamingComputerBuilder()
    director = ComputerDirector(gaming_builder)
    director.construct_computer()
    gaming_computer = director.get_computer()
    print(gaming_computer)
   
    print("\n" + "="*50 + "\n")
   
    # 创建办公电脑
    print("2. 构建办公电脑:")
    office_builder = OfficeComputerBuilder()
    director = ComputerDirector(office_builder)
    director.construct_computer()
    office_computer = director.get_computer()
    print(office_computer)
   
    print("\n" + "="*50 + "\n")
   
    # 创建自定义电脑
    print("3. 自定义电脑构建: 使用流式接口建造者")
    custom_builder = (
        CustomComputerBuilder()
        .build_cpu("AMD Ryzen 7 7800X3D", 5000)
        .build_memory(64, 1000)
        .build_storage(4000, 1000)    # 4TB
        .build_graphics_card("AMD RX 7900 XTX", 1000)
        .build_monitor("34寸曲面带鱼屏", 1000)
        .build_optical_drive("DVD光驱", 1000)
    )
    custom_computer = custom_builder.get_computer()
    print(custom_computer)

# 自定义建造者（可选步骤构建）
class CustomComputerBuilder:
    """自定义电脑建造者"""
   
    def __init__(self):
        self.computer = Computer()
   
    def build_cpu(self, cpu, price):
        self.computer.cpu = cpu
        self.computer.cpu_price = price
        return self  # 返回自身，支持链式调用
   
    def build_memory(self, memory, price):
        self.computer.memory = memory
        self.computer.memory_price = price
        return self
   
    def build_storage(self, storage, price):
        self.computer.storage = storage
        self.computer.storage_price = price
        return self
   
    def build_graphics_card(self, graphics_card, price):
        self.computer.graphics_card = graphics_card
        self.computer.graphics_card_price = price
        return self
   
    def build_monitor(self, monitor, price):
        self.computer.monitor = monitor
        self.computer.monitor_price = price
        return self
    
    def build_optical_drive(self, optical_drive, price):
        self.computer.opticalDrive = optical_drive
        self.computer.opticalDrive_price = price
        return self
   
    def get_computer(self):
        return self.computer

if __name__ == "__main__":
    main()