class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def test(self):
        print("父类的公有方法")


class B(A):
    """def demo(self):
        print("访问父类的私有属性: %d"%self.__num2)"""
    def demo(self):
        print("子类方法: %d "% self.num1)
        self.test()


# 子类不能访问父类的私有属性和方法
b=B()
print(b)
print(b.num1)
b.demo()