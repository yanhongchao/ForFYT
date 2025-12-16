from abc import ABC, abstractmethod
import time

class ElevatorState(ABC):
    """电梯状态接口"""
   
    @abstractmethod
    def open_doors(self):
        """开门操作"""
        pass
   
    @abstractmethod
    def close_doors(self):
        """关门操作"""
        pass
   
    @abstractmethod
    def move(self):
        """移动操作"""
        pass
   
    @abstractmethod
    def stop(self):
        """停止操作"""
        pass

    @abstractmethod
    def open_repair(self):
        """维修操作"""
        pass

    @abstractmethod
    def select_floor(self, floor):
        """选择楼层操作"""
        pass


class DoorOpenState(ElevatorState):
    """开门状态"""
   
    def open_doors(self):
        print("门已经是开着的")
        return self
   
    def close_doors(self):
        print("正在关门...")
        return DoorClosedState()
   
    def move(self):
        print("错误：门还开着，不能移动")
        return self
   
    def stop(self):
        print("电梯已经停止")
        return self

    def open_repair(self):
        """维修操作"""
        print("电梯进入维修状态")
        return RepairState()
    
    def select_floor(self, floor):
        """选择楼层操作"""
        print(f"电梯开门状态，选择楼层成功，选择楼层为{floor}")
        print("电梯进入关门状态")
        DoorClosedState()
        MovingState()
        print("电梯到达楼层，进入状态")
        DoorClosedState()
        return DoorOpenState()

        



class DoorClosedState(ElevatorState):
    """关门状态"""
   
    def open_doors(self):
        print("正在开门...")
        return DoorOpenState()
   
    def close_doors(self):
        print("门已经是关着的")
        return self
   
    def move(self):
        print("电梯开始移动...")
        return MovingState()
   
    def stop(self):
        print("电梯已经停止")
        return self

    def open_repair(self):
        """维修操作"""
        print("电梯进入维修状态")
        return RepairState()

    def select_floor(self, floor):
        """选择楼层操作"""
        print(f"选择楼层成功，选择楼层为{floor}")
        

        #等待楼层到达后，电梯进入开门状态
        for i in range(floor):
            print(f"电梯正在到达楼层{i}")
            time.sleep(1)
        
        print("电梯到达楼层，进入开门状态")
        return DoorOpenState()



class MovingState(ElevatorState):
    """移动状态"""
   
    def open_doors(self):
        print("错误：电梯在移动中，不能开门")
        return self
   
    def close_doors(self):
        print("门已经是关着的")
        return self
   
    def move(self):
        print("电梯正在移动中")
        return self
   
    def stop(self):
        print("电梯停止中...")
        return DoorClosedState()

    def open_repair(self):
        """维修操作"""
        print("电梯移动中，无法进入维修状态")
        return self

    def select_floor(self, floor):
        """选择楼层操作"""
        print(f"电梯移动中，无法选择楼层为{floor}")
        return self



class RepairState(ElevatorState):
    """开维修状态"""
   
    def open_doors(self):
        print("错误：电梯在维修中，不能开门")
        return self
   
    def close_doors(self):
        print("错误：电梯在维修中，不能关门")
        return self
   
    def move(self):
        print("错误：电梯在维修中，移动是非法操作")
        return self
   
    def stop(self):
        print("错误：电梯在维修中，不能停止")
        return self

    def open_repair(self):
        """关闭维修状态"""
        print("电梯已经是维修状态")
        return self

    def close_repair(self):
        """关闭维修状态"""
        print("电梯退出维修状态，进入关门状态")
        return DoorClosedState()

    def select_floor(self, floor):
        """选择楼层操作"""
        print(f"电梯维修中，无法选择楼层为{floor}")
        return self


