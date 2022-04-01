#!/bin/python

import tkinter as tk
import numpy as np
import random
import time

#pixel based approach
root = tk.Tk()

width = 1920
height = 1080

canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()

def mark(x, y, color="#ffffff"):
    global canvas
    canvas.create_line(x,y,x+1,y, fill=color)

curr_x, curr_y = 0,0

shape = 'triangle'
verticies = []

if shape == 'triangle':
    verticies.append((width/2, 0))
    verticies.append((width/3, height))
    verticies.append((width/3*2, height))

if shape == 'square':
    verticies.append((0,0)) 
    verticies.append((width,height))
    verticies.append((0,height))
    verticies.append((width,0))

print(verticies)

curr_x = 0 #randomize
curr_y = 0 #randomize

count = 0
while count < 50000:
    #choose vertex
    vertex = random.randrange(len(verticies))
    #calculate midpoint
    new_x = (curr_x + verticies[vertex][0]) / 2
    new_y = (curr_y + verticies[vertex][1]) / 2
    mark(new_x, new_y)
    curr_x, curr_y = (new_x, new_y)
    root.update()
    count += 1
    if count % 1000 == 0:
        print(count)
    time.sleep(.00001)


