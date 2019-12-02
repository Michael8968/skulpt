import random

word = random.choice(["code", "club",'cat','rose','dady','meat','night','mom','happy'])

right =[] #这一行是学生需要自己写的，包括列表名称需要自己起名
wrong=[]#这一行是学生需要自己写的，包括列表名称需要自己起名

tries = 7

while tries > 0:

    out = ""
    for letter in word:
        if letter in right:
            out = out + letter
        else:
            out = out + "_"

    if out == word:
        break

    print("猜一猜这个单词:", out)
    print(tries, "剩余机会：")

#需要学生自己写（开始）
    guess = input()

    if guess in right or guess in wrong:
        print("你猜过啦", guess)

    elif guess in word:
        print("你猜对啦！")
        right.append(guess)

    else:
        print("你猜错啦！")
        wrong.append(guess)
        
#需要学生自己写（结束）
        tries = tries - 1


if tries:
    print("厉害了完全猜中了单词", word)
else:
    print("QAQ机会用完了，没有猜中", word)
