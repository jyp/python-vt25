import math
# assumption: the surface where the robot move is a Euclidean space (in 2 dimensions)
# assumption: x,y are int.
cos_table = [1,0,-1,0]
sin_table = [0,1,0,-1]
class Robot:
    direction_names = ['EAST','NORTH','WEST','SOUTH']
    def forward(self,n):
        angle = self.direction * math.pi / 2
        direction = self.direction
        # self.x = self.x + n * math.cos(angle)
        # self.y = self.y + n * math.sin(angle)
        self.x = self.x + n * cos_table[direction % 4]
        self.y = self.y + n * sin_table[direction % 4]
    def turnLeft(self):
        self.direction = self.direction + 1
    def turnRight(self):
        self.direction = self.direction - 1 
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 1
        # direction is the angle of the robot / 90 degrees.
    def getPosition(self):
        return (self.x, self.y)
    def getDirection(self):
        return Robot.direction_names[self.direction % 4]

r = Robot()
r.forward(5)
print (r.getPosition())
r.turnLeft()
r.forward(5)
print (r.getPosition())
