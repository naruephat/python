x=1
fds=[]
print('ป้อนชื่ออาหารสุดโปรดของคุณหรือ exit เพื่อออกจากโปรแกรม')
for i in range (0,99):
   fd=str(input('อาหารจานโปรดจานที่ %d'%x))
   fds.append(fd)
   x=x+1
   if fd == 'exit':
       x=0
       break
print('หาหารจานโปรดมีดังนี้')
for i in range (0,len(fds)-1):
    x=x+1
    print('%d'%x,fds[i])