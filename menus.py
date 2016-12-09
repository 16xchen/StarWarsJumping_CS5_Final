from visual import *

def introMenu():
    """displays an intro menu. Prompts the user to press a key.
    If that key is 'g', returns True for grutor mode."""

    autoscale = False
    #construct the menu
    menu = box(pos=(0,0,-10), up=(0,0,1), length=90, width=90, height = 0.5, color=color.white, material = materials.texture(data=materials.loadTGA("introMenu"), mapping="top") )
    
    while True:
        rate(30)
        if scene.kb.keys:   # any keypress to be handled?
            s = scene.kb.getkey()
            print "You pressed the key", s  
            if s == 'g':
                return True
            else:
                return False