#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :  cle_circle.py
@Time    :  2020/11/30 21:03:31
@Author  :  Kearney
@Version :  0.0.0
@Contact :  191615342@qq.com
@License :  GPL 3.0
@Desc    :  两精灵的圆形碰撞检测，照片最好是方形且球心处于正中央
            相对像素级碰撞检测来说，圆形碰撞检测速度会快一些
'''
import pygame
import sys

BLACK = (0, 0, 0)


class Block(pygame.sprite.Sprite):
    '''
    color   方块颜色
    position(x, y)  方块初始位置
    image   方块要加载的图片
    radius  球形半径，圆形碰撞检测必备参数
    '''
    def __init__(self, position, image):
        pygame.sprite.Sprite.__init__(self)
        try:
            self.image = pygame.image.load(image)
        except Exception as e:  # 图片文件记载错误
            print("温馨提示： ", e, "， 请正确配置图片文件")
            raise
        self.rect = self.image.get_rect()  # 获取矩形区域
        # 当球直径和图片宽度一致用下面这个，半径为宽度的一半
        # self.radius = 0.5 * self.image.get_size()[0]
        # 不一致的时候用工具量吧。。。GIMP、PS啥的
        self.radius = 13.5
        (self.rect.x, self.rect.y) = position  # 设置初始位置


pygame.init()
screen = pygame.display.set_mode([800, 600])
clock = pygame.time.Clock()

ball = Block((200, 370), "./img/ball.png")  # 创建圆球
player = Block((0, 0), "./img/ball.png")  # 创建不规则球拍

allsp = pygame.sprite.Group()  # 创建存放全部sprite对象的组
allsp.add(ball)  # 往组中添加对象
allsp.add(player)

while True:
    clock.tick(30)  # 设置帧速率为30
    screen.fill(BLACK)  # 全屏填充背景色
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # 退出循环
            sys.exit(0)  # 结束程序

    (player.rect.x, player.rect.y) = pygame.mouse.get_pos()

    if pygame.sprite.collide_circle(player, ball):
        print("发生接触碰撞！！！！！")
    else:
        print("未发生接触碰撞")

    allsp.draw(screen)  # 绘制组中的所有sprite
    pygame.display.update()  # 更新画面
