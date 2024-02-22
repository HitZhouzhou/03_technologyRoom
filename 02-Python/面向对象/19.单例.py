class MusicPlayer():
    instance=None
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance=super().__new__(cls) #静态方法要传入cls
        return cls.instance


# 对new方法进行改造,在外面无论调用多少次这个类,得到的第一次创建的对象引用
player1 = MusicPlayer()
print(player1)

player2= MusicPlayer()
print(player2)