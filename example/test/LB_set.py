#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random

enemy = None


def move(anjian, anuo):

    if anjian == "up":
        anuo.movedown()
    if anjian == "down":
        anuo.moveup()
    if anjian == "left":
        anuo.moveright()
    if anjian == "right":
        anuo.moveleft()


    # if anjian == "up":
    #     anuo.moveup()
    # if anjian == "down":
    #     anuo.movedown()
    # if anjian == "left":
    #     anuo.moveleft()
    # if anjian == "right":
    #     anuo.moveright()


    pass


def set_enemy(abu, six, enemyPos):

    jun_tuan = abu
    wei_zhi = 3

    # jun_tuan = random.choice((abu, six))
    # wei_zhi = random.choice((1, 2, 3, 4, 5))

    return jun_tuan,wei_zhi



