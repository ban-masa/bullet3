import pybullet as p
from time import sleep

physicsClient = p.connect(p.GUI)

p.setGravity(0,0,-10)
planeId = p.loadURDF("plane.urdf", [0, 0, -0.2])
rigidId = p.loadURDF("cube.urdf")
matId = p.loadSoftBody("mat.obj", scale=0.2, mass=10, posObj=[0, 0, 50])
bunnyId = p.loadSoftBody("bunny.obj", scale=1, posObj=[0,0,4])
#sofaId = p.loadSoftBody("Chair.obj", scale=1)
useRealTimeSimulation = 1

if (useRealTimeSimulation):
    p.setRealTimeSimulation(1)

while p.isConnected():
    p.setGravity(0,0,-10)
    if (useRealTimeSimulation):
        sleep(0.01) # Time in seconds.
            #p.getCameraImage(320,200,renderer=p.ER_BULLET_HARDWARE_OPENGL )
    else:
        p.stepSimulation()
