class RGBFloat:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    
    def to_color_tuple(self):
        """Convert RGBFloat color to a tuple of integers for use with PIL."""
        return (int(self.r * 255), int(self.g * 255), int(self.b * 255))


    def __add__(self, other):
        if not isinstance(other, RGBFloat):
            raise TypeError("Unsupported operand type for +: 'RGBFloat' and '{}'".format(type(other).__name__))
        return RGBFloat(self.r + other.r, self.g + other.g, self.b + other.b)
    
    def __iadd__(self, other):
        if not isinstance(other, RGBFloat):
            raise TypeError("Unsupported operand type for +: 'RGBFloat' and '{}'".format(type(other).__name__))
        self.r += other.r
        self.g += other.g
        self.b += other.b
        return self

    def __truediv__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("Unsupported operand type for /: 'RGBFloat' and '{}'".format(type(other).__name__))
        return RGBFloat(self.r / other, self.g / other, self.b / other)