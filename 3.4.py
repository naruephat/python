print('ร้านคุณโด้')
def menu():
    global dodo
    print('เพิ่ม [a]')
    print('แสดง [s]')
    print('ออกจากระบบ [x]')
    dodo=str(input(' '))
def a():
    global name
    name=(input('รหัส:ชื่อ:จังหวัด:'))
    print('*****ข้อมูลได้รับเข้าสู่ระบบแล้ว*****')
def s():
    print('_'*10)
    print('รหัส--ชื่อ-----จังหวัด')
    print('_'*10)
    print('%s'%name)

        
while True:
    menu()
    if dodo == 'a':
        a()
    if dodo == 's':
        s()
    if dodo == 'x':
        d=str(input('ต้องการออกจากโปรแกรม (y/n):'))
        if d == 'y':
            break