class Cat:
    def eat(self):
        print("%s 爱吃鱼" % self.name)
    def drink(self):
        print("%s 爱喝水" % self.name)
tom = Cat()
tom.name="Tom"
tom.eat()
tom.drink()
