#ประกาศตัวแปลเรียกใช้เครื่องมือ
import pygame,random,math,time,sys,mixer,os,sqlite3
FPS = 60
clock = pygame.time.Clock()
s ='t'
w=800
l=600
x=400
y=500
speed=20
ax = 250
ay =370
RED = (255,0,0)
pygame.init()
over =0
run = True
sumen =0
ty =50
somscore1=0
#เปลี่ยบเทียบค่า
z=20
z=str(z)

#หน้าต่างเกม
screen = pygame.display.set_mode((w,l))
pygame.display.set_caption('JURNEY IN SPACE')

icon= pygame.image.load(r'D:\python naruephat\ff\New folder\11.png')
pygame.display.set_icon(icon)

bgp1=pygame.image.load(r'D:\python naruephat\ff\bg_1_1.png')
bgp2=pygame.transform.scale(bgp1,(800,600))

scrover = pygame.image.load(r'D:\python naruephat\ff\New folder\11.png')
scrover0=pygame.transform.scale(scrover,(800,600))

texbox = pygame.image.load(r'D:\python naruephat\ff\tex.png')


#ตัวหนังสือในเกม
def shownamegame():
    namegame = font.render('JOURNEY IN SPACE',font,(0,0,0))
    namegam =pygame.transform.scale(namegame,(600,350))
    screen.blit(namegam,(100,-50))
def playfont():
    playmenu = font.render('PLAY',font,(0,0,0))
    playmenu0 = pygame.transform.scale(playmenu,(100,150))
    screen.blit(playmenu0,(350,300))
def exitmenu():
    exit1 = font.render('EXIT',font,(0,0,0))
    exit2 = pygame.transform.scale(exit1,(100,150))
    screen.blit(exit2,(346,400))
def showover():
    overgame = font.render('GAME OVER',font,(0,0,0))
    overgame1 =pygame.transform.scale(overgame,(600,350))
    screen.blit(overgame1,(100,10))
def inputname():
    namegame = font.render('ป้อนชื่อผู้เล่น',font,(0,0,0))
    namegam =pygame.transform.scale(namegame,(200,100))
    screen.blit(namegam,(285,50))

cmenu2 = pygame.image.load(r'D:\python naruephat\ff\NA.png')
arrow = pygame.transform.scale(cmenu2,(80,50))
def ar():
    screen.blit(arrow,(ax,ay))

#1ตัวละครเอก
play0 = pygame.image.load(r'D:\python naruephat\ff\Spaceship_tut.png')
pl1=pygame.transform.scale(play0,(60,65))#ตัวที่ใช้

def player(x,y):
   screen.blit(pl1,(x,y))

#กระสุน
his = pygame.image.load(r'D:\python naruephat\ff\lazer.png')
hiss=pygame.transform.scale(his,(50,50))
hx = w
hy = y
hychange = 40
hstate = 'ready'
def fire(x,y):
    global hstate
    hstate = 'fire'
    screen.blit(hiss,(x,y))

#ตัวร้าย
alum =5
enemy =  pygame.image.load(r'D:\python naruephat\ff\alien11s.png')
pow1 =  pygame.image.load(r'D:\python naruephat\ff\dsx.png')
pow =pygame.transform.scale(pow1,(50,45))
enm=pygame.transform.scale(enemy,(50,50))
exlist=[]
eylist=[]
ey_change_list=[]
allenemy = alum
for i in range (allenemy):
    exlist.append(random.randint(0,750))
    eylist.append(random.randint(0,0))
    ey_change_list.append(random.randint(1,5))

#############จุดเกิด################
ex=0
ey=0
eychange = 3
def enemys(x,y):
    screen.blit(enm,(x,y))
def powv(x,y):
    screen.blit(pow,(x,y)) 

##################################

################คะแนนน############
somscore =0
font=pygame.font.Font(r'D:\python naruephat\ff\ZF#2ndPixelus.ttf',60)
def showscore():
    scroe = font.render('คะแนน {}คะแนน'.format(somscore),True,(255,255,255))
    screen.blit(scroe,(0,0))
    

#fontgame_over.
####################################################

