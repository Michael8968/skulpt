
'''
def logic(jiantou, anjian, score, game):
    if jiantou.ys == 'Blue':
        if anjian == jiantou.fx:
            score += 1
            jiantou.kill()
        else:
            game = 'lose'
    elif jiantou.ys == 'Red':
        if anjian == jiantou.ffx:
            score += 1
            jiantou.kill()
        else:
            game = 'lose'
    return game, score
'''
#####下面是改成分数减一的版本
def logic(jiantou, anjian, score, game):
    if jiantou.ys == 'Blue':
        if anjian == jiantou.fx:
            score += 1
            jiantou.kill()
        else:
            game = 'lose'

    elif jiantou.ys == 'Red':
        if anjian == jiantou.ffx:
            score += 1
            jiantou.kill()
        else:
            game = 'lose'
    elif jiantou.ys == 'Purple':
        if anjian == jiantou.fx:
            score += 1
            jiantou.kill()
        else:
            score -= 1
            jiantou.kill()

    return game, score
