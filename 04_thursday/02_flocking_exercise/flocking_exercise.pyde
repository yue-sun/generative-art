"""
Flocking simulation
(Click mouse to add a boid)

Code is based on the Processing example by Daniel Shiffman.

An implementation of Craig Reynolds' Boids algorithm to simulate
the (basic) flocking behavior of birds.

Each boid obeys a net steering force based on three flocking rules:
1. separation: avoid colliding with local flockmates
2. alignment: move towards the average direction of local flockmates
3. coherence: move towards the average position of local flockmates
"""

from boid import Boid
from flock import Flock

flock = Flock()

def setup():
    # Create a display window
    size(640, 360)
    # Add an initial set of boids into the system
    for i in range(60):
        int_x, int_y = random(width), random(height)
        flock.addBoid(Boid(int_x, int_y))
        
def draw():
    background(51, 153, 255)
    flock.run()
    
def mousePressed():
    # Click mouse to add a boid
    flock.addBoid(Boid(mouseX, mouseY))
