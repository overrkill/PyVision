from graphics import *


xcnt = int(input("enter circles centre x coord"))
ycnt = int(input("enter circles centre y coord"))
r = int(input("enter circle radius"))

x = r
y = 0

win=GraphWin()
print("({},{})".format(x+xcnt, y+ycnt))


if (r > 0):

    print("({},{})".format(x+xcnt, -y+ycnt))
    print("({},{})".format(y+xcnt, x+ycnt))
    print("({},{})".format(-y+xcnt, x+ycnt))
    Point(x+xcnt, -y+ycnt).draw(win)
    Point(y+xcnt, x+ycnt).draw(win)
    


P = 1 - r  
while (x > y) : 
      
    y += 1
          
        
    if (P <= 0):  
        P = P + 2 * y + 1
              

    else:          
        x -= 1
        P = P + 2 * y - 2 * x + 1
          

    if (x < y): 
        break
          
        
    print("({},{})".format(x+xcnt,y+ycnt))    
    print("({},{})".format(-x+xcnt,y+ycnt))    
    print("({},{})".format(x+xcnt,-y+ycnt))    
    print("({},{})".format(-x+xcnt,-y+ycnt))    
    Point(x+xcnt,y+ycnt).draw(win)
    Point(-x+xcnt,y+ycnt).draw(win)
    Point(x+xcnt,-y+ycnt).draw(win)
    Point(-x+xcnt,-y+ycnt).draw(win)      
       
    if (x != y) : 
          
            
        print("({},{})".format(y+xcnt,x+ycnt))    
        Point(y+xcnt,x+ycnt).draw(win)   
        print("({},{})".format(-y+xcnt,x+ycnt))    
        Point(-y+xcnt,x+ycnt).draw(win)    
        print("({},{})".format(y+xcnt,-x+ycnt))    
        Point(y+xcnt,-x+ycnt).draw(win)    
        print("({},{})".format(-y+xcnt,-x+ycnt))
        Point(-y+xcnt,-x+ycnt).draw(win)   
win.getMouse()
win.close()

"""
overkill@overkill-pc:~/Desktop/cv$ python midcir.py 
enter circles centre x coord100
enter circles centre y coord100
enter circle radius10
(110,100)
(110,100)
(100,110)
(100,110)
(110,101)
(90,101)
(110,99)
(90,99)
(101,110)
(99,110)
(101,90)
(99,90)
(110,102)
(90,102)
(110,98)
(90,98)
(102,110)
(98,110)
(102,90)
(98,90)
(110,103)
(90,103)
(110,97)
(90,97)
(103,110)
(97,110)
(103,90)
(97,90)
(109,104)
(91,104)
(109,96)
(91,96)
(104,109)
(96,109)
(104,91)
(96,91)
(109,105)
(91,105)
(109,95)
(91,95)
(105,109)
(95,109)
(105,91)
(95,91)
(108,106)
(92,106)
(108,94)
(92,94)
(106,108)
(94,108)
(106,92)
(94,92)
(107,107)
(93,107)
(107,93)
(93,93)
"""