#################################sound#################################
#sonde=pygame.mixer.sound(r'D:\python naruephat\ff\dd.wav')
#sonde.play()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
pygame.mixer.init()
song = pygame.mixer.Sound(r'D:\python naruephat\ff\dd.wav')
song.set_volume(1.0)
enemydie = pygame.mixer.Sound(r'D:\python naruephat\ff\enamydie.wav')
enemydie.set_volume(1.0)
shot = pygame.mixer.Sound(r'D:\python naruephat\ff\shot.mp3')
shot.set_volume(1.0)
oversoud = pygame.mixer.Sound(r'D:\python naruephat\ff\over.wav')
click = pygame.mixer.Sound(r'D:\python naruephat\ff\click-1.wav')
powgv = pygame.mixer.Sound(r'D:\python naruephat\ff\htpow.wav')
powgv.set_volume(1.0)
#pygame.mixer.Sound.play(song)
########################################################################

##########collision###############
def iscollision(ecx,ecy,hcx,hcy):
    distance =math.sqrt(math.pow(ecx-hcx,2)+math.pow(ecy - hcy,2))
    if distance < 48:
        return True
    else:
        return False
def iscollisov1(ecy,hcy):
    distance =math.sqrt(math.pow(ecy - hcy,2))
    if distance < 48:
        return True
    else:
        return False
def reset(ecy,hcy):
    distance =math.sqrt(math.pow(ecy - hcy,2))
    if distance > 0.1:
        return True
    else:
        return False
