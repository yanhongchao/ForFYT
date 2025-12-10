"""原型模式示例。

源代码参考自菜鸟教程原型模式示例：https://www.runoob.com/python-design-pattern/python-prototype.html
通过克隆（深拷贝）已有对象，避免每次从头初始化耗时资源。
原型模式是 Python 中一个非常实用的设计模式，它通过复制现有对象来创建新对象，特别适合以下场景：
对象创建成本高：当创建新对象的初始化过程很复杂或耗时
需要相似对象：当需要创建多个相似但略有不同的对象
动态配置：当对象的配置可能在运行时改变
关键要点：
使用 copy 模块实现复制功能
根据需求选择浅复制或深复制
考虑使用原型注册表来管理多个原型
注意处理循环引用和内存使用问题
"""


import copy
from abc import ABC, abstractmethod
from typing import Any, List


class Prototype(ABC):
    """原型抽象基类，约束子类必须实现 clone 方法。"""

    @abstractmethod
    def clone(self) -> Any:
        """返回当前对象的克隆。"""
        raise NotImplementedError


class CarPrototype(Prototype):
    """汽车原型类，演示克隆如何避免重复复杂初始化。"""

    def __init__(self, brand: str, model: str, color: str, engine_type: str):
        self.brand = brand
        self.model = model
        self.color = color
        self.engine_type = engine_type
        self.accessories: List[str] = []
        self.initialize_complex_components()

    def initialize_complex_components(self):
        """模拟耗时或复杂的初始化逻辑。"""
        print(f"正在初始化 {self.brand} {self.model} 的复杂组件...")

    def add_accessory(self, accessory: str) -> None:
        """添加配件信息。"""
        self.accessories.append(accessory)

    def clone(self) -> "CarPrototype":
        """使用深拷贝生成新实例，确保嵌套结构安全复制。"""
        return copy.deepcopy(self)

    def display_info(self) -> None:
        """打印车辆信息和配件列表。"""
        info = f"{self.brand} {self.model} - 颜色: {self.color}, 发动机: {self.engine_type}"
        if self.accessories:
            info += f", 配件: {', '.join(self.accessories)}"
        print(info)


class GameCharacter(Prototype):
    """游戏角色原型"""
   
    def __init__(self, name: str, character_class: str, level: int = 1):
        self.name = name
        self.character_class = character_class
        self.level = level
        self.skills = []
        self.equipment = {}
        self.initialize_character()
   
    def initialize_character(self):
        """初始化角色 - 模拟复杂的数据加载"""
        print(f"正在加载 {self.name} 的角色数据...")
        # 模拟从数据库或配置文件加载数据
        base_skills = {
            "Warrior": ["斩击", "格挡", "冲锋"],
            "Mage": ["火球术", "冰箭术", "传送术"],
            "Archer": ["精准射击", "陷阱布置", "快速移动"]
        }
        self.skills = base_skills.get(self.character_class, [])
   
    def add_skill(self, skill: str):
        """添加技能"""
        self.skills.append(skill)
   
    def equip_item(self, slot: str, item: str):
        """装备物品"""
        self.equipment[slot] = item
   
    def clone(self) -> 'GameCharacter':
        """克隆角色"""
        return copy.deepcopy(self)
   
    def show_status(self):
        """显示角色状态"""
        print(f"角色: {self.name} ({self.character_class}) - 等级: {self.level}")
        print(f"技能: {', '.join(self.skills)}")
        if self.equipment:
            equipment_str = ', '.join([f"{k}: {v}" for k, v in self.equipment.items()])
            print(f"装备: {equipment_str}")

class SmartPrototype(Prototype):
    def __init__(self, data):
        self.data = data
        self.reference_data = []  # 可能需要共享的数据
   
    def clone(self):
        """智能复制：根据需求选择浅复制或深复制"""
        new_obj = copy.copy(self)  # 浅复制主体
        new_obj.reference_data = self.reference_data  # 共享引用数据
        new_obj.data = copy.deepcopy(self.data)  # 深复制重要数据
        return new_obj

class Node(Prototype):
    def __init__(self, value):
        self.value = value
        self.children = []
   
    def add_child(self, child):
        self.children.append(child)
   
    def clone(self):
        """处理可能存在的循环引用"""
        # 使用深复制会自动处理循环引用
        return copy.deepcopy(self)

class PrototypeRegistry:
    """原型注册表 - 管理多个原型"""
   
    def __init__(self):
        self._prototypes = {}
   
    def register_prototype(self, name: str, prototype: Prototype):
        """注册原型"""
        self._prototypes[name] = prototype
   
    def unregister_prototype(self, name: str):
        """取消注册原型"""
        if name in self._prototypes:
            del self._prototypes[name]
   
    def clone_prototype(self, name: str) -> Prototype:
        """根据名称克隆原型"""
        if name not in self._prototypes:
            raise ValueError(f"原型 {name} 未注册")
        return self._prototypes[name].clone()
   
    def list_prototypes(self):
        """列出所有可用的原型"""
        return list(self._prototypes.keys())

# 使用注册表
registry = PrototypeRegistry()
registry.register_prototype("basic_car", CarPrototype("Toyota", "Camry", "白色", "2.5L"))
registry.register_prototype("warrior", GameCharacter("战士", "Warrior"))

# 快速创建对象
new_car = registry.clone_prototype("basic_car")
new_warrior = registry.clone_prototype("warrior")
new_car.display_info()