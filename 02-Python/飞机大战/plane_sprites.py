import random
import pygame

# 定义一个屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)

# 刷新帧率常量:
FRAME_PER_SEC = 100
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT

# 英雄发射子弹事件
HERO_FIRE_EVENT=pygame.USEREVENT+1
# sprite是模块名称,Sprite是类名称
class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):
        # 调用父类的初始化方法,才能享用到父类中已经封装好的代码
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        # self.rect.x = 50
        self.speed = speed

    def update(self):
        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed


class BackGround(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):
        # 1.调用父类方法实现精灵的创建
        super().__init__("G:\\pythonlearning\\飞机大战\\images\\background.png")
        # 2.判断是否为交替图像
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 1.调用父类的方法实现
        super().update()
        # 2.判断是否移出屏幕
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        # 1.调用父类方法,创建敌机精灵,同时指定敌机图片
        super().__init__("G:\\pythonlearning\\飞机大战\\images\\enemy1.png")
        # 2.指定敌机速度 1~3
        self.speed = random.randint(2, 3)

        # 3.指定位置
        self.rect.bottom = 0
        max_x=SCREEN_RECT.width-self.rect.width
        self.rect.x=random.randint(0,max_x)

    def update(self):
        # 1.垂直
        super().update()
        # 2.判断是否飞出
        if self.rect.y >= SCREEN_RECT.height:
            # print("飞出屏幕,从精灵组中删除...")
            # kill方法可以将精灵从精灵组中移出,精灵会自动销毁
            self.kill()
    def __del__(self):
        # print("敌机挂了 %s"% self.rect)
        pass

# 读取猪猪图像,并调整大小
# 读入图像，并获取其尺寸
pig = pygame.image.load("images\\pigpig.jpg")
image_width, image_height = pig.get_size()

# 调整图像大小
pig = pygame.transform.scale(pig, (102, 126))

class Hero(GameSprite):
    def __init__(self):
        # 1.调用父类,设置image&speed
        super().__init__("images\\缩小ye.png",0)
        # 2.设置英雄的初始位置
        # centerx可以指定中间位置
        self.rect.centerx=SCREEN_RECT.centerx
        self.rect.bottom=SCREEN_RECT.bottom-120
        self.speedy=0

        # 3.创建子弹的精灵组
        self.bullets=pygame.sprite.Group()


    def update(self):
        # 英雄在水平方向移动
        self.rect.x+=self.speed
        self.rect.y+=self.speedy

        # 控制英雄不能离开屏幕
        if self.rect.x<-10:
            self.rect.x=-10
        elif self.rect.right>SCREEN_RECT.right+10:
            self.rect.right=SCREEN_RECT.right+10

    def fire(self):
        for i in(0,1,2,3,4,5):
            # 1.创建子弹精灵
            bullet=Bullet()
            # 2.设置精灵的位置
            bullet.rect.bottom=self.rect.y-i*20
            bullet.rect.centerx=self.rect.centerx
            # 3.将精灵添加到精灵组
            self.bullets.add(bullet)




# 子弹类
class Bullet(GameSprite):
    """子弹精灵"""
    def __init__(self):
        super().__init__("images\\bullet1.png",-5)

    def update(self):
        super().update()
        # 判断子弹是否飞出屏幕
        if self.rect.bottom<0:
            self.kill()
    def __del__(self):
       # print("子弹被销毁...")
        pass



