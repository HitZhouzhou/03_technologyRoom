class Gun:
    def __init__(self,model):
        # 1.枪的型号
        self.model=model
        # 2.子弹数量
        self.bullet_count=0
    def add_bullet(self,count):
        self.bullet_count+=count
    def shoot(self):
        # 1 .判断子弹数量
        if self.bullet_count<=0:
            print("[%s] 没有子弹了" % self.model)
            return
        # 2.发射子弹
        self.bullet_count-=1
        print("[%s] 突突突...[%d]"% (self.model,self.bullet_count))

class Soldier:
    def __init__(self,name):
        # 1.姓名:
        self.name=name
        # 2.枪:
        self.gun=None
ak47=Gun("Ak47")
ak47.add_bullet(50)
ak47.shoot()
xusanduo=Soldier("许三多")
xusanduo.gun=ak47
print(xusanduo.gun)



