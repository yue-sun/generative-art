"""
Class for ellipse trail.
"""

class Trail:
    def __init__(self):
        self.trail = []
        
    def update_trail(self):
        self.trail.insert(0, [mouseX, mouseY])
        if len(self.trail) > 40:
            self.trail.pop()
    
    def draw_trail(self):
        for i, pos in enumerate(self.trail):
            cs = 255/len(self.trail) # color scale
            fill(66, 135, 245, 255-cs*i)
            ss = 40/len(self.trail)  # radius scale
            ellipse(pos[0], pos[1], 40-ss*i, 40-ss*i)
            
    def run(self):
        self.update_trail()
        self.draw_trail()
