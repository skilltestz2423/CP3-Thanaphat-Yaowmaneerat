userNameInSystem = 'admin'
passWordInSystem = '123456789'
count = 1
countpass = 1
loginInput = input('userID ของคุณ: ')
if loginInput != userNameInSystem:
    while count < 3 and loginInput != userNameInSystem:
        print('คุณกรอก UserID ผิด')
        loginInput = input('userID ของคุณ: ')
        count +=1
        if count > 3:
            print('หยุดการเข้าถึง')
            break

if count < 4 and loginInput == userNameInSystem:
    passwordInput = input('Your Password: ')
    if len(passwordInput) < 5:
        print('Password ต้องมีมากกว่า 5 ตัวขึ้นไป')
        while len(passwordInput) < 5 :
            passwordInput = input('Your Password Again!2: ')
            while passwordInput != passWordInSystem and countpass <3:
                print('รหัสผิดพลาดกรุณากรอกใหม่')
                passwordInput =input('Your Password Again!: ')
                count += 1
                if count > 3:
                    break
    if loginInput == userNameInSystem and passwordInput == passWordInSystem:
        print('Login สำเร็จ')
        print('เลือกที่ต้องการ')
        print('1. การบวก')
        print('2. การลบ')
        print('3. การคูณ')
        print('4. การหาร')
        selected = int(input('>>: '))
        while selected > 4 or selected < 1:
            selected = int(input('เลือกใหม่อีกครั้ง: '))
        if selected == 1:
            numbers_1 = int(input('เลขตัวที่1: '))
            numbers_2 = int(input('เลขตัวที่2: '))
            print(numbers_1,'+',numbers_2,'=',numbers_1+numbers_2)
        elif selected == 2:
            numbers_1 = int(input('เลขตัวที่1: '))
            numbers_2 = int(input('เลขตัวที่2: '))
            print(numbers_1,'-',numbers_2,'=',numbers_1-numbers_2)
        elif selected == 3:
            numbers_1 = int(input('เลขตัวที่1: '))
            numbers_2 = int(input('เลขตัวที่2: '))
            print(numbers_1, 'x', numbers_2, '=', numbers_1 * numbers_2)
        elif selected == 4:
            numbers_1 = float(input('เลขตัวที่1: '))
            numbers_2 = float(input('เลขตัวที่2: '))
            result = numbers_1/numbers_2
            if (result%1) == 0:
                print(numbers_1, '/', numbers_2, '=', numbers_1 // numbers_2)
            else:
                print(numbers_1, '/', numbers_2, '=', numbers_1 / numbers_2)
    elif loginInput != userNameInSystem and passwordInput == passWordInSystem:
        print('ชื่อผู้ใช้งานของคุณผิด')
    elif loginInput == userNameInSystem and passwordInput != passWordInSystem:
        print('รหัสผ่านของคุณผิด')
    else:
        print('ไม่สามารถ Login ได้')

        