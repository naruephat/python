print('\t          พจณานุกรม')
print('*'*50)
wocab=[]
wocab1=[]
wocab2=[]
num1=[]
def menu():
        global coish
        print('[1]เพิ่มคำศัพท์\n','[2]เพิ่มคำศัพท์\n','[3]เพิ่มคำศัพท์\n','[4]เพิ่มคำศัพท์')
        coish=int(input(' '))
        print('-'*30)
def up():
    print('ตัวเลือกที่1')
    sub=str(input('เพิ่มคำศัพท์\n'))
    wocab.append(sub)
    sub1=str(input('ชนิดคำศัพท์(n.,v.,adj.,adv.,'))
    if sub1 == 'n':
        num1.append(0)
    if sub1 == 'v':
        num1.append(1)
    if sub1 == 'adj':
        num1.append(2)
    if sub1 == 'adv':
        num1.append(3)
sub2=str(input('ความหมาย\t'))
woccab2.append(sub2)
print('เพิ่มคำศัพท์เสร็จสมบูรณ์')