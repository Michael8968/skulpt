#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
import easygui as g
import sys
name=g.enterbox(msg='你好，你叫什么名字?',title='quiz',default='')
g.buttonbox(msg=name+' ,你觉得自己聪明吗？',title='quiz',choices=('当然呢！','必须啊！','我最聪明！'))
g.buttonbox(msg='既然你觉得自己很聪明，那么我来考考你！',title='quiz',choices=('好的！','放马过来！'))
answer1=g.buttonbox(msg='下面这幅图里是什么动物？',image='lesson1/cat.png',title='quiz',choices=('兔子','狗'))
while answer1!='猫':
    g.msgbox(msg='哈哈哈，这道题都答错了',title='quiz',ok_button=('再来一遍'))
    answer1=g.buttonbox(msg='下面这幅图里是什么动物？',image='lesson1/cat.png',title='quiz',choices=('兔子','狗'))
g.msgbox('年轻人还是蛮有潜力的嘛！',image='lesson1/snake.png')
sys.exit(0)