##################################
runmenu = True
playgame = False
menugame = True
playnow = 'True'
keyup = 'F'
playshon = 'T'
game_over = False
nameply = False
saveg = 1
text = ""
active =False
rgb='F'
playnow1 = 'F'
oversoudpy ='T'
input_active = True
saveg = 1
name1=''
d=False
basi = True
gamesx = True
while True:
    while gamesx:
        clock.tick(FPS)
        ###################menugame#################
        while menugame:
            for event in pygame.event.get():
                if playshon == 'T':
                    x=400
                    song.play(-1)
                playshon ='F'
            #ออกเกม
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_KP_ENTER ]:
                    if playnow == 'True':
                        menugame =False
                        rgb ='T'
                        playnow1 = 'T'
                        pygame.mixer.stop()    
                    if playnow ==  'Flase':
                        pygame.quit()
                        exit()
                if keys[pygame.K_DOWN]:
                    if keyup == 'F':
                        ay +=100
                        playnow = 'Flase'
                        keyup = 'T'
                if keys[pygame.K_UP]:
                    if keyup == 'T':
                        ay -=100
                        keyup = 'F'
                        playnow = 'True'
                screen.blit(bgp2,(0,0))
                shownamegame()
                playfont()
                exitmenu()
                ar()
                pygame.display.update()
    #######################################
    ##########เขียนชื่อ###############
        if rgb == 'T' :
            screen.blit
            
            pygame.display.update()
            for event in pygame.event.get():
                 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    input_active = True
                    text = ""
                elif event.type == pygame.KEYDOWN and input_active:
                    click.play()
                    if event.key == pygame.K_RETURN:
                        input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        text =  text[:-1]
                    else:
                        text += event.unicode
                texbox1 = pygame.transform.scale(texbox,(800,200))
                screen.blit(bgp2,(0,0))
                screen.blit(texbox1, (0,200))
                text_surf = font.render(text, True, (255, 0, 0))
                screen.blit(text_surf,( text_surf.get_rect(center = screen.get_rect().center)))
                name1 = text
                pygame.display.flip()
                inputname()
                
                pygame.display.update()
                

    ################################################

        ############## main game ##################
        for event in pygame.event.get():
            #ออกเกม
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        #####คีย์
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            if playnow1 == 'T':
                rgb = 'F'
                playnow1 = 'F'
                playgame =True
            
        if keys[pygame.K_SPACE]:
            x=int(x)
            if hstate == 'ready':
                hx = x
                fire(hx,hy)
                shot.play()
        if keys[pygame.K_LEFT]:
            x -= speed
        if keys[pygame.K_RIGHT]:
            x += speed
        for i in z:
            x=str(x)
            w =str(w)
            j=0
            j=str(j)
            if x > w:
                x = 0
            x=str(x)
            if x < j:
                x=800
        
        if playgame == True:
            x=int(x)
            screen.blit(bgp2,(0,0))
            player(x,y)
        ############ยิง####################
            if hstate == 'fire':
                fire(hx,hy)
                hy -=  hychange

            if hy <= 0:
                hy = y
                hstate = 'ready'
        ####################################

        ############ตัวร้าย#############เช็คเกมโอเวอร์###############
            if sumen  >= 5 and sumen <= 15: 
                collision = iscollision(ex,ey,hx,hy)
                collisover = iscollisov1(ey,l)
                if collisover:
                    ey=0
                    ex = random.randint(10,750)
                if collision:
                    powgv.play()
                    hy = y
                    hstate = 'ready'
                    ey=0
                    ex = random.randint(10,750)
                    somscore1 +=1
                    somscore += 5
                powv(ex,ey)
                ey+=eychange 
            if sumen  >= 16 and sumen <= 29: 
                collision = iscollision(ex,ey,hx,hy)
                collisover = iscollisov1(ey,l)
                if collisover:
                    ey=0
                    ex = random.randint(10,750)
                if collision:
                    powgv.play()
                    hy = y
                    hstate = 'ready'
                    ey=0
                    ex = random.randint(10,750)
                    somscore1 +=1
                    somscore += 5
                powv(ex,ey)
                ey+=eychange 
            if sumen  >= 29 and sumen <= 39: 
                collision = iscollision(ex,ey,hx,hy)
                collisover = iscollisov1(ey,l)
                if collisover:
                    ey=0
                    ex = random.randint(10,750)
                if collision:
                    powgv.play()
                    hy = y
                    hstate = 'ready'
                    ey=0
                    ex = random.randint(10,750)
                    somscore1 +=1
                    somscore += 5
                powv(ex,ey)
                ey+=eychange 
            if sumen  >= 38 and sumen <= 9999999: 
                collision = iscollision(ex,ey,hx,hy)
                collisover = iscollisov1(ey,l)
                if collisover:
                    ey=0
                    ex = random.randint(10,750)
                if collision:
                    powgv.play()
                    hy = y
                    hstate = 'ready'
                    ey=0
                    ex = random.randint(10,750)
                    somscore1 +=1
                    somscore += 5
                powv(ex,ey)
                ey+=eychange 
            for i in range(allenemy): 
                #p2
                if sumen  >= 5 and sumen <= 15: 
                    ey_change_list[i]=random.randint(1,6)
                #p3
                if sumen  >= 16 and sumen <= 26: 
                    ey_change_list[i]=random.randint(3,6)
                #p4
                if sumen  >= 27 and sumen <= 37: 
                    ey_change_list[i]=random.randint(4,7)
                #p5ofgot
                if sumen  >= 38 and sumen <= 9999999: 
                    ey_change_list[i]=random.randint(5,10)
                eylist[i]+=ey_change_list[i]
                collisover = iscollisov1(eylist[i],l)
                collisionmulit = iscollision(exlist[i],eylist[i],hx,hy)
                if collisover:
                    over +=1
                    eylist[i]=0
                    exlist[i] = random.randint(10,750)
                if collisionmulit:
                    hy = y
                    hstate = 'ready'
                    eylist[i]=0
                    exlist[i] = random.randint(10,750)
                    enemydie.play()
                    sumen  +=1
                    somscore += 1
                enemys(exlist[i],eylist[i])
            showscore()

        if over == 5:
            game_over = True
        while game_over:
            playgame =False
            for event in pygame.event.get():
                if game_over == True:
                    if oversoudpy =='T':
                        oversoud.play(-1)
                        oversoudp ='F'
                screen.blit(bgp2,(0,0))
                showover()
                #ออกเกม
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                    menugame = True
                    saveg = 0
                    playshon = 'T'
                    text = ""
                    oversoudpy ='T'
                    game_over = False
                    pygame.mixer.stop()
                for i in range(allenemy):
                    eylist[i]+=ey_change_list[i]
                    reset1 = reset(eylist[i],l)
                    if reset1:
                        eylist[i]=0
                        exlist[i] = random.randint(10,750)
                        
                over = 0
                pygame.display.update()
                #newstring = str(name1)
        
        if saveg == 0 :
            text1=str(name1)
            conn = sqlite3.connect(r"D:\python naruephat\example.db")
            c = conn.cursor()
            data =(text1,somscore1,sumen,somscore)
            c.execute('INSERT INTO JOURNEYGAME  (name,coin,enemys_kill,score)VALUES (?,?,?,?)',data)
            conn.commit()
            c.close ()
        if saveg == 0:
            saveg = 1
            somscore =0
            sumen=0
            name1 =''
            basi =True
            s='f'
            gamesx=False
            
        
        
        pygame.display.update()

        ########################################
        pygame.display.update()
        clock.tick(FPS)
    while basi:
        conn = sqlite3.connect(r"D:\python naruephat\example.db")
        c=conn.cursor()
        c.execute('SELECT * FROM JOURNEYGAME ORDER BY score DESC')
        conn.commit()
        result =c.fetchall()
        print('    <<<<<score>>>>>')
        print(' name coin enemys score')
        for x in result :
            print(x)
        c.close()
        gamesx =True
        basi =False
