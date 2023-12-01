# Define the material with a diffuse coefficient (K value)
import numpy as np
from point import Point
from ray import Ray
from reflect import reflect
from refract import refract

def cast_ray(ray, objects, light, depth=0, max_depth=5):
    if depth > max_depth:
        return np.array([0, 0, 0])  # Base case: return black for too deep recursion

    closest_intersection = float('inf')
    closest_obj = None

    # Find closest object hit by the ray
    for obj in objects:
        hit, distance = obj.intersect(ray)
        if hit and distance < closest_intersection:
            closest_intersection = distance
            closest_obj = obj

    if closest_obj is None:
        return np.array([0, 0, 0])  # No intersection, return background color or black

    # Calculate intersection point and normal
    intersection_point = ray.point_at_parameter(closest_intersection)
    normal = closest_obj.normal_at(intersection_point)
    normal.normalize()

    # Calculate color at intersection point
    color = closest_obj.shade(intersection_point, light)

    # Calculate reflection if the object is reflective
    if closest_obj.reflectivity > 0:
        reflected_ray_direction = reflect(ray.direction, normal)
        reflected_ray = Ray(intersection_point + reflected_ray_direction * 0.001, reflected_ray_direction)  # Offset to prevent self-intersection
        reflection_color = cast_ray(reflected_ray, objects, light, depth + 1, max_depth)
        color += reflection_color * closest_obj.reflectivity

    # Calculate refraction if the object is transparent
    if closest_obj.transparency > 0:
        refracted_ray_direction = refract(ray.direction, normal, closest_obj.refractive_index)
        if refracted_ray_direction is not None:
            # Inside the cast_ray function, where the error is occurring
            offset = 0.001
            offset_vector = Point(*refracted_ray_direction) * offset  # Create a Point object from the ndarray and scale it
            new_origin = intersection_point + offset_vector  # Perform the addition with Point objects
            refracted_ray = Ray(new_origin, Point(*refracted_ray_direction))  # Create a new Ray with the offset origin
            # refracted_ray = Ray(intersection_point + refracted_ray_direction * 0.001, refracted_ray_direction)  # Offset to prevent self-intersection
            refraction_color = cast_ray(refracted_ray, objects, light, depth + 1, max_depth)
            color += refraction_color * closest_obj.transparency

    return np.clip(color, 0, 1)  # Clamp the color to [0, 1]

# Note: np.clip and np.array are part of the NumPy library for numerical operations in Python.
