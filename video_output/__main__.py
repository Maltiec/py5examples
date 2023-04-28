#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 12:59:23 2023

@author: evgeniy
"""

import py5
import ffmpeg


def setup():
    py5.size(500, 500)


def draw():
    for _ in range(10):
        py5.rect(py5.random_int(py5.width), py5.random_int(py5.height), 10, 10)
    py5.save_frame("./tmp/random_squares_####.jpg")
    if py5.is_key_pressed:
        if py5.key == "q":
            (
                ffmpeg.input("./tmp/*.jpg", pattern_type="glob", framerate=25)
                .filter("deflicker", mode="pm", size=10)
                .filter(
                    "scale",
                    size="hd1080",
                    force_original_aspect_ratio="increase",
                )
                .output(
                    "movie.mp4",
                    crf=20,
                    preset="slower",
                    movflags="faststart",
                    pix_fmt="yuv420p",
                )
                .view(filename="filter_graph")
                .run()
            )
            py5.exit_sketch()


py5.run_sketch()
