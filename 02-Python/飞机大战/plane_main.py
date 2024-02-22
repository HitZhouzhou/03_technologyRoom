import time

import pygame

# 初始化字体
pygame.font.init()
font = pygame.font.Font(None, 36)

start_time = time.time()
from plane_sprites import *


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化")
        # 1.创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2.创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3.调用私有方法,精灵和精灵组的创建
        self.__create_sprites()
        # 4.设置定时器事件 -创建敌机-1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 500)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprites(self):
        # 1.创建背景精灵和精灵组
        bg1 = BackGround()
        bg2 = BackGround(True)

        self.back_group = pygame.sprite.Group(bg1, bg2)
        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄的精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

        # clock = pygame.time.Clock()

    def start_game(self):
        print("游戏开始...")

        while True:
            # 1.设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 2.事件监听
            self.__event_handler()
            # 3.碰撞检测
            self.__check_collide()
            # 4.更新/绘制精灵组
            self.__update_sprites()
            # 更新显示
            pygame.display.update()
            # 显示时间

            # 更新显示
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            elif event.type == CREATE_ENEMY_EVENT:
                # print("敌机出场...")

                # 创建敌机精灵
                enemy = Enemy()
                self.enemy_group.add(enemy)

        # 使用键盘提供的方法来接收按键
        keys_pressed = pygame.key.get_pressed()
        # 判断元组对应的索引
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 3
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -3
        elif keys_pressed[pygame.K_DOWN]:
            self.hero.speedy = 3
        elif keys_pressed[pygame.K_UP]:
            self.hero.speedy = -3

        else:
            self.hero.speed = 0
            self.hero.speedy = 0

    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        # 敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        # 判断列表是否有内容:
        if len(enemies) > 0:
            # 让英雄牺牲
            self.hero.kill()
            # 结束游戏
            PlaneGame.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

        # 在窗口上显示计时器
        elapsed_time = int(time.time()  - start_time)
        timer_text = font.render(str(elapsed_time), True, (255, 255, 255))
        self.screen.blit(timer_text, (10, 10))

    @staticmethod
    def __game_over():
        print("游戏结束...")
        pygame.quit()
        exit()

if __name__ == '__main__':
    # 在主程序中希望执行的代码
    # 创建游戏对象
    game = PlaneGame()

    game.start_game()
