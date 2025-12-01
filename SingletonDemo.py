class AppConfig:
    _instance = None
   #使用__new__方法实现单例模式
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    #使用__new__方法实现单例模式，__init__方法会在实例化时被调用,需要防止被重复初始化
    def __init__(self):
        # 防止重复初始化
        if not self._initialized:
            self.config_data = {}
            self.load_config()
            self._initialized = True
   
    def load_config(self):
        """模拟从配置文件加载配置"""
        self.config_data = {
            "database": {
                "host": "localhost",
                "port": 5432,
                "name": "myapp_db"
            },
            "server": {
                "host": "0.0.0.0",
                "port": 8000
            },
            "features": {
                "cache_enabled": True,
                "debug_mode": False
            }
        }
        print("配置加载完成")
   
    def get(self, key_path, default=None):
        """通过路径获取配置值，如 'database.host'"""
        keys = key_path.split('.')
        value = self.config_data
       
        try:
            for key in keys:
                value = value[key]
            return value
        except (KeyError, TypeError):
            return default
   
    def set(self, key_path, value):
        """设置配置值"""
        keys = key_path.split('.')
        config = self.config_data
       
        # 遍历到最后一个键的前一个
        for key in keys[:-1]:
            if key not in config:
                config[key] = {}
            config = config[key]
       
        # 设置最终的值
        config[keys[-1]] = value
        print(f"配置已更新: {key_path} = {value}")

# 使用示例
def demonstrate_config_usage():
    print("\n=== 配置管理器使用演示 ===")
   
    # 在不同地方获取配置管理器实例
    config1 = AppConfig()
    config2 = AppConfig()
   
    print(f"是同一个配置管理器吗？ {config1 is config2}")
   
    # 读取配置
    db_host = config1.get("database.host")
    server_port = config1.get("server.port")
    print(f"数据库主机: {db_host}")
    print(f"服务器端口: {server_port}")
   
    # 更新配置
    config2.set("database.host", "192.168.1.100")
    config2.set("features.debug_mode", True)
   
    # 验证配置同步
    print(f"config1 数据库主机: {config1.get('database.host')}")
    print(f"config1 调试模式: {config1.get('features.debug_mode')}")

# 运行演示
demonstrate_config_usage()