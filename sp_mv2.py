#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :  sp_mv2.py
@Time    :  2020/12/01 14:29:31
@Author  :  Kearney
@Version :  0.0.0
@Contact :  191615342@qq.com
@License :  GPL 3.0
@Desc    :  一个精灵的原地动画-原地炸机-分立图片
    ref:    https://linux.cn/article-10858-1.html
            https://linux.cn/article-10874-1.html
'''
import pygame
import sys
import os

RED = (255, 0, 0)
FPS = 30  # 帧速率


class Block(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.last_time = 0
        self.frame = 4
        self.current_frame = 0  # 当前帧
        for i in range(1, 5):
            img = pygame.image.load(
                os.path.join('img', 'enemy0_down' + str(i)) + '.png')
            self.images.append(img)
        self.image = self.images[self.current_frame]
        self.rect = self.image.get_rect()

    def update(self, current_time, rate=300):
        if current_time > self.last_time + rate:  # 时辰已到，切换下一帧
            self.last_time = current_time
            if self.current_frame < (self.frame - 1):  # 是不是最后一帧
                self.current_frame = self.current_frame + 1
            else:
                self.current_frame = 0  # 从头开始
            self.image = self.images[self.current_frame]


pygame.init()
screen = pygame.display.set_mode([800, 600])
clock = pygame.time.Clock()

player = Block()  # 创建sprite对象
(player.rect.x, player.rect.y) = (100, 200)  # 设置飞机位置
allsp = pygame.sprite.Group()  # 创建存放全部sprite对象的组
allsp.add(player)  # 往组中添加对象

while True:
    clock.tick(FPS)  # 设置帧速率
    screen.fill(RED)  # 全屏填充背景色，红白对比
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # 退出循环
            sys.exit(0)  # 结束程序

    current_ticks = pygame.time.get_ticks()
    player.update(current_ticks)
    allsp.draw(screen)  # 绘制组中的所有sprite
    pygame.display.update()  # 更新画面
