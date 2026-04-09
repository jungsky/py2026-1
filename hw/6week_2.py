import random
from tkinter.simpledialog import *

def getString():
    restr = ''
    restr = askstring('문자열 입력', "거북이 쓸 문자열을 입력")
    return restr

def getRGB():
    r = g = b = 0
    r = random.random()
    g = random.random()
    b = random.random()
    return(r, g, b)

def setXYAS(sw, sh):
    X = Y = angle = size =0
    X = random.randrange(-sw/2, sw/2)
    Y = random.randrange(-sh/2, sh/2)
    angle = random.randrange(0, 360)
    size = random.randrange(10, 50)
    return(X, Y, angle, size)