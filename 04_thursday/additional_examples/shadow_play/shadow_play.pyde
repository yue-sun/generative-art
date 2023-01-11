"""
Create a 6x11 grid of quads of random colors.

Click window to generate a new color pattern.

Inspired by Bridget Riley "Shadow Play":
https://en.wikipedia.org/wiki/Bridget_Riley#/media/File:Riley,_Shadowplay.jpg
"""

# Set up geometry
nx = 6
ny = 10
lx = width/nx
ly = height/ny

# Color palette of Van Gogh's Starry Night
# https://www.schemecolor.com/starry-starry-night.php
colors = [(23, 54, 121), (72, 136, 200), (127, 197, 220), \
          (232, 225, 99), (219, 144, 28), (11, 30, 56)]

def setup():
    size(420, 600)
    noStroke()
    noLoop()

def draw():
    for i in range(nx):
        for j in range(ny+1):
            # Randomly select color from palette
            color = colors[int(random(0, len(colors)))]
            fill(color[0], color[1], color[2])
            quad(lx*i, ly*j, \
                 lx*i, ly*(j+1), \
                 lx*(i+1), ly*j, \
                 lx*(i+1), ly*(j-1))

def mousePressed():
    redraw()
