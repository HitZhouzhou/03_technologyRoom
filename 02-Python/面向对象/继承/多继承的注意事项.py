class A:
    def test(self):
        print("A---test 方法")
    def demo(self):
        print("A---demo 方法")

class B:
    def demo(self):
        print("B---demo 方法")
    def test(self):
        print("B---test 方法")
# 多继承让子类可以具有多个父类的属性和方法
class  C(B,A):
    pass
c=C()
c.test()
c.demo()

#MRO
print(C.__mro__)
"""(<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
"""