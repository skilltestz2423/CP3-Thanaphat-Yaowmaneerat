#จงบอกความหมายของคำต่อไปนี้
try:
    morning = input('ความหมายของคำว่า Morning: ')
    assert morning == 'ตอนเช้า','ตอบผิด'
    afternoon = input('ความหมายของคำว่า Afternoon: ')
    assert afternoon == 'ตอนเที่ยง','ตอบผิด'
except AssertionError:
    print('คุณบอกความหมายผิด')