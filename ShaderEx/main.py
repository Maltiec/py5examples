#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 18:09:28 2023

@author: evgeniy
"""
import py5

def setup():
    global noise, img, time
    py5.size(1200, 1000, py5.P3D)
    # shaders files must be in the "data" folder to load correctly
    #img = py5.load_image("1.jpg")
    #py5.image(img, 0, 0)
    noise = py5.load_shader("frag_2dnoise.glsl" )#, "vec_2dnoise.glsl")
    noise.set("u_resolution", float(py5.width), float(py5.height))
    #noise = py5.load_shader("frag-random.glsl")
    #py5.apply_filter(noise)
    py5.stroke(0, 102, 153)
    #py5.rect_mode(py5.CENTER)
    time = 0


def draw():
    global noise, img, time
    #py5.background(0)
    #py5.image(img, 0, 0)
    py5.rect(0, 0, 1200, 720)
    #py5.ellipse(py5.mouse_x+75, py5.mouse_y, 150, 150)
    noise.set("u_mouse", float(py5.mouse_x), float(py5.mouse_y))
    
    py5.shader(noise)
    #py5.image(img, 0, 0)
    time += 0.01
    noise.set("u_time", float(time))
    
py5.run_sketch()