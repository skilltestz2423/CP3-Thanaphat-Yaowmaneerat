menulist = []
pricelist =[]

def showBill():
    print('--------Welcome My Shop--------')
    sumprice = 0
    for i in range(len(menulist)):
        sumprice += int(pricelist[i])
        print('ชื่อเมนู: ',menulist[i],' ราคา: ',pricelist[i],' บาท',sep='')
        print('ยอดรวมค่าใช้จ่ายทั้งหมดคือ:',sumprice,'บาท')

while True:
    menuName = input('ชื่อเมนู: ')
    if (menuName.casefold() == 'exit'):
        print('ออกการทำงาน')
        break
    else:
        menuPrice = input('ราคา: ')
        menulist.append(menuName)
        pricelist.append(menuPrice)
showBill()

