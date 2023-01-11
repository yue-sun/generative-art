"""
Press mouse to drag and draw new circles.
"""

def setup():
    size(640, 360)  # set window size
    background(10) # set background color (grayscale)
    
    stroke(235, 64, 52) # set outline (stroke) color (RGB)
    strokeWeight(4)   # set stroke width
    
    fill(235, 64, 52) # set shape interior color (RGBA)
    # no fourth argument means 100% opacity
    # 255: 100% opacity, 191: 75% opacity, 63: 25% opacity
    
def draw():
    if mousePressed:
        strokeWeight(0.5)
        fill(235, 64, 52, 63)
        ellipse(mouseX, mouseY, 40, 40)
