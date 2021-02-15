#import sqlite3
#conn = sqlite3.connect (r'D:\python naruephat\example.db')
#c = conn.cursor()
#c.execute ('''CREATE TABLE student(ลำดับที่ integer PRIMARY KEY AUTOINCREMENT,
#ชื่อ_นามสกุล varchar(30)NOT NULL,
#email varchar(100)NOT NULL,
#เพศ   varchar(30)NOT NULL,
#อายุ   varchar(30)NOT NULL,
#ชั้นปี   varchar(30)NOT NULL)''')
#conn.commit()
#conn.close()
import sqlite3
def menu():
    global mg
    print('---ระบบทะเบียนนักเรียน---\n','='*20)
    print('เพิ่มนักเรียนกด [a]\nแสดงข้อมูลนักเรียน[s]\nแก้ไขข้อมูลนักเรียน][e]\nลบข้อมูลนักเรียน[d]\nออกจากโปรแกรม[x]')
    mg =str(input(' '))

def show():
    conn = sqlite3.connect(r'D:\python naruephat\example.db')
    c = conn.cursor()
    c.execute ('''SELECT * FROM student''')

    result = c.fetchall()
    print('ลำดับที่:ชื่อ          :email      :เพศ  :   อายุ :  ชั้นปี :')
    for x in result :
        print(x)
def addst():
    id1 = int(input('ป้อนลำดับที่'))
    namec = str(input('ป้อนชื่อนักเรียน=>'))
    em = str(input('ป้อนemail=>'))
    sex = str(input('ป้อนเพศ=>'))
    aer = int(input('ป้อนอายุ=>'))
    y = int(input('ป้อนชั้นปี=>'))
    import sqlite3
    conn = sqlite3.connect(r'D:\python naruephat\example.db')
    c = conn.cursor()
    try:
        data = (namec,em,sex,aer,y,id1)
        c.execute('''UPDATE student SET ชื่อ_นามสกุล  =?,email =?,เพศ =?,อายุ  =?,ชั้นปี =? WHERE ลำดับที่ =?''',data)
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print (e)
    finally :
        if conn :
            conn.close()
def ad():
    conn = sqlite3.connect(r'D:\python naruephat\example.db')
    c = conn.cursor()
    try:
        
        name2 = str(input('ป้อนชื่อนักเรียน=>'))
        em2 = str(input('ป้อนemail=>'))
        sex2 = str(input('ป้อนเพศ=>'))
        aer2 = int(input('ป้อนอายุ=>'))
        y2 = int(input('ป้อนชั้นปี=>'))
        data =(name2,em2,sex2,aer2,y2)
        c.execute('INSERT INTO student  ( ชื่อ_นามสกุล ,email,เพศ,อายุ,ชั้นปี)VALUES (?,?,?,?,?)',data)
        conn.commit()
        c.close ()
    except sqlite3.Error as e:
        print (e)
    finally :
        if conn :
            conn.close()
def fdel():
    conn = sqlite3.connect(r'D:\python naruephat\example.db')
    c = conn.cursor()
    try:
        data3 = str(input('Please enter ชื่อ_นามสกุล : '))
        mydata = c.execute('DELETE FROM student WHERE ชื่อ_นามสกุล =?', (data3,))
        #DELETE FROM your_student;    
        #DELETE FROM sqlite_sequence WHERE name = 'your_student';
        conn.commit()
        c.close()

    except sqlite3.Error as e:
        print (e)
    finally :
        if conn :
            conn.close()

while True:
    menu()
    if  mg == 'a' :
        ad()
    if  mg == 's' :
        show()
    if  mg == 'e' :
        addst()
    if  mg == 'd' :
        fdel()
    if  mg == 'x' :
        print('ต้องการจะออกจากโปรแกรม  y/n')
        ex=str(input(' '))
        if ex == 'y':
            break


   
