"""
The Boid class
"""

class Boid(object):
    
    def __init__(self, x, y):
        self.accel = PVector(0, 0)
        self.angle = random(TWO_PI)
        self.vel = PVector(cos(self.angle), sin(self.angle))
        self.pos = PVector(x, y)
        self.r = 2.0          # size radius of a boid
        self.max_speed = 2    # maximum speed (default speed)
        self.max_force = 0.03 # maximum force magnitude
       
    # Main update function to step forward in one timestep
    def run(self, boids):
        self.compute_force(boids)
        self.update_position()
        self.boundary_conditions()
        self.render()
        
    # Accumulate steering forces based on three rules
    def compute_force(self, boids):
        fs = self.separation(boids) # separation
        fa = self.alignment(boids)  # alignment
        fc = self.coherence(boids)  # cohesion
        # Assign (arbitrary) weighting among the forces
        fs.mult(1.5)
        fa.mult(1.0)
        fc.mult(1.0)
        # Add the net force to acceleration
        self.apply_force(fs)
        self.apply_force(fa)
        self.apply_force(fc)
        
    # Helper function to apply force to update acceleration
    def apply_force(self, force):
        # Assume mass = 1 in accel = force / mass
        self.accel.add(force)
    
    # Update boid position
    def update_position(self):
        # Update velocity
        self.vel.add(self.accel)
        # Limit speed
        self.vel.limit(self.max_speed)
        # Update position
        self.pos.add(self.vel)
        # Reset acceleration to 0
        self.accel.mult(0)
        
    # Periodic boundary conditions
    def boundary_conditions(self):
        # Left
        if self.pos.x < -self.r:
            self.pos.x = width + self.r
        # Right
        if self.pos.x > width + self.r:
            self.pos.x = -self.r
        # Bottom
        if self.pos.y < -self.r:
            self.pos.y = height + self.r
        # Top
        if self.pos.y > height + self.r:
            self.pos.y = -self.r
    
    # Display all boids in the display window
    def render(self):
        # Draw a triangle rotated in the direction of velocity
        theta = self.vel.heading() + PI/2
        fill(255, 100)
        stroke(255)
        with pushMatrix():
            translate(self.pos.x, self.pos.y)
            rotate(theta)
            with beginShape(TRIANGLES):
                vertex(0, -self.r * 2)
                vertex(-self.r, self.r * 2)
                vertex(self.r, self.r * 2)
            
    ############################################################
    ######################## SEPARATION ########################
    ############################################################
    # Separation (fs)
    # Avoid colliding with local flockmates
    # Check for nearby boids and steer away
    def separation(self, boids):
        # Initialize params. and variables
        separation_radius = 50   # impact radius
        fs = PVector(0, 0)       # separation force
        avg_diff = PVector(0, 0) # average opposite velocity
        count = 0                # number of relevant flockmates
        
        # For every boid, check whether within impact radius
        for other in boids:
            pass
            ####################################################
            ################## YOUR CODE HERE ##################
            ####################################################
            # 1. Compute distance btw. self and other boids
            # 2. Check whether within the impact radius
                # 2.1 Calculate vector pointing away from other
                # 2.2 Weight oppo. velocity vector by distance
                # 2.3 Add to sum of opposite velocities
                # 2.4 Update counter
            ####################################################
            
        if count > 0:
            pass
            ####################################################
            ################## YOUR CODE HERE ##################
            ####################################################
            # 1. Compute average opposite velocity
            # 2. Scale to maximum speed
            # 3. Compute steering force
            ####################################################
            
        return fs
    ############################################################
    
    ############################################################
    ######################## ALIGNMENT #########################
    ############################################################
    # Alignment (fa)
    # Move towards the average direction of local flockmates
    # Check for nearby boids and align to average velocity
    def alignment(self, boids):
        # Initialize params. and variables
        alignment_radius = 50   # impact radius
        fa = PVector(0, 0)      # alignment force
        avg_vel = PVector(0, 0) # average velocity
        count = 0               # number of relevant flockmates
        
        # For every boid, check whether within impact radius
        for other in boids:
            pass
            ####################################################
            ################## YOUR CODE HERE ##################
            ####################################################
            # 1. Compute distance btw. self and other boids
            # 2. Check whether within the impact radius
                # 2.1 Add flockmate velocity to sum of velocities
                # 2.2 Update counter
            ####################################################
            
        if count > 0:
            pass
            ####################################################
            ################## YOUR CODE HERE ##################
            ####################################################
            # 1. Compute average flockmates velocity
            # 2. Scale to maximum speed
            # 3. Compute steering force
            ####################################################
            
        return fa
    ############################################################
    
    ############################################################
    ######################## COHERENCE #########################
    ############################################################
    # Coherence (fc)
    # Move towards the average position of local flockmates
    # Check for nearby boids and move to average position
    def coherence(self, boids):
        # Initialize params. and variables
        coherence_radius = 50   # impact radius
        fc = PVector(0, 0)      # cohesion force
        avg_pos = PVector(0, 0) # average position
        count = 0               # number of relevant flockmates
        
        # For every boid, check whether within impact radius
        for other in boids:
            pass
            ####################################################
            ################## YOUR CODE HERE ##################
            ####################################################
            # 1. Compute distance btw. self and other boids
            # 2. Check whether within the impact radius
                # 2.1 Add flockmate position to sum of positions
                # 2.2 Update counter
            ####################################################
            
        if count > 0:
            pass
            ####################################################
            ################## YOUR CODE HERE ##################
            ####################################################
            # 1. Compute average flockmates position
            # 2. Compute target velocity (avg_pos - current_pos)
            # 2. Scale to maximum speed
            # 3. Compute steering force
            ####################################################
            
        return fc
    ############################################################
