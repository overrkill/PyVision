## Computer Vision Alogirthms and their implementation in Python2

view the code (https://github.com/overrkill/PyVision)

### window to viewport mapping

Translate to orgin->scale->translate to viewport
```


def w2v(wrx, wry, wlx, wly, vrx, vry, vlx, vly, a):
    sx = 1 / float((wlx - wrx) / (vlx - vrx))
    sy = 1 / float((wly - wry) / (vly - vry))
    # translate to origin

    transOP = array([1, 0, -wrx, 0, 1, -wry, 0, 0, 1]).reshape(3, 3)

    # scale to viewport

    scalOP = array([sx, 0, 0, 0, sy, 0, 0, 0, 1]).reshape(3, 3)

    theta = scalOP.dot(transOP)
    finalOP = theta.dot(a)
    return finalOP


```
While code in window2view.py


### 2D Tranformations
Translate,Rotate and Scale
using numpy ndarray 
only to calculate transforms
### driver code ->twoD.py
```markdown
def translate(x,y,a):
    return np.array([0,0,x,0,0,y,0,0,1]).reshape(3,3).dot(a)
def rotate(deg,a):
    return np.array([cos(deg),-sin(deg),0,sin(deg),cos(deg),0,0,0,1]).reshape(3,3).dot(a)
def scale(sx,sy,a):
    return np.array([sx,0,0,0,sy,0,0,0,1]).reshape(3,3).dot(a)

```


### DDA

```markdown
dy=y2-y
dx=x2-x
step=0.0
if abs(dx)>abs(dy):
    step=dx
else:
    step=dy
print(step)
xin=float(dx)/step
yin=float(dy)/step
print("inc x y ",xin,yin)
for i in range(step):
    x=x+xin
    y=y+yin
    print(x,y)
   
```

### Bresenhams
```markdown
dx=x2-x
dy=y2-y
dt=2*dy-2*dx
ds=2*dy
d=ds-dx
print("line ({},{}) and ({},{})\n dx {}\n dy {} \n dt {} \n ds {} \n d {}".format(x,y,x2,y2,dx,dy,dt,ds,d))
while(x<x2):
    x=x+1
    if d<0:
        d=d+ds
    else:
        y=y+1
        d=d+dt
    print("d:{} pt:({},{})".format(d,x,y))
    
```

