from operator import eq
from State.ElevatorState import DoorClosedState


class Elevator:
    """电梯上下文类"""
   
    def __init__(self):
        # 初始状态为门关闭状态
        self._state = DoorClosedState()
        self.current_floor = 0
   
    @property
    def state(self):
        """获取当前状态"""
        return self._state
   
    def set_state(self, state):
        """设置新状态"""
        self._state = state
        print(f"状态已切换为: {state.__class__.__name__}")
   
    def open_doors(self):
        """开门操作"""
        print("执行开门操作...")
        self.set_state(self._state.open_doors())
   
    def close_doors(self):
        """关门操作"""
        print("执行关门操作...")
        self.set_state(self._state.close_doors())
   
    def move(self):
        """移动操作"""
        print("执行移动操作...")
        self.set_state(self._state.move())
   
    def stop(self):
        """停止操作"""
        print("执行停止操作...")
        self.set_state(self._state.stop())

    def repair(self):
        """维修操作"""
        print("执行维修操作...")
        self.set_state(self._state.open_repair())

    def stop_repair(self):
        """维修操作"""
        print("执行关闭维修操作...")
        self.set_state(self._state.close_repair())

    def select_floor(self, floor):
        """选择楼层操作"""
        print("执行选择楼层操作...")
        if floor != self.current_floor:
            print("电梯正在到达楼层，请稍后...")
            self.current_floor = floor
            self.set_state(self._state.select_floor(floor))
        else:
            print("电梯已经在该楼层，请重新选择楼层...")
    