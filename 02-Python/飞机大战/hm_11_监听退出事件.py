import time
import pygame

# 游戏初始化
pygame.init()

# 创建游戏的窗口 480*700
screen = pygame.display.set_mode((480, 700))

# 1.加载图像数据
bg = pygame.image.load("images\\background.png")
# 2.blit绘制图像
screen.blit(bg, (0, 0))
# 3.update 更新图像显示
# pygame.display.update()

# 绘制英雄的飞机
hero = pygame.image.load("images\\me1.png")
screen.blit(hero, (150, 500))
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()
# 1.定义rect记录飞机的位置
hero_rect = pygame.Rect(150, 300, 102, 126)

while True:
    clock.tick(60)  # 可以指定游戏循环内部代码的执行频率
    # 捕获事件(捕获用户的操作,从而做出响应)

    # 监听事件
    for event in pygame.event.get():
        # 判断是否为退出事件
        if event.type== pygame.QUIT:
            print("游戏退出...")
            #quit 卸载所有模块
            pygame.quit()
            # exit() 直接终止正在执行的程序
            exit()
    hero_rect.y -= 2

    screen.blit(bg, (0, 0))

    screen.blit(hero, hero_rect)
    if hero_rect.y <= -126:
        hero_rect.y = 700
    pygame.display.update()

pygame.quit()