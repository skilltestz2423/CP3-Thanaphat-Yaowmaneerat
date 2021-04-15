'''
n = int(input('Test: '))
for i in range(n):
    space = ' '*(n-i)
    print(space,"*"*int((i*2)-1))
'''
for x in range(n):
    for y in range(x):
        text+= "*"*((i*2)-1)
    space =' '*(n-x)
    print(space,text)