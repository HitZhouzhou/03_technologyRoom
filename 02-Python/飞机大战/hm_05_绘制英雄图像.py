import time

import pygame

pygame.init()

# 创建游戏的窗口 480*700
screen=pygame.display.set_mode((480,700))

# 1.加载图像数据
bg=pygame.image.load("images\\background.png")
# 2.blit绘制图像
screen.blit(bg,(0,0))
# 3.update 更新图像显示
pygame.display.update()

# 绘制英雄的飞机
hero = pygame.image.load("images\\me1.png")
screen.blit(hero,(150,500))
pygame.display.update()

time.sleep(10)
pygame.quit()