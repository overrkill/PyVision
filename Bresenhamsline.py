from graphics import *
x=int(input("enter x coord"))
y=int(input("enter y coord"))
x2=int(input("enter x2 coord"))
y2=int(input("enter y2 coord"))

dx=x2-x
dy=y2-y
dt=2*dy-2*dx
ds=2*dy
d=ds-dx
print("line ({},{}) and ({},{})\n dx {}\n dy {} \n dt {} \n ds {} \n d {}".format(x,y,x2,y2,dx,dy,dt,ds,d))
win=GraphWin("Bressenhams line",500,500)
Point(x,y).draw(win)
while(x<x2):
    x=x+1
    if d<0:
        d=d+ds
    else:
        y=y+1
        d=d+dt
    print("d:{} pt:({},{})".format(d,x,y))
    Point(x,y).draw(win)
win.getMouse()
win.close()

"""
enter x coord10
enter y coord11
enter x2 coord20
enter y2 coord19
line (10,11) and (20,19)
 dx 10
 dy 8 
 dt -4 
 ds 16 
 d 6
d:2 pt:(11,12)
d:-2 pt:(12,13)
d:14 pt:(13,13)
d:10 pt:(14,14)
d:6 pt:(15,15)
d:2 pt:(16,16)
d:-2 pt:(17,17)
d:14 pt:(18,17)
d:10 pt:(19,18)
d:6 pt:(20,19)
run for graphical output
"""