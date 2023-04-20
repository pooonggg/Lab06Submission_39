import sys
import pygame as pg

class Rec :
    def __init__(self,x=0,y=0,w=0,h=0,r=255,g=0,b=0,):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.r = r # R color
        self.g = g # G color
        self.b = b # B color
    def draw(self,screen):
        pg.draw.rect(screen,(self.r,self.g,self.b),(self.x,self.y,self.w,self.h))

class Button(Rec):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rec.__init__(self, x, y, w, h)
     
        
    def isclicking(self):
        Mx,My= pg.mouse.get_pos()
        M1status,M2status,M3status= pg.mouse.get_pressed(num_buttons=3)
        if Mx>=(win_x/2)-100 and My>=(win_y/2)+100 and My<= (win_y/2)+150 and Mx<=(win_x/2)+100 :
            if M1status == True or M2status == True: 
                return True
        
class InputBox:

    def __init__(self, x, y, w, h, isage,text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.isage= isage

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if self.isage:
                        if event.unicode.isnumeric():
                            self.text += event.unicode
                    else:
                        self.text += event.unicode
                    # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)

pg.init()
win_x, win_y = 800, 700
screen = pg.display.set_mode((win_x, win_y))

COLOR_INACTIVE = pg.Color('lightskyblue3') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('dodgerblue2')     # ^^^
FONT = pg.font.Font(None, 32)

input_box1 = InputBox((win_x/2)-100, (win_y/2)-200, 200, 50,False ) # สร้าง InputBox1
input_box2 = InputBox((win_x/2)-100, (win_y/2)-100, 200, 50,False ) # สร้าง InputBox2
input_box3 = InputBox((win_x/2)-100, (win_y/2), 200, 50,True ) # สร้าง InputBox3
input_boxes = [input_box1, input_box2,input_box3] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
run = True

font = pg.font.Font('freesansbold.ttf', 32) # font and fontsize
text1 = font.render('Firstname', True,(120,20,220), (255,255,255)) # (text,is smooth?,letter color,background color)
text2 = font.render('Lastname', True,(120,20,220), (255,255,255))
text3 = font.render('Age', True,(120,20,220), (255,255,255))
text4 = font.render('Submit', True,(255,255,255), (255,0,0))
text5 = font.render('', True,(120,20,220), (255,255,255))
textRect1 = text1.get_rect()# text size
textRect2 = text2.get_rect()
textRect3 = text3.get_rect()
textRect4 = text4.get_rect()
textRect5 = text5.get_rect()
textRect1.center = (win_x // 2, (win_y // 2)-225)
textRect2.center = (win_x // 2, (win_y // 2)-125)
textRect3.center = (win_x // 2, (win_y // 2)-25)
textRect4.center = (win_x // 2, (win_y // 2)+125)

        
btn = Button((win_x/2)-100, (win_y/2)+100,200,50)


while run:
    screen.fill((255, 255, 255))
    btn.draw(screen)
    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)
    screen.blit(text4, textRect4)
    if btn.isclicking(): 
        text5 = font.render(('Hello '+str(input_box1.text)+' '+str(input_box2.text)+'! You are '+str(input_box3.text)+' years old.'), True,(120,20,220), (255,255,255))
        textRect5 = text5.get_rect()
        textRect5.center = (win_x // 2, (win_y // 2)+250)
    
    screen.blit(text5, textRect5)
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False

    pg.time.delay(1)
    pg.display.update()

