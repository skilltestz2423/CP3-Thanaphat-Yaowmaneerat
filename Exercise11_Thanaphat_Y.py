'''
for i in range(n):
    space = ' '*(n-i)
    print(space,"*"*int((i*2)-1))
'''
n = int(input('Test: '))
for x in range(n): #[0,1,2,3,4]
    for y in range(x+1): #range([1,2,3,4,5])
        text= ''
        text+= "*"*((x*2)+1) #x=[0,1,2,3,4]
    space =' '*(n-x) #n=[5] x=[0,1,2,3,4]
    print(space,text)
#output [1,3,5,7,9] = [1 = 0x2+1],[3 = 1x2+1],[5 = 2x2+1],[7 = 3x2+1],[9 = 4*2+1]