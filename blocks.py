from visual import *
import random
import math

''' intializes blocks'''
def make_blocks():
    block1 = box(pos = (0,0,0), length=10, height=2, width=5, color=(0,1,0))
    block2 = box(pos = (0,0,0), length=10, height=2, width=5, color=(0,1,0))
    block3 = box(pos = (0,0,0), length=10, height=2, width=5, color=(0,1,0))
    block4 = box(pos = (0,0,0), length=10, height=2, width=5, color=(0,1,0))
    block5 = box(pos = (0,0,0), length=10, height=2, width=5, color=(0,1,0))
    block6 = box(pos = (0,0,0), length=10, height=2, width=5, color=(0,1,0))
    block7 = box(pos = (0,0,0), length=10, height=2, width=5, color=(0,1,0))
    block8 = box(pos = (0,0,0), length=10, height=2, width=5, color=(0,1,0))
    block9 = box(pos = (0,0,0), length=10, height=2, width=5, color=(0,1,0))
    block10 = box(pos = (0,0,0), length=10, height=2, width=5, color=(0,1,0))
    #block11 = box(pos = (0,0,0), length=10, height=2, width=5, color=(0,1,0))
    #block12 = box(pos = (0,0,0), length=10, height=2, width=5, color=(0,1,0))
    #block13 = box(pos = (0,0,0), length=10, height=2, width=5, color=(0,1,0))
    #block14 = box(pos = (0,0,0), length=10, height=2, width=5, color=(0,1,0))
    #block15 = box(pos = (0,0,0), length=10, height=2, width=5, color=(0,1,0))
    #block16 = box(pos = (0,0,0), length=10, height=2, width=5, color=(0,1,0))
    #block17 = box(pos = (0,0,0), length=10, height=2, width=5, color=(0,1,0))
    #block18 = box(pos = (0,0,0), length=10, height=2, width=5, color=(0,1,0))
    #block19 = box(pos = (0,0,0), length=10, height=2, width=5, color=(0,1,0))
    #block20 = box(pos = (0,0,0), length=10, height=2, width=5, color=(0,1,0))
    Blocks = [block1, block2, block3, block4, block5, block6, block7, block8, block9, block10] #block11, block12, block13, block14, block15, block16, block17, block18, block19, block20]
    return Blocks


def main():
    wall = box(pos=(0,0,-10), length=50, height=90, width = 0.5, color=color.white)

    Blocks = make_blocks()
    b1, b2, b3, b4, b5, b6, b7, b8, b9, b10 = Blocks #, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20 = Blocks

    gravity = 9.8
    RATE = 30             # number of loops per second to run, if possible!
    dt = 1.0/(1.0*RATE)   # the amount of time per loop (again, if possible)
    autocenter = True     # do you want vPython to keep the scene centered?

    speed_mult = 1
    newpos = (0,0,0)
    #initial positions and velocities
    for i in range(len(Blocks)):
        Blocks[i].pos = (random.randint(-25, 25), 15*(i-3), 0)
        Blocks[i].vel = vector(0,0,0)

    print(type(Blocks[i].vel))
    poslist = []

    print(dt)
    print(Blocks[i].vel*dt)
    while True:
        rate(RATE)

        #physics
        for i in range(len(Blocks)):
            Blocks[i].pos = Blocks[i].pos + Blocks[i].vel*dt


        for i in range(len(Blocks)):
            poslist += [Blocks[i].pos.y]
            if Blocks[i].vel.y < 0: Blocks[i].vel.y = Blocks[i].vel.y + gravity*dt

        if max(poslist) < 90: 
            Blocks[minpos(Blocks)].pos = vector(random.randint(-25, 25), 105, 0)

        poslist = []

        if scene.kb.keys:   # any keypress to be handled?
            s = scene.kb.getkey()
            print "You pressed the key", s
            if s == ' ':
                for b in Blocks:
                    b.vel = vector(0,-20,0)



def minpos(L):
    minlist = []
    for i in range(len(L)):
        minlist += [L[i].pos.y]
    for i in range(len(L)):
        if L[i].pos.y == min(minlist): return i

# This should be the FINAL thing in the file...
if __name__ == "__main__":
    main()  # did we just RUN this file?
                     # if so, we call main()
