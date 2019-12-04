import random
import time

while True:
    time.sleep(0.2)
    a=random.randint(1,3)
    b=random.randint(1,3)
    c=random.randint(1,3)
    print(a,b,c)

    if a==b and b==c:
        print('大赢家')
        break
    if a==b or b==c or a==c:
        continue
    else:
        print('大输家')
        break
