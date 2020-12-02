#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :  sp_mvg.py
@Time    :  2020/12/02 21:12:19
@Author  :  Kearney
@Version :  0.0.0
@Contact :  191615342@qq.com
@License :  GPL 3.0
@Desc    :  一个精灵的原地动画-超级玛丽-多精灵组图。一张图上有多个精灵的多个形态
    ref：   https://blog.csdn.net/qq_39687901/article/details/88422493#commentBox
'''
import pygame
import sys

BLACK = (0, 0, 0)


class Block(pygame.sprite.Sprite):
    def __init__(self, screen, filename, position):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        try:
            self.image = pygame.image.load(filename)
        except Exception as e:  # 图片文件记载错误
            print("温馨提示： ", e, "， 请正确配置图片文件")
            raise
        self.rect = self.image.get_rect()  # 获取矩形区域
        # (self.rect.x, self.rect.y) = position  # 设置初始位置
        self.position = position

    def update(self):
        # blit参数： 显示的图像，显示图像的位置，要显示图片的那个矩形区域
        # self.screen.blit(self.image, self.position)
        self.screen.blit(self.image, self.position, (0, 0, 95, 60))
        self.screen.blit(self.image, (50, 400), (190, 32, 320, 64))


pygame.init()
screen = pygame.display.set_mode([800, 600])
clock = pygame.time.Clock()

player = Block(screen, './img/mario.png', (50, 200))  # 创建

while True:
    clock.tick(30)  # 设置帧速率为30
    screen.fill(BLACK)  # 全屏填充背景色
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # 退出循环
            sys.exit(0)  # 结束程序

    player.update()
    pygame.display.update()  # 更新画面
