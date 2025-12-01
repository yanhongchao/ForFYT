class DatabaseConnection:
    _instance = None
   
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("创建新的数据库连接")
        return cls._instance
   
    def connect(self):
        print("连接到数据库")

# 使用示例
db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(f"db1 和 db2 是同一个实例吗？{db1 is db2}")  # 输出：True
