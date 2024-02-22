class Person:
    def __init__(self,name,weight):
        self.name=name
        self.weight=weight
    def __str__(self):
        return "我的名字是 %s 体重是 %.2f 公斤" % (self.name,self.weight)
    def run(self):
        print("%s 爱跑步"% self.name)
        self.weight-=0.5
    def eat(self):
        print("%s 吃东西" % self.name)
        self.weight+=1
xiaoming=Person("小明",75.0)
xiaoming.run()
xiaoming.eat()
xm=Person("小美",45)
xm.eat()
i=0
while i<5:

    xm.run()
    i+=1

print(xm)
print(xiaoming)