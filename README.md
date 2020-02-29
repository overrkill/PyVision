## Computer Vision Alogirthms and their implementation in Python2

view the code (https://github.com/overrkill/PyVision)

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
