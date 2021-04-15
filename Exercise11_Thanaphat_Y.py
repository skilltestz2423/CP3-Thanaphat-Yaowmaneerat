'''
for i in range(n):
    space = ' '*(n-i)
    print(space,"*"*int((i*2)-1))
'''
n = int(input('Test: '))
for x in range(n): #[0,1,2]
    for y in range(x+1): #range([1,2,3])
        text= ''
        text+= "*"*((x*2)+1) #(y=[0],y=[0,1],y=[0,1,2])
    space =' '*(n-x)
    print(space,text)