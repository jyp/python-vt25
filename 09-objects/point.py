# x = 1234567
# represent a point in 2-d space.
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def move(self,dx,dy):
        self.x =self.x + dx
        self.y = self.y + dy
    def __repr__(self):
        return "Point(" + str(self.x) + ", " + str(self.y) + ")"

q = Point(1,1)
p = Point(123,456)
print(p)
