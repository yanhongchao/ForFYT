##############################################################
# 单例模式是一种设计模式,用于确保一个类只有一个实例,并提供一个全局访问点
# 单例模式有以下特点:
# 1. 单例类只能有一个实例
# 2. 单例类必须自己创建自己的唯一实例
# 3. 单例类必须给所有其他对象提供这一实例
# 单例模式有以下应用场景:
# 1. 数据库连接
# 2. 日志记录
# 3. 配置管理
# 4. 线程池
# 5. 缓存
# 6. 对话框
# 7. 打印机
##############################################################







########################################################
# 使用装饰器实现单例模式
def singleton(cls):
    """单例装饰器"""
    instances = {}
   
    def get_instance(*args, **kwargs):
        # 如果该类还没有实例，则创建新实例
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
            print(f"创建 {cls.__name__} 的新实例")
        else:
            print(f"返回已存在的 {cls.__name__} 实例")
        return instances[cls]
   
    return get_instance

@singleton
class ConfigurationManager:
    
    #__init__方法会在实例化时被调用,用于初始化实例, 由于是单例模式,所以__init__方法只会被调用一次
    def __init__(self, name):
        print(f"初始化实例，名称: {name}")
        self.settings = {}
        self.load_default_settings()
        self.name = name
   
    def load_default_settings(self):
        self.settings = {
            "app_name": "我的应用",
            "version": "1.0.0",
            "debug_mode": True,
            "language": "zh-CN"
        }
   
    def get_setting(self, key):
        return self.settings.get(key)
   
    def set_setting(self, key, value):
        self.settings[key] = value

# 测试代码
print("\n=== 测试装饰器单例 ===")
config1 = ConfigurationManager("config1")
config1.set_setting("theme", "bulue")
print(f"config1 主题: {config1.get_setting('theme')}")
config2 = ConfigurationManager("config2")

print(f"config1 name: {config1.name}, 主题: {config1.get_setting('theme')}")
print(f"config2 name: {config2.name}, 主题: {config2.get_setting('theme')}")  # 两个实例共享同一配置


########################################################
# 使用__new__方法实现单例模式
class Singleton:
    _instance = None
   
    def __new__(cls, *args, **kwargs):
        # 如果实例不存在，则创建新实例
        if not cls._instance:
            cls._instance = super().__new__(cls)
            print("创建新的单例实例")
        else:
            print("返回已存在的单例实例")
        return cls._instance
   
    def __init__(self, name):
        # 注意：__init__ 每次都会被调用
        self.name = name
        print(f"初始化实例，名称: {name}")

# 测试代码
print("=== 测试单例模式 ===")
s1 = Singleton("第一个实例")
s2 = Singleton("第二个实例")

print(f"s1 的 ID: {id(s1)}")
print(f"s2 的 ID: {id(s2)}")
print(f"s1 和 s2 是同一个对象吗？ {s1 is s2}")
print(f"s1 名称: {s1.name}")
print(f"s2 名称: {s2.name}")  # 注意：这里会显示"第二个实例"


########################################################
# 使用元类实现单例模式
class SingletonMeta(type):
    """单例元类"""
    _instances = {}
   
    def __call__(cls, *args, **kwargs):
        # 如果该类还没有实例，则创建新实例
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
            print(f"元类：创建 {cls.__name__} 的新实例")
        else:
            print(f"元类：返回已存在的 {cls.__name__} 实例")
        return cls._instances[cls]

class Logger(metaclass=SingletonMeta):
    def __init__(self, log_file="app.log"):
        self.log_file = log_file
        self.logs = []
        print(f"日志器初始化，文件: {log_file}")
   
    def log(self, message):
        log_entry = f"[{self.get_timestamp()}] {message}"
        self.logs.append(log_entry)
        print(f"记录日志: {log_entry}")
        return log_entry
   
    def get_timestamp(self):
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   
    def get_logs(self):
        return self.logs.copy()

# 测试代码
print("\n=== 测试元类单例 ===")
logger1 = Logger("application.log")
logger2 = Logger("different.log")  # 这个文件名会被忽略

logger1.log("系统启动")
logger2.log("用户登录")

print(f"logger1 日志数量: {len(logger1.get_logs())}")
print(f"logger2 日志数量: {len(logger2.get_logs())}")
print(f"是同一个日志器吗？ {logger1 is logger2}")