def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menuSelect():
    userSelected = int(input(">>"))
    return userSelected

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)

if login() == True:
    print('Login Success')
    showMenu()
    selected = menuSelect()
    if selected == 1:
        totalprice = int(input('ราคาสินค้าที่นำมาคำนวณ: '))
        print(vatCalculator(totalprice))
    elif selected ==2:
        print(priceCalculator())
    else:
        'กรุณากรอกเมนูที่ต้องการ'
else:
    print('Login Fail')