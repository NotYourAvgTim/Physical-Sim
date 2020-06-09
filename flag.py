from cloth import *


cloth = Cloth(1, 10, 6, 33, 21, numpy.zeros(3), numpy.array([1, 0, 0]), numpy.array([0, 1, 0]))
framerate = 30
dt = 1 / framerate

cloth.particles[0][0].isMovable = False
cloth.particles[0][1].isMovable = False
cloth.particles[0][2].isMovable = False
cloth.particles[0][3].isMovable = False
cloth.particles[0][4].isMovable = False

for j in range(cloth.nWidth):
        if cloth.particles[0][j]:
            cloth.particles[0][j].isMovable = False

# Pre compute simulation
t = 0
frames = [cloth.getFrame()]
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