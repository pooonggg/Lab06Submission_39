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
    
pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(20,20,100,100) # สร้าง Object จากคลาส Button ขึ้นมา

while(run):
    screen.fill((255, 255, 255))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

        if event.type == pg.KEYDOWN and event.key == pg.K_d: #ปุ่มถูกกดลงและเป็นปุ่ม D
            btn.x+=15
            
            # print("Key D down")
        if event.type == pg.KEYDOWN  and event.key == pg.K_a: #ปุ่มถูกปล่อยและเป็นปุ่ม A
            btn.x-=15
            # print("Key A up")
        if event.type == pg.KEYDOWN and event.key == pg.K_w: #ปุ่มถูกกดลงและเป็นปุ่ม D
            btn.y-=15
        if event.type == pg.KEYDOWN and event.key == pg.K_s: #ปุ่มถูกกดลงและเป็นปุ่ม D
            btn.y+=15
    btn.draw(screen)
    
    pg.display.update()
    