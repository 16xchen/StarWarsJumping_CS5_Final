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

from visual import *
import random


def make_walls():
    """ makes several walls and returns them in a list
        Docs here:  http://vpython.org/contents/docs/box.html
    """

    w0 = box(pos=(-20,0,0), axis=(0,0,1), 
             length=40, width=1, height = 2, color = (1, 0, 0))
    w1 = box(pos=(20,0,0), axis=(0,0,1), 
             length=40, width=1, height = 2, color=(1,0,0))
    list_of_walls = [ w0, w1 ]
    return list_of_walls


def make_alien():
    """ makes an alien! -- in the process, this shows how to
        group many objects into a single coordinate system ("frame")
        and treat that as a single object
        Docs here:  http://vpython.org/contents/docs/frame.html
    """
    alien = frame( pos=(10,0,-10) )  # makes a new "frame" == a container
    # with a local coordinate system that can have any number of parts...
    # here are the "parts":
    sphere( frame=alien, radius=1, color=color.green )
    sphere( frame=alien, radius=0.3, pos=(.7,.5,.2), color=color.white )
    sphere( frame=alien, radius=0.3, pos=(.2,.5,.7), color=color.white )
    cylinder( frame=alien, pos=(0,.9,-.2), axis=(.02,.2,-.02),  # the hat!
              radius=.7, color=color.magenta)
    return alien   # always use the _frame_, not any of its parts...




def main():
    """ this is the main function, including
        all of the data objects and the "event loop"
        which is the while True: loop that will
        be the universe's "time stream" :-)
    """

    

    # create an object named floor of class (type) box:
    floor = box(pos=(0,-1,0), length=40, width=40, height = 0.5, color=color.white, material = materials.texture(data=materials.loadTGA("cloud_city"), mapping="top") )

    # this creates a list of walls 
    Walls = make_walls()
    w0, w1 = Walls   # and gives each one a name...

    # color names? they are black, blue, cyan, green, gray(v), 0.0<=v<=1.0
    #                       magenta, orange, red, white, yellow
    # or you can use rgb tuples (from 0.0 to 1.0, not 0 to 255), e.g.,
    ball = sphere( radius=1, pos=(0,0,-20), color=(1,0.7,0.2) )
    ball.vel = vector(0,0,0)   # this is the "game piece" w/ zero starting vel.

    #player 2
    ball2 = sphere( radius=1, pos=(0,0,20), color=(1,0.7,0.2) )
    ball2.vel = vector(0,0,0)

    globe = sphere( radius=1, pos= (0, 0, 0,), color = (0, 1, 0))
    globe.vel = vector(0,0,-3)
    # We set some variables to control the display and the event loop
    RATE = 60             # number of loops per second to run, if possible!
    dt = 1.0/(1.0*RATE)   # the amount of time per loop (again, if possible)
    autocenter = True     # do you want vPython to keep the scene centered?

    # this is the main loop of the program! it's "time" or the "event loop"
    while True:
        rate(RATE)     # run no faster than RATE loops/second

        # +++++ start of all position updates: once per loop +++++ 

        ball.pos = ball.pos + ball.vel*dt           # PHYSICS!
        ball2.pos = ball2.pos + ball2.vel*dt
        globe.pos = globe.pos + globe.vel*dt


        # +++++ end of all once-per-loop position updates +++++ 




        # ----- start of other checks - especially *collisions* -----

        # collision check for the ball and globe...
        # vector docs:   http://vpython.org/contents/docs/vector.html
        vec_from_ball_to_globe = globe.pos - ball.pos
        if mag( vec_from_ball_to_globe ) < ball.radius + globe.radius:
            globe.pos = ball.pos + vec_from_ball_to_globe * (ball.radius + globe.radius)/mag( vec_from_ball_to_globe) #move the globe out of the ball
            globe.vel = vec_from_ball_to_globe * 5

        vec_from_ball2_to_globe = globe.pos - ball2.pos
        if mag( vec_from_ball2_to_globe ) < ball2.radius + globe.radius:
            globe.pos = ball2.pos + vec_from_ball2_to_globe * (ball2.radius + globe.radius)/mag( vec_from_ball2_to_globe) #move the globe out of the ball
            globe.vel = vec_from_ball2_to_globe * 5

        # need to handle wall collisions next...
        # here is an example of one wall collision - you'll need more!
        
        # ball colliding with wall 0, w0:
        if ball.pos.x < w0.pos.x + w0.width/2:  # w0 has the smallest x value
            ball.pos.x = w0.pos.x  # make sure we stay in bounds
            ball.vel.x = -1.0 * ball.vel.x   # bounce (in the x direction)
        
        # ball colliding with wall 1, w1
        if ball.pos.x > w1.pos.x - w1.width/2:
            ball.pos.x = w1.pos.x
            ball.vel.x *= -1

        # globe colliding with wall 0, w0
        if globe.pos.x < w0.pos.x + w0.width/2:  # w0 has the smallest x value
            globe.pos.x = w0.pos.x  # make sure we stay in bounds
            globe.vel.x *= -1 # bounce (in the x direction)
        
        #globe colliding with wall 1, w1
        if globe.pos.x > w1.pos.x -  w1.width/2:
            globe.pos.x = w1.pos.x
            globe.vel.x *= -1

        # ----- end of other checks - especially *collisions*  -----

        #did someone win?
        if globe.pos.z < -20:
            print("Tim wins!")
            ball.vel = vector(0,0,0)
            ball.pos = vector(0,0,-20)
            ball2.vel = vector(0,0,0)
            ball2.pos = vector(0,0,20)
            globe.vel = vector(0,0,-1)
            globe.pos = vector(0,0,0)
        elif globe.pos.z > 20:
            print("Tim wins!")
            ball.vel = vector(0,0,0)
            ball.pos = vector(0,0,-20)
            ball2.vel = vector(0,0,0)
            ball2.pos = vector(0,0,20)
            globe.vel = vector(0,0,-1)
            globe.pos = vector(0,0,0)





        # ===== handling user events: keypresses and mouse =====

        # here, we see if the user has pressed any keys
        if scene.kb.keys:   # any keypress to be handled?
            s = scene.kb.getkey()
            print "You pressed the key", s  

            # Key presses to give the ball velocity (in the x-z plane)
            dx = 2; dz = 1   # easily-changeable values
            if s == 'left': ball.vel += vector(-dx,0,0)
            if s == 'right': ball.vel += vector(dx,0,0)
            # if s == 'up': ball.vel += vector(0,0,-dz)
            # if s == 'down': ball.vel += vector(0,0,dz)

            if s == 'a': ball2.vel += vector(-dx,0,0)
            if s == 'd': ball2.vel += vector(dx,0,0)
            # if s == 'up': ball2.vel += vector(0,0,-dz)
            # if s == 'down': ball2.vel += vector(0,0,dz)

            # space to stop everything
            if s == ' ':  # space to stop things
                ball.vel = vector(0,0,0)
                alien.vel = vector(0,0,0)

            # capital R to reset things
            if s == 'R':
                ball.vel = vector(0,0,0)
                ball.pos = vector(0,0,-20)
                ball2.vel = vector(0,0,0)
                ball2.pos = vector(0,0,20)
                globe.vel = vector(0,0,-1)
                globe.pos = vector(0,0,0)

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







