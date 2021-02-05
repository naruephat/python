laka=[2000,1000,300,250,]
zenka=['แบตเตอรรี่','ยาง','น้ำมันเครื่อง','น้ำมันเบรค']
class shop:
    def __init__(self,zenka,laka):
        self.laka =  laka=[]
        self.zenka = zenka=[]
    def addzenka(self):
        print('*'*10,'เพิ่มรายการสินค้า','*'*10)
        for i in range (0,99):
            zen=str(input('เพิ่มชื่อสินค้า =>'))
            lak=int(input('ราคาของ%s=>'%zen))
            zenka.append(zen)
            laka.append(lak)
            st=str(input('หากเพิ่มสินค้าเสร็จแล้วใช่หรือไม่ yes/no :'))
            if st == 'yes':
                break
    def show (self):
        print('*'*10,'รายการสินค้ามีดังนี้','*'*10)
        for x in range (0,len(zenka)):
            print('[%d]'%x,zenka[x],laka[x])
def menu():
    global dodo
    print('*'*10,'โด้การช่าง','*'*10)
    print('1. แสดงรายการสินค้า  [s]')
    print('2.เพิ่มรายการสินค้า    [a] ')
    print('3.ออกจากระบบ       [x]')
    dodo=str(input(' '))
x= shop(['แบตเตอรรี่','ยาง','น้ำมันเครื่อง','น้ำมันเบรค'],[2000,1000,300,250,])
while True :
    menu()
    if dodo == 's':
        x.show()
    if dodo == 'a':
        x.addzenka()
    if dodo == 'x':
        ex=str(input('ต้องการออกจากโปรแกรมหรือไม่ y/n'))
        if ex =='y':
            break