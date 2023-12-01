
import math
import numpy as np
class Point:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def normalize(self):
        length = math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        if length == 0:
            return Point(0, 0, 0)  # Return a zero vector if the length is 0
        return Point(self.x / length, self.y / length, self.z / length)
    #  Overload the '*' operator for scalar multiplication
    def __mul__(self, other):
        if isinstance(other, (int, float)):  # Check if 'other' is a number
            return Point(self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError("Unsupported operand type for *: 'Point' and '{}'".format(type(other).__name__))

    def __rmul__(self, scalar):
            return self.__mul__(scalar)
    # Overload the '+' operator for adding two Points
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise TypeError("Unsupported operand type for +: 'Point' and '{}'".format(type(other).__name__))

    def __neg__(self):
        return Point(-self.x, -self.y, -self.z)

    def to_np(self):
        return np.array([self.x, self.y, self.z])

    # Method for dot product
    def dot(self, other):
        if isinstance(other, Point):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            raise TypeError("Dot product requires another Point object")
        
    @staticmethod
    def from_array(arr):
        return Point(arr[0], arr[1], arr[2])
