from rigidbody import *

class World:
    """Represents our entire simulation"""
    def __init__(self):
        self.bodies = [] # List of RigidBodies in the simulation
        self.boundaries = [] # List of boundaries in the simulation

    def update(self, dt):
        """Advances all objects dt into the future using our integrator,
           performs collision detection and resolution if necessary"""
        for body in self.bodies:
            body.update(dt)

        contacts = []
        for body in self.bodies:
            for boundary in self.boundaries:
                collisionDetected, contact = body.collidesWithBoundary(boundary)

                if collisionDetected:
                    contacts.append(contact)

        for ia in range(len(self.bodies)):
            for ib in range(ia + 1, len(self.bodies)):
                a = self.bodies[ia]
                b = self.bodies[ib]

                collisionDetected, contact = a.collidesWith(b)
                if collisionDetected:
                    contacts.append(contact)
        
        for contact in contacts:
            if contact.isColliding():
                contact.resolveCollision(0.85)
            else:
                contacts.remove(contact)
    
    def render(self):
        """Updates the graphical representation of all objects to reflect their
           new positions"""
        for body in self.bodies:
            body.render()

    def removeObjectsBelow(self, y):
        """Removes all objects below a certain height to keep the simulation
           from getting bogged down"""
        for i in range(len(self.bodies) - 1, -1, -1):
            if self.bodies[i].x[1] < y:
                self.bodies[i].graphic.visible = False
                del self.bodies[i]



framerate = 60
dt = 1 / framerate

scene.foward = vector(0, 0, 0)
scene.camera.pos = vector(4, 2, 0)
scene.range = 12

world = World()
world.bodies.append(Sphere(0.1, 0.2, numpy.array([0, 5, 0])))
world.bodies.append(Sphere(0.1, 0.2, numpy.array([0.2, 5, 0]), numpy.array([0, 0, 0])))
world.boundaries.append(Boundary(numpy.array([0,0,0]), 12, 12, numpy.array([1,0,0]), numpy.array([1.8,1,0])))
world.boundaries.append(Boundary(numpy.array([8,0,0]), 12, 12, numpy.array([1,0,0]), numpy.array([-1.8,1,0])))



t = 0

while t < 120:
    rate(framerate)
    world.update(dt)
    world.render()
    world.removeObjectsBelow(-6)
    t += dt

    if numpy.random.uniform() < (10/framerate):
        world.bodies.append(Sphere(0.1, 0.2, numpy.array([numpy.random.uniform(-5.0, 10.0),numpy.random.uniform(5.0, 10), numpy.random.uniform(-3.7, 3.7)])))
     
    