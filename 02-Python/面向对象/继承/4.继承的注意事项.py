class Animal:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")
    def run(self):
        print("跑")
    def sleep(self):
        print("睡")


class Dog(Animal): # 子类拥有父类的所有属性

    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):
    def fly(self):
        print("我会飞")
    def bark(self):
        # 1.针对子类特有
        print("神狗")
        # 2.使用super().
        super().bark()
        # XiaoTianQuan.bark(self)
        print("%$%#$%#%")


class Cat(Animal):
    def catch(self):
        print("抓老鼠")

xtq=XiaoTianQuan()

xtq.bark()
# 子类中重写了父类的方法,调用会调用子类中的方法实现
