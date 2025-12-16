from abc import ABC, abstractmethod
from typing import List

# 抽象中介者
class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: object, event: str, data: dict = None):
        pass

# 具体中介者 - 聊天室
class ChatRoomMediator(Mediator):
    def __init__(self):
        self.users: List[User] = []
   
    def add_user(self, user):
        self.users.append(user)
        user.set_mediator(self)
        user.join_chat()

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)
            user.leave_chat()
            user.set_mediator(None)         
        else:
            print(f"用户 {user.name} 不存在")
   
    def notify(self, sender, event, data=None):
        if event == "send_message":
            message = data.get("message")
            target_user = data.get("target_user")
           
            if target_user:  # 私聊
                for user in self.users:
                    if user.name == target_user:
                        user.receive_message(message, sender.name)
            else:  # 群聊
                for user in self.users:
                    if user != sender:
                        user.receive_message(message, sender.name)
       
        elif event == "user_joined":
            message = f"系统: {sender.name} 加入了聊天室"
            for user in self.users:
                if user != sender:
                    user.receive_message(message, "系统")
        elif event == "user_left":
            message = f"系统: {sender.name} 离开了聊天室"
            for user in self.users:
                if user != sender:
                    user.receive_message(message, "系统")

# 基础组件类
class BaseComponent:
    def __init__(self):
        self._mediator = None
   
    def set_mediator(self, mediator: Mediator):
        self._mediator = mediator

# 具体组件 - 用户
class User(BaseComponent):
    def __init__(self, name):
        super().__init__()
        self.name = name
   
    def send_message(self, message, target_user=None):
        print(f"{self.name} 发送消息: {message}")
        self._mediator.notify(self, "send_message", {
            "message": message,
            "target_user": target_user
        })
   
    def join_chat(self):
        self._mediator.notify(self, "user_joined")
    
    def leave_chat(self):
        self._mediator.notify(self, "user_left")
   
    def receive_message(self, message, from_name):
        print(f"{self.name} 收到来自 {from_name} 的消息: {message}")

# 使用示例
def main():
    # 创建中介者
    chat_room = ChatRoomMediator()
   
    # 创建用户
    alice = User("Alice")
    bob = User("Bob")
    charlie = User("Charlie")
   
    # 注册用户到聊天室
    chat_room.add_user(alice)
    chat_room.add_user(bob)
    chat_room.add_user(charlie)
   
    print("=== 聊天室演示 ===")
   
   
    # 发送消息
    alice.send_message("大家好，我是 Alice！")
    bob.send_message("欢迎 Alice！")
    charlie.send_message("Alice 你好！", "Alice")  # 私聊
   
    # Bob 发送群消息
    bob.send_message("有人在线吗？")

    # Charlie 离开聊天室
    chat_room.remove_user(charlie)

if __name__ == "__main__":
    main()