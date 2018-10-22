#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Input GUI for the simulation.
@author: SamBloom
"""

import tkinter as tk
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.backends.tkagg as tkagg
from matplotlib.backends.backend_agg import FigureCanvasAgg
import numpy as np


root = tk.Tk()
root.title('Delivery Robots Simulation')


inputs = tk.Frame(root) # Frame
FIELD_WIDTH = 25
label = tk.Label(root, text="Enter the simulation parameters:")
label.pack()

### Input fields ###

# Carts input
carts_label = tk.Label(inputs, text="No. of carts")
carts_label.pack(side=tk.TOP)
carts_entry = tk.Entry(inputs, width = FIELD_WIDTH)
carts_entry.pack(side=tk.TOP)

def submit_carts():
    st = carts_entry.get()
    if st == "":
        print("No carts submitted.")
    else:
        print(st + " order submitted.") 
        
enter_carts_button = tk.Button(inputs, text='Enter',command=submit_carts)
enter_carts_button.pack(side=tk.TOP,padx=10,pady=10)

# Nodes input
nodes_label = tk.Label(inputs, text="No. of nodes")
nodes_label.pack()
nodes_entry = tk.Entry(inputs, width = FIELD_WIDTH)
nodes_entry.pack(side=tk.TOP)

def submit_nodes():
    st = nodes_entry.get()
    if st == "":
        print("No nodes submitted.")
    else:
        print(st + " nodes submitted.") 
        
enter_nodes_button = tk.Button(inputs, text='Enter',command=submit_nodes)
enter_nodes_button.pack(padx=10,pady=10)


order_label = tk.Label(inputs, text='Enter an order') #Label
order_label.pack(side=tk.BOTTOM)
order_entry = tk.Entry(inputs, width = FIELD_WIDTH) #Entry field
order_entry.pack(side=tk.BOTTOM)
def submit_order(): #Button function
    st = order_entry.get()
    if st == "":
        print("No order submitted.")
    else:
        print(st + " order submitted.")
        
enter_order_button = tk.Button(inputs, text='Enter',command=submit_order) #Button
enter_order_button.pack(side=tk.BOTTOM,padx=10,pady=20)

inputs.pack(side=tk.LEFT)

### Display screen ###

screen = tk.Canvas(root, width=500, height=500)
screen.pack(side=tk.RIGHT, expand=True)

# Function to draw the pyplot figure into tkinter - from Matplotlib
def draw_figure(canvas, figure, loc=(0,0)):
    
    figure_canvas_agg = FigureCanvasAgg(figure)
    figure_canvas_agg.draw()
    figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
    figure_w, figure_h = int(figure_w), int(figure_h)
    photo = tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)

    # Position: convert from top-left anchor to center anchor
    canvas.create_image(loc[0] + figure_w/2, loc[1] + figure_h/2, image=photo)

    # Unfortunately, there's no accessor for the pointer to the native renderer
    tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)
    # return the photo object to keep the image alive
    return photo

# Create the mpl figure 
fig = mpl.figure.Figure(figsize=(5,5))
ax = fig.add_axes([0, 0, 1, 1])
fig, ax = plt.subplots()
Path = mpl.path.Path

## Enter the path data here
path_data = [
    (Path.MOVETO, (0,0)),
    (Path.MOVETO, (0,1)),
    (Path.MOVETO, (0,2)),
    (Path.MOVETO, (1,0)),
    (Path.MOVETO, (1,1)),
    (Path.MOVETO, (1,2)),
    (Path.MOVETO, (2,0)),
    (Path.MOVETO, (2,1)),
    (Path.MOVETO, (2,2)),
    ]

def get_path_data(route_nodes):
    pass

codes, verts = zip(*path_data) # Collect the data into tuples
path = mpl.path.Path(verts, codes) # Create the paths

# plot control points and connecting lines
x, y = zip(*path.vertices)
line, = ax.plot(x, y, 'go-')
ax.grid()
ax.axis('equal')

# Keep this handle alive to keep the figure displaying
fig_x, fig_y = 100, 100
fig_photo = draw_figure(screen, fig, loc=(fig_x, fig_y))
fig_w, fig_h = fig_photo.width(), fig_photo.height()


### Finally, run the tkinter mainloop
root.mainloop()
