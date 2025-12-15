"""外观模式示例与要点总结。

参考：Python 外观模式 - 菜鸟教程 https://www.runoob.com/python-design-pattern/python-facade.html
外观模式通过提供统一入口，隐藏子系统复杂度，降低耦合。
"""

# 导入时间模块
import time

# 关键要点与优缺点
KEY_POINTS = [
    "为复杂子系统提供一个高层统一接口，简化使用",
    "降低客户端与子系统的耦合度，避免直接依赖多个类",
    "让调用顺序、初始化细节集中在外观类，客户端更易用",
]

PROS = [
    "简化调用，降低学习成本",
    "隔离变化，减少耦合",
    "便于统一做日志、监控等横切处理",
]

CONS = [
    "额外增加一层封装，可能隐藏过多细节",
    "外观类若膨胀，可能成为上帝类，需要拆分子外观",
]

def log_execution(func):
    def wrapper(*args, **kwargs):
        # 打印 函数名 和 参数 开始时间
        print(f"开始执行: {func.__name__}, 参数: {args}, {kwargs}, 开始时间: {time.time()}")
        
        try:
            result = func(*args, **kwargs)
            print(f"成功完成: {func.__name__}, 结束时间: {time.time()}")
            return result
        except Exception as e:
            print(f"执行失败: {func.__name__}, 错误: {e}, 结束时间: {time.time()}")
            raise
    return wrapper

# 子系统类（家庭影院设备）
class Amplifier:
    @log_execution
    def on(self):
        print("功放已开启")
    @log_execution
    def set_volume(self, level: int):
        print(f"音量设置为 {level}")
    @log_execution
    def off(self):
        print("功放已关闭")


class DVDPlayer:
    @log_execution
    def on(self):
        print("DVD播放器已开启")

    @log_execution
    def play(self, movie: str):
        print(f"开始播放电影: {movie}")

    @log_execution
    def stop(self):
        print("DVD播放器已停止")

    @log_execution
    def off(self):
        print("DVD播放器已关闭")


class Projector:
    @log_execution
    def on(self):
        print("投影仪已开启")

    @log_execution
    def set_input(self, source: str):
        print(f"投影仪输入源设置为: {source}")

    @log_execution
    def off(self):
        print("投影仪已关闭")


class Lights:
    @log_execution
    def dim(self, level: int):
        print(f"灯光调暗到 {level}%")

    @log_execution
    def on(self):
        print("灯光全开")


class Screen:
    @log_execution
    def down(self):
        print("屏幕已降下")

    @log_execution
    def up(self):
        print("屏幕已升起")

class CDPlayer:
    @log_execution
    def on(self):
        print("CD播放器已开启")

    @log_execution
    def play(self, music: str):
        print(f"开始播放音乐: {music}")

    @log_execution
    def stop(self):
        print("CD播放器已停止")

    @log_execution
    def off(self):
        print("CD播放器已关闭")

# 外观类
class HomeTheaterFacade:
    """家庭影院外观，封装启动/结束观影的操作顺序。"""

    def __init__(self):
        self.amplifier = Amplifier()
        self.dvd_player = DVDPlayer()
        self.projector = Projector()
        self.lights = Lights()
        self.screen = Screen()
        self.cd_player = CDPlayer()

    def watch_movie(self, movie: str):
        print("\n=== 开始家庭影院模式 ===")
        self.lights.dim(10)
        self.screen.down()
        self.projector.on()
        self.projector.set_input("DVD")
        self.amplifier.on()
        self.amplifier.set_volume(5)
        self.dvd_player.on()
        self.dvd_player.play(movie)
        print("=== 家庭影院准备就绪 ===\n")

    def end_movie(self):
        print("\n=== 结束家庭影院模式 ===")
        self.dvd_player.stop()
        self.dvd_player.off()
        self.amplifier.off()
        self.projector.off()
        self.screen.up()
        self.lights.on()
        print("=== 所有设备已关闭 ===\n")
    
    def listen_to_music(self, music: str):
        print("\n=== 开始听音乐 ===")
 
        self.amplifier.on()
        self.amplifier.set_volume(5)
        self.cd_player.on()
        self.cd_player.play(music)
        print("=== 音乐准备就绪 ===\n")
    
    def end_music(self):
        print("\n=== 结束听音乐 ===")
        self.cd_player.stop()
        self.cd_player.off()
        self.amplifier.off()
        print("=== CD 功放 已关闭 ===\n")


def main():
    # 输出要点与优缺点
    print("外观模式关键要点：")
    for item in KEY_POINTS:
        print(f"- {item}")
    print("\n外观模式优点：")
    for item in PROS:
        print(f"- {item}")
    print("\n外观模式缺点：")
    for item in CONS:
        print(f"- {item}")

    # 演示家庭影院外观
    home_theater = HomeTheaterFacade()
    home_theater.watch_movie("《星际穿越》")
    home_theater.end_movie()

    # 演示听音乐
    home_theater.listen_to_music("《天空之城》")
    home_theater.end_music()


if __name__ == "__main__":
    main()

