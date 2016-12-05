#
# billiard_bounce.py
#
# starting file for the game in Lab 11 (hw11pr1.zip)
#
# If you enjoy vPython, you might consider it as a final project...
#   docs: http://vpython.org/contents/docs/index.html
#   gallery of shapes: http://vpython.org/contents/docs/primitives.html
#
# Name:
#

from characters import *
from visual import *
import random
import math

def make_walls():
    """ makes several walls and returns them in a list
        Docs here:  http://vpython.org/contents/docs/box.html
    """
    w0 = box(pos=(25,0,0), axis=(0,0,1), 
             length=90, width=1, height = 2, color=color.red)
    w1 = box(pos=(0,0,45), axis=(1,0,0), 
             length=50, width=1, height = 2, color=(1,0,0))
    w2 = box(pos=(-25,0,0), axis=(0,0,1), 
             length=90, width=1, height = 2, color=(1,0,0))
    w3 = box(pos=(0,0,-45), axis=(1,0,0), 
             length=50, width=1, height = 2, color=(1,0,0))
    list_of_walls = [w0, w1, w2, w3]
    return list_of_walls

def make_balls():
    b1 = sphere( radius=1, pos=(0,0,-20), color=(1,0.9647,0.56) )
    b2 = sphere( radius=1, pos=(-1,0,-20-sqrt(2)), color=(0.596,0.96,1) )
    b3 = sphere( radius=1, pos=(1,0,-20-sqrt(2)), color=(1,0.412,0.7) )
    b4 = sphere( radius=1, pos=(-2,0,-20-2*sqrt(2)), color=(0.87843,0.4,1) )
    b5 = sphere( radius=1, pos=(0,0,-20-2*sqrt(2)), color=(1,0.647,0) )
    b6 = sphere( radius=1, pos=(2,0,-20-2*sqrt(2)), color=(0.67843,1,0.1843) )
    b7 = sphere( radius=1, pos=(-3,0,-20-3*sqrt(2)), color=(0.957,0.643,0.37647) )
    b8 = sphere( radius=1, pos=(-1,0,-20-3*sqrt(2)), color=(0,0,0) )
    b9 = sphere( radius=1, pos=(1,0,-20-3*sqrt(2)), color=(0.8549,0.647,0.1255) )
    b10 = sphere( radius=1, pos=(3,0,-20-3*sqrt(2)), color=(0,0,0.5) )
    b11 = sphere( radius=1, pos=(-4,0,-20-4*sqrt(2)), color=(0.545,0.145,0) )
    b12 = sphere( radius=1, pos=(-2,0,-20-4*sqrt(2)), color=(0.47843,0.2157,0.545) )
    b13 = sphere( radius=1, pos=(0,0,-20-4*sqrt(2)), color=(0.8,0.4,0) )
    b14 = sphere( radius=1, pos=(2,0,-20-4*sqrt(2)), color=(0,0.545,0) )
    b15 = sphere( radius=1, pos=(4,0,-20-4*sqrt(2)), color=(0.545,0.27,0.0745) )
    c1 = sphere( radius=1, pos=(0,0,20), color=(1,1,1) )
    list_of_balls = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, c1]
    return list_of_balls

def make_holes():
    h1 = cylinder(radius=2, pos=(25,0,45), axis=(0,-1,0), color=(0,0,0) )
    h2 = cylinder(radius=2, pos=(25,0,-45), axis=(0,-1,0), color=(0,0,0) )
    h3 = cylinder(radius=2, pos=(-25,0,45), axis=(0,-1,0), color=(0,0,0) )
    h4 = cylinder(radius=2, pos=(-25,0,-45), axis=(0,-1,0), color=(0,0,0) )
    h5 = cylinder(radius=2, pos=(25,0,0), axis=(0,-1,0), color=(0,0,0) )
    h6 = cylinder(radius=2, pos=(-25,0,0), axis=(0,-1,0), color=(0,0,0) )
    list_of_holes = [h1,h2,h3,h4,h5,h6]
    return list_of_holes

def sign(a, b):
    if(a <= 0 and b <= 0 or a >= 0 and b >= 0): return True
    return False

