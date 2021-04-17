systemList={'ข้าวมันไก่':40,'ข้าวหมกไก่':45,'ข้าวมันไก่ผสม':50,'ข้าวหน้าไก่':45}
selectedList=[]
def showBill():
    totalprice = 0
    print('--------Welcome My Shop--------')
    for i in range(len(selectedList)):
        print('ชื่อเมนู: ',selectedList[i][0],'ราคา',selectedList[i][1],'บาท')
        totalprice = totalprice + int(selectedList[i][1])
    print('ยอดจ่ายรวมคือ: ',totalprice)

while True:
    menuName = input('ชื่อเมนู: ')
    if (menuName.casefold() == 'exit'):
        print('ออกการทำงาน')
        break
    else:
        print(systemList[menuName])
        selectedList.append([menuName,systemList[menuName]])
print(selectedList)
showBill()