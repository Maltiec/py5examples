# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 17:27:32 2023

@author: Evgeniy
"""
import py5

rects = []

lastX=0
lastY=0
lastWidth=0
lastHeight=0

currX=0
currY=0
currWidth=0
currHeight=0

startX=0

def setup():
    global i,j
    py5.size(1080, 1080)
    py5.no_stroke()
    i=3
    j=0.0001
    #noLoop()
    py5.rect_mode(py5.CENTER)
    
def draw():
    global i,j
    py5.background(0)
   #translate(width/2,height/2)
    #drawCircPolar(py5.width/2,py5.height/2,700)
    drawRect(py5.width/2,py5.height/2,700, 500)
    j+=0.001
    py5.noise_detail(i,j)

"""
    rects[0].move(mouseX - (width / 2), mouseY + (height * 0.1), 30)
    rects[1].move((mouseX + (width * 0.05)) %
                  width, mouseY + (height * 0.025), 20)
    rects[2].move(mouseX / 4, mouseY - (height * 0.025), 40)
    rects[3].move(mouseX - (width / 2), (height - mouseY), 50)
"""

def drawCirc(ixp, iyp, id):
    py5.stroke(255)
    py5.no_fill()
    py5.circle(ixp,iyp,id)
    if(id > 20):
        noiseVal = py5.noise(id, id/2)
        drawCirc(ixp + id*noiseVal , iyp, id/2)
        drawCirc(ixp - id*noiseVal , iyp, id/2)

def drawCircPolar(ixp, iyp, id):
    py5.stroke(255)
    py5.no_fill()
    py5.circle(ixp,iyp,id)
    if(id > 20):
        noiseVal = py5.noise(id, id/2)
        drawCircPolar(ixp+id*noiseVal, iyp, id*0.6)
        drawCircPolar(ixp-id*noiseVal, iyp, id*0.6)
                

def drawRect(ixp, iyp, iw, ih):
    py5.stroke(255)
    py5.no_fill()
    py5.rect(ixp,iyp,iw,ih)
    if(iw > 20):
        noiseVal = py5.noise(iw, ih)
        drawRect(ixp + iw*noiseVal , iyp, iw/2, ih/2)
        drawRect(ixp - iw*noiseVal , iyp, iw/2, ih/2)
        if (ih>20):
            noiseVal = py5.noise(iw, ih)
            drawRect(ixp, iyp+ih*noiseVal, iw/2, ih/2)
            drawRect(ixp, iyp-ih*noiseVal, iw/2, ih/2)

py5.run_sketch()