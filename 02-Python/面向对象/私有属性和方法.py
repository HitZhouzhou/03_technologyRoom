class Woman:
    def __init__(self,name):
        self.name=name
        self.__age=18
    def __secret(self):
        print("%s 的年龄是 %d "%(self.name,self.__age))
xiaofang=Woman("小芳")
# 私有属性在外部不能被直接访问,私有方法也不能
print(xiaofang)
