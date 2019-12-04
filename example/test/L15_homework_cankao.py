dict1 = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4,
    'e': 5, 'f': 6, 'g': 7, 'h': 8,
    'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
    'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18,
    's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
    'x': 24, 'y': 25, 'z': 26
}

dict2= {1:"a"}
for key, value in dict1.items():
    dict2[value] = key

##################input
#写一个接收函数（）用变量a接收，并用split分隔开，用法：a.split(" ")



##########
list1=[]
for aa in range(len(a)):
    b=int(a[aa])
    list1.append(b)

str1=''
for ll in list1:
    str1=str1+dict2[ll]

print(str1)
