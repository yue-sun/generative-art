"""
Create a 37x10 grid of circles of random existence,
random radius, random position, and random color.

Click window to generate a new circle composition.

Inspired by Bridget Riley "Composition With Circles 2, 2001":
https://www.artsy.net/artwork/bridget-riley-composition-with-circles-2
"""

def setup():
    size(1440, 360)           # set window size
    background(238, 238, 238) # set background color to paper-white
    stroke(62, 68, 73)        # set stroke color to pencil-black
    strokeWeight(0.75)        # set stroke weight
    noLoop()                  # stop continously executing draw()
    noFill()                  # disable filling geometry
    
def draw():
    background(238, 238, 238) # reset background color
    circles_horizontal()      # draw random circle grid
        
def mousePressed():
    redraw() # execute the code within draw() one time

def circles_horizontal():
    # Set circle radius
    r = height/9
    # Loop through 37x10 grid
    for i in range(36+1):
        for j in range(9+1):
            # Random number to determine whether to draw a circle
            if random(-2,2) < -0.25:
                # Randomly set the RGB values
                R = random(256)
                G = random(256)
                B = random(256)
                fill(R, G, B, 25)   # set fill colors
                stroke(R, G, B, 50) # set stroke colors
                # Add random perturbation to circle pos and radius
                rx, ry, rr = 0, 0, 0
                if random(-2,2) < -0.25:
                    rx = random(-2, 2)
                    ry = random(-2, 2)
                    rr = random(-10, 10)
                # Draw circle
                ellipse(i*(r+rx), j*(r+ry), 2*(r+rr), 2*(r+rr))
