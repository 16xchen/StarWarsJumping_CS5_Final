
from visual import *
class Characters(object):
    def __init__(self, Name, scale, pos=vector(0,0,0)):
        self.scale=scale
        self.pos=pos
        self.Name=Name
    
    def __repr__(self):
        return self.Name+" of size "+str(self.scale)+" at "+str(self.pos)
    



class R2D2(Characters):
    def __init__(self, scale=1.0, pos=vector(0,0,0), Name="R2D2"):
        self.scale=scale
        self.pos=pos
        self.Name=Name

    def build(self):
        scale=self.scale
        size=vector(1.8,1.5,2.3)*scale
        width=4.0*scale
        offset=0.1*scale
        radius=(width/2.0)-offset
        height=radius*2.5
        r2 = frame(pos=self.pos) 
        x=self.pos.x
        y=self.pos.y
        z=self.pos.z
        midfoot=pyramid(frame=r2, size=size,axis=(0,1,0))
        leftfoot=pyramid(frame=r2, size=size, pos=(width/2.0,0,0),axis=(0,1,0))
        rightfoot=pyramid(frame=r2, size=size, pos=(-width/2.0,0,0),axis=(0,1,0))
        cylinder(frame=r2, axis=(0,height,0),radius=radius, color=color.white, pos=(0,size.y-2*offset,0))
        sphere(frame=r2, radius=radius, pos=(0,height+size.y,0),color=color.gray(0.8),
        material=materials.shiny)
        box(frame=r2, length=0.7*scale, width=1*scale, height=height, pos=(width/2.0,offset+height/2.0,0), color=color.white)
        box(frame=r2, length=0.7*scale, width=1*scale, height=height, pos=(-width/2.0,offset+height/2.0,0), color=color.white)
        cylinder(frame=r2, pos=((width/2.0)-(0.5*0.7*scale),height,0), axis=(1.02*0.7*scale,0,0),radius=0.8*scale, color=color.blue)
        cylinder(frame=r2, pos=(-((width/2.0)+(0.5*0.7*scale)),height,0), axis=(1.01*0.7*scale,0,0),radius=0.8*scale, color=color.blue)
        return r2   # always use 



def main():
    r2=R2D2(scale=1.0)
    print(r2)
    robot=r2.build()
    while True:  # time loop!
        rate(10)

# This calls main when the file is run...
if __name__ == "__main__":
    main() 
