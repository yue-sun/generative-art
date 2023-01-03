"""
The Flock class (a list of Boid objects)
"""

class Flock(object):
    
    def __init__(self):
        # Initialize a list to store all boids
        self.boids = []
        
    def run(self):
        for boid in self.boids:
            # Pass the complete flock information (list of all boids)
            # to each boid individually (b/c for each boid, the three
            # flocking rules iterate through all boids in the simulation)
            boid.run(self.boids)
            
    def addBoid(self, new_boid):
        self.boids.append(new_boid)
