# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 17:14:17 2023

@author: Evgeniy
"""

import py5_tools

if not py5_tools.is_jvm_running():
    py5_tools.add_jars("./jars")

import py5
from com.hamoid import VideoExport



def setup():
    global videoExport, delta
    py5.size(500, 500)
    videoExport = VideoExport(py5.get_current_sketch(), 'output.mp4')
    #videoExport.setFrameRate(25)
    #videoExport.setQuality(100, 128)
    videoExport.startMovie()
    py5.background(255)
    py5.stroke(255)
    delta = 0

def draw():
    global videoExport, delta
    py5.clear()
    py5.circle(250, 250, 90)
    py5.square(250 + delta, 250, 45)
    delta += 0.2
    #py5.save("result.png", drop_alpha=False)
    videoExport.saveFrame()
    
    if py5.is_key_pressed:
        if py5.key == "q":
            videoExport.endMovie()
            py5.exit_sketch()

py5.run_sketch()