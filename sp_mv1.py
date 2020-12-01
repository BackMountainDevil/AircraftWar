#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :  sp_mv1.py
@Time    :  2020/12/01 08:56:46
@Author  :  Kearney
@Version :  0.0.0
@Contact :  191615342@qq.com
@License :  GPL 3.0
@Desc    :  一个精灵的原地动画-原地奔跑的猫1。如：爆炸、原地跑动、逐渐蹲下
    ref:    https://www.cnblogs.com/msxh/p/5013555.html
    Q&A:    咋调整猫片的位置哦？？？
'''
import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
FPS = 30  # 帧速率


class Block(pygame.sprite.Sprite):
    def __init__(self, target):
        pygame.sprite.Sprite.__init__(self)
        self.target_surface = target
        self.image = None
        self.rect = None
        self.topleft = 0, 0
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.last_time = 0

    ''' 加载图片。参数：文件名，一帧的宽度、高度，列数'''

    def load(self, filename, width, height, columns):
        self.imag = pygame.image.load(filename)
        self.frame_width = width
        self.frame_height = height
        self.rect = 0, 0, width, height
        self.columns = columns
        rect = self.imag.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) - 1

    # 更新帧。参数：当前tick数，帧数率
    def update(self, current_time, rate=60):
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time
        if self.frame != self.old_frame:
            # 用帧数目除以行数，然后在乘上帧的高度
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = (frame_x, frame_y, self.frame_width, self.frame_height)
            self.image = self.imag.subsurface(rect)
            self.old_frame = self.frame


pygame.init()
screen = pygame.display.set_mode([800, 600])
clock = pygame.time.Clock()

player = Block(screen)  # 创建sprite对象
player.load("./img/runcat.png", 100, 100, 4)  # 设置精灵图参数
allsp = pygame.sprite.Group()  # 创建存放全部sprite对象的组
allsp.add(player)  # 往组中添加对象

while True:
    clock.tick(FPS)  # 设置帧速率
    ticks = pygame.time.get_ticks()
    screen.fill(BLACK)  # 全屏填充背景色
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # 退出循环
            sys.exit(0)  # 结束程序

    allsp.update(ticks, FPS)
    allsp.draw(screen)  # 绘制组中的所有sprite
    pygame.display.update()  # 更新画面
