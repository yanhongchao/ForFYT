"""
基础策略接口
定义所有策略的通用接口
"""

from abc import ABC, abstractmethod


class BaseStrategy(ABC):
    """基础策略接口"""
    
    @abstractmethod
    def execute(self) -> bool:
        """执行策略"""
        pass

