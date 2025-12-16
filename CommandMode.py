from abc import ABC, abstractmethod
from typing import List

# 1. 命令接口
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
   
    @abstractmethod
    def undo(self):
        pass

# 2. 接收者 - 灯光设备
class Light:
    def turn_on(self):
        print("💡 灯光已打开")
   
    def turn_off(self):
        print("💡 灯光已关闭")

# 3. 具体命令 - 开灯命令
class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light
   
    def execute(self):
        self.light.turn_on()
   
    def undo(self):
        self.light.turn_off()

# 4. 具体命令 - 关灯命令
class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light
   
    def execute(self):
        self.light.turn_off()
   
    def undo(self):
        self.light.turn_on()

# 5. 调用者 - 遥控器
class RemoteControl:
    def __init__(self):
        self.command = None
        self.history: List[Command] = []
   
    def set_command(self, command: Command):
        self.command = command
   
    def press_button(self):
        if self.command:
            self.command.execute()
            self.history.append(self.command)
   
    def press_undo(self):
        if self.history:
            last_command = self.history.pop()
            last_command.undo()

# 客户端代码
if __name__ == "__main__":
    # 创建设备
    living_room_light = Light()
   
    # 创建命令
    light_on = LightOnCommand(living_room_light)
    light_off = LightOffCommand(living_room_light)
   
    # 创建遥控器
    remote = RemoteControl()
   
    # 测试开灯
    print("=== 测试开灯 ===")
    remote.set_command(light_on)
    remote.press_button()
   
    # 测试关灯
    print("\n=== 测试关灯 ===")
    remote.set_command(light_off)
    remote.press_button()
   
    # 测试撤销
    print("\n=== 测试撤销操作 ===")
    remote.press_undo()  # 撤销关灯，应该开灯
    remote.press_undo()  # 撤销开灯，应该关灯