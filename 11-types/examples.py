
# activate the typechecker!

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


u = Vec(23,34)
v = Vec(232,343)


def my_sum(l,start=0):
    result = start
    for x in l:
        result = result + x
    return result

l = [u,v]
# print(my_sum(l,start=Vec(0,0)))
# print(sum(l,start=Vec(0,0)))

x : int = 5
y : float = 2345.2345
message : str = "Hello!"
list_example : list = [123, 123.456, message, len, Vec]
int_list_example : list[float] = [123, 23, 345]

def greeting(name: str) -> str:
    return 'Hello ' + name

# def greeting(name):
#     return 'Hello ' + name

def print_greeting(name: str) -> None:
    print('Hello ' + name)

# print(greeting("world"))
# print(greeting(123))

# for x in list_example:
#     print("list element:",  x)

len([2,3,4,5])
len((2,3,4,5))
len("23456")
len({"x":5})

def identity(x):
    return x

l = [2,3,4,5]
print("popped:",l.pop())
print("l is now: ",l)



