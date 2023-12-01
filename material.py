# Define the material with a diffuse coefficient (K value)
import numpy as np
class Material:
    def __init__(self, color, reflectivity=0, transparency=0, refractive_index=1):
        self.color = color
        self.reflectivity = reflectivity
        self.transparency = transparency
        self.refractive_index = refractive_index

