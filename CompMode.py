"""组合模式示例：文件系统模拟

参考：Python 组合模式 - 菜鸟教程 https://www.runoob.com/python-design-pattern/python-composite.html
要点：
- 定义统一组件接口（文件/目录一视同仁）
- 叶子节点：文件，提供基础行为
- 组合节点：目录，管理子组件并递归聚合操作
- 客户端无需区分单个对象或组合，统一调用接口
"""

from abc import ABC, abstractmethod
from typing import List, Optional


# 组件接口
class FileSystemComponent(ABC):
    def __init__(self, name: str):
        self.name = name
        self.parent: Optional["Directory"] = None

    @abstractmethod
    def display(self, indent: int = 0) -> None:
        """显示组件信息"""
        raise NotImplementedError

    @abstractmethod
    def get_size(self) -> int:
        """获取大小"""
        raise NotImplementedError

    def get_path(self) -> str:
        """获取完整路径"""
        if self.parent:
            return f"{self.parent.get_path()}/{self.name}"
        return self.name


# 叶子节点：文件
class File(FileSystemComponent):
    def __init__(self, name: str, size: int):
        super().__init__(name)
        self._size = size

    def display(self, indent: int = 0) -> None:
        spaces = " " * indent
        print(f"{spaces}📄 {self.name} ({self._size} bytes)")

    def get_size(self) -> int:
        return self._size


# 组合节点：目录
class Directory(FileSystemComponent):
    def __init__(self, name: str):
        super().__init__(name)
        self._children: List[FileSystemComponent] = []

    def add(self, component: FileSystemComponent) -> None:
        component.parent = self
        self._children.append(component)

    def remove(self, component: FileSystemComponent) -> None:
        self._children.remove(component)
        component.parent = None

    def display(self, indent: int = 0) -> None:
        spaces = " " * indent
        print(f"{spaces}📁 {self.name}/")
        for child in self._children:
            child.display(indent + 2)

    def get_size(self) -> int:
        return sum(child.get_size() for child in self._children)

    def find_component(self, name: str) -> Optional[FileSystemComponent]:
        for child in self._children:
            if child.name == name:
                return child
            if isinstance(child, Directory):
                found = child.find_component(name)
                if found:
                    return found
        return None


def demonstrate_composite_pattern() -> None:
    """构建示例文件系统并演示操作"""
    # 构建目录
    root = Directory("root")
    documents = Directory("documents")
    pictures = Directory("pictures")
    music = Directory("music")
    document1 = Directory("documents1")
    document2 = Directory("documents2")
    document3 = Directory("documents3")

    # 文件
    readme = File("README.txt", 1024)
    notes = File("notes.md", 2048)
    photo1 = File("vacation.jpg", 1_536_000)
    photo2 = File("family.png", 2_048_000)
    song1 = File("song1.mp3", 4_096_000)
    song2 = File("song2.mp3", 5_120_000)
    document4 = File("document4.txt", 1024)

    # 组装树
    root.add(readme)
    root.add(documents)
    root.add(pictures)
    root.add(music)

    documents.add(notes)
    pictures.add(photo1)
    pictures.add(photo2)
    music.add(song1)
    music.add(song2)

    documents.add(document1)
    document1.add(document2)
    document2.add(document3)
    document3.add(document4)


    # 展示
    print("=== 文件系统结构 ===")
    root.display()

    print("\n=== 大小统计 ===")
    print(f"根目录总大小: {root.get_size()} bytes")
    print(f"图片目录大小: {pictures.get_size()} bytes")
    print(f"音乐目录大小: {music.get_size()} bytes")

    print("\n=== 路径示例 ===")
    print(f"photo2 路径: {photo2.get_path()}")


def main() -> None:
    demonstrate_composite_pattern()


if __name__ == "__main__":
    main()

