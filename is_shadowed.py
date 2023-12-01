from point import Point
from ray import Ray
import numpy as np

def is_shadowed(point, light_pos, objects):
    # Convert Point objects to numpy arrays for subtraction
    point_np = point.to_np() if isinstance(point, Point) else np.array(point)
    light_pos_np = light_pos.to_np() if isinstance(light_pos, Point) else np.array(light_pos)

    direction_to_light = Point.from_array(light_pos_np - point_np)
    
    shadow_ray = Ray(point, direction_to_light.normalize())
    for obj in objects:
        hit, _ = obj.intersect(shadow_ray)
        if hit:
            return True
    return False