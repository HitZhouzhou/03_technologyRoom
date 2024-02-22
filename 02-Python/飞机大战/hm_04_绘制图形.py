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

time.sleep()
pygame.quit()