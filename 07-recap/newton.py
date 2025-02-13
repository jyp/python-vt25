import math


def newton(f, f_derivative, initial_guess):
  x = initial_guess
  while abs(f(x)) > 0.0000001:
      x = x - f(x) / f_derivative(x)
      print(x)
  return x


r = 245
def squared_minus(x):
    return x**2 - r
def squared_derivative(x):
    return 2*x

def cube_minus(x):
    return x**3 - r
def cube_derivative(x):
    return 3*x**2


print(newton(squared_minus,squared_derivative,r/2), math.sqrt(r))
print(newton(cube_minus,cube_derivative,r/2), (r)**(1/3))
