menulist = []
def showBill():
    totalprice = 0
    print('--------Welcome My Shop--------')
    for i in range(len(menulist)):
        print('ชื่อเมนู: ',menulist[i][0],'ราคา',menulist[i][1],'บาท')
        totalprice = totalprice + int(menulist[i][1])
    print('ยอดจ่ายรวมคือ: ',totalprice)

while True:
    menuName = input('ชื่อเมนู: ')
    if (menuName.casefold() == 'exit'):
        print('ออกการทำงาน')
        break
    else:
        menuPrice = input('ราคา: ')
        menulist.append([menuName,menuPrice])
print(menulist)
showBill()