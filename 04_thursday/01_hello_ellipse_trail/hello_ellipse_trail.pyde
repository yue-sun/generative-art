from trail import Trail

trail = Trail()

def setup():
    size(640, 360)
    
def draw():
    background(240)
    trail.run()
