x= 0
a= 0
senca =['ยาอม','ลูกอม','ไฟเย็น','ระเบิด','สบู่']
laka =[10,2,15,99,5]
sumlaka=[0,0,0,0,0,]
laka1=[0,0,0,0,0,]
print('\tโปรแกรมร้านค้าออนไลน์')
print('-'*30)
def shop():
    print('_'*30)
    global chh
    print('1.แสดงรายการสินค้า\n2.หยิบสินค้าเข้าตะกร้า\n3.แสดงรายการจำนวนแลราคาของสินค้าที่หยิบ\4.หยิบสินค้าออกจากตะกร้า\n5.ปิดโปรแกรม')
    chh=(input(' '))
    print('_'*30)
def menu() :
    print('\t[1]รายการสินค้า')
    print('-'*30)
    for x in range (0,5) :
        print(senca[x],'ราคา',laka[x],'บาท')
def bag1() :
    print('\t[2กรุณาเลือกสินค้า]')
    for x in range (0,5) :
        print('[%d]'%x,senca[x],'ราคา',laka[x],'บาท')
    print('หรือกด11เพื่อยกเลิก')
    for x in range (0,99) :
        ck=int(input('เลือกหมายเลขเสินค้าที่ต้องการ'))
        if ck == 0 :
            ck0()
        if ck == 1 :
            ck1()
        if ck == 2 :
            ck2()
        if ck == 3 :
            ck3()
        if ck == 4 :
            ck4()
        if ck == 11 :
            break      
def ck0():
    sum=int(input('จำนวณยาอมที่ต้องการ'))
    sumlaka[0]+=sum
    laka[0]*=sum
    laka1[0]+=laka[0]
def ck1():
    sum=int(input('จำนวณลูกอมที่ต้องการ'))
    sumlaka[1]+=sum
    laka1[1]+=laka[1]
       
def ck2():
    sum=int(input('จำนวณไฟเย็นที่ต้องการ'))
    sumlaka[2]+=sum
    laka1[2]+=laka[2]
def ck3():
    sum=int(input('จำนวณระเบิดที่ต้องการ'))
    sumlaka[3]+=sum
    laka1[3]+=laka[3]
def ck4():
    sum=int(input('จำนวณสบู่ที่ต้องการ'))
    sumlaka[4]+=sum
    laka1[4]+=laka[4]
def inbag():
    print('เลือกรายการที่3\t\n________สินค้าที่คุณได้หยิบมามีดังนี้________')
    for x in range (0,5) :
        print(senca[x],'_____จำนวน',sumlaka[x],'ชิ้น_____ราคา',laka1[x],'บาท')
    print('ราคาสินค้าทั้งหมด=>',laka[0]+laka1[1]+laka1[2]+laka1[3]+laka1[4],'บาท')
while True :
    shop()
    if chh == '1':
        menu()
    if chh == '2':
        bag1()
    if chh == '3':
        inbag()
    if chh == '5':
        break