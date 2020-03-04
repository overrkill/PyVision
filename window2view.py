from graphics import *
from numpy import *


def draw(wrx, wry, wlx, wly, vrx, vry, vlx, vly, a, b, c, x, y, z):

    # initialization
    win = GraphWin("window to viewport", 500, 500)

    # window

    window = Rectangle(Point(wrx, wry), Point(wlx, wly))
    window.setFill("gray")
    window.draw(win)

    # viewport

    view = Rectangle(Point(vlx, vly), Point(vrx, vry))
    view.setFill("blue")
    view.draw(win)

    # points
    p1 = Point(a[0][0], a[1][0])
    p2 = Point(b[0][0], b[1][0])
    p3 = Point(c[0][0], c[1][0])
    p4 = Point(x[0][0], x[1][0])
    p5 = Point(y[0][0], y[1][0])
    p6 = Point(z[0][0], z[1][0])

    # objects from points
    obj = Polygon(p1, p2, p3)
    obj2 = Polygon(p4, p5, p6)
    obj.draw(win)
    obj.setFill("red")
    obj2.draw(win)
    obj2.setFill("yellow")

    # closing

    win.getMouse()
    win.close()


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


if __name__ == "__main__":
    # original coordinates of te 2d object

    alpha = array([150, 150, 1]).reshape(3, 1)
    beta = array([250, 150, 1]).reshape(3, 1)
    gamma = array([200, 200, 1]).reshape(3, 1)

    # window to viewport transformation

    a1 = w2v(100, 100, 300, 300, 0, 0, 100, 100, alpha)
    b1 = w2v(100, 100, 300, 300, 0, 0, 100, 100, beta)
    c1 = w2v(100, 100, 300, 300, 0, 0, 100, 100, gamma)
    print("original \n{}\n{}\n{} \n ported \n{}\n{}\n{}".format(alpha, beta, gamma, a1, b1, c1))

    # drawing with all transformed coordinates as well original to show the transformation

    draw(100, 100, 300, 300, 0, 0, 100, 100, alpha, beta, gamma, a1, b1, c1)