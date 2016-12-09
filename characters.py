
from visual import *
from blocks import *

def flame(r2d2, scale):
    width=getWdith(r2d2)
    flame=frame(pos=item.pos)
    mid=cone(frame=flame,pos=(0,0,0),  axis=(0,-1.5*scale,0),radius=0.5, color=color.red)
    left=cone(frame=flame, pos=(width/2.0,0,0),axis=(0,-1.5*scale,0), radius=0.5*scale, color=color.red)
    right=cone(frame=flame, pos=(-width/2.0,0,0),axis=(0,-1.5*scale,0), radius=0.5*scale, color=color.red)
    return flame
        


def build_R2D2(pos=vector(0,0,0), scale=1):
    size=vector(1.8,1.5,2.3)*scale
    width=4.0*scale
    offset=0.1*scale
    radius=(width/2.0)-offset
    height=radius*2.5
    r2 = frame(pos=pos) 
    x=pos.x
    y=pos.y
    z=pos.z

        #basic body structure
    midfoot=pyramid(frame=r2, size=size,axis=(0,1,0), material=materials.shiny, make_trail=True)
    leftfoot=pyramid(frame=r2, size=size, pos=(width/2.0,0,0),axis=(0,1,0), material=materials.shiny)
    rightfoot=pyramid(frame=r2, size=size, pos=(-width/2.0,0,0),axis=(0,1,0), material=materials.shiny)
    cylinder(frame=r2, axis=(0,height,0),radius=radius, color=color.white, pos=(0,size.y-2*offset,0), material=materials.shiny)
        
    cylinder(frame=r2, axis=(0,0.2*scale,0),radius=radius+offset/2.0, color=color.blue, pos=(0,1.25*height,0))
    sphere(frame=r2, radius=radius, pos=(0,height+size.y,0),color=color.gray(0.8),
    material=materials.shiny)
    box(frame=r2, length=0.7*scale, width=1*scale, height=height, pos=(width/2.0,offset+height/2.0,0), color=color.white, material=materials.shiny)
    box(frame=r2, length=0.7*scale, width=1*scale, height=height, pos=(-width/2.0,offset+height/2.0,0), color=color.white, material=materials.shiny)
    g = shapes.gear(n=12,radius=radius+offset/2.0, addendum=0, dedendum=0.5*scale, phi=10)
    extrusion(frame=r2, pos=[(0,height+radius/1.3,0),(0,height+1.05*radius,0)], shape=g, color=color.blue)
        
        #the little black camera thing
    cylinder(frame=r2, pos=(radius/2.2,1.35*height,0), axis=(0,0,2*scale),radius=0.2*scale, color=color.black)     
        
        #the center thing
    tr=paths.trapezoid(pos=(0,0), width=1.1*scale, height=1*scale, top=0.8*scale)   
    extrusion(frame=r2, pos=[(0,height+0.75*radius,0),(0,height+1.12*radius,1.8*scale)], shape=tr, color=color.blue)
        #the "eye"
    sphere(frame=r2, radius=0.3*scale, pos=(0,height+1.12*radius,radius),color=color.black, material=materials.shiny)              
    cylinder(frame=r2, pos=(radius/4,1.35*height,0), axis=(0,0,2*scale),radius=0.15*scale, color=color.red)     

        #his tophat
    p = paths.circle(pos=(0,height+radius*1.25,0), radius=radius/4.0)
    cr = shapes.circle(radius=radius/2.0, np=64,angle1=0, angle2=pi/2 )
    extrusion(frame=r2, pos=p, shape=cr, color=color.blue)

        #body details....
    ar = paths.arc(radius=radius, angle1=8*pi/6, angle2=10*pi/6, pos=(0,height*1.2,0))
    rt = shapes.rectangle(width=0.2*scale, height=0.2*scale)
    extrusion(frame=r2, pos=ar, shape=rt, color=color.blue)

    ar2 = paths.arc(radius=radius, angle1=8*pi/6, angle2=10*pi/6, pos=(0,height*1.125,0))
    extrusion(frame=r2, pos=ar2, shape=rt, color=color.blue)

    ar3 = paths.arc(radius=radius, angle1=8*pi/6, angle2=10*pi/6, pos=(0,height*1.05,0))
    extrusion(frame=r2, pos=ar3, shape=rt, color=color.blue)

    button_frame = shapes.rectangle(width=0.2*scale, height=1.6*scale)
    ar4 = paths.arc(radius=radius, angle1=11.5*pi/8, angle2=12.5*pi/8, pos=(0,height*0.8,0))
    extrusion(frame=r2, pos=ar4, shape=button_frame, color=color.blue)

    button1 = shapes.rectangle(width=0.5*scale, height=0.6*scale,roundness=0.2)
    extrusion(frame=r2, pos=[(0,height*0.88,radius), (0,height*0.88,radius+0.1*scale)], shape=button1, color=color.gray(0.7))
    extrusion(frame=r2, pos=[(0,height*0.72,radius), (0,height*0.72,radius+0.1*scale)], shape=button1, color=color.gray(0.7))

    button_frame2 = shapes.rectangle(width=0.2*scale, height=0.8*scale)
    ar5 = paths.arc(radius=radius, angle1=11.5*pi/8, angle2=12.5*pi/8, pos=(0,height*0.45,0))
    extrusion(frame=r2, pos=ar5, shape=button_frame2, color=color.blue)
    extrusion(frame=r2, pos=[(0,height*0.45,radius), (0,height*0.45,radius+0.1*scale)], shape=button1, color=color.gray(0.7))
        

        #arm details...
    cylinder(frame=r2, pos=((width/2.0)-(0.5*0.7*scale),height,0), axis=(0.7*scale,0,0),radius=0.8*scale, color=color.white, material=materials.shiny)
    cylinder(frame=r2, pos=(-((width/2.0)+(0.5*0.7*scale)),height,0), axis=(0.7*scale,0,0),radius=0.8*scale, color=color.white, material=materials.shiny)        
    shoulder_l=shapes.circle(radius=0.8*scale)
    shoulder_inner=shapes.circle(radius=0.25*scale)
    extrusion(frame=r2, pos=[(-((width/2.0)+(0.5*0.7*scale)),height,0),(-((width/2.0)+(0.5*1*scale)),height,0)], 
    shape=shoulder_l-shoulder_inner, color=color.white,material=materials.shiny)
    extrusion(frame=r2, pos=[(((width/2.0)+(0.5*0.7*scale)),height,0),(((width/2.0)+(0.5*1*scale)),height,0)], 
    shape=shoulder_l-shoulder_inner, color=color.white, material=materials.shiny)

    sleeve=shapes.rectangle(width=0.35*scale, height=height*0.65)
    pads=shapes.rectangle(width=0.4*scale, height=0.6*scale, roundness=0.3)
    extrusion(frame=r2, pos=[(width/2.0,height*0.88,0),(width/1.55,height*0.88,0)], shape=pads, color=color.blue)
    extrusion(frame=r2, pos=[(-width/2.0,height*0.88,0),(-width/1.55,height*0.88,0)], shape=pads, color=color.blue)


    extrusion(frame=r2, pos=[(width/2.0,offset+height/2.0,0),(width/1.6,offset+height/2.0,0)], shape=sleeve, color=color.blue, material=materials.shiny)
    extrusion(frame=r2, pos=[(-width/2.0,offset+height/2.0,0),(-width/1.6,offset+height/2.0,0)], shape=sleeve, color=color.blue)
    return r2   



