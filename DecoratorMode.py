import time
import tracemalloc
from functools import wraps

"""
Python 装饰器是一个强大而灵活的工具，它提供了以下优势：

代码复用：将横切关注点（如日志、缓存、验证）从业务逻辑中分离
动态扩展：在不修改原始代码的情况下添加新功能
保持简洁：使用 @ 语法让代码更加清晰易读
符合开闭原则：对扩展开放，对修改关闭
使用装饰器的最佳实践：

使用 functools.wraps 保留函数元信息
保持装饰器的单一职责
合理处理装饰器中的异常
注意装饰器的执行顺序
"""

"""
性能监控装饰器，用于记录函数的执行时间、内存使用情况
"""

def performance_monitor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 开始内存跟踪
        tracemalloc.start()
       
        # 记录开始时间
        start_time = time.time()
       
        # 执行函数
        result = func(*args, **kwargs)
       
        # 记录结束时间
        end_time = time.time()
       
        # 获取内存使用情况
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
       
        print(f"函数 {func.__name__} 性能报告:")
        print(f"执行时间: {end_time - start_time:.4f} 秒")
        print(f"内存使用: 当前 {current/1024:.2f} KB, 峰值 {peak/1024:.2f} KB")
       
        return result
    return wrapper

@performance_monitor
def process_large_data():
    """模拟处理大量数据"""
    data = [i**2 for i in range(100000)]
    return sum(data)

process_large_data()


def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        print(f"函数 {func.__name__} 执行失败，已达到最大重试次数")
                        raise
                    print(f"函数 {func.__name__} 第 {attempts} 次执行失败: {e}")
                    print(f"等待 {delay} 秒后重试...")
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

@retry(max_attempts=3, delay=2)
def unstable_operation():
    """模拟不稳定的操作"""
    import random
    if random.random() < 0.7:  # 70% 的概率失败
        raise ValueError("随机失败")
    return "操作成功"

# 测试重试机制
result = unstable_operation()
print(f"最终结果: {result}")