from graph import *
import math
def oval(x,y,a,b,q=0):
    moveTo(x-a,y)
    for j in range(b+1):
        for i in range(2*a+1):
            lineTo(x + (-a + i) * math.cos(q) + ((b - j) * (1 - ((-a + i) / a) ** 2) ** 0.5) * math.sin(q),
                   y + ((b - j) * (1 - ((-a + i) / a) ** 2) ** 0.5) * math.cos(q))
        for i in range(2 * a + 1):
            lineTo(x + (a - i) * math.cos(q) - ((b - j) * (1 - ((-a + i) / a) ** 2) ** 0.5) * math.sin(q),
                       y - ((b - j) * (1 - ((-a + i) / a) ** 2) ** 0.5) * math.cos(q))
def soplo_left(x,y):
    polygon([(x, y), (x-30,y+100),
             (x-70,y+195),(x-60,y+201),(x-50,y+205), (x-40,y+209), (x-30,y+211),(x-10,y+214), (x,y+216), (x+3,y+213),(x+4,y+213), (x+6,y+215),(x+8,y+213),(x+9,y+214),(x+11,y+204),(x+2,y+100),])
def soplo_right(x,y):
    polygon([(x, y), (x+30,y+100),
             (x+70,y+195),(x+60,y+201),(x+50,y+205), (x+40,y+209), (x+30,y+211),(x+10,y+214), (x,y+216), (x-3,y+213),(x-4,y+213), (x-6,y+215),(x-8,y+213),(x-9,y+214),(x-11,y+204),(x-2,y+100),])
def soplo_right(x,y):
    polygon([(x, y), (x+30,y+100),
             (x+70,y+195),(x+60,y+201),(x+50,y+205), (x+40,y+209), (x+30,y+211),(x+10,y+214), (x,y+216), (x-3,y+213),(x-4,y+213), (x-6,y+215),(x-8,y+213),(x-9,y+214),(x-11,y+204),(x-2,y+100),])


penColor("black")
penSize(5)
brushColor("black")
###Размеры поля
rectangle(0, 0, 1000, 300)
penColor(90, 35, 17)
penSize(5)
brushColor(90, 35, 17)
rectangle(0, 600, 1000, 300)
###Saturn
penColor(195,152,35)
brushColor(195,152,35)
circle(380, 150, 90)
###Raketa
penColor('black')
penSize(1)
brushColor(195,195,195)
polygon([(80,195), (103,167),
         (126,195), (80, 195)])
rectangle(90, 70, 116, 185)
polygon([(90,70), (103,45),
         (116,70), (90,70)])
penColor("black")
brushColor("gray")
circle(103, 90, 8)
circle(103, 115, 8)
circle(103, 140, 8)
###Astroman
penColor("gray")
brushColor("gray")
oval(400,425,16,30,0)###body
oval(415,460,8,25,0)
oval(385,460,8,25,0)
oval(415,485,8,10,0)
oval(385,485,8,10,0)
oval(425,488,10,7,0)
oval(375,488,10,7,0)
oval(415,408,10,10,0)
oval(385,408,10,10,0)
oval(428,410,8,8,0)
oval(372,410,8,8,0)
oval(437,412,6,6,0)
oval(363,412,6,6,0)
oval(400,388,13,15,0)###head
penColor("black")
oval(400,388,9,11,0)
###Soplo left
penColor("yellow")
brushColor("yellow")
soplo_left(90,210)
penColor("orange")
brushColor("orange")
soplo_left(80,260)
penColor("red")
brushColor("red")
soplo_left(70,310)
penColor("yellow")
brushColor("yellow")
soplo_right(110,210)
penColor("orange")
brushColor("orange")
soplo_right(120,260)
penColor("red")
brushColor("red")
soplo_right(130,310)






run()