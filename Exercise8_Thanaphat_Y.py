'''Price Product'''
tomato = 10
apple = 15
mango = 12.5
listtomato = ['TOMATO','Tomato','TOmato','TOMato','TOMAto','TOMATo','tOMATO','toMATO','tomATO','tomaTO','tomatO','tomato']
listapple = ['APPLE','Apple','APple','APPle','APPLe','aPPLE','apPLE','appLE','applE','apple']
listmango = ['MANGO','Mango','MAngo','MANgo','MANGo','mANGO','maNGO','manGO','mangO','mango']
userNameInput = (input('Your Username: '))
passInput = (input('Your Password: '))
if userNameInput == 'admin' and passInput == '2703':
    print('Welcome To My Shop')
    print('รายการสินค้าในร้านมีดังนี้')
    print('1. Tomato',tomato,' THB /1ea')
    print('2. Apple ',apple,' THB /1ea')
    print('3. Mango ',mango,' THB /1ea')
    userSelected = (input('ลูกค้าโปรดเลือกสินค้าที่ต้องการค่ะ : '))
    if userSelected == '1' or userSelected in listtomato:
        print('สินค้าที่ท่านเลือกคือ Tomato')
        total = int(input('จำนวนที่ท่านต้องการซื้อ: '))
        print('ยอดรวมสินค้า คือ: ',tomato*total,'THB')
    elif userSelected == '2' or userSelected in listapple:
        print('สินค้าที่ท่านเลือกคือ Apple')
        total = int(input('จำนวนที่ต้องการซื้อ: '))
        print('ยอดรวมสินค้า คือ: ',apple*total,'THB')
    elif userSelected == '3' or userSelected in listmango:
        print('สินค้าที่ท่านเลือกคือ Mango')
        total = int(input('จำนวนที่ต้องการซื้อ: '))
        if (mango*total)%1 == 0:
            print('ยอดรวมสินค้า คือ:',int(mango*total),'THB')
        else:
            print('ยอดรวมสินค้า คือ: ',mango*total,'THB')

elif userNameInput == 'admin' and passInput != '2703':
    print('รหัสผ่านของคุณผิดพลาด')
    print('กรอกใหม่อีกครั้ง')
elif userNameInput != 'admin' and passInput == '2703':
    print('UserID ของคุณผิดพลาด')
    print('กรอกใหม่อีกครั้ง')
else:
    print('ไม่มีข้อมูลในระบบ กรุณาลงทะเบียน')