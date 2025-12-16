"""组合模式示例：公司组织结构系统

实现一个公司组织结构系统，使用组合模式：
- 员工（叶子节点）：有年龄、工资属性
- 部门（组合节点）：可以包含员工或子部门
- 统计功能：总人数、总薪资、总部门数（递归）
- 当前层级统计：当前层级下总人数、总薪资、总部门数（不递归）
"""

from abc import ABC, abstractmethod
from typing import List, Optional


class OrganizationComponent(ABC):
    """组织组件抽象基类
    
    定义员工和部门的统一接口，使得可以统一处理单个员工和部门组合
    """
    
    def __init__(self, name: str):
        """
        Args:
            name: 组件名称（员工姓名或部门名称）
        """
        self.name = name
        self.parent: Optional["Department"] = None
    
    @abstractmethod
    def get_total_employees(self) -> int:
        """获取总人数（递归统计所有子级）
        
        Returns:
            总人数
        """
        raise NotImplementedError
    
    @abstractmethod
    def get_total_salary(self) -> float:
        """获取总薪资（递归统计所有子级）
        
        Returns:
            总薪资
        """
        raise NotImplementedError
    
    @abstractmethod
    def get_total_departments(self) -> int:
        """获取总部门数（递归统计所有子级）
        
        Returns:
            总部门数
        """
        raise NotImplementedError
    
    @abstractmethod
    def get_current_level_employees(self) -> int:
        """获取当前层级总人数（不递归，只统计直接下属）
        
        Returns:
            当前层级总人数
        """
        raise NotImplementedError
    
    @abstractmethod
    def get_current_level_salary(self) -> float:
        """获取当前层级总薪资（不递归，只统计直接下属）
        
        Returns:
            当前层级总薪资
        """
        raise NotImplementedError
    
    @abstractmethod
    def get_current_level_departments(self) -> int:
        """获取当前层级总部门数（不递归，只统计直接下属）
        
        Returns:
            当前层级总部门数
        """
        raise NotImplementedError
    
    @abstractmethod
    def display(self, indent: int = 0) -> None:
        """显示组件信息
        
        Args:
            indent: 缩进级别，用于树形结构显示
        """
        raise NotImplementedError


class Employee(OrganizationComponent):
    """员工类（叶子节点）
    
    代表公司中的单个员工，包含年龄和工资属性
    """
    
    def __init__(self, name: str, age: int, salary: float):
        """
        Args:
            name: 员工姓名
            age: 员工年龄
            salary: 员工工资
        """
        super().__init__(name)
        self.age = age
        self.salary = salary
    
    def get_total_employees(self) -> int:
        """获取总人数（员工本身算1人）
        
        Returns:
            1
        """
        return 1
    
    def get_total_salary(self) -> float:
        """获取总薪资（员工本身的薪资）
        
        Returns:
            员工薪资
        """
        return self.salary
    
    def get_total_departments(self) -> int:
        """获取总部门数（员工不是部门，返回0）
        
        Returns:
            0
        """
        return 0
    
    def get_current_level_employees(self) -> int:
        """获取当前层级总人数（员工本身算1人）
        
        Returns:
            1
        """
        return 1
    
    def get_current_level_salary(self) -> float:
        """获取当前层级总薪资（员工本身的薪资）
        
        Returns:
            员工薪资
        """
        return self.salary
    
    def get_current_level_departments(self) -> int:
        """获取当前层级总部门数（员工不是部门，返回0）
        
        Returns:
            0
        """
        return 0
    
    def display(self, indent: int = 0) -> None:
        """显示员工信息
        
        Args:
            indent: 缩进级别
        """
        spaces = " " * indent
        print(f"{spaces}👤 {self.name} (年龄: {self.age}, 薪资: {self.salary:.2f})")


class Department(OrganizationComponent):
    """部门类（组合节点）
    
    代表公司中的部门，可以包含员工或子部门
    """
    
    def __init__(self, name: str):
        """
        Args:
            name: 部门名称
        """
        super().__init__(name)
        self._children: List[OrganizationComponent] = []
    
    def add(self, component: OrganizationComponent) -> None:
        """添加子组件（员工或子部门）
        
        Args:
            component: 要添加的组织组件
        """
        component.parent = self
        self._children.append(component)
    
    def remove(self, component: OrganizationComponent) -> None:
        """移除子组件
        
        Args:
            component: 要移除的组织组件
        """
        if component in self._children:
            self._children.remove(component)
            component.parent = None
        else:
            print(f"组件 '{component.name}' 不在部门 '{self.name}' 中")
    
    def get_total_employees(self) -> int:
        """获取总人数（递归统计所有子级）
        
        Returns:
            总人数
        """
        return sum(child.get_total_employees() for child in self._children)
    
    def get_total_salary(self) -> float:
        """获取总薪资（递归统计所有子级）
        
        Returns:
            总薪资
        """
        return sum(child.get_total_salary() for child in self._children)
    
    def get_total_departments(self) -> int:
        """获取总部门数（递归统计所有子级）
        
        部门本身不算在内，只统计子部门
        
        Returns:
            总部门数
        """
        # 统计所有子组件中的部门数，加上子组件中如果是部门则再加1
        total = sum(child.get_total_departments() for child in self._children)
        # 加上直接子部门数量
        total += sum(1 for child in self._children if isinstance(child, Department))
        return total
    
    def get_current_level_employees(self) -> int:
        """获取当前层级总人数（不递归，只统计直接下属）
        
        Returns:
            当前层级总人数
        """
        return sum(child.get_current_level_employees() for child in self._children)
    
    def get_current_level_salary(self) -> float:
        """获取当前层级总薪资（不递归，只统计直接下属）
        
        Returns:
            当前层级总薪资
        """
        return sum(child.get_current_level_salary() for child in self._children)
    
    def get_current_level_departments(self) -> int:
        """获取当前层级总部门数（不递归，只统计直接下属）
        
        Returns:
            当前层级总部门数
        """
        return sum(1 for child in self._children if isinstance(child, Department))
    
    def display(self, indent: int = 0) -> None:
        """显示部门信息及其子组件
        
        Args:
            indent: 缩进级别
        """
        spaces = " " * indent
        print(f"{spaces}🏢 {self.name} (总人数: {self.get_total_employees()}, "
              f"总薪资: {self.get_total_salary():.2f}, "
              f"总部门数: {self.get_total_departments()})")
        for child in self._children:
            child.display(indent + 2)


