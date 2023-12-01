import numpy as np
# Define the eye (camera) location
class Eye:
    def __init__(self, position):
        self.position = np.array(position)