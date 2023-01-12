import maya.cmds as cmds
import random

# Clear up current scene
cmds.select(all=True)
cmds.delete()

n = 100 # number of spheres
for i in range(n):
    # Random radius
    rr = random.random() + 0.1
    cmds.polySphere(r=rr)
    # Random position
    x = random.random()*10 - 5
    y = random.random()*10 - 5
    z = random.random()*10 - 5
    cmds.move(x, y, z)