def demonstrate_organization_system() -> None:
    """演示公司组织结构系统"""
    
    # 创建公司
    company = Department("科技有限公司")
    
    # 创建一级部门
    tech_dept = Department("技术部")
    hr_dept = Department("人力资源部")
    finance_dept = Department("财务部")
    
    # 创建技术部的子部门
    backend_dept = Department("后端开发组")
    frontend_dept = Department("前端开发组")
    devops_dept = Department("运维组")
    
    # 创建员工
    # 技术部员工
    emp1 = Employee("张三", 28, 15000.0)
    emp2 = Employee("李四", 32, 18000.0)
    
    # 后端开发组员工
    emp3 = Employee("王五", 26, 12000.0)
    emp4 = Employee("赵六", 30, 16000.0)
    emp5 = Employee("钱七", 29, 14000.0)
    
    # 前端开发组员工
    emp6 = Employee("孙八", 25, 11000.0)
    emp7 = Employee("周九", 27, 13000.0)
    
    # 运维组员工
    emp8 = Employee("吴十", 31, 17000.0)
    
    # 人力资源部员工
    emp9 = Employee("郑一", 28, 10000.0)
    emp10 = Employee("王二", 30, 12000.0)
    
    # 财务部员工
    emp11 = Employee("李三", 35, 14000.0)
    emp12 = Employee("张四", 32, 15000.0)
    
    # 组装组织结构
    # 公司 -> 一级部门
    company.add(tech_dept)
    company.add(hr_dept)
    company.add(finance_dept)
    
    # 技术部 -> 子部门和员工
    tech_dept.add(emp1)
    tech_dept.add(emp2)
    tech_dept.add(backend_dept)
    tech_dept.add(frontend_dept)
    tech_dept.add(devops_dept)
    
    # 后端开发组 -> 员工
    backend_dept.add(emp3)
    backend_dept.add(emp4)
    backend_dept.add(emp5)
    
    # 前端开发组 -> 员工
    frontend_dept.add(emp6)
    frontend_dept.add(emp7)
    
    # 运维组 -> 员工
    devops_dept.add(emp8)
    
    # 人力资源部 -> 员工
    hr_dept.add(emp9)
    hr_dept.add(emp10)
    
    # 财务部 -> 员工
    finance_dept.add(emp11)
    finance_dept.add(emp12)
    
    # 显示组织结构
    print("=" * 60)
    print("公司组织结构")
    print("=" * 60)
    company.display()
    
    # 统计信息
    print("\n" + "=" * 60)
    print("统计信息（递归统计）")
    print("=" * 60)
    print(f"公司总人数: {company.get_total_employees()}")
    print(f"公司总薪资: {company.get_total_salary():.2f}")
    print(f"公司总部门数: {company.get_total_departments()}")
    
    print("\n" + "-" * 60)
    print("技术部统计（递归统计）")
    print("-" * 60)
    print(f"技术部总人数: {tech_dept.get_total_employees()}")
    print(f"技术部总薪资: {tech_dept.get_total_salary():.2f}")
    print(f"技术部总部门数: {tech_dept.get_total_departments()}")
    
    print("\n" + "-" * 60)
    print("后端开发组统计（递归统计）")
    print("-" * 60)
    print(f"后端开发组总人数: {backend_dept.get_total_employees()}")
    print(f"后端开发组总薪资: {backend_dept.get_total_salary():.2f}")
    print(f"后端开发组总部门数: {backend_dept.get_total_departments()}")
    
    # 当前层级统计
    print("\n" + "=" * 60)
    print("当前层级统计（不递归，只统计直接下属）")
    print("=" * 60)
    print(f"公司当前层级人数: {company.get_current_level_employees()}")
    print(f"公司当前层级薪资: {company.get_current_level_salary():.2f}")
    print(f"公司当前层级部门数: {company.get_current_level_departments()}")
    
    print("\n" + "-" * 60)
    print("技术部当前层级统计")
    print("-" * 60)
    print(f"技术部当前层级人数: {tech_dept.get_current_level_employees()}")
    print(f"技术部当前层级薪资: {tech_dept.get_current_level_salary():.2f}")
    print(f"技术部当前层级部门数: {tech_dept.get_current_level_departments()}")
    
    print("\n" + "-" * 60)
    print("后端开发组当前层级统计")
    print("-" * 60)
    print(f"后端开发组当前层级人数: {backend_dept.get_current_level_employees()}")
    print(f"后端开发组当前层级薪资: {backend_dept.get_current_level_salary():.2f}")
    print(f"后端开发组当前层级部门数: {backend_dept.get_current_level_departments()}")


def main() -> None:
    """主函数"""
    demonstrate_organization_system()


if __name__ == "__main__":
    main()

