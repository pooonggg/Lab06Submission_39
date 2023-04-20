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
    
    def isMouseOn(self):
        Mx,My= pg.mouse.get_pos()
        #Implement your code here
        if Mx>=20 and My>=20 and My<= 120 and Mx<=120:
            return True
        
    def isclicking(self):
        M1status,M2status,M3status = pg.mouse.get_pressed(num_buttons=3)
        if M1status == True or M2status == True: 
            return True

pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(20,20,100,100) # สร้าง Object จากคลาส Button ขึ้นมา

while(run):
    screen.fill((255, 255, 255))
    if btn.isMouseOn():
        btn.w = 200
        btn.h = 300
    if btn.isclicking():
        btn.b = 120
        btn.g = 20
        btn.r = 220
    else:
        btn.w = 100
        btn.h = 100
    btn.draw(screen)
    
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
