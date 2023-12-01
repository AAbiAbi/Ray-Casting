import numpy as np
from point import Point
class Light:
    def __init__(self, position, color):
        self.position =  position  # Unpack the tuple into x, y, z
        self.color = color

    def __init__(self, position, intensity):
        self.position = position
        self.intensity = np.array(intensity)
