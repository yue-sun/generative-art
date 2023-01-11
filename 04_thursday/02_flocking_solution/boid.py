"""
The Boid class
"""

class Boid(object):
    
    def __init__(self, x, y):
        self.accel = PVector(0, 0)
        self.angle = random(TWO_PI)
        self.vel = PVector(cos(self.angle), sin(self.angle))
        self.pos = PVector(x, y)
        self.r = 2.0
        self.max_speed = 2
        self.max_force = 0.03
        
    def run(self, boids):
        self.compute_force(boids)
        self.update_position()
        self.boundary_conditions()
        self.render()
        
    # Apply force to update acceleration
    # Assume mass = 1 in accel = force / mass
    def apply_force(self, force):
        self.accel.add(force)
        
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
                
    # Separation (fs)
    # Avoid colliding with local flockmates
    # Check for nearby boids and steer away
    def separation(self, boids):
        separation_radius = 50
        fs = PVector(0, 0)       # separation force
        avg_diff = PVector(0, 0) # average opposite velocity
        count = 0                # number of relevant flockmates
        # For every boid in the system, check whether it is too close
        for other in boids:
            d = PVector.dist(self.pos, other.pos)
            # If flockmates are within the separation range
            # Need to exclude 0 distance b/c it's the current boid
            if 0 < d < separation_radius:
                diff = PVector.sub(self.pos, other.pos)
                diff.normalize()
                diff.div(d) # weighted by distance, closer move faster
                avg_diff.add(diff)
                count += 1
        if count > 0:
            avg_diff.div(count) # average opposite velocity
            avg_diff.normalize()
            avg_diff.mult(self.max_speed) # boid moves at max. speed
            fs = PVector.sub(avg_diff, self.vel)
            fs.limit(self.max_force)
        return fs
            
    # Alignment (fa)
    # Move towards the average direction of local flockmates
    # Check for nearby boids and align to average velocity
    def alignment(self, boids):
        alignment_radius = 50
        fa = PVector(0, 0)      # alignment force
        avg_vel = PVector(0, 0) # average velocity
        count = 0               # number of relevant flockmates
        # For every boid in the system, check whether it is too close
        for other in boids:
            d = PVector.dist(self.pos, other.pos)
            # If flockmates are within the separation range
            # Need to exclude 0 distance b/c it's the current boid
            if 0 < d < alignment_radius:
                avg_vel.add(other.vel)
                count += 1
        if count > 0:
            avg_vel.div(count) # average flockmates velocity
            avg_vel.normalize()
            avg_vel.mult(self.max_speed) # boid moves at max. speed
            # Implement Reynolds' algorithm
            # accel_steer = target_vel - current_vel
            fa = PVector.sub(avg_vel, self.vel)
            fa.limit(self.max_force)
        return fa
    
    # Coherence (fc)
    # Move towards the average position of local flockmates
    # Check for nearby boids and move to average position
    def coherence(self, boids):
        coherence_radius = 50
        fc = PVector(0, 0)      # cohesion force
        avg_pos = PVector(0, 0) # average position
        count = 0               # number of relevant flockmates
        # For every boid in the system, check whether it is too close
        for other in boids:
            d = PVector.dist(self.pos, other.pos)
            # If flockmates are within the separation range
            # Need to exclude 0 distance b/c it's the current boid
            if 0 < d < coherence_radius:
                avg_pos.add(other.pos)
                count += 1
        if count > 0:
            avg_pos.div(count) # average flockmates position
            desired = PVector.sub(avg_pos, self.pos)
            # Scale to maximum speed
            desired.normalize()
            desired.mult(self.max_speed)
            fc = PVector.sub(desired, self.vel)
            fc.limit(self.max_force)
        return fc
