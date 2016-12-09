from characters import *
from blocks import *
from menus import *

def main():
    """The main loop of the starjump.py game"""
    #set scene parameters
    RATE = 30             # number of loops per second to run, if possible!
    dt = 1.0/(2.0*RATE)   # the amount of time per loop (again, if possible)
    gravity = 9.8
    # the camera does not move.
    scene.width=800
    scene.height=800
    scene.range = 42
    scene.autocenter = False    
    scene.autoscale = False
    scene.userzoom = False
    scene.userspin = False

    #display the initial menu, and get whether the user is a grutor (if they enter 'g')
    isGrutor = introMenu()

    #if the user is in grutor mode, create a BB8. Otherwise, create an R2D2.
    if(isGrutor):
        player = build_BB8(scale=1.0, pos=vector(0,3,0))
    else:
        player = build_R2D2(scale=2.0, pos=vector(0,3,0))
    
    player.vel=vector(0,0,0)

    #construct the game
    wall = box(pos=(0,0,-10), length=90, height=0.5, width = 90, up=(0,0,1), color=color.white, material = materials.texture(data=materials.loadTGA("cloud_city"), mapping="top"))
    Blocks = make_blocks()
    b1, b2, b3, b4, b5, b6, b7, b8, b9, b10 = Blocks

    #KINEMATICS, KINEMATICS, IM A KINEMATICS ADDICT
    speed_mult = 1
    newpos = (0,0,0)
    #initial positions and velocities
    for i in range(len(Blocks)):
        Blocks[i].pos = (random.randint(-25, 25), 15*(i-3), 0)
        Blocks[i].vel = vector(0,-30,0)

    print(type(Blocks[i].vel))

    poslist = [] #declare a list of heights of the blocks.

    print(dt)
    print(Blocks[i].vel*dt)

    score = 0

        #physics loop
    while True:
        rate(RATE)

        if player.pos.y < 50:
            print("DEATH!!")

        #move the robot.
        player.pos = player.pos + player.vel 
        player.vel.y -= 0.3 * gravity * dt

        #move the blocks
        for i in range(len(Blocks)):
            Blocks[i].pos = Blocks[i].pos + Blocks[i].vel*dt
        
        for i in range(len(Blocks)):
            poslist += [Blocks[i].pos.y] #populate a list with the heights of the blocks
            if Blocks[i].vel.y < 0: Blocks[i].vel.y = Blocks[i].vel.y + gravity*dt #if the block is moving, accelerate it.
            #note: gravity is +9.8 upwards.
        
        #when the top block enters the viewing range, teloport the lowest block to the top.
        if max(poslist) < 90: 
            Blocks[minpos(Blocks)].pos = vector(random.randint(-25, 25), 105, 0)


        if(fellOnBlock(player, Blocks, poslist)):
            score += 1
            print(score)
            player.vel = vector(0, 1.5, 0)
            for b in Blocks:
                b.vel = vector(0, -30, 0)

        #USER INPUT FOR MOTION
        if scene.kb.keys:   # any keypress to be handled?
            s = scene.kb.getkey()
            print "You pressed the key", s

            if s == 'left': #move left
                if player.vel.x > 0:
                    player.vel.x = -0.1 #moving right? arrest your motion before going left.
                else: 
                    player.vel.x = -0.8
            if s == 'right': #move right
                if player.vel.x < 0:
                    player.vel.x = 0.1 #moving left? arrest your motion before going right.
                else: 
                    player.vel.x = 0.8
        else:
            #slow down the robot's lateral velocity.
            player.vel.x *= 0.95
        
        #clear poslist for next time.
        poslist = []






if __name__ == "__main__":   # did we just RUN this file?
    main()                   # if so, we call main()