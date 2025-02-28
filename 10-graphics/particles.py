from random import uniform
from graphics import *
import time
import math
class Vec:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "Vec(" + str(self.x) + "," + str(self.y) + ")"
    def __add__(self,other):
        return Vec(self.x + other.x,self.y + other.y)
    def __sub__(self,other):
        return self + (-1) * other
    def __mul__(self,s):
        return Vec (s *self.x, s * self.y)
    __rmul__ = __mul__
    def norm(self):
        return math.sqrt(self.x**2 + self.y**2)

M1 = 1000
G = 5

class Particle:
    def __init__(self,mass,pos,vel):
        self.pos = pos
        self.vel = vel
        self.mass = mass
    def simulate(self,dt):
        self.simulate_gravity(dt)
        self.pos = self.pos + dt * self.vel
    def apply_force(self,dt,f):
        self.vel = self.vel + (dt / self.mass) * f
    def simulate_gravity(self,dt):
        r = self.pos.norm()
        force_intensity = (G * M1 * self.mass) / (r**2)
        direction =  (-1 / r) * self.pos
        self.apply_force(dt,force_intensity * direction)


class ParticleView:
    def __init__(self,particle,color):
        self.particle = particle
        p = Point(10,20)
        self.circle = Circle(p,particle.mass)
        self.circle.draw(win)
        self.circle.setFill(color)
    def reflect_model(self):
        # print("moved particle to", self.particle.pos)
        currentPosPoint = self.circle.getCenter()
        currentPosVector = Vec(currentPosPoint.x,currentPosPoint.y)
        targetPos = self.particle.pos
        displacement = targetPos - currentPosVector
        self.circle.move(displacement.x,displacement.y)

win = GraphWin("Particles" , 640, 480)
win.setCoords(-320, -240, 320, 240)

# initialise simulation
particles = []
view = []
for color in ["red","blue","green","magenta","black","white","yellow"]:
    pos = Vec(uniform(-300,300), uniform(-200,200))
    vel = Vec(uniform(-3,3), uniform(-3,3))
    mass = uniform(2,10)
    particle = Particle(mass,pos,vel)
    particles.append(particle)
    view.append(ParticleView(particle,color))

win.getKey()
prev_time = time.time()
while True:
    k = win.checkKey()
    user_force = Vec(0,0)
    if k:
        if k == "q":
            break
        elif k == "Up":
            user_force = Vec(0,1)
        elif k == "Down":
            user_force = Vec(0,-1)
        elif k == "Left":
            user_force = Vec(-1,0)
        elif k == "Right":
            user_force = Vec(1,0)
    now = time.time()
    dt = (now-prev_time)*20
    prev_time = now
    particles[0].apply_force(dt,10 * user_force)
    # update model according to simulation rules
    for p in particles:
        p.simulate(dt)
    # view model
    for p in view:
        p.reflect_model()

print("got key:", win.getKey())





