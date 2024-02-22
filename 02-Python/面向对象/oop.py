class Cat:
    def eat(self):
        print("小猫爱吃鱼")
    def drink(self):
        print("小猫爱喝水")
tom=Cat()
tom.eat()
tom.drink()
print(tom)#打印出tom的地址



# 再创建一个猫对象
lazy_cat=Cat()
lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)