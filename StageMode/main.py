from contexts.Elevator import Elevator
# 创建电梯实例
elevator = Elevator()

# 测试状态转换
print("=== 电梯状态转换测试 ===")

elevator.open_doors()   # 从关门状态切换到开门状态
elevator.close_doors()  # 从开门状态切换回关门状态
elevator.move()         # 从关门状态切换到移动状态
elevator.stop()         # 从移动状态切换回关门状态
elevator.select_floor(13)   # 选择楼层

elevator.select_floor(13)   # 选择楼层

# print("\n=== 测试非法操作 ===")
# elevator.open_doors()   # 正常开门
# elevator.move()         # 尝试在开门状态下移动（应该报错）


# #测试楼层选择
# elevator.close_doors() 
# elevator.stop()
# elevator.repair()
# elevator.open_doors()   # 选择楼层
# elevator.stop_repair()  # 关闭维修状态
