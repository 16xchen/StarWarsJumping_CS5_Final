
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
        
        cylinder(frame=r2, axis=(0,0.2*scale,0),radius=radius+offset/2.0, color=color.blue, pos=(0,1.25*height,0))
        sphere(frame=r2, radius=radius, pos=(0,height+size.y,0),color=color.gray(0.8),
        material=materials.shiny)
        box(frame=r2, length=0.7*scale, width=1*scale, height=height, pos=(width/2.0,offset+height/2.0,0), color=color.white)
        box(frame=r2, length=0.7*scale, width=1*scale, height=height, pos=(-width/2.0,offset+height/2.0,0), color=color.white)
        cylinder(frame=r2, pos=((width/2.0)-(0.5*0.7*scale),height,0), axis=(1.02*0.7*scale,0,0),radius=0.8*scale, color=color.white)
        cylinder(frame=r2, pos=(-((width/2.0)+(0.5*0.7*scale)),height,0), axis=(1.01*0.7*scale,0,0),radius=0.8*scale, color=color.white)        
        g = shapes.gear(n=12,radius=radius+offset/2.0, addendum=0, dedendum=0.5*scale, phi=10)
        extrusion(frame=r2, pos=[(0,height+radius/1.3,0),(0,height+1.05*radius,0)], shape=g, color=color.blue)
        
        #the little black camera thing
        cylinder(frame=r2, pos=(radius/3.0,1.35*height,0), axis=(0,0,2),radius=0.2*scale, color=color.black)     
        
        #the center thing
        tr=paths.trapezoid(pos=(0,0), width=1.1*scale, height=1*scale, top=0.8*scale)   
        extrusion(frame=r2, pos=[(0,height+0.75*radius,0),(0,height+1.12*radius,1.8*scale)], shape=tr, color=color.blue)
        #the "eye"
        sphere(frame=r2, radius=0.3*scale, pos=(0,height+1.12*radius,radius),color=color.black, material=materials.shiny)        
        p = paths.circle(pos=(0,height+radius*1.25,0), radius=radius/4.0)
        cr = shapes.circle(radius=radius/2.0, np=64,angle1=0, angle2=pi/2 )
        extrusion(frame=r2, pos=p, shape=cr, color=color.blue)
        return r2   

def main():
    r2=R2D2(scale=1.0)
    print(r2)
    robot=r2.build()
    while True:  # time loop!
        rate(10)

# This calls main when the file is run...
if __name__ == "__main__":
    main() 
