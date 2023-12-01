class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction.normalize()  # Ensure the direction is normalized

    # Method to compute a point along the ray at a given distance 't'
    def point_at_parameter(self, t):
        return self.origin + self.direction * t
    