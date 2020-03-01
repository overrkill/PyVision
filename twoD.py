from graphics import *
from math import *
import numpy as np
#a=np.array([1,2,3,4]).reshape(2,2)
#b=np.array([1,2,3,4]).reshape(2,2)
#print(b.dot(a))
def translate(x,y,a):
    return np.array([0,0,x,0,0,y,0,0,1]).reshape(3,3).dot(a)
def rotate(deg,a):
    return np.array([cos(deg),-sin(deg),0,sin(deg),cos(deg),0,0,0,1]).reshape(3,3).dot(a)
def scale(sx,sy,a):
    return np.array([sx,0,0,0,sy,0,0,0,1]).reshape(3,3).dot(a)
if __name__=="__main__":
    a=np.array([1,2,1]).reshape(3,1)
    print("Original coords \n{}".format(a))
    print("translated coords \n{}".format(translate(2,3,a)))
    print("roatation \n{}".format(rotate(60,a)))
    print("scale \n{}".format(scale(2,4,a)))
    
"""
overkill@overkill-pc:~/Desktop/cv$ python twoD.py 
Original coords 
[[1]
 [2]
 [1]]
translated coords 
[[2]
 [3]
 [1]]
roatation 
[[-0.34279174]
 [-2.20963658]
 [ 1.        ]]
scale 
[[2]
 [8]
 [1]]
"""