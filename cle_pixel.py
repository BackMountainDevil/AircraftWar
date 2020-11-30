#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :  cle_pixel.py
@Time    :  2020/11/30 20:47:34
@Author  :  Kearney
@Version :  0.0.0
@Contact :  191615342@qq.com
@License :  GPL 3.0
@Desc    :  两精灵的像素级碰撞检测，多用在不规则对象的碰撞，敌人、飞机、坦克
            图片要有透明的背景
'''
import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


class Block(pygame.sprite.Sprite):
    '''
    color   方块颜色
    position(x, y)  方块初始位置
    image   方块要加载的图片
    '''
    def __init__(self, color, position, image):
        pygame.sprite.Sprite.__init__(self)
        try:
            self.image = pygame.image.load(image)
        except Exception as e:  # 图片文件记载错误
            print("温馨提示： ", e, "， 请正确配置图片文件")
            raise
        self.rect = self.image.get_rect()  # 获取矩形区域
        (self.rect.x, self.rect.y) = position  # 设置初始位置


pygame.init()
screen = pygame.display.set_mode([800, 600])
clock = pygame.time.Clock()

ball = Block(WHITE, (200, 370), "./img/ball.png")  # 创建圆球
player = Block(RED, (0, 0), "./img/pingpongbat.png")  # 创建不规则球拍

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
    # 像素级碰撞检测，试一下rect和mask的区别
    # if pygame.sprite.collide_rect(ball, player):
    if pygame.sprite.collide_mask(ball, player):
        print("发生接触碰撞！！！！！")
    else:
        print("未发生接触碰撞")

    allsp.draw(screen)  # 绘制组中的所有sprite
    pygame.display.update()  # 更新画面
