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

# 产品接口
class Button(ABC):
    @abstractmethod
    def render(self):
        pass
   
    @abstractmethod
    def onClick(self):
        pass

# 具体产品
class WindowsButton(Button):
    def render(self):
        return "渲染 Windows 风格按钮"
   
    def onClick(self):
        return "Windows 按钮被点击"

class MacButton(Button):
    def render(self):
        return "渲染 Mac 风格按钮"
   
    def onClick(self):
        return "Mac 按钮被点击"

# 创建者抽象类
class Dialog(ABC):
    def __init__(self):
        print("Dialog 初始化")
        self.button = self.createButton()

    @abstractmethod
    def createButton(self) -> Button:
        pass
   
    def render(self):
        # 调用工厂方法创建产品
        #button = self.createButton()
        #print(f"button: {button}")
        result = self.button.render()
        return result

# 具体创建者
class WindowsDialog(Dialog):
    def createButton(self) -> Button:
        return WindowsButton()

class MacDialog(Dialog):
    def createButton(self) -> Button:
        return MacButton()

# 使用示例
def test_factory_method():
    # 根据配置选择具体的工厂
    config = "windows"  # 可以从配置文件读取
   
    if config == "windows":
        dialog = WindowsDialog()
    else:
        dialog = MacDialog()

    result = dialog.render()
    print(result)

if __name__ == "__main__":
    test_factory_method()


########################################################
# 抽象工厂模式 抽象工厂模式提供了一个创建一系列相关或依赖对象的接口，而无需指定具体类


# 抽象产品 A
class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

# 抽象产品 B
class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass

# 具体产品 A1
class WindowsButton(Button):
    def paint(self):
        return "abstract 渲染 Windows 按钮"

# 具体产品 A2
class MacButton(Button):
    def paint(self):
        return "abstract 渲染 Mac 按钮"

# 具体产品 B1
class WindowsCheckbox(Checkbox):
    def paint(self):
        return "abstract 渲染 Windows 复选框"

# 具体产品 B2
class MacCheckbox(Checkbox):
    def paint(self):
        return "abstract 渲染 Mac 复选框"

# 抽象工厂
class GUIFactory(ABC):
    @abstractmethod
    def createButton(self) -> Button:
        pass
   
    @abstractmethod
    def createCheckbox(self) -> Checkbox:
        pass

# 具体工厂 1
class WindowsFactory(GUIFactory):
    def createButton(self) -> Button:
        return WindowsButton()
   
    def createCheckbox(self) -> Checkbox:
        return WindowsCheckbox()

# 具体工厂 2
class MacFactory(GUIFactory):
    def createButton(self) -> Button:
        return MacButton()
   
    def createCheckbox(self) -> Checkbox:
        return MacCheckbox()

# 客户端代码
class Application:
    def __init__(self, factory: GUIFactory):
        self.factory = factory
        self.button = None
        self.checkbox = None
   
    def createUI(self):
        self.button = self.factory.createButton()
        self.checkbox = self.factory.createCheckbox()
   
    def paint(self):
        result = []
        if self.button:
            result.append(self.button.paint())
        if self.checkbox:
            result.append(self.checkbox.paint())
        return "\n".join(result)

# 使用示例
def test_abstract_factory():
    # 根据系统类型选择工厂
    system_type = "windows"  # 可以自动检测或从配置读取
   
    if system_type == "windows":
        factory = WindowsFactory()
    else:
        factory = MacFactory()
   
    app = Application(factory)
    app.createUI()
    print(app.paint())

if __name__ == "__main__":
    test_abstract_factory()    


# 服务接口
class NotificationService(ABC):
    @abstractmethod
    def send(self, message):
        pass

# 具体服务
class EmailService(NotificationService):
    def send(self, message):
        return f"发送邮件: {message}"

class SMSService(NotificationService):
    def send(self, message):
        return f"发送短信: {message}"

# 工厂
class NotificationFactory:
    @staticmethod
    def create_service(service_type):
        if service_type == "email":
            return EmailService()
        elif service_type == "sms":
            return SMSService()
        else:
            raise ValueError(f"未知的服务类型: {service_type}")

# 使用依赖注入的类
class OrderProcessor:
    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service
   
    def process_order(self, order):
        # 处理订单逻辑
        result = self.notification_service.send("订单处理完成")
        return result

# 使用
def main():
    # 通过工厂创建服务
    notification_service = NotificationFactory.create_service("email")
   
    # 注入依赖
    processor = OrderProcessor(notification_service)
    result = processor.process_order({"id": 1})
    print(result)

if __name__ == "__main__":
    main()


import logging
from abc import ABC, abstractmethod
import sys

# 日志记录器接口
class Logger(ABC):
    @abstractmethod
    def info(self, message):
        pass
   
    @abstractmethod
    def error(self, message):
        pass
   
    @abstractmethod
    def debug(self, message):
        pass

# 控制台日志记录器
class ConsoleLogger(Logger):
    def info(self, message):
        print(f"INFO: {message}")
   
    def error(self, message):
        print(f"ERROR: {message}", file=sys.stderr)
   
    def debug(self, message):
        print(f"DEBUG: {message}")

# 文件日志记录器
class FileLogger(Logger):
    def __init__(self, filename):
        self.filename = filename
   
    def info(self, message):
        with open(self.filename, 'a') as f:
            f.write(f"INFO: {message}\n")
   
    def error(self, message):
        with open(self.filename, 'a') as f:
            f.write(f"ERROR: {message}\n")
   
    def debug(self, message):
        with open(self.filename, 'a') as f:
            f.write(f"DEBUG: {message}\n")

# 日志工厂
class LoggerFactory:
    @staticmethod
    def get_logger(logger_type, **kwargs):
        if logger_type == "console":
            return ConsoleLogger()
        elif logger_type == "file":
            return FileLogger(**kwargs)
        else:
            raise ValueError(f"不支持的日志类型: {logger_type}")

# 使用示例
def test_logger_factory():
    # 创建控制台日志记录器
    console_logger = LoggerFactory.get_logger("console")
    console_logger.info("这是一个信息消息")
    console_logger.error("这是一个错误消息")
   
    # 创建文件日志记录器
    file_logger = LoggerFactory.get_logger("file", filename="app.log")
    file_logger.info("记录到文件的信息")
    file_logger.debug("调试信息")

if __name__ == "__main__":
    test_logger_factory()