"""
Press mouse to drag and draw new circles.
"""

def setup():
    size(640, 360)         # set window size
    background(43, 42, 42) # set background color (grayscale)
    # no fourth argument means 100% opacity
    # 255: 100% opacity, 191: 75% opacity, 63: 25% opacity
    
    fill(189, 191, 190, 63)
    stroke(189, 191, 190)
    strokeWeight(0.5)      # set stroke width
    
def draw():
    if mousePressed:
        # Change color if key pressed
        if keyPressed:
            if key == 'r' or key == 'R':
                fill(219, 79, 79, 63) # set interior fill color (RGBA)
                stroke(219, 79, 79)   # set outline (stroke) color (RGB)
            elif key == 'g' or key == 'G':
                fill(7, 163, 35, 63)
                stroke(7, 163, 35)
            elif key == 'b' or key == 'B':
                fill(18, 135, 219, 63)
                stroke(18, 135, 219)
            else:
                fill(255)
                stroke(255)
        # Draw ellipse when mouse pressed
        ellipse(mouseX, mouseY, 40, 40)
