a=input('输入你想要加密的信息： ')

# 方法1
print(a[::-1])


# 方法2
b=[]
for aa in a:
    b.append(aa)

c=b[::-1]
print(''.join(c))




