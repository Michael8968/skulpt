#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
import easygui as g
import sys

def my_input(a):
	return g.enterbox(msg=a,title='quiz',default='')

def my_print(a,b,c):
	return g.msgbox(msg=a,title='quiz',image=b,ok_button=(c))

def my_print2(a,b,c):
	return g.buttonbox(msg=a,title='quiz',image=b,choices=c)

name=my_input('想脱离这里吗？你必须回答正确全部的问题。首先，告诉我你的名字')
if name==None or name=='':
	name='小朋友'
my_print2(name+' ,你觉得自己聪明吗？','',('当然呢！','必须啊！','我最聪明！'))
my_print('既然你觉得自己很聪明，那么我来考考你！','','没问题！')
answer1=my_print2('下面这幅图里是什么动物？','lesson1/cat.png',('猫','狗'))
while answer1!='猫':
	my_print('哈哈哈，这道题都答错了','','再来一遍')
	answer1=my_print2('下面这幅图里是什么动物？','lesson1/cat.png',('猫','狗'))
my_print('年轻人还是蛮有潜力的嘛！','lesson1/snake.png','成功逃离！')
sys.exit(0)
