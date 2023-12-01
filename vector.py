# this is a vector class
try:
    import numpy as np
except ImportError:
    print("Please install the 'numpy' package.")
import math

class Vector:
    def __init__(self, x, y,z) :
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vector(self.y * other.z - self.z * other.y,
                       self.z * other.x - self.x * other.z,
                       self.x * other.y - self.y * other.x)

    def normalize(self):
        norm = np.sqrt(self.dot(self))
        return Vector(self.x / norm, self.y / norm, self.z / norm)
    
    # Add other necessary vector operations