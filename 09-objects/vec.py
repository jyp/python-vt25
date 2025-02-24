# vectors in 2d space.

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
    # def scale(self,s): # this changes the object, and that's confusing.
    #     self.x = s * self.x
    #     self.y = s * self.y

u = Vec(1,2)
v = Vec(3,4)
# u.scale(7)
print("7*u+v = ", u.__mul__(7).__add__(v))
print("7*u+v = ", u * 7 + v)
print("7*u+v = ", 7 * u  - v)
print("u=",u)

