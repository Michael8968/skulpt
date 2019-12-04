import random
import time

#####################################################
score=5
while True:
    time.sleep(0.2)
    a=random.randint(1,3)
    b=random.randint(1,3)
    c=random.randint(1,3)
    print(a,b,c,'分数：'+str(score))

    if a==b and b==c:
        print('大赢家')
        break
    if a==b or b==c or a==c:
        continue
    else:
        score-=1

    if score==0:
        print('输家')
        break
 
 ###################################################################
 
score=5
while True:
    time.sleep(0.2)
    a=random.randint(1,3)
    b=random.randint(1,3)
    c=random.randint(1,3)
    print(a,b,c,'分数：'+str(score))

    if a==b and b==c:
        print('大赢家')
        break
    if a==b or b==c or a==c:
        continue
    score-=1

    if score==0:
        print('输家')
        break
 
########################################################### 
score=5
while True:
    time.sleep(0.2)
    a=random.randint(1,3)
    b=random.randint(1,3)
    c=random.randint(1,3)
    print(a,b,c,'分数：'+str(score))

    if a==b and b==c:
        print('大赢家')
        break
    if a==b or b==c or a==c:
        score -= 0
    else:
        score-=1

    if score==0:
        print('输家')
        break 
 
######################################################## 
score=5
while True:
    time.sleep(0.2)
    a=random.randint(1,3)
    b=random.randint(1,3)
    c=random.randint(1,3)
    print(a,b,c,'分数：'+str(score))

    if a==b and b==c:
        print('大赢家')
        break
    if not(a==b or b==c or a==c):
        score-=1
        
    if score==0:
        print('输家')
        break 
 
    