def main():
    """ this is the main function, including
        all of the data objects and the "event loop"
        which is the while True: loop that will
        be the universe's "time stream" :-)
    """
    r2=R2D2(scale=1.5, pos=vector(0,0,0))
    power = 0
    # create an object named floor of class (type) box:
    floor = box(pos=(0,-1,0), length=50, width=90, height = 0.5, color=color.white, material = materials.texture(data=materials.loadTGA("cloud_city"), mapping="top") )

    # this creates a list of walls 
    Walls = make_walls()
    w0, w1, w2, w3 = Walls   # and gives each one a name...

    holes = make_holes()
    h1, h2, h3, h4, h5, h6 = holes

    #creating stripes texture
    #stripes = ((1,0,0,1),(1,0,0,1),(1,0,0,1),(1,0,0,1))
    #stripes_tex = materials.texture(data=stripes, mapping="spherical", interpolate=False)

    # color names? they are black, blue, cyan, green, gray(v), 0.0<=v<=1.0
    #                       magenta, orange, red, white, yellow
    # or you can use rgb tuples (from 0.0 to 1.0, not 0 to 255), e.g.,
    balls = make_balls()
    b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, c1 = balls
    solids = b1, b2, b3, b4, b5, b6, b6, b7
    stripes = b9, b10, b11, b12, b13, b14, b15

    p1score = label(pos=(0,10,10), text = "0")
    p2score = label(pos=(0,10,-10), text = "0")

    #b3 = sphere( radius=1, pos=(0,0,0), color=(1,1,1), material=stripes_tex )
    
    #initialize velocities
    for i in range(len(balls)):
        balls[i].vel = vector(0,0,0)

    cue = frame(pos = c1.pos)
    dot = sphere(frame=cue, radius = .001, pos=(0,0,0), color = (0,0,0), visible = False)
    stick = cylinder(frame=cue, radius=.2, pos=(0,1,5), axis=(0,5,30), color=(0,1,0) )

    num_balls_out = []
    #b1.vel = vector(0,0,0)   # this is the "game piece" w/ zero starting vel.
    #b2.vel = vector(0,0,0)
    # We set some variables to control the display and the event loop
    RATE = 30             # number of loops per second to run, if possible!
    dt = 1.0/(1.0*RATE)   # the amount of time per loop (again, if possible)
    autocenter = True     # do you want vPython to keep the scene centered?

    #initialize prevpos
    prevpos = [vector(0,0,0)]*len(balls)
    for i in range(len(balls)):
        prevpos[i] = balls[i].pos
    # this is the main loop of the program! it's "time" or the "event loop"
    while True:
        robot=r2.build()
        rate(RATE)     # run no faster than RATE loops/second

        # +++++ start of all position updates: once per loop +++++ 
        #PHYSICS!
        for i in range(len(balls)):
            if mag(balls[i].vel) < 0.3: balls[i].vel = vector(0,0,0)
            balls[i].pos = balls[i].pos + balls[i].vel*dt
        
        totvel = vector(0,0,0)
        for b in balls: totvel += b.vel
        
        if(power == 0 and totvel == (0,0,0)):
            cue.pos = c1.pos
        # +++++ end of all once-per-loop position updates +++++ 




        # ----- start of other checks - especially *collisions* -----

        # collision check for the b1 and alien...
        # vector docs:   http://vpython.org/contents/docs/vector.html
        
        # need to handle wall collisions next...
        # here is an example of one wall collision - you'll need more!

        #handling collisions with wall and holes
        for i in range(len(balls)):
            if math.fabs(balls[i].pos.x) > w0.pos.x - w0.width:
                balls[i].pos = prevpos[i]
                balls[i].vel.x = -1*balls[i].vel.x
            if math.fabs(balls[i].pos.z) > w1.pos.z - w1.width:
                balls[i].pos = prevpos[i]
                balls[i].vel.z = -1*balls[i].vel.z
            for h in holes:
                hole_vect = h.pos - balls[i].pos
                if mag(hole_vect) < h.radius:
                    balls[i].pos = (-30, 0, -50 + len(num_balls_out)*2*balls[i].radius)
                    num_balls_out += [i]

        for i in num_balls_out:
            balls.pop(i)

        num_balls_out = []      

        '''if math.fabs(b1.pos.x) > w0.pos.x - w0.width:
            b1.pos = b1prevpos
            b1.vel.x = -1*b1.vel.x
        if math.fabs(b1.pos.z) > w1.pos.z - w1.width:
            b1.pos = b1prevpos
            b1.vel.z = -1*b1.vel.z

        #handling collisions with wall
        if math.fabs(b2.pos.x) > w0.pos.x - w0.width:
            b2.pos = b2prevpos
            b2.vel.x = -1*b2.vel.x
        if math.fabs(b2.pos.z) > w1.pos.z - w1.width:
            b2.pos = b2prevpos
            b2.vel.z = -1*b2.vel.z'''

        #handling collisions between balls
        for i in range(len(balls)):
            for k in range(i,len(balls)):
                dist_vect = balls[i].pos - balls[k].pos
                if(mag(dist_vect) < 2*balls[i].radius and i != k):
                    #print('collision!')
                    #calculate pos
                    move_vect = -dist_vect
                    move_vect.mag = 2*balls[i].radius
                    balls[i].pos = balls[k].pos - move_vect
                    #balls[i].pos = prevpos[i]
                    #balls[k].pos = prevpos[k]
                    rel_vel = balls[i].vel - balls[k].vel
                    #print(rel_vel)
                    b2_vel = proj(rel_vel, dist_vect)
                    #print('b2_vel: ', b2_vel)
                    b1_vel = rel_vel - b2_vel
                    temp = balls[k].vel
                    #print('temp: ', temp)
                    balls[i].vel = b1_vel + temp
                    #print('b1vel: ', balls[i].vel)
                    balls[k].vel = b2_vel + temp
                    #print('b2vel: ', balls[k].vel)

        for i in range(len(balls)):
            fric_vect = balls[i].vel
            fric_vect.mag = balls[i].vel.mag*0.99
            balls[i].vel = fric_vect
        


        '''b1_b2 = b1.pos - b2.pos
        if(mag(b1_b2) < 2*b1.radius):
            b1.pos = b1prevpos
            b2.pos = b2prevpos
            rel_vel = b1.vel - b2.vel
            b2_vel = proj(rel_vel, b1_b2)
            b1_vel = rel_vel - b2_vel
            temp = b2.vel
            b1.vel = b1_vel + temp
            b2.vel = b2_vel + temp'''

        # ----- end of other checks - especially *collisions*  -----

        for i in range(len(balls)):
            prevpos[i] = balls[i].pos
        #b1prevpos = b1.pos
        #b2prevpos = b2.pos


        # ===== handling user events: keypresses and mouse =====

        # here, we see if the user has pressed any keys
        if scene.kb.keys:   # any keypress to be handled?
            s = scene.kb.getkey()
            print "You pressed the key", s  

            # Key presses to give the b1 velocity (in the x-z plane)
            dx = .5; dz = .5   # easily-changeable values
            '''if s == 'left': c1.vel += (0,0,-dx)
            if s == 'right': c1.vel += (0,0,dx)
            if s == 'up': c1.vel += (0,0,-dz)
            if s == 'down': c1.vel += (0,0,dz)'''
            if s == 'left' and totvel == (0,0,0): cue.rotate(angle=-0.1,axis=(0,1,0))
            if s == 'right'and totvel == (0,0,0): cue.rotate(angle=0.1,axis=(0,1,0))
            if s == 'up':
                stick.pos -= (0,0.16667,1)
                power -= 1
            if s == 'down':
                power += 1
                stick.pos += (0,0.16667,1)
            # space to hit
            if s == ' ' and power > 0:
                c1.vel = cue.axis.rotate(angle=math.pi/2,axis=(0,1,0))
                c1.vel.mag = power*3
                power = 0
                stick.pos = (0,1,5)
                

            #if s == 'a': b2.vel += vector(-dx,0,0)
            #if s == 'd': b2.vel += vector(dx,0,0)
            #if s == 'w': b2.vel += vector(0,0,-dz)
            #if s == 's': b2.vel += vector(0,0,dz)

            


            # capital R to reset things
            if s == 'r':
                b1.vel = vector(0,0,0)
                b1.pos = vector(10,0,0)
                b2.vel = vector(0,0,0)
                b2.pos = vector(-10,0,0)

            if s == 'Q':  # Quit!
                print "Quitting..."
                break  # breaks out of the main loop

            # mouse is better handled only when a particular key is pressed
            # see http://vpython.org/contents/docs/mouse.html for more

        # ===== end of handling user events: keypresses and mouse =====

    print "Done with the main loop. Ending this vPython session..."
    print "Close the vPython window to finish."
# this ends the main() function - it tends to get large!


# This should be the FINAL thing in the file...
if __name__ == "__main__":   # did we just RUN this file?
    main()                   # if so, we call main()







