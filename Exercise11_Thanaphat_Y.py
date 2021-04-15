n = int(input('Test: '))
for i in range(n):
    space = ' '*(n-i)
    print(space,("*"*int(((i+1)*2)-1)))