def build_BB8(pos=vector(0,0,0), scale=1):
    bb8= frame(pos=pos) 
    radius=4.0*scale
    offset=0.1*scale
    sphere(radius=radius, material=materials.shiny)
    circle = shapes.circle(radius=1.8*scale, angle1=0, angle2=pi) 
    rotation = paths.arc(radius=0.1*scale, angle2=2*pi,pos=(0,radius+0.3,0))
    extrusion(pos=rotation,shape=circle, frame=bb8, material=materials.shiny)
        
    cr_path = paths.circle(radius=0.1*scale,pos=(0,radius,0))
    tr=shapes.trapezoid(width=radius*0.65, height=0.3*scale, top=radius*0.91)
    extrusion(pos=cr_path,shape=tr, frame=bb8, color=color.white)
        
    rect=shapes.rectangle(width=radius*0.9, height=0.1*scale)
    cr_path = paths.circle(radius=0.15*scale,pos=(0,radius*1.06,0))
    extrusion(pos=cr_path,shape=rect, frame=bb8, color=color.gray(0.5), material=materials.shiny)

        #head details
        #the camera/lights
    sphere(radius=0.4*scale, pos=(0,radius*1.3,1.8*scale), color=color.black, material=materials.shiny)
            
    bigcover = shapes.circle(radius=radius*0.109, thickness=0.08*scale)
    extrusion(pos=[(0,radius*1.295,1.7*scale), (0,radius*1.31,1.82*scale)],shape=bigcover, frame=bb8, color=color.gray(0.2))
       
    sphere(radius=0.1*scale, pos=(0.7*scale,radius*1.2,1.95*scale), color=color.blue, material=materials.shiny)
        
    cover = shapes.circle(radius=0.115*scale, thickness=0.05*scale)
    extrusion(pos=[(0.7*scale,radius*1.2,1.8*scale), (0.7*scale,radius*1.2,1.9*scale)],shape=cover, frame=bb8, color=color.gray(0.2))

    ring = shapes.circle(radius=0.25*scale, thickness=0.05*scale)
    extrusion(pos=[(0.7*scale,radius*1.2,1.8*scale), (0.7*scale,radius*1.2,1.85*scale)],shape=ring, frame=bb8, color=color.black, material=materials.shiny)

    bar=shapes.rectangle(height=0.2*scale, width=0.1*scale)


    for i in range(0,24*8):
        if i%3==1:
            angle1=i*pi/(12*8)
            angle2=(i+1)*pi/(12*8)
            barcode_arc=paths.arc(radius=1.85*scale, angle1=angle1, angle2=angle2, pos=(0,radius*1.105,0))
            extrusion(pos=barcode_arc,shape=bar, frame=bb8, color=color.orange)

        
    bar=shapes.rectangle(height=0.2*scale, width=0.10*scale)
    for i in range(0,24):
        if i%2==1:
            angle1=i*pi/12
            angle2=(i+1)*pi/12
            barcode_arc=paths.arc(radius=1.88*scale, angle1=angle1, angle2=angle2, pos=(0,radius*1.105,0))
            extrusion(pos=barcode_arc,shape=bar, frame=bb8, color=color.orange)
        
        #head strip
    halo=shapes.trapezoid(width=0.2*scale, height=0.07*scale, top=0.1*scale)
    halo_path=paths.arc(radius=1.48*scale, pos=(0,radius*1.35,0), angle2=-9*pi/24, angle1=33*pi/24)
    extrusion(pos=halo_path, frame=bb8, shape=halo, color=color.orange)



    hat=shapes.trapezoid(width=0.7*scale, height=0.2*scale, top=0.01*scale)
    for i in range(0,14):
        angle1=i*pi/7
        angle2=(i+0.9)*pi/7
        hat_path=paths.arc(radius=0.8*scale, pos=(0,radius*1.47,0), angle1=angle1, angle2=angle2)
        extrusion(pos=hat_path, frame=bb8, shape=hat, color=color.gray(0.5),material=materials.shiny)
        


def getR2Width(r2d2, scale):
    return scale*4

def getBB8idth(BB8, scale):
    return 8.0*scale


def main():
    #bb8=BB8(scale=1)
    #sphere(radius=2, pos=(-5,5,0),color=color.green)        
    robot=build_R2D2()
    floor = box (pos=(0,0,0), length=10, height=0.5, width=10, color=color.red)
    while True:  # time loop!
        rate(30)
    
# This calls main when the file is run...
if __name__ == "__main__":
    main() 

