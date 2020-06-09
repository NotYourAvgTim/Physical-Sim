from cloth import *

cloth = Cloth(1, 5, 3, 11, 7, numpy.zeros(3), numpy.array([1, 0, 0]), numpy.array([0, 1, 0]))
cloth.particles[0][0].isMovable = False
cloth.particles[0][-1].isMovable = False
cloth.particles[-1][0].isMovable = False
cloth.particles[-1][-1].isMovable = False

framerate = 30
dt = 1 / framerate

# Pre compute simulation
t = 0
frames = [cloth.getFrame()]
while t < 2:
    cloth.update(dt, numpy.array([0.7, 0, 0.4]))
    frames.append(cloth.getFrame())
    t += dt
    print(t)

cloth.particles[-1][-1].isMovable = True

while t < 5:
    cloth.update(dt, numpy.array([0.7, 0, 0.4]))
    frames.append(cloth.getFrame())
    t += dt
    print(t)

input("Press Enter to render...")

# Render
#scene.autoscale = False
mesh = MeshRendering(frames[0], 0.02)
for frame in frames:
    rate(framerate)
    mesh.update(frame)

print("Done!")