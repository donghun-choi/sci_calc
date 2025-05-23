# calculator/solver.py
import math
import cmath

def solve_quadratic(a, b, c):
    D = b ** 2 - 4 * a * c  # Discriminant
    if D < 0:
        # Complex roots
        return (cmath.sqrt(D) - b) / (2*a), (-cmath.sqrt(D) - b) / (2*a)
    else:
        # Real roots
        root1 = (-b + math.sqrt(D)) / (2 * a)
        root2 = (-b - math.sqrt(D)) / (2 * a)
        return root1, root2

def solve_cubic(a, b, c, d):
    # Cardano's method (incomplete for all root cases)
    f = ((3*c/a) - ((b**2)/(a**2)))/3
    g = ((2*(b**3)/(a**3)) - (9*b*c)/(a**2) + (27*d/a))/27
    h = (g**2)/4 + (f**3)/27

    if h > 0:
        # One real root
        r = -(g/2) + math.sqrt(h)
        s = r**(1/3)
        t = -(g/2) - math.sqrt(h)
        u = t**(1/3)
        root = (s + u) - (b / (3 * a))
        return (root,)
    else:
        # Not handling other cases yet
        return ("Cubic root-solving for complex/multiple real roots not fully implemented",)
