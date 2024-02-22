class MusicPlayer():
    instance = None
    init_flag=False
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)  # 静态方法要传入cls
        return cls.instance
    def __init__(self):
        if self.init_flag: # 如果已经执行过初始化,就直接返回
            return
        print("初始化播放器")
        self.init_flag=True

# 对new方法进行改造,在外面无论调用多少次这个类,得到的第一次创建的对象引用
player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)