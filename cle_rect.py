#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :  cle_rect.py
@Time    :  2020/11/30 17:40:14
@Author  :  Kearney
@Version :  0.0.0
@Contact :  191615342@qq.com
@License :  GPL 3.0
@Desc    :  矩形方块碰撞检测
'''

import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


class Block(pygame.sprite.Sprite):
    '''
    color   方块颜色
    width   方块宽度
    heigth  方块高度
    position(x, y)  方块初始位置
    '''
    def __init__(self, color, width, height, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])  # 创建一个对应大小的矩形作为img
        self.image.fill(color)  # 往img里填充颜色
        self.rect = self.image.get_rect()  # 获取矩形区域
        (self.rect.x, self.rect.y) = position  # 设置初始位置


pygame.init()
screen = pygame.display.set_mode([800, 600])
clock = pygame.time.Clock()

block = Block(WHITE, 20, 15, (200, 370))  # 创建白块，大小为 20×15 px

player = Block(RED, 80, 15, (0, 0))  # 创建红块

allsp = pygame.sprite.Group()  # 创建存放全部sprite对象的组
allsp.add(block)  # 往组中添加对象
allsp.add(player)

while True:
    clock.tick(30)  # 设置帧速率为30
    screen.fill(BLACK)  # 全屏填充背景色
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # 退出循环
            sys.exit(0)  # 结束程序
    # 由鼠标位置更新红块位置
    (player.rect.x, player.rect.y) = pygame.mouse.get_pos()
    # 方块矩形碰撞检测
    if pygame.sprite.collide_rect(block, player):
        print("发生接触碰撞！！！！！")
    else:
        print("未发生接触碰撞")

    allsp.draw(screen)  # 绘制组中的所有sprite
    pygame.display.update()  # 更新画面
