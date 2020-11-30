#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :  cle_rectg.py
@Time    :  2020/11/30 20:26:35
@Author  :  Kearney
@Version :  0.0.0
@Contact :  191615342@qq.com
@License :  GPL 3.0
@Desc    :  一个精灵和精灵组的矩形碰撞检测
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

enemy = pygame.sprite.Group()  # 创建存放全部敌方对象的组
allsp = pygame.sprite.Group()  # 创建存放全部sprite对象的组

player = Block(RED, 20, 20, (0, 0))  # 创建红块
allsp.add(player)
for i in range(20):  # 创建20个白块，大小为 15×15 px
    block = Block(WHITE, 15, 15, (25 * i, 25 * i))
    enemy.add(block)  # 往组中添加对象
    allsp.add(block)

while True:
    clock.tick(30)  # 设置帧速率为30
    screen.fill(BLACK)  # 全屏填充背景色
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # 退出循环
            sys.exit(0)  # 结束程序
    # 由鼠标位置更新红块位置
    (player.rect.x, player.rect.y) = pygame.mouse.get_pos()
    # 方块矩形碰撞检测，把第三个参数True改成False试一下
    if pygame.sprite.spritecollide(player, enemy, True,
                                   pygame.sprite.collide_rect):
        print("发生接触碰撞！！！！！")
    # else: # 试着去掉这两行注释看看
    # print("未发生接触碰撞")

    allsp.draw(screen)  # 绘制组中的所有sprite
    pygame.display.update()  # 更新画面
