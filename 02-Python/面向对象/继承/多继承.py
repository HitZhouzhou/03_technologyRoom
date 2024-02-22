class A:
    def test(self):
        print("test 方法")
class B:
    def demo(self):
        print("demo 方法")

# 多继承让子类可以具有多个父类的属性和方法
class  C(A,B):
    pass
c=C()
c.test()
c.demo()